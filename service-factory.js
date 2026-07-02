/**
 * ╔══════════════════════════════════════════════════════════════════╗
 * ║  OLAI Service Factory v2                                        ║
 * ║  Generate complete, production-ready nodes from a JSON config.  ║
 * ║                                                                  ║
 * ║  Usage:  node service-factory.js <config.json>                  ║
 * ║  Output: Frontend (index.ts + ConfigPanel.tsx) + Backend handler ║
 * ╚══════════════════════════════════════════════════════════════════╝
 */

const fs = require('fs');
const path = require('path');

// ─── CLI ──────────────────────────────────────────────────────────────────────

const args = process.argv.slice(2);
if (!args[0]) {
  console.log(`
  🏭 OLAI Service Factory v2
  ─────────────────────────────────────────
  Usage:   node service-factory.js <config.json>

  Config JSON format:
  {
    "id":          "tools.weather",           // category.name (kebab-case)
    "name":        "Weather Lookup",          // Display name
    "category":    "Tools",                   // AI | Processing | Tools | Database | Input / Output
    "icon":        "🌤️",                     // Emoji icon
    "description": "Get weather for any city",
    "handlerType": "api",                     // "api" | "browser" | "mcp" | "local"
    "url":         "https://wttr.in",         // For browser-based nodes
    "actions": [
      {
        "value": "get_weather",
        "label": "Get Weather",
        "fields": ["city"],
        "description": "Fetch current weather for a city"
      }
    ],
    "fields": [
      { "key": "city", "label": "City", "type": "text", "default": "Mumbai", "placeholder": "Enter city name" },
      { "key": "apiKey", "label": "API Key", "type": "text", "default": "", "placeholder": "Optional API key" }
    ]
  }
  `);
  process.exit(0);
}

const configPath = path.resolve(args[0]);
if (!fs.existsSync(configPath)) { console.error('❌ File not found:', configPath); process.exit(1); }

const configInput = JSON.parse(fs.readFileSync(configPath, 'utf8'));
const configs = Array.isArray(configInput) ? configInput : [configInput];

console.log(`\n🏭 OLAI Service Factory v2`);
console.log(`───────────────────────────────`);
console.log(`   Processing ${configs.length} node(s)...`);
console.log(`───────────────────────────────\n`);

