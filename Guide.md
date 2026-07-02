# LLM_NOAPI_Automation: External Integration Guide

This guide is designed for developers and AI agents who need to integrate with the `LLM_NOAPI_Automation` service. This service exposes a local REST API that automates interactions with ChatGPT, Gemini, and Claude via a browser.

**You do not need to understand the internal source code.** Treat this service as a local "black box" API provider.

## 1. Service Overview

- **Base URL**: `http://localhost:6547` (Default)
- **Supported Models**: `chatgpt`, `gemini`, `claude`
- **Authentication**: None (Localhost only)
- **Concept**: The service launches a real browser instance and automates the chat interface. It is **not** using official APIs.
- **Orchestration**: Supports parallel multi-agent calls using independent browser profiles.
- **Memory**: Persistent RAG-based memory (ChromaDB + Llama) automatically augments prompts with past context.

## 2. Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                        Node.js Server (:6547)                    │
│                                                                  │
│  ┌────────────────┐   ┌────────────────┐   ┌────────────────┐  │
│  │  /chat/complete │   │  /orchestrate  │   │  /manage/open  │  │
│  │  (Single Agent) │   │ (Multi-Agent)  │   │   (Profiles)   │  │
│  └───────┬────────┘   └───────┬────────┘   └───────┬────────┘  │
│          │                    │                     │            │
│          ▼                    ▼                     ▼            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              BrowserManager (WorkerPool, max 6)           │   │
│  │  ┌─────────────────┐ ┌──────────┐ ┌──────────┐          │   │
│  │  │ universal_profile│ │ profile_1│ │ profile_2│ ...      │   │
│  │  │ (default, 3 tabs)│ │ (3 tabs) │ │ (3 tabs) │          │   │
│  │  │  [always open]   │ │[5min TTL]│ │[5min TTL]│          │   │
│  │  └─────────────────┘ └──────────┘ └──────────┘          │   │
│  └──────────────────────────────────────────────────────────┘   │
│          │                                                      │
│          ▼                                                      │
│  ┌──────────────────┐                                           │
│  │  Memory Service   │  Python (:6548)                          │
│  │  ChromaDB + Llama │  RAG Context Retrieval                   │
│  └──────────────────┘                                           │
└──────────────────────────────────────────────────────────────────┘
```

## 3. API Reference

### A. List Available Models
- **Endpoint**: `GET /v1/models`
- **Response**:
  ```json
  {
    "data": [
      { "id": "chatgpt", "object": "model" },
      { "id": "gemini", "object": "model" },
      { "id": "claude", "object": "model" }
    ]
  }
  ```

### B. Chat Completions (Single Agent)
Send a prompt to a single model using the default profile.

- **Endpoint**: `POST /v1/chat/completions`
- **Content-Type**: `application/json` (text) or `multipart/form-data` (text + files)

#### Request Body (JSON)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `model` | string | Yes | One of: `chatgpt`, `gemini`, `claude` |
| `prompt` | string | Yes | The text input for the model. |

#### Request Body (Form-Data)
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `model` | text | Yes | One of: `chatgpt`, `gemini`, `claude` |
| `prompt` | text | Yes | The text input. |
| `files` | file | No | One or more image files to upload. |

#### Response Format
```json
{
  "model": "gemini",
  "text": "The full text response from the AI...",
  "json": { "parsed": "object" },
  "images": ["url1", "url2"]
}
```

### C. Multi-Agent Orchestration
Execute prompts across multiple models and profiles **simultaneously**.

- **Endpoint**: `POST /v1/orchestrate`
- **Content-Type**: `application/json`

#### Worker Limit & Auto-Queuing
- **Hard cap: 6 workers** (1 default + 5 extra registered profiles).
- If total tasks exceed 6, they are **automatically queued** and processed in batches of 6.
- Each batch runs fully in parallel; the next batch starts after the previous completes.
- All results are returned together in a single response, in order.

#### Request Body
```json
{
  "tasks": [
    { "model": "chatgpt", "prompt": "Write a haiku.", "quantity": 3 },
    { "model": "gemini", "prompt": "Write a limerick.", "quantity": 2 },
    { "model": "claude",  "prompt": "Write a sonnet.", "quantity": 1 }
  ]
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `tasks` | array | Yes | Array of task objects |
| `tasks[].model` | string | Yes | Model name |
| `tasks[].prompt` | string | Yes | Prompt to send |
- **Hard cap: 4 workers** (1 default + 3 extra profiles).
- If total tasks exceed 4, they are **automatically queued** and processed in batches.
- **Always-Visible Mode**: Browser windows open automatically (no longer headless).
| `tasks[].filePaths` | string[] | No | File paths to upload |

#### Response Format
```json
{
  "results": [
    { "model": "chatgpt", "workerIndex": 0, "status": "success", "text": "..." },
    { "model": "chatgpt", "workerIndex": 1, "status": "success", "text": "..." },
    { "model": "gemini",  "workerIndex": 0, "status": "success", "text": "..." }
  ]
}
```

### D. Profile Management
- **Open Profile**: `GET /v1/manage/open?profile=<index>` — Opens a browser window with 3 model tabs for manual login.
- **Worker Status**: `GET /v1/workers/status` — Returns active profiles and model tabs.

#### Worker Status Response
```json
{
  "agents": {
    "0": { "tabs": ["chatgpt", "gemini", "claude"] },
    "1": { "tabs": ["chatgpt", "gemini", "claude"] }
  },
  "alwaysActive": true,
  "headless": false
}
```

## 4. Profile System (IMPORTANT)

### How It Works
- **Profile 0** (`universal_profile`): Your default profile. **Never auto-closes.**
- **Profile 1-3** (`profile_1` through `profile_3`): Extra profiles for orchestration. **Always active.**
- Each profile is a **separate browser** with **independent login sessions** for all 3 models.
- Profiles are persistent to disk (`browser_data/<profile_name>/`).

### Setup
```bash
npm run setup-profiles
```
1. Enter how many profiles to create (max 5 extra, for a total of 6).
2. Each profile opens one-at-a-time.
3. Log in to ChatGPT, Gemini, and Claude in the browser window.
4. Press Enter to save and move to the next profile.

### Worker-to-Profile Mapping
| Worker Index (in API) | Profile Directory | Lifecycle |
| :--- | :--- | :--- |
| `0` | `browser_data/universal_profile` | Always active (Visible) |
| `1` | `browser_data/profile_1` | Always active (Visible) |
| `2` | `browser_data/profile_2` | Always active (Visible) |
| `3` | `browser_data/profile_3` | Always active (Visible) |

## 5. Constraints & Limitations (CRITICAL)

### Concurrency Rules
1. **One prompt per model per profile at a time.** A model tab in a given profile can only handle one request.
2. **Different models CAN run in parallel** within the same profile (each model has its own tab).
3. **Same model CANNOT run in parallel** within the same profile.
4. **To run the same model in parallel**, you **must** use multiple profiles via orchestration.

### Worker Limits
5. **Hard cap: 6 workers total** (1 default + 5 extra). This matches the number of registered profiles.
6. **Requests exceeding 6 workers are automatically queued** — no error, just sequential batching.
7. **Profiles must exist before use.** Run `npm run setup-profiles` first.
8. **Each profile must be logged in** to all 3 models independently.
9. **Login sessions persist.** You don't need to re-login every time you restart.
10. **Do NOT manually interact** with an automation browser window while a request is in progress.

### Worker Lifecycle
11. **All workers are persistent.** They do not close or timeout unless the server is stopped.
12. **Stability Limit**: Capped at **4 Agents** (12 total tabs) to ensure reliable performance.
13. **Always Visible**: Headless mode is disabled to prevent background-related timeouts.

### Resource
18. **Each extra profile = 1 Chrome process.** 5 profiles = 5 browser windows (~500MB RAM each).
19. **Default profile** opens 1 browser with 3 tabs (lighter).

## 6. Error Handling

| Status Code | Meaning | Action |
| :--- | :--- | :--- |
| `200 OK` | Success | Process the response. |
| `400 Bad Request` | Missing `model`, `prompt`, or invalid `tasks` | Check your payload. |
| `404 Not Found` | Model not supported | Check `/v1/models`. |
| `500 Internal Error` | Browser automation failed | Check logs. Retry or restart profile. |

## 7. Integration Code

### Python
```python
import requests

API_URL = "http://localhost:6547"

# Single agent call
def ask_llm(model, prompt, image_path=None):
    if image_path:
        data = {"model": model, "prompt": prompt}
        with open(image_path, "rb") as f:
            response = requests.post(f"{API_URL}/v1/chat/completions", data=data, files={"files": f})
    else:
        response = requests.post(f"{API_URL}/v1/chat/completions", json={"model": model, "prompt": prompt})
    response.raise_for_status()
    return response.json()

# Multi-agent orchestration (auto-queues if >6 workers)
def orchestrate(tasks):
    """
    tasks = [
        {"model": "chatgpt", "prompt": "...", "quantity": 3},
        {"model": "gemini",  "prompt": "...", "quantity": 2}
    ]
    Total quantity across all tasks must not exceed 6 per batch.
    If it does, tasks are automatically queued internally.
    """
    response = requests.post(f"{API_URL}/v1/orchestrate", json={"tasks": tasks}, timeout=600)
    response.raise_for_status()
    return response.json()["results"]
```

### Node.js
```javascript
const axios = require('axios');
const API_URL = 'http://localhost:6547';

// Single agent call
async function askLLM(model, prompt) {
  const { data } = await axios.post(`${API_URL}/v1/chat/completions`, { model, prompt });
  return data;
}

// Multi-agent orchestration (auto-queues if >6 workers)
async function orchestrate(tasks) {
  const { data } = await axios.post(`${API_URL}/v1/orchestrate`, { tasks }, { timeout: 600000 });
  return data.results;
}

// Example: 4 ChatGPT tasks in parallel (uses workers 0-3)
// const results = await orchestrate([
//   { model: 'chatgpt', prompt: 'Task 1', quantity: 1 },
//   { model: 'chatgpt', prompt: 'Task 2', quantity: 1 },
//   { model: 'chatgpt', prompt: 'Task 3', quantity: 1 },
//   { model: 'chatgpt', prompt: 'Task 4', quantity: 1 },
// ]);

// Example: 10 tasks — auto-queued into 2 batches of 6 and 4
// const results = await orchestrate([
//   { model: 'chatgpt', prompt: 'Summarize this...', quantity: 10 }
// ]);
```
