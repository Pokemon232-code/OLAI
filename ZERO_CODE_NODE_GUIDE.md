# OLAI Playground — Node Development Guide

> **Purpose**: This document is everything an external developer needs to create new nodes for the OLAI Playground — without access to the rest of the codebase. Follow it exactly.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [What You Deliver](#2-what-you-deliver)
3. [File 1 — Node JSON Config](#3-file-1--node-json-config)
4. [File 2 — Backend Handler (.handler.ts)](#4-file-2--backend-handler-handlerts)
5. [Payload I/O Specification](#5-payload-io-specification)
6. [Handler Runtime Patterns](#6-handler-runtime-patterns)
7. [Type Library Reference](#7-type-library-reference)
8. [Rules & Constraints](#8-rules--constraints)
9. [End-to-End Example: Camera Capture Node](#9-end-to-end-example-camera-capture-node)
10. [End-to-End Example: Python Script Runner](#10-end-to-end-example-python-script-runner)
11. [Compilation & Deployment](#11-compilation--deployment)
12. [Checklist Before Submission](#12-checklist-before-submission)

---

## 1. Architecture Overview

```
┌────────────────────────────────────┐
│           OLAI Frontend            │
│  (React + Vite, auto-discovers     │
│   nodes via import.meta.glob)      │
│                                    │
│  Your JSON config → add-node.js    │
│  → generates frontend/src/nodes/   │
│    <category>/<NodeName>/index.ts  │
│  → UI is DONE. No further work.   │
└──────────────┬─────────────────────┘
               │  HTTP POST /api/tasks/execute
               │  { type: "category.node-name", payload: {...} }
               ▼
┌────────────────────────────────────┐
│           OLAI Backend             │
│  (Fastify + TypeScript)            │
│                                    │
│  TaskDispatcher routes by `type`   │
│  → Your .handler.ts file           │
│  → auto-discovered by registry.ts  │
│    (scans for *.handler.ts files)  │
│                                    │
│  YOU write the handle() logic.     │
└────────────────────────────────────┘
```

**Key points:**
- The **frontend is fully generated** from your JSON config. You never touch React code.
- The **backend handler** is where your custom logic lives (Python calls, API calls, hardware drivers, etc.).
- The registry auto-discovers any `*.handler.ts` file — no manual registration required.

---

## 2. What You Deliver

For each node, you deliver **exactly 2 files**:

| # | File | Purpose |
|---|------|---------|
| 1 | `<node-name>.node.json` | Node appearance, ports, settings — fed into `add-node.js` to generate the frontend |
| 2 | `<node-name>.handler.ts` | Backend handler with your custom logic |

The project owner runs `node add-node.js <your-file>.json` which generates the frontend automatically. They then drop your `.handler.ts` into the correct backend folder.

---

## 3. File 1 — Node JSON Config

### 3.1 Full Schema

```json
{
  "id": "<category>.<node-name>",
  "name": "<Human Readable Name>",
  "category": "<Category>",
  "icon": "<emoji>",
  "description": "<One-line description of what the node does>",
  "inputs": [
    {
      "name": "<port_name>",
      "type": "<port_type>",
      "required": true,
      "description": "<optional description>"
    }
  ],
  "outputs": [
    {
      "name": "<port_name>",
      "type": "<port_type>",
      "description": "<optional description>"
    }
  ],
  "settings": [
    {
      "key": "<setting_key>",
      "label": "<Display Label>",
      "type": "<setting_type>",
      "default": "<default_value>",
      "description": "<optional help text>",
      "placeholder": "<optional placeholder>",
      "group": "<optional group name>",
      "options": [{ "label": "Option A", "value": "a" }],
      "min": 0,
      "max": 100,
      "step": 1
    }
  ]
}
```

### 3.2 Field-by-Field Rules

#### `id` (string, REQUIRED)
- Format: `category.node-name`
- Must be **all lowercase**
- Words separated by **hyphens** (kebab-case)
- The category prefix must match one of the allowed categories below
- Examples: `processing.pdf-reader`, `ai.sentiment-analyzer`, `tools.screenshot-capture`

#### `name` (string, REQUIRED)
- Human-readable display name shown to the user
- Use **Title Case**
- Examples: `PDF Reader`, `Sentiment Analyzer`, `Screenshot Capture`

#### `category` (string, REQUIRED)
- Determines which sidebar group the node appears under
- **Allowed values:**

| Category Value | Sidebar Group | Use For |
|----------------|---------------|---------|
| `Input / Output` | Input / Output | Nodes that accept user input or display output (text entry, file upload, display) |
| `AI` | AI | Machine learning, inference, LLM calls, model execution |
| `Processing` | Processing | Data transformation, cleaning, parsing, format conversion |
| `Database` | Database | Database operations, queries, CRUD, storage |
| `Tools` | Tools | Utilities, hardware access, screenshots, notifications, system commands |

> **⚠️ IMPORTANT**: The category in the JSON `"category"` field must match one of the values above **exactly**, including spacing (e.g. `"Input / Output"`, not `"input/output"`). The `id` prefix uses the lowercase-kebab version (e.g. `io.text-input`, `ai.sentiment`, `processing.cleaner`, `database.query`, `tools.screenshot`).

#### `icon` (string, REQUIRED)
- A single **emoji** character
- Displayed on the node in the canvas
- Choose an emoji that visually represents the node's function
- Examples: `🧹` (cleaner), `📸` (camera), `🐍` (python), `🔍` (search), `📊` (chart), `🗄️` (database)

#### `description` (string, REQUIRED)
- One-line summary (max ~80 characters)
- Shown as tooltip/subtitle in the node palette
- Example: `"Clean and normalize tabular datasets"`

#### `inputs` (array, OPTIONAL)
- List of input ports. **If the node takes no input from other nodes, use `[]`**
- Each input is an object — see Port Type Reference below

#### `outputs` (array, OPTIONAL)
- List of output ports. **Every node should have at least one output** (even if it's just a status)
- Each output is an object — see Port Type Reference below

#### `settings` (array, OPTIONAL)
- User-configurable parameters that appear in the node's settings panel
- Each setting is an object — see Settings Type Reference below

---

## 4. File 2 — Backend Handler (.handler.ts)

### 4.1 Template

Every handler **must** follow this exact structure:

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';

// Optional: import child_process, axios, fs, or any Node.js module you need
// import { execSync, spawn } from 'child_process';
// import axios from 'axios';

export class <NodeName>Handler extends TaskHandler {
  readonly type = '<category>.<node-name>';   // MUST match the JSON id exactly

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();

    try {
      // ─── YOUR CUSTOM LOGIC HERE ───

      // 'payload' contains:
      //   - payload.settings  → user-configured settings from the node panel
      //   - payload.inputs    → data received from connected upstream nodes
      //   - payload.files     → any files attached/uploaded

      // 'context' contains:
      //   - context.userId    → the logged-in user's ID
      //   - context.requestId → unique identifier for this execution
      //   - context.request   → the raw Fastify HTTP request object

      const result = { /* your output data */ };

      return {
        success: true,
        data: result,
        executionTime: this.endTime(startTime),
      };
    } catch (error: any) {
      return {
        success: false,
        error: error.message || 'Execution failed',
        executionTime: this.endTime(startTime),
      };
    }
  }
}
```

### 4.2 Naming Convention

| JSON `id` | Handler Class Name | File Name | File Location |
|---|---|---|---|
| `processing.data-cleaner` | `DataCleanerHandler` | `data-cleaner.handler.ts` | `backend/src/tasks/processing/` |
| `ai.sentiment-analyzer` | `SentimentAnalyzerHandler` | `sentiment-analyzer.handler.ts` | `backend/src/tasks/ai/` |
| `tools.screenshot-capture` | `ScreenshotCaptureHandler` | `screenshot-capture.handler.ts` | `backend/src/tasks/tools/` |

**Rule**: The `type` field inside the class MUST **exactly match** the `id` from your JSON config. A mismatch means the frontend will not be able to reach your handler.

### 4.3 The `TaskResponse` Contract

Your `handle()` method must always return this shape:

```typescript
{
  success: boolean;       // true = node executed correctly, false = error
  data?: any;             // your output data (object, string, array — anything)
  error?: string;         // error message (only when success is false)
  executionTime?: number; // milliseconds (use this.startTime() / this.endTime())
}
```

### 4.4 The `TaskContext` Object

```typescript
{
  userId: string;             // The currently logged-in user
  requestId: string;          // Unique ID for this execution run
  request: FastifyRequest;    // The raw HTTP request (for headers, auth, etc.)
}
```

### 4.5 Available Node.js Built-ins for Your Handler

You can import **any** of these in your handler:

| Module | Use Case |
|--------|----------|
| `child_process` (`execSync`, `spawn`, `exec`) | Execute Python scripts, C++ binaries, Bash commands, hardware CLIs |
| `fs` / `path` | Read/write files, resolve script paths |
| `axios` / `node-fetch` | Call external REST APIs, webhooks, cloud services |
| `net` / `dgram` | TCP/UDP socket communication (IoT, hardware) |
| `os` | System info (CPU, memory, platform detection) |
| Any npm package installed in backend | As long as it's in `backend/package.json` |

---

## 5. Payload I/O Specification

This section defines exactly what your `handle(payload, context)` method *receives* at runtime — no guessing.

### 5.1 Full `payload` Structure

```typescript
payload = {

  // ── Settings ──────────────────────────────────────────────────────────────
  // All values the user configured in the node's settings panel.
  // Keys match the "key" fields in your JSON settingsSchema.
  settings: {
    scriptPath: "scripts/main.py",   // type: text
    timeout: 60,                      // type: number
    verbose: true,                    // type: toggle
    mode: "fast",                     // type: select  (the selected .value)
    threshold: 0.85,                  // type: slider
    params: { k: 3, algo: "kmeans" }  // type: json
  },

  // ── Text Input ────────────────────────────────────────────────────────────
  // Received when an upstream node outputs a text/string value.
  text: "The quick brown fox...",

  // ── Structured Data ───────────────────────────────────────────────────────
  // Received when an upstream node outputs a JSON or csv port.
  data: { rows: 42, schema: [...] },

  // ── Files / Media ─────────────────────────────────────────────────────────
  // Array of file objects. Present when upstream node outputs image/audio/
  // video/document/any ports, or user uploads a file.
  files: [
    {
      name: "report.pdf",           // original filename
      type: "application/pdf",      // MIME type
      size: 1048576,                // bytes
      url: "blob:http://...",       // browser blob URL (frontend-side)
      base64: "JVBERi0x...",        // base64 string of file content
      data: Buffer,                 // raw Node.js Buffer (backend-side)
      path: "/tmp/upload_abc123"    // temp file path (if saved to disk)
    }
  ],

  // ── Pass-through from upstream nodes ─────────────────────────────────────
  // When multiple upstream nodes connect to your node, each upstream node's
  // output is merged into payload at the top level using the OUTPUT PORT NAME
  // as the key. For example, if an upstream node has an output port named
  // "result_matrix", your payload will contain:
  result_matrix: { ... },

  // ── Node Identity ─────────────────────────────────────────────────────────
  nodeId: "node_k7x2m",       // The specific node instance ID on the canvas
  type: "processing.my-node", // The node's type (same as handler.type)
}
```

### 5.2 Accessing Payload Values in Your Handler

```typescript
async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {

  // ── Settings (always use optional chaining + fallback defaults) ──
  const scriptPath = payload.settings?.scriptPath || 'scripts/default.py';
  const timeout    = (payload.settings?.timeout   || 60) * 1000;
  const verbose    = payload.settings?.verbose    ?? false;
  const mode       = payload.settings?.mode       || 'normal';

  // ── Text from upstream text node ──
  const inputText = payload.text || '';

  // ── JSON/structured data from upstream node ──
  const inputData = payload.data || {};

  // ── Files ──
  const files = payload.files || [];
  if (files.length > 0) {
    const firstFile = files[0];
    // Use firstFile.base64 to get the raw content as a base64 string
    // Use firstFile.name, firstFile.type, firstFile.size for metadata
  }

  // ── Named port data from upstream node with output port "embedding" ──
  const embedding = payload.embedding || null;

  // ...
}
```

### 5.3 Output Data Shapes

The `data` field in your `TaskResponse` is fully flexible — you return whatever your node is supposed to output. The downstream node receives it in `payload` keyed by the **output port name**.

```typescript
// Example: node with outputs ["result", "metadata"]
return {
  success: true,
  data: {
    result: "classified as: positive",  // → downstream payload.result
    metadata: { confidence: 0.94, label: "positive" }  // → downstream payload.metadata
  }
};
```

**Output data type conventions by port type:**

| Port Type | Expected `data` Shape | Example |
|-----------|-----------------------|---------|
| `text` | `string` | `"Hello world"` |
| `json` | `object` or `array` | `{ score: 0.9 }` |
| `csv` | `string` (CSV rows) | `"name,age\nAlice,30"` |
| `image` | `string` (base64 data URI) | `"data:image/png;base64,iVBOR..."` |
| `audio` | `string` (base64 data URI) | `"data:audio/wav;base64,UklGRi..."` |
| `video` | `string` (base64 data URI or URL) | `"data:video/mp4;base64,..."` |
| `document` | `object` with `{ content, name, type }` | `{ content: "...", name: "out.pdf" }` |
| `any` | Anything — document your choice | `{ format: "custom", value: [...] }` |

---

## 6. Handler Runtime Patterns

The `.handler.ts` file is just a **bridge**. Your real logic can live in **any language or runtime**. Below are the standard patterns — pick the one that fits your node.

---

### Pattern 1 — Pure Node.js (built-in logic)

**When to use**: Data transformation, string manipulation, HTTP calls to APIs, JSON processing — anything that can be done with JavaScript/TypeScript directly.

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import axios from 'axios';

export class MyApiCallerHandler extends TaskHandler {
  readonly type = 'tools.my-api-caller';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    try {
      const apiKey  = payload.settings?.apiKey  || '';
      const endpoint = payload.settings?.endpoint || 'https://api.example.com/process';
      const inputText = payload.text || '';

      const response = await axios.post(
        endpoint,
        { text: inputText },
        { headers: { Authorization: `Bearer ${apiKey}` }, timeout: 30000 }
      );

      return { success: true, data: response.data, executionTime: this.endTime(startTime) };
    } catch (error: any) {
      return { success: false, error: error.message, executionTime: this.endTime(startTime) };
    }
  }
}
```

---

### Pattern 2 — Python Script (via child_process)

**When to use**: ML inference, OpenCV, NumPy/Pandas, PyTorch, any Python library, data science work.

**I/O Contract for the Python script:**
- **Input**: a JSON file path passed as `sys.argv[1]`
- **Output**: print **only** a single JSON object to `stdout`
- **Logging**: use `sys.stderr` for debug prints (never `stdout`)

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

export class MyPythonHandler extends TaskHandler {
  readonly type = 'processing.my-python-node';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    const tmpIn  = path.join(process.cwd(), 'temp', `in_${context.requestId}.json`);
    const script = path.join(process.cwd(), 'scripts', payload.settings?.scriptName || 'main.py');
    const python = payload.settings?.pythonBin || 'python';
    const timeout = (payload.settings?.timeout || 120) * 1000;

    try {
      // Write the entire payload to a temp file (avoids shell-escaping issues)
      fs.mkdirSync(path.dirname(tmpIn), { recursive: true });
      fs.writeFileSync(tmpIn, JSON.stringify(payload));

      const stdout = execSync(`${python} "${script}" "${tmpIn}"`, {
        timeout,
        encoding: 'utf-8',
        // stderr is inherited — Python prints to stderr, won't pollute stdout
      });

      return { success: true, data: JSON.parse(stdout.trim()), executionTime: this.endTime(startTime) };
    } catch (error: any) {
      return { success: false, error: error.message, executionTime: this.endTime(startTime) };
    } finally {
      if (fs.existsSync(tmpIn)) fs.unlinkSync(tmpIn);
    }
  }
}
```

**Python script skeleton (`scripts/main.py`):**

```python
import sys, json

def main():
    with open(sys.argv[1]) as f:
        payload = json.load(f)

    settings = payload.get('settings', {})
    text_in  = payload.get('text', '')
    files    = payload.get('files', [])

    # ─── YOUR LOGIC HERE ───
    result = { "output": text_in.upper(), "chars": len(text_in) }

    print(json.dumps(result))  # ONLY this goes to stdout

    # Debug logging → stderr (never stdout)
    print(f"Processed {len(text_in)} chars", file=sys.stderr)

if __name__ == '__main__':
    main()
```

---

### Pattern 3 — PowerShell Script (.ps1)

**When to use**: Windows system automation, registry access, WMI queries, Active Directory, MS Office COM automation, anything Windows-native.

**I/O Contract for the ps1 script:**
- **Input**: a JSON file path passed as `-InputFile` parameter
- **Output**: `Write-Output` a single JSON string (use `ConvertTo-Json`)
- **Logging**: use `Write-Error` or `Write-Verbose` (not `Write-Output`)

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

export class MyPowerShellHandler extends TaskHandler {
  readonly type = 'tools.my-ps-node';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    const tmpIn  = path.join(process.cwd(), 'temp', `in_${context.requestId}.json`);
    const script = path.join(process.cwd(), 'scripts', payload.settings?.scriptName || 'main.ps1');
    const timeout = (payload.settings?.timeout || 60) * 1000;

    try {
      fs.mkdirSync(path.dirname(tmpIn), { recursive: true });
      fs.writeFileSync(tmpIn, JSON.stringify(payload));

      // -ExecutionPolicy Bypass avoids script-signing requirements
      // -NonInteractive prevents prompts that would hang the process
      const stdout = execSync(
        `powershell -ExecutionPolicy Bypass -NonInteractive -File "${script}" -InputFile "${tmpIn}"`,
        { timeout, encoding: 'utf-8' }
      );

      return { success: true, data: JSON.parse(stdout.trim()), executionTime: this.endTime(startTime) };
    } catch (error: any) {
      return { success: false, error: error.message, executionTime: this.endTime(startTime) };
    } finally {
      if (fs.existsSync(tmpIn)) fs.unlinkSync(tmpIn);
    }
  }
}
```

**PowerShell script skeleton (`scripts/main.ps1`):**

```powershell
param ([string]$InputFile)

$payload  = Get-Content $InputFile | ConvertFrom-Json
$settings = $payload.settings
$textIn   = $payload.text

# ─── YOUR LOGIC HERE ───
$result = @{
    output  = $textIn.ToUpper()
    chars   = $textIn.Length
    machine = $env:COMPUTERNAME
}

# ONLY this line goes to stdout
Write-Output ($result | ConvertTo-Json -Compress)

# Debug logging - goes to stderr stream
Write-Error "Processed $($textIn.Length) chars"
```

---

### Pattern 4 — REST API / Webhook Call

**When to use**: External cloud services (OpenAI, Google Vision, Twilio, Stripe, any REST API), microservices, webhooks, IoT cloud APIs.

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import axios from 'axios';

export class MyRestApiHandler extends TaskHandler {
  readonly type = 'ai.my-cloud-api';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    try {
      const apiKey    = payload.settings?.apiKey   || '';
      const model     = payload.settings?.model    || 'default';
      const endpoint  = payload.settings?.endpoint || 'https://api.example.com/v1/infer';
      const inputText = payload.text || '';
      const inputFile = payload.files?.[0];

      // Build request body
      const body: any = { model, input: inputText };
      if (inputFile?.base64) {
        body.image = inputFile.base64;  // pass binary as base64
      }

      const response = await axios.post(endpoint, body, {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
        timeout: 60000, // 60 second timeout
      });

      return {
        success: true,
        data: {
          result: response.data.output || response.data,
          metadata: { statusCode: response.status, model },
        },
        executionTime: this.endTime(startTime),
      };
    } catch (error: any) {
      // Expose API error details (HTTP status, message)
      const apiError = error.response?.data?.error?.message || error.message;
      return { success: false, error: apiError, executionTime: this.endTime(startTime) };
    }
  }
}
```

---

### Pattern 5 — Bash / Shell Script

**When to use**: ffmpeg, ImageMagick, git, system CLIs, Linux utilities, piped commands, hardware tools (raspistill, aplay, nmcli, etc.).

**I/O Contract**: same as Python — read from a temp JSON file, print JSON to stdout.

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

export class MyBashHandler extends TaskHandler {
  readonly type = 'tools.my-bash-node';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    const tmpIn  = path.join(process.cwd(), 'temp', `in_${context.requestId}.json`);
    const script = path.join(process.cwd(), 'scripts', payload.settings?.scriptName || 'main.sh');
    const timeout = (payload.settings?.timeout || 60) * 1000;

    try {
      fs.mkdirSync(path.dirname(tmpIn), { recursive: true });
      fs.writeFileSync(tmpIn, JSON.stringify(payload));

      const stdout = execSync(`bash "${script}" "${tmpIn}"`, {
        timeout,
        encoding: 'utf-8',
      });

      return { success: true, data: JSON.parse(stdout.trim()), executionTime: this.endTime(startTime) };
    } catch (error: any) {
      return { success: false, error: error.message, executionTime: this.endTime(startTime) };
    } finally {
      if (fs.existsSync(tmpIn)) fs.unlinkSync(tmpIn);
    }
  }
}
```

**Bash script skeleton (`scripts/main.sh`):**

```bash
#!/usr/bin/env bash
INPUT_FILE="$1"

# Read settings from the JSON payload file using jq
SCRIPT_ARG=$(jq -r '.settings.someArg // "default"' "$INPUT_FILE")

# ─── YOUR LOGIC HERE ───
# e.g. run ffmpeg, convert, grep, etc.

# Output ONLY valid JSON to stdout
echo "{\"status\": \"done\", \"arg\": \"$SCRIPT_ARG\"}"

# Debug to stderr
echo "Executed with arg: $SCRIPT_ARG" >&2
```

---

### Pattern 6 — Long-Running Process with Streaming Output (spawn)

**When to use**: Processes that take many minutes (training, video encoding, large file processing). Uses `spawn` instead of `execSync` to collect output incrementally.

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';

export class MyLongRunningHandler extends TaskHandler {
  readonly type = 'processing.my-long-runner';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    const script = path.join(process.cwd(), 'scripts', payload.settings?.script || 'train.py');
    const python = payload.settings?.pythonBin || 'python';
    const timeout = (payload.settings?.timeout || 600) * 1000; // default 10 min

    return new Promise((resolve) => {
      const proc = spawn(python, [script], { timeout });

      let stdout = '';
      let stderr = '';

      proc.stdout.on('data', (chunk) => { stdout += chunk.toString(); });
      proc.stderr.on('data', (chunk) => { stderr += chunk.toString(); });

      proc.on('close', (code) => {
        if (code === 0) {
          try {
            const data = JSON.parse(stdout.trim());
            resolve({ success: true, data, executionTime: this.endTime(startTime) });
          } catch {
            resolve({ success: true, data: { raw: stdout }, executionTime: this.endTime(startTime) });
          }
        } else {
          resolve({ success: false, error: stderr || `Process exited with code ${code}`, executionTime: this.endTime(startTime) });
        }
      });

      proc.on('error', (err) => {
        resolve({ success: false, error: err.message, executionTime: this.endTime(startTime) });
      });
    });
  }
}
```

---

### Pattern 7 — Hardware Driver / Native Module

**When to use**: GPIO pins, serial ports, cameras, microphones, Bluetooth, USB devices, Arduino/Raspberry Pi hardware.

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
// Hardware-specific npm packages — must be installed in backend/package.json
// import { SerialPort } from 'serialport';   // for serial/COM ports
// import { usb } from 'usb';                 // for USB devices
// import { Gpio } from 'onoff';              // for GPIO (Linux/RPi)

export class MyHardwareHandler extends TaskHandler {
  readonly type = 'tools.my-hardware-node';

  // NOTE: Open the hardware resource in handle() *each time*, close it when done.
  // Do NOT open hardware connections in the constructor or as class properties.

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();
    try {
      const portPath = payload.settings?.port || 'COM3';   // or '/dev/ttyUSB0'
      const baudRate = payload.settings?.baudRate || 9600;
      const command  = payload.text || 'READ';

      // ─── YOUR HARDWARE CODE HERE ───
      // Example: open serial, send command, read response, close port
      const result = await this.sendSerialCommand(portPath, baudRate, command);

      return { success: true, data: result, executionTime: this.endTime(startTime) };
    } catch (error: any) {
      return { success: false, error: error.message, executionTime: this.endTime(startTime) };
    }
  }

  private async sendSerialCommand(port: string, baud: number, cmd: string): Promise<any> {
    // Implement using the appropriate hardware library
    throw new Error('Not implemented — replace with hardware library code');
  }
}
```

---

### Pattern Summary

| Pattern | Language/Runtime | Trigger Method | Best For |
|---------|-----------------|---------------|----------|
| 1 | Node.js (TypeScript) | Direct in handler | HTTP APIs, JSON transforms, simple logic |
| 2 | Python (.py) | `execSync` + temp JSON file | ML/AI, Pandas, OpenCV, PyTorch |
| 3 | PowerShell (.ps1) | `execSync` + temp JSON file | Windows automation, WMI, Office, AD |
| 4 | Any REST API | `axios.post()` | Cloud services, SaaS APIs, webhooks |
| 5 | Bash (.sh) | `execSync` + temp JSON file | ffmpeg, system CLIs, Linux utilities |
| 6 | Any (long-running) | `spawn` + event stream | Training, encoding, processing > 30s |
| 7 | Native/Hardware | npm hardware library | GPIO, serial, USB, cameras, Bluetooth |

---

## 7. Type Library Reference

### 7.1 Port Types (for `inputs` and `outputs`)

These define what data can flow between connected nodes:

| Type | Description | Connects With | Example Use |
|------|-------------|---------------|-------------|
| `text` | Plain text / string data | `text`, `any` | Prompts, messages, raw text content |
| `image` | Image data (base64, URL, or binary) | `image`, `any` | Photos, screenshots, generated images |
| `audio` | Audio data (base64, URL, or binary) | `audio`, `any` | Recordings, TTS output, music files |
| `video` | Video data (URL or binary) | `video`, `any` | Video clips, screen recordings |
| `document` | Document data (PDF, DOCX, etc.) | `document`, `any` | Uploaded files, reports |
| `json` | Structured JSON/object data | `json`, `any` | API responses, structured results, metadata |
| `csv` | Tabular CSV data | `csv`, `any` | Spreadsheets, data tables |
| `any` | Universal port — connects to anything | ALL types | When your node can accept/emit any format |

**Connection compatibility rule**: A connection is valid if the output port type matches the input port type, OR either side is `any`.

### 7.2 Settings Field Types (for `settings`)

These determine what UI control the user sees in the node's settings panel:

| Type | UI Control | Required Properties | Optional Properties | Example |
|------|-----------|---------------------|---------------------|---------|
| `text` | Single-line text input | `key`, `label` | `default`, `placeholder`, `description`, `group` | Script path, API endpoint, model ID |
| `textarea` | Multi-line text area | `key`, `label` | `default`, `placeholder`, `description`, `group` | System prompts, code snippets, long text |
| `number` | Numeric input with +/- buttons | `key`, `label` | `default`, `min`, `max`, `step`, `description`, `group` | Port numbers, retry counts, timeouts |
| `select` | Dropdown selector | `key`, `label`, `options` | `default`, `description`, `group` | Choose mode, select format, pick language |
| `toggle` | On/off switch | `key`, `label` | `default`, `description`, `group` | Enable verbose, strict mode, dry-run |
| `slider` | Draggable range slider | `key`, `label` | `default`, `min`, `max`, `step`, `description`, `group` | Temperature, confidence threshold, volume |
| `color` | Color picker | `key`, `label` | `default`, `description`, `group` | Highlight color, theme accent |
| `json` | JSON code editor | `key`, `label` | `default`, `description`, `group` | Custom parameters, headers, raw config |

### 7.3 Settings Field Properties

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `key` | `string` | ✅ | Unique identifier used to access this value in `payload.settings.<key>`. Must be **camelCase**, no spaces, no special characters. |
| `label` | `string` | ✅ | Human-readable label displayed above the control |
| `type` | `string` | ✅ | One of the types from the table above |
| `default` | `any` | ❌ | Default value — type must match the field type |
| `options` | `array` | ⚠️ Required for `select` | Array of `{ "label": "Display", "value": "actual_value" }` objects |
| `min` | `number` | ❌ | Minimum value (for `number` and `slider`) |
| `max` | `number` | ❌ | Maximum value (for `number` and `slider`) |
| `step` | `number` | ❌ | Step increment (for `number` and `slider`) |
| `description` | `string` | ❌ | Help text shown below the control |
| `placeholder` | `string` | ❌ | Placeholder text (for `text` and `textarea`) |
| `group` | `string` | ❌ | Groups related settings under a collapsible header |

### 7.4 Node Execution Result Format (Frontend Return)

When the frontend executor runs (for frontend-only nodes), it must return:

```typescript
{
  text: string;                          // Human-readable output text
  format: 'text' | 'json' | 'image' | 'audio' | 'video' | 'document' | 'csv' | 'other';
  files?: MediaFile[];                   // Optional array of file objects
  data?: any;                            // Optional structured data
  metadata?: any;                        // Optional metadata
}
```

> **Note**: For most nodes you build, the frontend executor returns `null` (meaning "send to backend"). Only pure frontend nodes (like Text Input, Display Text) implement logic in the frontend.

---

## 8. Rules & Constraints

### 8.1 Naming Rules

| What | Rule | ✅ Valid | ❌ Invalid |
|------|------|---------|-----------|
| JSON `id` | `category.node-name` — all lowercase, hyphenated | `processing.pdf-reader` | `Processing.PdfReader`, `pdf_reader` |
| JSON `name` | Title Case | `PDF Reader` | `pdf reader`, `PDF reader` |
| Handler class | PascalCase + `Handler` suffix | `PdfReaderHandler` | `pdfReaderHandler`, `PdfReader` |
| Handler file | `<node-name>.handler.ts` — matches the `id`'s node-name part | `pdf-reader.handler.ts` | `PdfReader.handler.ts`, `pdfReader.ts` |
| Settings `key` | camelCase, no spaces | `scriptPath`, `maxRetries` | `script_path`, `Script Path` |

### 8.2 ID ↔ Handler Type Match (CRITICAL)

The `type` field inside your handler class **must exactly equal** the `id` field in your JSON config:

```
JSON:    "id": "processing.data-cleaner"
                     ↕ must match exactly
TS:      readonly type = 'processing.data-cleaner';
```

If these don't match, the node will appear in the UI but **silently fail** because the dispatcher cannot find the handler.

### 8.3 File Structure Rules

```
backend/src/tasks/
├── index.ts              ← DO NOT MODIFY (base class)
├── registry.ts           ← DO NOT MODIFY (auto-discovery)
├── ai/                   ← handlers for id prefix "ai."
│   └── your-node.handler.ts
├── processing/           ← handlers for id prefix "processing."
│   └── your-node.handler.ts
├── database/             ← handlers for id prefix "database."
│   └── your-node.handler.ts
├── io/                   ← handlers for id prefix "io."
│   └── your-node.handler.ts
└── tools/                ← handlers for id prefix "tools."
    └── your-node.handler.ts
```

- Place your `.handler.ts` in the folder matching the id-prefix category.
- If the category folder doesn't exist, create it.
- **Never** modify `index.ts` or `registry.ts`.

### 8.4 Handler Class Rules

1. **Must extend `TaskHandler`** — `export class YourHandler extends TaskHandler`
2. **Must have `readonly type`** — a string literal matching your JSON `id`
3. **Must implement `async handle()`** — with the exact signature shown in the template
4. **Must always return `TaskResponse`** — never throw unhandled exceptions; catch errors and return `{ success: false, error: "..." }`
5. **Must be an exported class** — `export class`, not `export default` or a function

### 8.5 General Constraints

- **No circular dependencies** — your handler should only import from `'../index'` and standard libraries
- **Timeout safety** — if calling child processes or external APIs, always set a timeout (recommended: 30–300 seconds depending on task)
- **Error isolation** — always wrap your logic in try/catch. A crashing handler crashes the entire request pipeline
- **No global state** — handlers are instantiated once and shared. Don't store request-specific data on `this`
- **File paths** — use `path.join(process.cwd(), ...)` for absolute paths. Never hardcode OS-specific paths

---

## 9. End-to-End Example: Camera Capture Node

### 9.1 JSON Config — `camera-capture.node.json`

```json
{
  "id": "tools.camera-capture",
  "name": "Camera Capture",
  "category": "Tools",
  "icon": "📸",
  "description": "Capture a photo from the system camera",
  "inputs": [],
  "outputs": [
    {
      "name": "image",
      "type": "image",
      "description": "Captured camera image"
    },
    {
      "name": "metadata",
      "type": "json",
      "description": "Image dimensions, timestamp, camera info"
    }
  ],
  "settings": [
    {
      "key": "device",
      "label": "Camera Device",
      "type": "select",
      "default": "0",
      "options": [
        { "label": "Default Camera", "value": "0" },
        { "label": "Camera 2", "value": "1" },
        { "label": "Camera 3", "value": "2" }
      ],
      "description": "Which camera device index to use"
    },
    {
      "key": "resolution",
      "label": "Resolution",
      "type": "select",
      "default": "1080p",
      "options": [
        { "label": "480p", "value": "480p" },
        { "label": "720p", "value": "720p" },
        { "label": "1080p", "value": "1080p" },
        { "label": "4K", "value": "4k" }
      ]
    },
    {
      "key": "autoFocus",
      "label": "Auto Focus",
      "type": "toggle",
      "default": true
    },
    {
      "key": "quality",
      "label": "JPEG Quality",
      "type": "slider",
      "default": 85,
      "min": 10,
      "max": 100,
      "step": 5
    }
  ]
}
```

### 9.2 Backend Handler — `camera-capture.handler.ts`

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

export class CameraCaptureHandler extends TaskHandler {
  readonly type = 'tools.camera-capture';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();

    try {
      const device = payload.settings?.device || '0';
      const resolution = payload.settings?.resolution || '1080p';
      const quality = payload.settings?.quality || 85;

      // Call a Python script that uses OpenCV to capture from camera
      const scriptPath = path.join(process.cwd(), 'scripts', 'camera_capture.py');
      const outputPath = path.join(process.cwd(), 'temp', `capture_${context.requestId}.jpg`);

      const args = JSON.stringify({ device, resolution, quality, outputPath });
      const rawOutput = execSync(
        `python "${scriptPath}" '${args}'`,
        { timeout: 15000 }
      ).toString();

      const result = JSON.parse(rawOutput);

      // Read the captured image as base64
      const imageBuffer = fs.readFileSync(outputPath);
      const base64Image = imageBuffer.toString('base64');

      // Clean up temp file
      fs.unlinkSync(outputPath);

      return {
        success: true,
        data: {
          image: `data:image/jpeg;base64,${base64Image}`,
          metadata: {
            width: result.width,
            height: result.height,
            timestamp: new Date().toISOString(),
            device: device,
          }
        },
        executionTime: this.endTime(startTime),
      };
    } catch (error: any) {
      return {
        success: false,
        error: error.message || 'Camera capture failed',
        executionTime: this.endTime(startTime),
      };
    }
  }
}
```

---

## 10. End-to-End Example: Python Script Runner

### 10.1 JSON Config — `python-runner.node.json`

```json
{
  "id": "processing.python-runner",
  "name": "Python Runner",
  "category": "Processing",
  "icon": "🐍",
  "description": "Execute a custom Python script with JSON input/output",
  "inputs": [
    {
      "name": "data",
      "type": "any",
      "required": true,
      "description": "Input data passed to the Python script as JSON"
    }
  ],
  "outputs": [
    {
      "name": "result",
      "type": "any",
      "description": "JSON output from the Python script"
    }
  ],
  "settings": [
    {
      "key": "scriptPath",
      "label": "Script Path",
      "type": "text",
      "default": "scripts/main.py",
      "placeholder": "path/to/your/script.py",
      "description": "Relative path from the backend root to your Python script"
    },
    {
      "key": "pythonBin",
      "label": "Python Binary",
      "type": "text",
      "default": "python",
      "placeholder": "python3 or /usr/bin/python3",
      "description": "Python executable name or full path"
    },
    {
      "key": "timeout",
      "label": "Timeout (seconds)",
      "type": "number",
      "default": 60,
      "min": 5,
      "max": 600,
      "description": "Maximum execution time before the script is killed"
    },
    {
      "key": "verbose",
      "label": "Verbose Logging",
      "type": "toggle",
      "default": false
    }
  ]
}
```

### 10.2 Backend Handler — `python-runner.handler.ts`

```typescript
import { TaskHandler, TaskContext, TaskResponse } from '../index';
import { execSync } from 'child_process';
import path from 'path';
import fs from 'fs';

export class PythonRunnerHandler extends TaskHandler {
  readonly type = 'processing.python-runner';

  async handle(payload: any, context: TaskContext): Promise<TaskResponse<any>> {
    const startTime = this.startTime();

    try {
      const scriptPath = path.join(process.cwd(), payload.settings?.scriptPath || 'scripts/main.py');
      const pythonBin = payload.settings?.pythonBin || 'python';
      const timeout = (payload.settings?.timeout || 60) * 1000;
      const verbose = payload.settings?.verbose || false;

      if (!fs.existsSync(scriptPath)) {
        return {
          success: false,
          error: `Script not found: ${scriptPath}`,
          executionTime: this.endTime(startTime),
        };
      }

      // Write input to a temp file to avoid shell escaping issues
      const inputPath = path.join(process.cwd(), 'temp', `input_${context.requestId}.json`);
      fs.writeFileSync(inputPath, JSON.stringify(payload.inputs || {}));

      try {
        const rawOutput = execSync(
          `${pythonBin} "${scriptPath}" "${inputPath}"`,
          { timeout, encoding: 'utf-8' }
        );

        if (verbose) {
          console.log(`[PythonRunner] Raw output:`, rawOutput);
        }

        const result = JSON.parse(rawOutput.trim());

        return {
          success: true,
          data: result,
          executionTime: this.endTime(startTime),
        };
      } finally {
        // Always clean up temp file
        if (fs.existsSync(inputPath)) fs.unlinkSync(inputPath);
      }
    } catch (error: any) {
      return {
        success: false,
        error: error.message || 'Python script execution failed',
        executionTime: this.endTime(startTime),
      };
    }
  }
}
```

### 10.3 Corresponding Python Script — `scripts/main.py`

```python
#!/usr/bin/env python3
"""
OLAI Node Script Contract:
- Receives: path to a JSON file as sys.argv[1]
- Must print: valid JSON to stdout (this becomes the node's output)
- Must not print anything else to stdout (use stderr for logs)
"""
import sys
import json

def main():
    input_path = sys.argv[1]
    with open(input_path, 'r') as f:
        data = json.load(f)

    # ─── YOUR LOGIC HERE ───
    result = {
        "processed": True,
        "input_keys": list(data.keys()),
        "message": "Processing complete"
    }

    # Print ONLY valid JSON to stdout
    print(json.dumps(result))

if __name__ == '__main__':
    main()
```

---

## 11. Compilation & Deployment

The project owner runs:

```bash
# From the project root
node add-node.js path/to/your-node.node.json
```

This auto-generates:
1. `frontend/src/nodes/<category>/<NodeName>/index.ts` — UI is instantly live (hot-reload)
2. The owner manually places your `.handler.ts` into `backend/src/tasks/<category>/`

The backend auto-discovers and registers it on the next restart (or on hot-reload during development).

---

## 12. Checklist Before Submission

Use this checklist before submitting your deliverables:

```
JSON Config:
  □ "id" is lowercase and in format "category.node-name"
  □ "name" is in Title Case
  □ "category" is one of: Input / Output, AI, Processing, Database, Tools
  □ "icon" is a single emoji
  □ "description" is a clear one-liner
  □ All input/output port types are from the allowed list
  □ All settings field types are from the allowed list
  □ Settings keys are camelCase
  □ "select" type settings have an "options" array
  □ File validates as valid JSON (use jsonlint or similar)

Backend Handler:
  □ File name is "<node-name>.handler.ts"
  □ Class extends TaskHandler
  □ Class is exported (not default export)
  □ "readonly type" matches the JSON "id" exactly
  □ handle() is async and returns Promise<TaskResponse<any>>
  □ All logic is wrapped in try/catch
  □ External calls have timeouts
  □ Uses path.join() for file paths (no hardcoded paths)
  □ Temp files are cleaned up in a finally block
  □ No global mutable state on the class

If using external scripts (Python, etc.):
  □ Script reads input from a file path (sys.argv[1])
  □ Script outputs ONLY valid JSON to stdout
  □ Script uses stderr for debug logging
  □ Script handles its own errors gracefully
```

---

> **Questions?** Contact the project owner. Do not modify any files outside of your deliverables.