configs.forEach((config, idx) => {
  if (!config.id || !config.name || !config.category) {
    console.error(`❌ [Node ${idx+1}] Missing: id, name, or category. Skipping.`);
    return;
  }

  const parts = config.id.split('.');
  if (parts.length < 2) {
    console.error(`❌ [Node ${idx+1}] ID must be "category.node-name". Skipping.`);
    return;
  }

  const idName = parts.slice(1).join('-');
  const componentName = idName.split('-').map(p => p.charAt(0).toUpperCase() + p.slice(1)).join('');
  const actions = config.actions || [];
  const fields = config.fields || config.settings || [];
  const handlerType = config.handlerType || 'local';
  const serviceUrl = config.url || '';

  console.log(`🏭 Generating: ${config.name} (${config.id}) [${handlerType}]`);

// ─── Paths ────────────────────────────────────────────────────────────────────

const frontendDir = path.join(__dirname, 'frontend', 'src', 'nodes', config.category.toLowerCase(), componentName);
const backendDir  = path.join(__dirname, 'backend', 'src', 'tasks', config.category.toLowerCase());
fs.mkdirSync(frontendDir, { recursive: true });
fs.mkdirSync(backendDir, { recursive: true });

// ─── 1. Generate index.ts (metadata + executor) ──────────────────────────────

const settingsSchema = [
  ...(actions.length > 0 ? [{
    key: 'action',
    label: 'Action',
    type: 'select',
    default: actions[0]?.value || '',
    options: actions.map(a => ({ label: a.label, value: a.value })),
    description: 'Select which action to perform',
  }] : []),
  ...fields.map(f => ({
    key: f.key,
    label: f.label,
    type: f.type || 'text',
    default: f.default || '',
    placeholder: f.placeholder || '',
    description: f.description || '',
    ...(f.options ? { options: f.options } : {}),
    ...(f.group ? { group: f.group } : {}),
  })),
];

// Build action→field visibility map
const actionFieldMap = {};
if (actions.length > 0) {
  actions.forEach(a => {
    actionFieldMap[a.value] = a.fields || fields.map(f => f.key);
  });
}

const indexTs = `import { NodeDefinition } from '@/config/nodeRegistry';
import { ExecutionHandler } from '@/config/nodeExecutors';
export { default as ConfigPanel } from './ConfigPanel';

${actions.length > 0 ? `// Action → visible fields mapping
export const actionFieldMap: Record<string, string[]> = ${JSON.stringify(actionFieldMap, null, 2)};
` : ''}
export const metadata: NodeDefinition = {
  id: '${config.id}',
  label: '${config.name}',
  category: '${config.category}',
  icon: '${config.icon || '⚙️'}',
  description: \`${config.description || ''}\`,
  inputs: [
    { name: 'input', type: 'any', description: 'Incoming data from upstream nodes' },
  ],
  outputs: [
    { name: 'result', type: 'any', description: 'Output data from this node' },
    { name: 'text', type: 'text', description: 'The text representation of result' },
  ],
  settingsSchema: ${JSON.stringify(settingsSchema, null, 2)},
  requiresInput: false,
};

export const executor: ExecutionHandler = async (input, settings, _nodeData, { addActivity, api }) => {
  const action = settings.action || '${actions[0]?.value || 'default'}';

  addActivity({
    type: 'activity',
    title: '${config.name}',
    description: \`Executing action: \${action}...\`,
    status: 'info',
  });

  try {
    const { data } = await api.post('/api/tasks/execute', {
      type: '${config.id}',
      payload: {
        settings: { ...settings, action },
        text: input?.text || '',
        data: input?.data || {},
        files: input?.files || [],
      },
    });

    if (!data.success) {
      throw new Error(data.error || '${config.name} execution failed');
    }

    addActivity({
      type: 'activity',
      title: '${config.name}',
      description: \`Action \${action} completed successfully.\`,
      status: 'completed',
    });

    // Handle standard OLAI output format
    return {
      text: data.data?.text || JSON.stringify(data.data, null, 2),
      data: data.data?.data || data.data,
      files: data.data?.files || [],
    };
  } catch (error: any) {
    const msg = error.response?.data?.error || error.message || 'Unknown error';
    addActivity({
      type: 'activity',
      title: '${config.name} Error',
      description: msg,
      status: 'error',
    });
    throw new Error(msg);
  }
};
`;

fs.writeFileSync(path.join(frontendDir, 'index.ts'), indexTs);
console.log(`  ✅ Frontend executor:   ${componentName}/index.ts`);

// ─── 2. Generate ConfigPanel.tsx ──────────────────────────────────────────────

const hasActions = actions.length > 0;

const configPanelTsx = `/**
 * ${config.name} — Auto-generated Config Panel
 * Single-tab unified view with action selector and dynamic fields.
 */

import { useState } from 'react';
import { Loader2 } from 'lucide-react';

interface ConfigPanelProps {
  node: { id: string; data: any };
  nodeSettings: Record<string, any>;
  onSettingChange: (key: string, value: any) => void;
  onUpdateNode: (nodeId: string, updates: any) => void;
  theme: string;
  isRunning?: boolean;
}

${hasActions ? `const ACTIONS = ${JSON.stringify(actions.map(a => ({
  value: a.value,
  label: a.label,
  description: a.description || '',
  fields: a.fields || [],
})), null, 2)};` : ''}

const FIELDS = ${JSON.stringify(fields.map(f => ({
  key: f.key,
  label: f.label,
  type: f.type || 'text',
  placeholder: f.placeholder || '',
  options: f.options || undefined,
})), null, 2)};

const ${componentName}ConfigPanel = ({
  node,
  nodeSettings,
  onSettingChange,
  theme,
  isRunning,
}: ConfigPanelProps) => {
  ${hasActions ? `const action = nodeSettings.action || '${actions[0]?.value || ''}';
  const actionDef = ACTIONS.find(a => a.value === action) || ACTIONS[0];
  const visibleFields = actionDef?.fields?.length > 0
    ? FIELDS.filter(f => actionDef.fields.includes(f.key))
    : FIELDS;` : `const visibleFields = FIELDS;`}

  const inputCls = \`w-full px-3 py-2 text-xs rounded-lg border transition-colors outline-none \${
    theme === 'light'
      ? 'bg-white border-gray-300 text-gray-900 focus:border-purple-500'
      : 'bg-white/5 border-white/10 text-white focus:border-purple-500'
  }\`;

  const labelCls = \`text-[11px] font-medium mb-1 block \${
    theme === 'light' ? 'text-gray-700' : 'text-gray-300'
  }\`;

  const outputData = node.data.output;
  const outputText = typeof outputData === 'string'
    ? outputData
    : outputData?.text || (outputData?.data ? JSON.stringify(outputData.data, null, 2) : '');

  return (
    <div className="space-y-4">
      ${hasActions ? `{/* Action Selector */}
      <div>
        <label className={labelCls}>Action</label>
        <div className="grid grid-cols-2 gap-1.5">
          {ACTIONS.map((a) => (
            <button
              key={a.value}
              type="button"
              onClick={() => onSettingChange('action', a.value)}
              className={\`flex items-center gap-2 p-2 rounded-lg text-left text-[10px] font-medium transition-all border \${
                action === a.value
                  ? theme === 'light'
                    ? 'bg-purple-50 border-purple-400 text-purple-700'
                    : 'bg-purple-500/15 border-purple-500/50 text-purple-300'
                  : theme === 'light'
                    ? 'bg-white border-gray-200 text-gray-500 hover:border-gray-300'
                    : 'bg-white/5 border-white/10 text-gray-400 hover:border-white/20'
              }\`}
            >
              <span className="truncate">{a.label}</span>
            </button>
          ))}
        </div>
        {actionDef?.description && (
          <p className={\`text-[10px] mt-1.5 \${theme === 'light' ? 'text-gray-400' : 'text-gray-500'}\`}>
            {actionDef.description}
          </p>
        )}
      </div>` : ''}

      {/* Dynamic Fields */}
      {visibleFields.map((field: any) => (
        <div key={field.key}>
          <label className={labelCls}>{field.label}</label>
          {field.type === 'select' && field.options ? (
            <select
              className={inputCls}
              value={nodeSettings[field.key] || ''}
              onChange={(e) => onSettingChange(field.key, e.target.value)}
            >
              {field.options.map((opt: any) => (
                <option key={opt.value} value={opt.value}>{opt.label}</option>
              ))}
            </select>
          ) : field.type === 'textarea' ? (
            <textarea
              className={\`\${inputCls} resize-none\`}
              rows={3}
              value={nodeSettings[field.key] || ''}
              onChange={(e) => onSettingChange(field.key, e.target.value)}
              placeholder={field.placeholder}
            />
          ) : field.type === 'toggle' ? (
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                checked={nodeSettings[field.key] || false}
                onChange={(e) => onSettingChange(field.key, e.target.checked)}
                className="w-4 h-4 rounded accent-purple-600"
              />
              <span className={\`text-xs \${theme === 'light' ? 'text-gray-600' : 'text-gray-400'}\`}>
                {field.placeholder || 'Enabled'}
              </span>
            </label>
          ) : (
            <input
              className={inputCls}
              type={field.type === 'number' ? 'number' : 'text'}
              value={nodeSettings[field.key] || ''}
              onChange={(e) => onSettingChange(field.key, field.type === 'number' ? Number(e.target.value) : e.target.value)}
              placeholder={field.placeholder}
            />
          )}
        </div>
      ))}

      {/* Output Display */}
      <div className={\`rounded-lg border p-3 \${
        theme === 'light' ? 'border-gray-200 bg-gray-50' : 'border-white/10 bg-white/5'
      }\`}>
        <div className="flex items-center justify-between mb-2">
          <label className={labelCls}>Output</label>
          {isRunning && <Loader2 className="w-3.5 h-3.5 animate-spin text-purple-500" />}
        </div>
        {isRunning ? (
          <p className={\`text-[11px] animate-pulse \${theme === 'light' ? 'text-gray-500' : 'text-gray-400'}\`}>
            Processing...
          </p>
        ) : outputText ? (
          <pre className={\`text-[11px] whitespace-pre-wrap break-words max-h-[200px] overflow-y-auto \${
            theme === 'light' ? 'text-gray-800' : 'text-gray-200'
          }\`}>
            {outputText}
          </pre>
        ) : (
          <div className={\`text-center py-4 \${theme === 'light' ? 'text-gray-400' : 'text-gray-600'}\`}>
            <p className="text-xs">No output yet</p>
            <p className="text-[10px] mt-1 opacity-75">Run the node to see results</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ${componentName}ConfigPanel;
`;

fs.writeFileSync(path.join(frontendDir, 'ConfigPanel.tsx'), configPanelTsx);
console.log(`  ✅ Config Panel:        ${componentName}/ConfigPanel.tsx`);

// ─── 3. Generate Backend Handler ──────────────────────────────────────────────

let handlerBody = '';

if (handlerType === 'browser') {
  handlerBody = `
    // ─── Browser Automation Mode (Session-Aware) ───────────────────
    const axios = require('axios');
    const action = settings.action || '${actions[0]?.value || 'default'}';
    const automationId = '${idName}'; // e.g. 'zerodha', 'whatsapp', 'gmail'

    // 1. Try to call the internal LLM_NOAPI_Automation service first
    // This allows for robust, session-aware Playwright automation.
    try {
      console.log(\`[Factory] Routing browser request for \${automationId} to local automation service...\`);
      const authResponse = await axios.post('http://localhost:6547/v1/execute', {
        automation: automationId,
        action: action,
        payload: { ...settings, ...inputData, text: inputText }
      }, { timeout: 60000 });

      if (authResponse.data && authResponse.data.success) {
        return {
          success: true,
          data: authResponse.data.data,
          executionTime: this.endTime(startTime),
        };
      }
    } catch (e) {
      console.warn(\`[Factory] Local automation service unavailable or action failed: \${(e as any).message}. Falling back to basic fetch.\`);
    }

    // 2. FALLBACK: Basic fetch (no session / legacy mode)
    const url = settings.url || '${serviceUrl}';
    ${fields.map(f => `const ${f.key} = settings.${f.key} || '${f.default || ''}';`).join('\n    ')}

    let finalUrl = url;
    const params = new URLSearchParams();
    ${fields.map(f => `if (typeof ${f.key} === 'string' && ${f.key}) params.append('${f.key}', ${f.key});`).join('\n      ')}
    finalUrl = url + (url.includes('?') ? '&' : '?') + params.toString();

    const response = await axios.get(finalUrl, {
      headers: { 'User-Agent': 'OLAI-Automation/1.0' },
      timeout: 30000,
    });

    const isJson = typeof response.data === 'object';
    let summaryText = isJson ? JSON.stringify(response.data).substring(0, 200) + '...' : String(response.data).substring(0, 500);

    return {
      success: true,
      data: {
        text: summaryText,
        data: response.data,
      },
      executionTime: this.endTime(startTime),
    };`;
} else if (handlerType === 'mcp') {
  handlerBody = `
    // ─── MCP Client Mode ───────────────────────────────────────────
    const { execSync } = require('child_process');
    const action = settings.action || '${actions[0]?.value || 'default'}';

    const toolArgs = {};
    ${fields.map(f => `if (settings.${f.key}) toolArgs['${f.key}'] = settings.${f.key};`).join('\n    ')}

    const mcpRequest = JSON.stringify({
      jsonrpc: '2.0', id: 1,
      method: 'tools/call',
      params: { name: action, arguments: toolArgs },
    });

    try {
      const result = execSync(\`echo '\${mcpRequest}' | npx -y @modelcontextprotocol/server-${idName}\`, {
        encoding: 'utf-8', timeout: 30000,
      });
      const parsed = JSON.parse(result.trim());
      return {
        success: true,
        data: { text: JSON.stringify(parsed.result || parsed, null, 2), data: parsed.result || parsed },
        executionTime: this.endTime(startTime),
      };
    } catch (mcpErr: any) {
      return { success: false, error: 'MCP call failed: ' + mcpErr.message, executionTime: this.endTime(startTime) };
    }`;
} else {
  // 'api' or 'local' logic fallback
  handlerBody = `
    // ─── REST API / Local Mode ─────────────────────────────────────
    const axios = require('axios');
    const action = settings.action || '${actions[0]?.value || 'default'}';
    ${fields.map(f => `const ${f.key} = settings.${f.key} || '${f.default || ''}';`).join('\n    ')}

    const result = {
      success: true,
      action,
      ${fields.map(f => `${f.key}`).join(', ')},
      processedAt: new Date().toISOString(),
    };

    return {
      success: true,
      data: {
        text: \`Action \${action} processed locally.\`,
        data: result,
      },
      executionTime: this.endTime(startTime),
    };`;
}

const handlerTs = `import { TaskHandler, TaskContext, TaskResponse } from '../index';

export class ${componentName}Handler extends TaskHandler {
  readonly type = '${config.id}';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();

    try {
      const settings = payload.settings || {};
      const inputText = payload.text || '';
      const inputData = payload.data || {};
      ${handlerBody}
    } catch (error: any) {
      return {
        success: false,
        error: error.message || '${config.name} execution failed',
        executionTime: this.endTime(startTime),
      };
    }
  }
}
`;

const handlerPath = path.join(backendDir, `${idName}.handler.ts`);
fs.writeFileSync(handlerPath, handlerTs);
console.log(`  ✅ Backend handler:     ${idName}.handler.ts`);

// ─── 4. Summary ───────────────────────────────────────────────────────────────

console.log(`
───────────────────────────────
🚀 Node "${config.name}" generated successfully!

  📁 Frontend:
     frontend/src/nodes/${config.category.toLowerCase()}/${componentName}/index.ts
     frontend/src/nodes/${config.category.toLowerCase()}/${componentName}/ConfigPanel.tsx

  📁 Backend:
     backend/src/tasks/${config.category.toLowerCase()}/${idName}.handler.ts

  ⚡ The node is instantly available in the UI (hot-reload).
     No server restart required.

  Handler type: ${handlerType}
  ${serviceUrl ? `Service URL: ${serviceUrl}` : ''}
───────────────────────────────
`);
}); // End of configs.forEach
