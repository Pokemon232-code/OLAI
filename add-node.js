const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
if (!args[0]) {
  console.error("Usage: node add-node.js <path-to-node.json>");
  process.exit(1);
}

const configPath = path.resolve(args[0]);
if (!fs.existsSync(configPath)) {
  console.error("File not found:", configPath);
  process.exit(1);
}

let config;
try {
  config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
} catch (e) {
  console.error("Invalid JSON:", e.message);
  process.exit(1);
}

if (!config.id || !config.name || !config.category) {
  console.error("JSON must contain id, name, and category.");
  process.exit(1);
}

const parts = config.id.split('.');
if (parts.length < 2) {
  console.error("error: ID must be in format 'category.node-name' (e.g. 'processing.pdf-reader')");
  process.exit(1);
}
const idName = parts[1];

const componentName = idName.split('-').map(p => p.charAt(0).toUpperCase() + p.slice(1)).join('');
const frontendDir = path.join(__dirname, 'frontend', 'src', 'nodes', config.category.toLowerCase());
const frontendNodeDir = path.join(frontendDir, componentName);

if (!fs.existsSync(frontendNodeDir)) {
  fs.mkdirSync(frontendNodeDir, { recursive: true });
}

const frontendCode = `import { NodeDefinition } from '@/config/nodeRegistry';
import { ExecutionHandler } from '@/config/nodeExecutors';

export const metadata: NodeDefinition = {
  id: '${config.id}',
  label: '${config.name}',
  category: '${config.category}',
  icon: '${config.icon || '⚙️'}',
  description: \`${config.description || ''}\`,
  inputs: ${JSON.stringify(config.inputs || [], null, 2)},
  outputs: ${JSON.stringify(config.outputs || [], null, 2)},
  settingsSchema: ${JSON.stringify(config.settings || [], null, 2)},
  requiresInput: false
};

export const executor: ExecutionHandler = async (input, settings, nodeData, { addActivity }) => {
  // Logic to execute on the frontend. 
  // By default, returning null or an empty result will trigger the backend task dispatcher 
  // if the node is registered there.
  
  return {
    text: '${config.name} executed',
    format: 'json',
    data: { status: 'success' }
  };
};
`;
fs.writeFileSync(path.join(frontendNodeDir, 'index.ts'), frontendCode);
console.log(`✅ Frontend UI Node deployed: frontend/src/nodes/${config.category.toLowerCase()}/${componentName}/index.ts`);

const backendDir = path.join(__dirname, 'backend', 'src', 'tasks', config.category.toLowerCase());
if (!fs.existsSync(backendDir)) {
  fs.mkdirSync(backendDir, { recursive: true });
}

const backendFile = path.join(backendDir, `${idName}.handler.ts`);
const backendCode = `import { TaskHandler, TaskContext, TaskResponse } from '../index';

export class ${componentName}Handler extends TaskHandler {
  readonly type = '${config.id}';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    console.log(\`[${componentName}] Triggered with payload keys:\`, Object.keys(payload || {}));
    
    // ==========================================================
    // 💡 YOUR CUSTOM BACKEND SCRIPT CONNECTION GOES HERE
    // You can write internal Node.js code, OR use 'child_process' 
    // to execute external Python / C++ / Bash / hardware drivers.
    // 
    // Example Node 'child_process' to execute a Python script:
    //
    // const { execSync } = require('child_process');
    // const result = execSync(\`python my_script.py "\${JSON.stringify(payload)}"\`).toString();
    // return { success: true, data: result };
    // ==========================================================

    return {
      success: true,
      data: {
        message: '${config.name} execution completed. Replace this code with your custom Python/JS integration.',
        receivedPayload: payload
      }
    };
  }
}
`;
fs.writeFileSync(backendFile, backendCode);
console.log(`✅ Backend Logic Node deployed: backend/src/tasks/${config.category.toLowerCase()}/${idName}.handler.ts`);
console.log('');
console.log('🚀 Zero-Code Node creation successful! The node is instantly available in the UI without restarting.');
