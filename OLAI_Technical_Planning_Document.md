# OLAI Technical Planning Document
## Multi-Agent Architecture & Automatic Application Generator

**Version:** 1.0  
**Date:** September 27, 2025  
**Status:** Planning Phase

---

## 📋 Document Ownership & Copyright

**© September 2025 Omkar Raju Hundre. All Rights Reserved.**

This technical planning document and all associated intellectual property, concepts, designs, architectures, and implementations described herein are the **exclusive property** of:

**Owner & Creator:**  
**Omkar Raju Hundre**

**Official Identification:**
- **Aadhaar Card:** 826093745860
- **PAN Card:** BDZPH9453F

**Professional Profiles:**
- **LinkedIn:** [https://www.linkedin.com/in/hundreomkar/](https://www.linkedin.com/in/hundreomkar/)
- **GitHub:** [https://github.com/Omkar-Hundre/](https://github.com/Omkar-Hundre/)

**Contact:**
- **Email:** hundreomkar7@gmail.com
- **Location:** Belgaum, India

---

### 🔒 Copyright Notice & Intellectual Property Declaration

**This document constitutes original intellectual property** created, developed, and documented by **Omkar Raju Hundre**.

**Declaration of Ownership:**

I, **Omkar Raju Hundre**, hereby declare and affirm that:

1. **Original Creation:** The OLAI (AI-Native Workflow & Productization Platform) concept, architecture, multi-agent system design, and all technical specifications contained in this document are my **original work and intellectual property**.

2. **Sole Ownership:** I am the **sole creator, owner, and rights holder** of this idea, concept, and all associated technical designs, architectures, and implementations described herein.

3. **Timestamp:** This document was created and timestamped on **September 27, 2025** and represents my original intellectual property as of this date.

4. **Rights Reserved:** All rights, including but not limited to:
   - Copyright
   - Patent rights
   - Trade secret rights
   - Trademark rights
   - Commercial exploitation rights
   - Distribution rights
   - Derivative works rights
   
   Are **exclusively reserved** by Omkar Raju Hundre.

5. **Confidentiality:** This document contains proprietary and confidential information. Unauthorized copying, distribution, modification, or use of this document or any portion thereof is strictly prohibited.

---

### ⚖️ Legal Protection

**This document is protected under:**
- **Indian Copyright Act, 1957**
- **Indian Patents Act, 1970**
- **Information Technology Act, 2000**
- **International copyright treaties and conventions**

**Warning:** Unauthorized use, reproduction, distribution, or derivative works based on this intellectual property may result in civil and criminal penalties under applicable laws.

---

### 📝 Document Authentication

**Markdown File Hash (SHA-256):** `8F859EFA7F99F5EA4B02F01FBB4AD4D67DE419DFC8EACD4AAC6CC2C5BCD300B0`  
**PDF File Hash (SHA-256):** `[To be generated upon PDF finalization]`  
**Creation Timestamp:** September 27, 2025, 13:56:40 IST (GMT+5:30)  
**Document Version:** 1.0  
**Document Statistics:**
- **Total Lines:** 25,082 lines
- **Total Characters:** 774,730 characters
- **Total Words:** 84,180 words
- **File Size:** ~755 KB (markdown)

**PDF Statistics:** [To be calculated upon PDF generation]
- **Total Pages:** [Will be calculated]
- **PDF Size:** [Will be calculated]

**Unique Document ID:** OLAI-TPD-2025-OR-001

---

**🔐 How to Verify Document Integrity:**

**For Markdown File:**
```powershell
# Windows PowerShell - Run this to verify the markdown file hasn't been tampered with
Get-FileHash -Path "OLAI_Technical_Planning_Document.md" -Algorithm SHA256

# Expected Hash: 8F859EFA7F99F5EA4B02F01FBB4AD4D67DE419DFC8EACD4AAC6CC2C5BCD300B0
# If the hash matches, the document is authentic and unmodified!
# If it doesn't match, the document has been altered!
```

**For PDF File (after generation):**
```powershell
# Windows PowerShell - Run this to verify the PDF file hasn't been tampered with
Get-FileHash -Path "OLAI_Technical_Planning_Document.pdf" -Algorithm SHA256

# Expected Hash: [Will be generated when PDF is created]
# Compare with the hash shown in this document
```

**Online Hash Verification:**
You can also verify the document hash using online tools:
1. Go to: https://emn178.github.io/online-tools/sha256_checksum.html
2. Upload the markdown file
3. Compare the generated hash with the one above

**What This Means:**
- ✅ **Authenticity:** Proves this document was created by Omkar Raju Hundre
- ✅ **Integrity:** Detects any modifications (even a single character change)
- ✅ **Timestamp:** Combined with hash, proves document existed on September 27, 2025
- ✅ **Legal Evidence:** Admissible in court as proof of ownership and creation date
- ✅ **Non-Repudiation:** Cannot deny authorship once hash is verified

**Security Notice:**
This SHA-256 hash was calculated on the markdown file BEFORE this authentication section was added. This is standard practice for legal document authentication. The hash represents the document content at the time of creation.

---

### 🛡️ Confidentiality & Non-Disclosure

**This document is CONFIDENTIAL and PROPRIETARY.**

Any person or entity accessing this document agrees to:
- Maintain strict confidentiality
- Not disclose any information to third parties without written consent
- Not use any information for competitive purposes
- Return or destroy all copies upon request

**For permissions, licensing, or inquiries, contact:**  
**Omkar Raju Hundre**  
Email: hundreomkar7@gmail.com

---

## Table of Contents

1. [Current Implementation Analysis](#1-current-implementation-analysis)
2. [Multi-Agent Architecture Plan](#2-multi-agent-architecture-plan)
3. [System Architecture for Multi-Agent Coordination](#3-system-architecture-for-multi-agent-coordination)
4. [Implementation Plan for Chat-first PM](#4-implementation-plan-for-chat-first-pm)
5. [Code Generation System Design](#5-code-generation-system-design)
6. [Automatic UI Generator Plan](#6-automatic-ui-generator-plan)
7. [Automatic Deployment & Build](#7-automatic-deployment--build)
8. [Hardware Model Selection Strategy](#8-hardware-model-selection-strategy)
9. [Architecture for Auto-Updating Core Templates](#9-architecture-for-auto-updating-core-templates)
10. [Future Expansion Plan](#10-future-expansion-plan)
11. [Complete End-to-End Workflow](#11-complete-end-to-end-workflow)

---

## 1. Current Implementation Analysis

### 1.0 Vision Statement

**OLAI: Complete Software Company Replacement**

OLAI (Open Language AI) is an AI-native, multi-agent orchestration platform designed to replace an entire software company workforce through an intelligent chat-first interface. The core vision is to democratize software development by allowing anyone—regardless of technical expertise—to transform ideas into production-ready applications through natural language conversation.

**The Problem OLAI Solves:**

Traditional software development requires specialized teams (project managers, architects, developers, testers, DevOps engineers) working in sequential phases over weeks or months. This creates barriers:
- **High Cost**: Hiring multiple specialists is expensive
- **Time Delays**: Sequential workflows slow down iteration
- **Technical Barriers**: Non-developers struggle to articulate requirements
- **Knowledge Silos**: Each specialist operates in isolation
- **Deployment Complexity**: Multi-platform builds require separate expertise

**OLAI's Solution:**

OLAI uses a specialized multi-agent system where AI agents collaborate to handle the entire software development lifecycle. Users interact with a single conversational interface (the PM Agent), which coordinates with other specialist agents behind the scenes. The system works autonomously until completion or a specified deadline, continuously improving the application based on best practices and optimization opportunities.

**Core Design Philosophy:**

1. **Chat-to-Application**: Natural language input directly generates working applications
2. **Agent Specialization**: Each agent focuses on one domain (similar to human specialists)
3. **Modular Assembly**: Pre-built, tested components are assembled rather than generating code from scratch
4. **Continuous Operation**: System works autonomously until deadline or project completion
5. **Adaptive Intelligence**: Agents learn project context and ask clarifying questions only when necessary

**Key Capabilities:**

**1. Chat-First Interface**
- **Technical**: Natural Language Processing (NLP) engine parses user prompts, extracts intent, and maintains conversational context across multiple interactions
- **Layman**: Talk to OLAI like you would to a project manager—describe what you want, and it figures out the details
- **Implementation**: PM Agent acts as primary interface, using conversation history and project context to minimize redundant questions

**2. Time-Based Project Management**
- **Technical**: Deadline-aware task scheduler allocates time across agent workloads, prioritizes critical-path tasks, and adjusts execution strategies based on remaining time
- **Layman**: Tell OLAI "finish by 6:00 PM," and it manages all tasks to meet your deadline
- **Implementation**: Task queue with priority scoring based on deadline proximity, dependency resolution, and estimated completion time

**3. Complete Automation**
- **Technical**: End-to-end pipeline from requirements gathering → **three-document creation** → architecture design → code generation → testing → building → deployment across multiple platforms (web, desktop, mobile)
- **Layman**: From idea to downloadable apps (Windows EXE, macOS app, Android APK, web) without manual intervention
- **Implementation**: **Three-Document Requirements-First Flow** creates comprehensive project documentation before implementation begins, ensuring all agents work from the same approved specifications

**4. Continuous Improvement Loop**
- **Technical**: Review Agent continuously monitors application performance, code quality, and optimization opportunities; suggests improvements until deadline or diminishing returns threshold
- **Layman**: OLAI doesn't stop at "working"—it keeps improving your app (faster servers, better UI, more features) until time runs out
- **Implementation**: Post-initial-build analysis phase identifies refactoring opportunities, performance bottlenecks, and feature enhancements

**5. Intelligent Questioning Strategy**
- **Technical**: Context-aware question generation minimizes user interruptions; questions are asked when information becomes relevant (not all upfront); conversation history prevents redundant queries
- **Layman**: OLAI only asks questions when it truly needs information—no overwhelming questionnaires
- **Implementation**: Missing information detection triggers targeted questions at appropriate development phases

**6. Model-Aware System**
- **Technical**: Static analysis of project requirements determines AI model necessity; distinguishes between pure UI/backend projects (no models) and AI-powered applications (model integration required)
- **Layman**: OLAI knows when your project needs AI (like image recognition) vs. when it's just a website
- **Implementation**: Requirement parser classifies project type; Research Agent suggests appropriate models only when AI functionality is detected

**7. Multi-Model Execution**
- **Technical**: Resource orchestration enables 4-5 models to run concurrently without memory conflicts or performance degradation; includes load balancing, memory management, and GPU scheduling
- **Layman**: If your app needs multiple AI features (text, image, voice), OLAI runs them smoothly together
- **Implementation**: Resource allocation algorithm distributes GPU/CPU/RAM across models; isolated execution environments prevent conflicts

**8. Multi-Platform Export**
- **Technical**: Parallel build pipeline generates platform-specific artifacts (web bundle, Electron/Tauri executables, React Native APK, macOS app bundle) with shared codebase
- **Layman**: Get your app as a website, Windows program, Mac app, and Android app—all in one go
- **Implementation**: Platform-specific build configurations; shared component library; automated packaging and signing

**Example Workflows:**

**Workflow 1: Portfolio Website (No AI Models)**
- **User Input**: "Build me a portfolio website by 6:00 PM"
- **PM Agent Actions**: 
  - Asks: Name, profession, social links, projects to showcase, color preferences
  - Determines: Pure UI/backend project, no AI models needed
  - Timeline: Allocates 30% requirements, 20% design, 30% implementation, 10% testing, 10% building
- **Technical Flow**:
  - Architect Agent: Designs responsive layout, selects React + Tailwind, defines component structure
  - Coding Agent: Generates React components, Fastify backend API, integrates social links
  - Testing Agent: Creates end-to-end tests for navigation, form submission, responsive design
  - Builder Agent: Builds production web bundle, Windows EXE (Electron), macOS app bundle
  - Release Agent: Packages all builds, generates deployment instructions
- **Outcome**: User receives working portfolio in all formats before 6:00 PM deadline

**Workflow 2: AI-Powered Patient Monitoring System**
- **User Input**: "Create an AI patient monitoring system"
- **PM Agent Actions**:
  - Asks: Monitoring type (vital signs, behavior, medication), data sources (sensors, cameras, manual input), alert thresholds
  - Determines: AI models required (pose estimation, anomaly detection, predictive analytics)
  - Timeline: Extended timeline due to model integration complexity
- **Technical Flow**:
  - Research Agent: 
    - Scans hardware (8GB RAM, NVIDIA GTX 1060 6GB, Intel i7)
    - Suggests: Lightweight pose estimation model (MoveNet), time-series anomaly detection (Prophet), classification model (MobileNet v3)
    - Validates: All 3 models can run simultaneously on available hardware
    - Fallback: Provides quantized alternatives if memory constraints detected
  - Architect Agent: Designs microservices architecture with model inference service, real-time data pipeline, alert management system
  - Coding Agent: Implements video processing pipeline, integrates models with error handling, creates monitoring dashboard
  - Testing Agent: Generates test datasets, validates model accuracy, stress-tests concurrent model execution
  - Builder Agent: Creates deployable packages with model weights bundled
- **Outcome**: Complete monitoring system with 3 AI models running smoothly on user's hardware

**Success Metrics:**
- **Time to Application**: Idea to working app in hours (not weeks)
- **Technical Accuracy**: Generated code follows best practices and architecture patterns
- **Platform Coverage**: Single prompt → 4+ platform builds
- **Resource Efficiency**: Optimal hardware utilization without oversubscription
- **User Satisfaction**: Minimal clarifying questions, meeting deadlines consistently

### 1.1 System Architecture Overview

OLAI's architecture is designed as a hybrid system that balances cloud scalability with local privacy and control. The architecture consists of three primary delivery surfaces, each optimized for different user needs and deployment scenarios.

#### Hybrid Product Architecture

**1. Cloud SaaS Web Application (Primary Surface)**

**Technical Architecture:**
- **Frontend**: Single-page React application with TypeScript for type safety
- **State Management**: Redux Toolkit for centralized state, React Query for server state
- **WebSocket Layer**: Real-time bidirectional communication for agent updates, workflow execution status, collaborative editing
- **API Gateway**: RESTful endpoints + GraphQL for complex queries
- **Authentication**: JWT (JSON Web Tokens) with refresh token rotation, OAuth 2.0 for social login
- **Deployment**: Containerized (Docker) on Kubernetes with horizontal pod autoscaling

**User Experience:**
- **Chat Interface**: Primary interaction point; conversational AI responds in natural language
- **Visual Workflow Editor**: ReactFlow-based canvas for drag-and-drop workflow building
- **Marketplace**: Browse, purchase, and install pre-built workflows, agents, and connectors
- **Billing Dashboard**: Real-time cost tracking, usage analytics, subscription management

**Why Cloud-First:**
- **Instant Access**: No installation required; accessible from any device with a browser
- **Scalability**: Handles millions of users with elastic infrastructure
- **Automatic Updates**: Users always get the latest features without manual updates
- **Collaboration**: Real-time co-editing like Figma (multiple users building workflows simultaneously)
- **Centralized Marketplace**: One place for discovering and sharing workflows

**2. Self-Hostable Runtime / Local Agent (Enterprise & Privacy-Focused)**

**Technical Architecture:**
- **Packaging**: Available as Docker image, npm package (`npm i -g olai`), pip package (`pip install olai`), and native binaries (Windows .exe, macOS .app, Linux binary)
- **Local Server**: Lightweight Node.js/Python server runs on `localhost:3000` (configurable)
- **Model Storage**: Local directory structure (`OLAI-Models/`) with organized subfolders by provider/type
- **Dependency Isolation**: Per-model virtual environments (Python venv) or containers to prevent conflicts
- **Offline Operation**: Full functionality without internet for local models and file-based connectors

**User Experience:**
- **CLI Commands**:
  - `olai start`: Launches local server and opens UI (VS Code webview or browser)
  - `olai run workflow.json`: Execute workflow from command line
  - `olai models list`: View installed models
  - `olai models download llama-3-8b`: Download specific model
- **VS Code Integration**: Extension provides webview panel with full OLAI interface inside editor
- **Hybrid Mode**: Can connect to cloud for marketplace/billing while running workflows locally

**Why Self-Hosted:**
- **Data Privacy**: Sensitive data never leaves local machine (healthcare, finance, legal)
- **Enterprise Compliance**: Meets strict regulatory requirements (HIPAA, GDPR, SOC 2)
- **Offline Capability**: Works without internet (airports, remote locations, secure facilities)
- **Cost Control**: No API call charges for local model execution
- **Customization**: Full control over model selection, dependencies, and configurations

**First-Run Experience:**
- **Hardware Detection**: Scans GPU (CUDA, ROCm, Metal), CPU, RAM, disk space
- **Model Recommendations**: Suggests models compatible with detected hardware
- **Account Linking (Optional)**: Connect to cloud for marketplace access or skip for complete local operation
- **Initial Setup**: Downloads essential models if internet available; provides offline templates if not

**3. Developer SDKs + CLI (Programmatic Access)**

**Technical Architecture:**
- **JavaScript/TypeScript SDK**: 
  - ESM and CommonJS support
  - Type definitions included
  - Framework-agnostic (works with React, Vue, Angular, vanilla JS)
  - Browser and Node.js compatible
- **Python SDK**:
  - Type hints with MyPy compatibility
  - Async/await support with asyncio
  - Jupyter notebook integration
  - Framework-agnostic (works with Flask, FastAPI, Django)

**API Surface:**
```typescript
// Universal Model.run() API
await Model.run({
  input: { text: "Summarize this document", file: "./report.pdf" },
  output: { type: "text", format: "markdown" },
  prompt: "Extract key points in bullet format",
  config: { 
    model: "gemini-1.5-pro", 
    temperature: 0.7,
    maxTokens: 1000 
  }
});

// Workflow execution
const flow = await Workflow.load("email-summarizer.json");
const result = await flow.run({ emails: emailList });

// Model chaining
const summary = await Model.run({ input: document, model: "gpt-4" });
const translation = await Model.run({ input: summary.output, model: "gpt-4", prompt: "Translate to Spanish" });
```

**Why SDKs:**
- **Integration**: Embed OLAI workflows into existing applications
- **Automation**: Script complex multi-step workflows
- **CI/CD**: Integrate into build pipelines and testing frameworks
- **Custom UIs**: Build custom interfaces on top of OLAI engine
- **Flexibility**: Full programmatic control for power users

**Visual-to-Code Parity:**
- Every visual workflow has corresponding code representation
- Editing visual node automatically updates generated code
- Editing code syncs changes back to visual editor
- Export workflows as standalone code projects

---

#### Two Primary Audiences

**Audience 1: Developers (Local-First Experience)**

**Installation & Setup:**
```bash
# Option 1: npm (Node.js developers)
npm install -g olai
olai start

# Option 2: pip (Python developers)  
pip install olai
olai start

# Option 3: Docker (DevOps/Enterprise)
docker run -p 3000:3000 -v ~/olai-models:/app/models olai/agent:latest

# Option 4: Native binary (No runtime dependencies)
# Download from releases page, double-click to run
```

**Developer Workflow:**
1. **Start Local Server**: `olai start` launches server and opens VS Code webview or browser at `localhost:3000`
2. **Chat or Code**: Describe workflow in chat OR write code using SDK
3. **Visual Editor**: See workflow as interactive node graph; click nodes to see/edit code
4. **Debug Locally**: Set breakpoints in VS Code, inspect variables, step through execution
5. **Export Project**: Generate complete project scaffold (server file, tests, Dockerfile, README)
6. **Deploy Anywhere**: Self-contained project runs on any platform

**Developer Features:**
- **Code-First Option**: Write workflows as code; see visual representation
- **Breakpoint Debugging**: Full debugging in VS Code with breakpoints and variable inspection
- **Git Integration**: Export workflows as code for version control
- **Custom Nodes**: Create custom nodes with Python/JavaScript; AI helps debug
- **Hot Reload**: Code changes reflect immediately in running workflows
- **Performance Profiling**: Built-in profiler shows bottlenecks and optimization opportunities

**Audience 2: Non-Developers (Web-First SaaS Experience)**

**Onboarding Flow:**
1. **Sign Up**: Simple email or social login (Google, GitHub)
2. **Interactive Wizard**: Chat-driven setup creates first workflow live
3. **Template Selection**: Choose from pre-built templates (HR bot, invoice extractor, etc.)
4. **Customization**: Guided chat helps customize template for specific use case
5. **One-Click Deploy**: Launch workflow as API or web app with single click

**Non-Developer Features:**
- **Natural Language Only**: No code required; describe what you want in plain English
- **Guided Templates**: Step-by-step wizard for common use cases
- **Visual Editor**: Drag-and-drop nodes; no coding required
- **Explainability Mode**: AI explains each step in plain language
- **Collaborative Editing**: Share workflows with team; co-edit in real-time
- **White-Label Export**: Reskin workflow as branded tool for clients

---

#### Current Implementation Details

**Backend Architecture (Fastify + TypeScript)**

**Why Fastify:**
- **Performance**: 3x faster than Express.js; handles 76,000 requests/second vs Express's 23,000
- **Type Safety**: First-class TypeScript support with schema validation
- **Plugin Architecture**: Modular design allows clean separation of concerns
- **Built-in Validation**: JSON Schema validation prevents invalid data from reaching business logic

**Core Modules:**

**1. Authentication System (JWT-based)**
- **Token Structure**: Access token (15 min expiry) + Refresh token (30 days)
- **Security**: Tokens signed with RS256 (asymmetric encryption); private keys stored in secure vault
- **Flow**: Login → Issue both tokens → Client stores refresh token in httpOnly cookie → Access token in memory → On expiry, use refresh token to get new access token
- **Session Management**: Redis stores active sessions; logout invalidates both tokens

**2. API Key Management**
- **Storage**: Encrypted at rest using AES-256-GCM; encryption keys stored in environment variables or HSM
- **Access Control**: RBAC (Role-Based Access Control) determines who can create/view/delete keys
- **Rotation**: Automatic rotation with configurable schedule; old keys remain valid during grace period
- **Usage Tracking**: Every API call logs which key was used for audit trails

**3. Database Integrations**
- **PostgreSQL**: Relational data (users, projects, workflows, permissions)
  - **Schema**: Fully normalized with foreign keys, indexes on frequently queried columns
  - **Connection Pool**: Maintains 10 connections by default; scales based on load
  - **Migrations**: Automated migrations with rollback capability
- **MongoDB**: Document storage (workflow execution logs, large JSON payloads, analytics)
  - **Collections**: Workflows, executions, logs, user_preferences
  - **Indexes**: Compound indexes on userId + createdAt for efficient querying
  - **TTL Indexes**: Automatic cleanup of old execution logs after 90 days

**4. RESTful API with Dynamic Route Generation**
- **Pattern**: Each node type gets auto-generated CRUD endpoints
  - POST `/api/nodes/{nodeType}/execute` - Execute node
  - GET `/api/nodes/{nodeType}/schema` - Get node configuration schema
  - POST `/api/nodes/{nodeType}/validate` - Validate configuration before execution
- **Code Generation**: Node schema JSON → TypeScript route handlers → Fastify route registration
- **Validation**: JSON Schema validation ensures only valid configs reach execution handlers

**5. WebSocket Support (Real-Time Communication)**
- **Protocol**: WebSocket over HTTP/HTTPS; Socket.IO for automatic fallback to long-polling
- **Channels**:
  - `workflow:${workflowId}:status` - Execution status updates
  - `workflow:${workflowId}:logs` - Real-time log streaming
  - `workflow:${workflowId}:agents` - Agent activity feed (which agent is working on what)
  - `collaboration:${workflowId}` - Multi-user editing (cursor positions, selections)
- **Scalability**: Redis pub/sub for multi-instance WebSocket synchronization

**Frontend Architecture (React + TypeScript)**

**1. React + TypeScript Application**
- **Build Tool**: Vite for fast development and optimized production builds
- **State Management**: 
  - **Redux Toolkit**: Global state (user auth, workflows, settings)
  - **React Query**: Server state (API calls, caching, synchronization)
  - **Local State**: Component-level state with useState/useReducer
- **Type Safety**: Strict TypeScript mode; all components and hooks fully typed

**2. ReactFlow Workflow Canvas**
- **Rendering**: HTML5 Canvas-based with React wrappers; supports 1000+ nodes without performance degradation
- **Interactions**:
  - **Drag & Drop**: Drag nodes from palette → Drop on canvas → Auto-connects to nearby nodes
  - **Connection Rules**: Type-checking ensures output types match input types (text → text, image → image)
  - **Zoom & Pan**: Infinite canvas with minimap for navigation
  - **Selection**: Multi-select with Shift+Click or drag rectangle; bulk operations on selected nodes
- **Custom Nodes**: Each node type renders with custom UI (forms, file upload, code editor)

**3. Theme System**
- **Implementation**: CSS custom properties (variables) for colors, spacing, typography
- **Themes**: Light (default), Dark, High Contrast (accessibility)
- **Persistence**: User preference stored in localStorage and synced to server
- **Dynamic Switching**: No page reload required; instant theme change

**4. Real-Time Execution Monitoring**
- **Status Indicators**: Green (completed), Yellow (running), Red (failed), Gray (pending)
- **Progress Bars**: Show percentage completion for long-running nodes
- **Log Streaming**: Real-time logs appear in bottom panel as workflow executes
- **Activity Feed**: Shows which agent is currently working and what they're doing

**5. Node Configuration Panels**
- **Dynamic Forms**: Generated from node schema JSON; supports text inputs, selects, file uploads, code editors
- **Multi-Modal Support**: 
  - **Text**: Rich text editor with markdown support
  - **Images**: Drag & drop or select from file system; preview before upload
  - **Audio**: Record from microphone or upload file; waveform visualization
  - **Video**: Upload with automatic thumbnail generation
  - **Files**: Any file type with MIME type detection

**Workflow Engine Architecture**

**1. Node-Based Execution System**
- **Execution Model**: Directed Acyclic Graph (DAG) with topological sorting
- **Flow**:
  1. Parse workflow JSON → Build dependency graph
  2. Topological sort → Determine execution order
  3. Execute nodes in order → Pass outputs to dependent nodes
  4. Handle errors → Retry failed nodes or escalate
- **Parallelization**: Nodes with no dependencies run concurrently using worker threads

**2. Status Tracking**
- **States**: `pending` → `running` → `completed` | `failed`
- **Persistence**: Status saved to database after each state change
- **Recovery**: If server crashes, workflow resumes from last completed node
- **History**: Complete audit trail of every state transition with timestamps

**3. Checkpoint System**
- **Purpose**: Save workflow state at key points for long-running workflows
- **Trigger**: Auto-checkpoint after every 10 nodes or 5 minutes (whichever comes first)
- **Storage**: Checkpoint data includes:
  - Completed node IDs
  - Node outputs (for passing to future nodes)
  - Execution context (variables, configurations)
- **Resume**: On crash/restart, load last checkpoint and continue from that point

**4. Performance Optimization Hooks**
- **Caching**: Node outputs cached based on input hash; identical inputs skip execution
- **Lazy Loading**: Nodes only loaded into memory when needed
- **Resource Limits**: Max memory per node (1GB default); nodes exceeding limit are terminated
- **Timeout Handling**: Configurable timeout per node; long-running nodes can opt-in for extended timeout

**5. Streaming Support**
- **Use Case**: Processing large files or real-time data streams
- **Implementation**: Node can yield partial results as they're produced
- **Example**: Video processing node yields processed frames one at a time instead of waiting for entire video

**AI Model Integration**

**1. Gemini API Integration**
- **Models Supported**: 
  - `gemini-1.5-pro` - Long context (1M tokens), best quality
  - `gemini-1.5-flash` - Fast inference, shorter context (32k tokens)
  - `gemini-nano` - Browser-based, no server required
- **Features**: Text, images, audio, video inputs; structured output; function calling
- **Pricing**: Pay-per-token with transparent cost tracking before execution

**2. Ollama Local Model Support**
- **Integration**: HTTP API calls to local Ollama server (runs on `localhost:11434`)
- **Model Management**: OLAI auto-detects installed Ollama models; can trigger downloads
- **Models**: LLaMA 3, Mistral, CodeLlama, Vicuna, and 50+ others
- **Advantage**: Free execution; data stays local; works offline

**3. Hugging Face Inference**
- **API Options**: 
  - **Hosted API**: Pay-per-request; instant inference on Hugging Face servers
  - **Local Inference**: Download model and run locally with `transformers` library
- **Model Selection**: 100,000+ models available; OLAI suggests appropriate models based on task
- **Hardware Optimization**: Automatically selects quantized models if GPU/RAM is limited

**4. Model Discovery & Orchestration**
- **Discovery**: OLAI scans available models across Ollama, Hugging Face, Gemini APIs
- **Orchestration**: Manages multiple models running concurrently; load balancing; memory management
- **ChainId Tracking**: Unique ID for each model chain execution; enables tracing and debugging

**5. GPU Management**
- **Detection**: Scans for NVIDIA (CUDA), AMD (ROCm), Apple (Metal) GPUs
- **Allocation**: Distributes models across available GPUs; prevents oversubscription
- **Fallback**: If GPU unavailable or full, automatically falls back to CPU execution

**6. RAG Pipelines Built-In**
- **Vector Databases**: Integrated Pinecone, Weaviate, Qdrant, Chroma, and FAISS (local)
- **Embedding Models**: Sentence-BERT, OpenAI text-embedding-ada-002, Cohere embeddings
- **Pipeline**: Document ingestion → Chunking → Embedding → Vector storage → Semantic search → Context injection → LLM query
- **Templates**: Pre-built RAG workflows (chat-over-docs, semantic search, question answering)

**7. One-Line Execution**
- **API**: `flow.run("summarize emails")` or `olai run email-workflow.json`
- **Behind the Scenes**: 
  - Loads workflow definition
  - Resolves all dependencies
  - Downloads required models if not present
  - Allocates resources
  - Executes workflow
  - Returns results
- **Transparency**: Full logging of every step; user sees what's happening

**Hardware Integration**

OLAI provides direct access to device hardware through a unified API, enabling workflows to interact with physical sensors and peripherals.

**1. Camera Capture**
- **API**: MediaDevices API (browser) or platform-specific APIs (desktop/mobile)
- **Features**: 
  - Capture single image or video stream
  - Select front/back camera on mobile
  - Resolution control (4K, 1080p, 720p, etc.)
  - Flash/torch control
- **Use Cases**: QR code scanning, document scanning, facial recognition, object detection

**2. Microphone Recording**
- **API**: Web Audio API (browser) or platform-specific audio libraries
- **Features**:
  - Record audio in real-time
  - Select input device (built-in mic, USB mic, etc.)
  - Sample rate control (44.1kHz, 48kHz)
  - Audio format selection (WAV, MP3, OGG)
- **Use Cases**: Voice commands, speech-to-text, audio analysis, podcasting

**3. Speaker/Audio Output**
- **API**: Web Audio API or platform audio playback libraries
- **Features**:
  - Play audio files or synthesized audio
  - Volume control
  - Playback speed adjustment
  - Spatial audio (3D positioning)
- **Use Cases**: Text-to-speech, audio notifications, music playback, sound effects

**4. Device Sensors**
- **Accelerometer**: Detects device motion and orientation
- **Gyroscope**: Measures rotation rate
- **Compass**: Provides heading/direction
- **Proximity**: Detects nearby objects
- **Ambient Light**: Measures surrounding light levels
- **Use Cases**: Motion-controlled games, fitness tracking, navigation, auto-brightness

**5. Battery Monitoring**
- **API**: Battery Status API (browser) or platform battery APIs
- **Data**: Battery level (%), charging status, time to full charge, time to empty
- **Use Cases**: Low-battery warnings, power-saving mode triggers, battery health tracking

**6. Network Status**
- **API**: Network Information API or platform network APIs
- **Data**: Connection type (WiFi, cellular, ethernet), signal strength, bandwidth estimate
- **Use Cases**: Adaptive quality (lower resolution on slow connection), offline mode triggers, sync optimization

**7. Geolocation**
- **API**: Geolocation API (browser) or platform location services
- **Data**: Latitude, longitude, altitude, accuracy, heading, speed
- **Features**: One-time location or continuous tracking
- **Use Cases**: Maps, location-based services, geocaching, fitness tracking

**8. Hardware Automation**
- **Workflows Can**:
  - Capture image → Process with AI → Send notification
  - Record audio → Transcribe → Save to database
  - Monitor battery → If below 20% → Save work and shutdown
  - Track location → If near home → Turn on smart lights
- **Implementation**: Event-driven triggers; hardware events can start workflows automatically

### 1.2 Implemented Nodes (50+)

OLAI's node system is the core building block of workflows. Each node represents a reusable, configurable operation that processes input data and produces output data. Nodes are connected via edges (threads) to form complete workflows. The current implementation includes 50+ production-ready nodes organized into functional categories.

#### Node Architecture Pattern

**Design Principles:**
- **Single Responsibility**: Each node does one thing well
- **Type Safety**: Inputs and outputs are strongly typed
- **Composability**: Nodes can be chained in any combination
- **Configurability**: Behavior customizable through JSON schema configuration
- **Error Handling**: Graceful failure with clear error messages

**Node Structure:**
```typescript
interface Node {
  id: string;                    // Unique identifier
  type: string;                  // Node type (e.g., "text-splitter")
  config: Record<string, any>;   // Configuration parameters
  inputs: NodeInput[];           // Input connections
  outputs: NodeOutput[];         // Output connections
  position: { x: number; y: number }; // Canvas position
}

interface NodeSchema {
  type: string;
  category: string;
  inputs: InputSchema[];
  outputs: OutputSchema[];
  config: JSONSchema;            // JSON Schema for configuration validation
  executor: (input: any, config: any) => Promise<any>;
}
```

**Execution Flow:**
1. **Validation**: Config validated against JSON Schema
2. **Input Resolution**: Gather all input data from connected nodes
3. **Execution**: Run node's executor function with inputs and config
4. **Output**: Emit output data to connected downstream nodes
5. **State Update**: Mark node as completed and save output to checkpoint

---

#### Text Processing Nodes

Text processing nodes handle string manipulation, formatting, parsing, and transformation. These are the workhorses for data extraction and content generation workflows.

**1. text-input (Manual Text Entry)**
- **Purpose**: Allows user to manually enter text as starting point for workflow
- **Technical**: Creates React text area component; stores text in workflow state
- **Use Cases**: 
  - Seed data for testing workflows
  - User-provided content for processing
  - Template variables for dynamic workflows
- **Configuration**: 
  - `placeholder`: Hint text
  - `defaultValue`: Pre-filled text
  - `multiline`: Enable multi-line input (true) or single-line (false)
  - `maxLength`: Character limit

**2. display-text (Formatted Text Output)**
- **Purpose**: Renders text output with syntax highlighting and formatting
- **Technical**: Monaco Editor (VSCode's editor) for code; markdown renderer for formatted text; plain text for simple output
- **Formatting Modes**:
  - `plain`: Raw text, no formatting
  - `markdown`: GitHub-flavored markdown with tables, checkboxes, syntax highlighting
  - `code`: Syntax-highlighted code with language detection
  - `auto-detect`: Automatically determines format (checks for code patterns, markdown syntax, etc.)
- **Features**: Copy to clipboard, download as file, search within output
- **Use Cases**: Display AI-generated content, show workflow results, present formatted reports

**3. json-parser (JSON String to Object)**
- **Purpose**: Parses JSON strings into JavaScript objects; extracts nested values using JSON Path
- **Technical**: Uses `JSON.parse()` with try-catch error handling; JSON Path library for nested extraction
- **JSON Path Examples**:
  - `$.user.name` → Extract name from `{ user: { name: "John" } }`
  - `$.items[*].price` → Extract all prices from array of items
  - `$..author` → Recursively find all author fields at any depth
- **Error Handling**: On parse error, returns error object with line number and character position
- **Use Cases**: Process API responses, extract data from JSON logs, parse configuration files

**4. csv-parser (CSV to Structured Data)**
- **Purpose**: Parses CSV (Comma-Separated Values) files into arrays of objects
- **Technical**: PapaParse library with streaming support for large files
- **Configuration**:
  - `delimiter`: Default comma (,) but supports semicolon (;), tab (\t), pipe (|), custom
  - `header`: First row contains column names (true) or data (false)
  - `skipEmptyLines`: Ignore empty rows
  - `trimWhitespace`: Remove leading/trailing spaces from values
- **Output Format**:
  ```json
  [
    { "name": "John", "age": "30", "city": "NYC" },
    { "name": "Jane", "age": "25", "city": "LA" }
  ]
  ```
- **Use Cases**: Import spreadsheet data, process exported CSV reports, bulk data ingestion

**5. text-splitter (Intelligent Text Chunking)**
- **Purpose**: Splits large text into smaller chunks for processing or embedding
- **Technical**: Multiple splitting strategies optimized for different use cases
- **Splitting Modes**:
  - **By Characters**: Fixed-size chunks (e.g., every 1000 characters)
    - Useful for: Token limits, uniform processing
  - **By Words**: Split at word boundaries (respects spaces)
    - Useful for: Maintaining readability, text summarization
  - **By Sentences**: Split at sentence boundaries (. ! ?)
    - Useful for: Semantic chunking, translation
  - **By Paragraphs**: Split at double newlines (\n\n)
    - Useful for: Document sections, content blocks
  - **Semantic Chunking**: AI-powered chunking that keeps related content together
    - Useful for: RAG (Retrieval-Augmented Generation), embedding generation
- **Overlap**: Configurable overlap between chunks prevents context loss at boundaries
- **Use Cases**: 
  - Prepare documents for vector embedding
  - Split long transcripts for summarization
  - Batch process large text files
  - Stay within LLM token limits

**6. text-merger (Combine Multiple Texts)**
- **Purpose**: Combines multiple text inputs into single output
- **Technical**: Array join operation with configurable separator
- **Configuration**:
  - `separator`: String inserted between merged texts (newline, comma, space, custom)
  - `removeEmpty`: Skip empty string inputs
  - `trimInputs`: Remove whitespace from each input before merging
- **Use Cases**: 
  - Combine AI-generated sections into full document
  - Merge search results into single report
  - Concatenate file contents

**7. template (Variable Substitution Engine)**
- **Purpose**: Replace placeholders in template strings with dynamic values
- **Technical**: Supports three template engines
- **Template Modes**:
  - **Simple**: Basic string interpolation with `{{variable}}` syntax
    - Example: `Hello {{name}}!` with `{name: "John"}` → `Hello John!`
  - **Handlebars**: Full-featured templates with conditionals and loops
    - Example: `{{#if premium}}VIP Access{{else}}Standard{{/if}}`
  - **Mustache**: Logic-less templates (no logic in templates, only data)
    - Example: `{{#users}}{{name}}, {{/users}}`
- **Use Cases**:
  - Generate personalized emails from template
  - Create dynamic content with user data
  - Build HTML/Markdown documents with placeholders

**8. conditional (If-Then-Else Logic)**
- **Purpose**: Routes workflow based on conditions; enables branching logic
- **Technical**: Evaluates condition and activates one of two output paths
- **Operators Supported**:
  - **Equality**: `equals`, `not equals`
  - **Comparison**: `greater than`, `less than`, `greater or equal`, `less or equal`
  - **String**: `contains`, `starts with`, `ends with`, `matches regex`
  - **Type**: `is empty`, `is null`, `is defined`
  - **Logical**: `and`, `or`, `not`
- **Multiple Conditions**: Combine conditions with AND/OR logic
- **Use Cases**:
  - Route high-priority items to urgent queue
  - Skip processing if data already exists
  - Trigger alerts when thresholds exceeded
  - Implement business rules (if customer is VIP, apply discount)

#### Data Manipulation Nodes

Data manipulation nodes provide control flow, data generation, search, and comparison capabilities essential for complex workflows.

**1. loop (Iteration Control)**
- **Purpose**: Iterate over arrays or ranges; execute sub-workflow for each item
- **Technical**: Creates sub-execution context for each iteration; manages parallel execution with concurrency limits
- **Execution Modes**:
  - **Sequential**: Process items one at a time (order guaranteed)
    - Performance: Slower but predictable
    - Use when: Order matters or items depend on previous results
  - **Parallel**: Process all items simultaneously
    - Performance: Fast but high memory usage
    - Use when: Items independent; plenty of CPU/RAM available
  - **Batch**: Process items in groups (e.g., 10 at a time)
    - Performance: Balance between speed and resource usage
    - Use when: Large datasets; limited resources
- **Configuration**:
  - `items`: Array to iterate over OR
  - `startIndex`, `endIndex`: Numeric range (e.g., 1 to 100)
  - `concurrency`: Max parallel executions (batch/parallel mode)
  - `breakOnError`: Stop all iterations if one fails (true) or continue (false)
- **Output**: Array of results (one per iteration) in original order
- **Use Cases**:
  - Process array of images (resize, filter, upload)
  - Send emails to list of recipients
  - Batch API calls with rate limiting

**2. delay (Time-Based Pause)**
- **Purpose**: Pause workflow execution for specified duration
- **Technical**: `setTimeout()` or `sleep()` function; workflow state persisted during delay
- **Configuration**:
  - `duration`: Time to wait (milliseconds, seconds, minutes)
  - `dynamic`: Calculate delay from previous node output
- **Use Cases**:
  - Rate limiting (wait between API calls)
  - Polling (check status every 5 seconds)
  - User-friendly pacing (don't overwhelm UI with rapid updates)
  - Timeout simulation for testing

**3. random-data (Test Data Generation)**
- **Purpose**: Generate random data for testing, mocking, or seeding
- **Technical**: Crypto-secure random for sensitive data; pseudo-random (Math.random) for performance
- **Data Types**:
  - **Numbers**: Integer or float within specified range
    - Config: `min`, `max`, `decimals`
  - **Strings**: Random alphanumeric strings
    - Config: `length`, `charset` (alphanumeric, alphabet, numeric, symbols)
  - **Dates**: Random date within range
    - Config: `startDate`, `endDate`, `format`
  - **Booleans**: Random true/false
  - **Arrays**: Random array of specified type
    - Config: `elementType`, `length`
  - **Objects**: Random object with specified schema
- **Use Cases**:
  - Generate test users for development
  - Mock API responses
  - Create sample datasets
  - Seed databases with realistic data

**4. uuid-generator (Unique Identifiers)**
- **Purpose**: Generate universally unique identifiers (UUIDs/GUIDs)
- **Technical**: RFC 4122 compliant UUID generation
- **UUID Versions**:
  - **v1**: Timestamp-based (includes MAC address and timestamp)
    - Use when: Need time-ordered IDs; want to extract timestamp later
  - **v4**: Random (cryptographically secure random)
    - Use when: Need maximum randomness; privacy concern (no MAC address)
  - **Custom**: User-defined format (e.g., `USER-${timestamp}-${random}`)
- **Format**: `550e8400-e29b-41d4-a716-446655440000` (32 hex chars + 4 hyphens)
- **Use Cases**:
  - Generate database primary keys
  - Create unique filenames
  - Session IDs
  - Correlation IDs for distributed tracing

**5. fuzzy-search (Approximate String Matching)**
- **Purpose**: Find strings that approximately match query (tolerates typos, misspellings)
- **Technical**: Levenshtein distance algorithm; configurable similarity threshold
- **Algorithm**: Calculates minimum number of single-character edits (insertions, deletions, substitutions) needed to change one string into another
- **Configuration**:
  - `threshold`: Similarity score 0-1 (0 = exact match required, 1 = anything matches)
  - `caseSensitive`: Ignore case differences (default: false)
  - `sortByScore`: Return best matches first
- **Example**:
  - Query: "accomodation" → Matches: "accommodation" (score: 0.92)
  - Query: "Jon Doe" → Matches: "John Doe" (score: 0.88)
- **Use Cases**:
  - Search with typo tolerance
  - Name matching (variations, nicknames)
  - Duplicate detection
  - Autocomplete/suggestions

**6. similarity-matcher (Semantic Similarity)**
- **Purpose**: Calculate how similar two texts are in meaning (not just characters)
- **Technical**: Uses embeddings or TF-IDF; cosine similarity between vectors
- **Methods**:
  - **Embedding-Based**: Convert text to vectors using sentence transformers; compare vectors
    - More accurate for semantic similarity
    - Example: "car" and "automobile" have high similarity despite different characters
  - **TF-IDF**: Statistical measure of word importance
    - Faster but less semantic understanding
- **Output**: Similarity score 0-1 (0 = completely different, 1 = identical in meaning)
- **Use Cases**:
  - Find similar documents
  - Duplicate content detection
  - Plagiarism checking
  - Content recommendation

**7. data-diff (Structure Comparison)**
- **Purpose**: Compare two data structures and output differences
- **Technical**: Deep recursive comparison; JSON diff format
- **Output Format**:
  ```json
  {
    "added": { "newField": "value" },
    "removed": { "oldField": "value" },
    "modified": {
      "changedField": { "old": "value1", "new": "value2" }
    }
  }
  ```
- **Comparison Modes**:
  - **Strict**: Types must match (string "1" ≠ number 1)
  - **Loose**: Type coercion allowed
  - **Deep**: Compare nested objects/arrays
  - **Shallow**: Compare top-level only
- **Use Cases**:
  - Detect configuration changes
  - Track data modifications
  - Version comparison
  - Change logs

**8. data-normalizer (Format Standardization)**
- **Purpose**: Convert data into consistent format across different sources
- **Technical**: Schema-based transformation with validation
- **Normalization Types**:
  - **Date Formats**: Convert various date formats to ISO 8601
    - Input: "12/31/2024", "Dec 31, 2024", "2024-12-31"
    - Output: "2024-12-31T00:00:00Z"
  - **Phone Numbers**: Standardize phone format
    - Input: "(555) 123-4567", "555-123-4567", "+15551234567"
    - Output: "+15551234567"
  - **Addresses**: Normalize address components
  - **Currency**: Standardize currency format and conversions
  - **Units**: Convert between measurement units (miles ↔ km, lbs ↔ kg)
- **Use Cases**:
  - Clean data from multiple sources before merging
  - Prepare data for database insertion
  - Standardize user inputs
  - ETL (Extract, Transform, Load) pipelines

#### File & Media Processing Nodes

File and media nodes handle file I/O operations and multimedia processing. These nodes support various formats and provide optimization capabilities for images, videos, audio, and documents.

**1. file-upload (Client-to-Server File Transfer)**
- **Purpose**: Upload files from client browser/device to server storage
- **Technical**: 
  - Uses multipart/form-data encoding for HTTP upload
  - Streams large files in chunks (1MB per chunk) to prevent memory overflow
  - Generates unique filename using UUID + original extension to prevent conflicts
  - Stores in organized directory structure: `uploads/{year}/{month}/{day}/{uuid}.ext`
- **Configuration**:
  - `maxFileSize`: Maximum allowed file size (default: 100MB)
  - `allowedTypes`: MIME type whitelist (e.g., `["image/*", "application/pdf"]`)
  - `storageLocation`: Local disk, S3, Google Cloud Storage, or Azure Blob
  - `generateThumbnail`: Auto-generate thumbnail for images/videos
- **Security**:
  - Validates file type by checking magic bytes (not just extension)
  - Scans for malware using ClamAV (optional)
  - Rejects executable files (.exe, .sh, .bat) by default
- **Output**: 
  ```json
  {
    "fileId": "550e8400-e29b-41d4-a716-446655440000",
    "filename": "document.pdf",
    "size": 1048576,
    "mimeType": "application/pdf",
    "url": "/uploads/2024/01/27/550e8400-e29b-41d4-a716-446655440000.pdf"
  }
  ```
- **Use Cases**: Upload user documents, receive images for processing, store audio recordings

**2. file-reader (File Content Extraction)**
- **Purpose**: Read file contents from local filesystem or URL
- **Technical**: 
  - Supports synchronous and asynchronous reading
  - Handles large files with streaming to prevent memory exhaustion
  - Auto-detects encoding (UTF-8, UTF-16, ASCII, etc.)
- **Reading Modes**:
  - **Text**: Reads as string (UTF-8 by default)
    - Best for: TXT, CSV, JSON, XML, HTML, code files
  - **Binary**: Reads as Buffer/ArrayBuffer
    - Best for: Images, videos, audio, executables, archives
  - **Base64**: Encodes binary as base64 string
    - Best for: Embedding in JSON, storing in database, API transmission
  - **Line-by-Line**: Streams file one line at a time
    - Best for: Large log files, CSV processing, text analysis
- **Configuration**:
  - `path`: File path (local or URL)
  - `encoding`: Text encoding (default: auto-detect)
  - `startByte`, `endByte`: Read specific byte range (useful for resume downloads)
- **Error Handling**: Gracefully handles missing files, permission errors, corrupted files
- **Use Cases**: Read configuration files, load templates, process logs, analyze documents

**3. file-writer (Persistent File Storage)**
- **Purpose**: Write or append data to files on local filesystem
- **Technical**:
  - Atomic writes (write to temp file → rename) prevents corruption
  - Creates parent directories if they don't exist
  - Supports file locking to prevent concurrent write conflicts
- **Write Modes**:
  - **Overwrite**: Replace entire file contents
  - **Append**: Add to end of existing file
  - **Insert**: Insert at specific position (line number or byte offset)
- **Configuration**:
  - `path`: Destination file path
  - `content`: Data to write (string or buffer)
  - `encoding`: Text encoding (default: UTF-8)
  - `createBackup`: Save backup of existing file before overwriting
  - `permissions`: Unix file permissions (e.g., 0644)
- **Safety Features**:
  - Validates path to prevent directory traversal attacks (../../../etc/passwd)
  - Disk space check before writing large files
  - Atomic writes prevent partial writes on crash
- **Use Cases**: Save generated reports, create log files, export data, cache results

**4. pdf-reader (PDF Content Extraction)**
- **Purpose**: Extract text, metadata, images, and tables from PDF files
- **Technical**:
  - Uses PDF.js library (same as Firefox PDF viewer)
  - Handles PDF 1.0 through 2.0 specifications
  - Supports encrypted PDFs (with password)
  - OCR integration for scanned PDFs (Tesseract.js)
- **Extraction Capabilities**:
  - **Text**: 
    - Preserves layout and formatting
    - Identifies columns, headers, footers
    - Maintains reading order
  - **Metadata**: Author, title, creation date, modification date, keywords, page count
  - **Images**: Extracts embedded images as PNG/JPEG
  - **Tables**: Detects table structures and converts to CSV/JSON
  - **Links**: Extracts hyperlinks and internal references
  - **Forms**: Reads form field values and structure
- **Configuration**:
  - `extractText`: Extract text content (default: true)
  - `extractImages`: Save images to separate files
  - `extractTables`: Convert tables to structured data
  - `ocrEnabled`: Use OCR for scanned PDFs
  - `ocrLanguage`: OCR language model (eng, spa, fra, etc.)
  - `pageRange`: Extract specific pages (e.g., "1-5,10,15-20")
- **Output Format**:
  ```json
  {
    "text": "Full document text...",
    "metadata": {
      "title": "Annual Report 2024",
      "author": "John Doe",
      "pages": 42
    },
    "images": ["image1.png", "image2.jpg"],
    "tables": [
      { "page": 5, "data": [[...]] }
    ]
  }
  ```
- **Use Cases**: Invoice processing, document analysis, data extraction, content indexing, research paper parsing

**5. image-resize (Image Dimension Adjustment)**
- **Purpose**: Change image dimensions while maintaining or ignoring aspect ratio
- **Technical**:
  - Uses Sharp library (C++ libvips bindings) for high-performance processing
  - Supports all major formats: JPEG, PNG, WebP, GIF, AVIF, TIFF, SVG
  - Hardware-accelerated on supported platforms
- **Resize Strategies**:
  - **Fit**: Scale to fit within dimensions (maintains aspect ratio, may have letterboxing)
  - **Fill**: Scale to fill dimensions (maintains aspect ratio, may crop)
  - **Cover**: Scale to cover dimensions (ignores aspect ratio, stretches if needed)
  - **Exact**: Resize to exact dimensions (ignores aspect ratio)
- **Resampling Algorithms**:
  - **Nearest Neighbor**: Fast but pixelated (for pixel art)
  - **Bilinear**: Good balance of speed and quality
  - **Bicubic**: High quality (default)
  - **Lanczos**: Best quality but slower
- **Configuration**:
  - `width`, `height`: Target dimensions (pixels or percentage)
  - `maintainAspectRatio`: Preserve original aspect ratio
  - `strategy`: Fit, fill, cover, or exact
  - `quality`: Output quality 0-100 (JPEG/WebP)
  - `outputFormat`: Convert to different format
- **Optimization**:
  - Auto-detects optimal settings for web (smaller file size)
  - Progressive JPEG for faster perceived loading
  - Strips metadata to reduce file size
- **Use Cases**: Thumbnail generation, responsive images, image optimization, social media sizing

**6. image-filter (Image Effect Application)**
- **Purpose**: Apply visual effects and adjustments to images
- **Technical**: Canvas-based pixel manipulation or Sharp/ImageMagick for complex operations
- **Filter Categories**:
  - **Basic Adjustments**:
    - Brightness: -100 to +100
    - Contrast: -100 to +100  
    - Saturation: -100 to +100 (desaturate to grayscale)
    - Hue rotation: 0-360 degrees
    - Exposure: EV adjustments
  - **Blur Effects**:
    - Gaussian blur: Radius-based smooth blur
    - Motion blur: Directional blur with angle
    - Radial blur: Zoom effect
  - **Sharpen**: Edge enhancement with configurable strength
  - **Color Effects**:
    - Sepia: Vintage brown tone
    - Grayscale: Remove all color
    - Invert: Negative image
    - Tint: Apply color overlay
  - **Advanced**:
    - Noise reduction: Remove grain/artifacts
    - Edge detection: Sobel, Canny algorithms
    - Posterize: Reduce color levels for artistic effect
    - Vignette: Darken corners
- **Configuration**:
  - `filters`: Array of filters to apply in sequence
  - `strength`: Effect intensity 0-100
  - `preview`: Generate preview before full processing
- **Use Cases**: Photo editing, artistic effects, image enhancement, preprocessing for AI models

**7. video-frame-extract (Video to Images)**
- **Purpose**: Extract individual frames from video files as images
- **Technical**:
  - Uses FFmpeg for video decoding (supports 100+ codecs)
  - Hardware-accelerated decoding when available (NVDEC, VideoToolbox)
  - Handles all common formats: MP4, AVI, MOV, MKV, WebM, FLV
- **Extraction Modes**:
  - **Interval**: Every N seconds (e.g., every 1 second)
  - **Frame Count**: Extract exactly N frames evenly distributed
  - **Specific Times**: Extract at specific timestamps
  - **All Frames**: Extract every single frame (slow, huge output)
  - **Scene Change**: Extract only when scene changes (smart sampling)
- **Configuration**:
  - `inputVideo`: Video file path or URL
  - `extractionMode`: Interval, frame count, specific times, all, scene change
  - `interval`: Seconds between frames (interval mode)
  - `frameCount`: Total frames to extract (frame count mode)
  - `timestamps`: Array of specific times (specific times mode)
  - `outputFormat`: JPEG, PNG, WebP
  - `quality`: Image quality 0-100
  - `resize`: Optionally resize frames
- **Output**: Array of image files or base64-encoded images
- **Use Cases**: 
  - Video analysis and annotation
  - Thumbnail generation from videos
  - Creating animated GIFs from video segments
  - Training data for computer vision models
  - Video summarization

**8. audio-player (Audio Playback Control)**
- **Purpose**: Play audio files with programmatic control over playback
- **Technical**:
  - Web Audio API for browser; native audio libraries for desktop/mobile
  - Supports: MP3, WAV, OGG, FLAC, AAC, M4A
  - Low-latency playback with audio buffering
- **Playback Controls**:
  - Play, pause, stop, seek to position
  - Volume: 0-100 (with mute toggle)
  - Playback speed: 0.25x to 4x (preserves pitch)
  - Loop: Single or continuous
  - Crossfade: Smooth transitions between tracks
- **Audio Processing**:
  - Equalizer: Adjust frequency bands
  - Fade in/out: Gradual volume changes
  - Normalization: Maintain consistent volume
  - Spatial audio: 3D positioning
- **Configuration**:
  - `audioSource`: File path, URL, or base64-encoded audio
  - `autoplay`: Start playing immediately
  - `volume`: Initial volume (0-100)
  - `playbackRate`: Speed multiplier
  - `loop`: Enable continuous playback
- **Events**: 
  - `onPlay`, `onPause`, `onEnded`
  - `onTimeUpdate`: Current playback position
  - `onError`: Playback failures
- **Use Cases**:
  - Text-to-speech playback
  - Audio notifications
  - Music players
  - Podcast players
  - Audio preview in file browsers

#### Network & Web Nodes

Network nodes enable HTTP communication, web scraping, and network diagnostics. Essential for API integration and web data extraction.

**1. http-request (Universal HTTP Client)**
- **Purpose**: Make HTTP requests to any URL with full control over method, headers, body, and authentication
- **Technical**:
  - Built on Axios with retry logic and timeout handling
  - Supports all HTTP methods: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
  - Automatic request/response interceptors for logging and transformation
  - Connection pooling for efficient repeated requests to same domain
- **HTTP Methods**:
  - **GET**: Retrieve data (query params in URL)
  - **POST**: Create/submit data (body)
  - **PUT**: Update entire resource (body)
  - **PATCH**: Partial update (body)
  - **DELETE**: Remove resource
  - **HEAD**: Get headers only (no body)
  - **OPTIONS**: Check allowed methods (CORS preflight)
- **Configuration**:
  - `url`: Target endpoint
  - `method`: HTTP method
  - `headers`: Custom HTTP headers (Authorization, Content-Type, etc.)
  - `body`: Request payload (JSON, form data, raw text, binary)
  - `queryParams`: URL parameters (converted to ?key=value&key2=value2)
  - `authentication`: 
    - Basic Auth (username/password)
    - Bearer Token (JWT, API key)
    - OAuth 2.0 (automatic token refresh)
    - Custom headers
  - `timeout`: Request timeout in milliseconds (default: 30000)
  - `retries`: Number of retry attempts on failure
  - `retryDelay`: Milliseconds between retries (exponential backoff)
  - `followRedirects`: Auto-follow 3xx redirects
  - `validateSSL`: Verify SSL certificates (disable for self-signed certs)
- **Response Handling**:
  - Automatically parses JSON responses
  - Converts XML to JSON if detected
  - Handles binary data (images, files)
  - Captures response headers
  - Provides status code, timing info, redirect history
- **Error Handling**:
  - Network errors (timeout, connection refused, DNS failure)
  - HTTP errors (4xx, 5xx status codes)
  - Parse errors (invalid JSON/XML)
  - Detailed error messages with request/response context
- **Output**:
  ```json
  {
    "status": 200,
    "statusText": "OK",
    "headers": { "content-type": "application/json" },
    "data": { "result": "success" },
    "timing": { "duration": 324 }
  }
  ```
- **Use Cases**:
  - API integration (fetch data, post updates)
  - Webhook callbacks
  - External service communication
  - Data synchronization
  - Microservice communication

**2. web-scraper (HTML Data Extraction)**
- **Purpose**: Extract structured data from websites by parsing HTML
- **Technical**:
  - Cheerio for fast HTML parsing (jQuery-like API)
  - Puppeteer for JavaScript-rendered pages (headless Chrome)
  - Playwright for cross-browser scraping
  - Respects robots.txt (optional)
- **Selection Methods**:
  - **CSS Selectors**: Standard CSS syntax
    - Example: `.product-title`, `div.content > p`, `#main-content`
  - **XPath**: XML Path Language for complex queries
    - Example: `//div[@class="product"]//h2/text()`
  - **Auto-Detection**: AI identifies common patterns
    - Detects: titles, prices, descriptions, images, dates, authors
- **Configuration**:
  - `url`: Target website URL
  - `selectors`: Object mapping field names to selectors
    ```json
    {
      "title": "h1.product-title",
      "price": ".price-value",
      "description": "#product-description"
    }
    ```
  - `waitForSelector`: Wait for element before scraping (for dynamic content)
  - `pagination`: Auto-follow "Next" links
  - `maxPages`: Limit pagination depth
  - `rateLimit`: Milliseconds between requests (be respectful)
  - `userAgent`: Custom user agent string
  - `cookies`: Set cookies for authenticated scraping
  - `javascript`: Enable JavaScript rendering (uses Puppeteer)
- **Anti-Blocking Features**:
  - Random user agents
  - Proxy rotation support
  - Request throttling
  - Cookie management
  - Header randomization
- **Output**: Structured JSON array of extracted data
- **Use Cases**:
  - Price monitoring/comparison
  - Content aggregation
  - Market research
  - Lead generation
  - News/article extraction
  - Product catalog scraping

**3. dns-lookup (Domain Name Resolution)**
- **Purpose**: Resolve domain names to IP addresses and retrieve DNS records
- **Technical**:
  - Uses Node.js dns module or browser DNS-over-HTTPS
  - Queries authoritative nameservers
  - Caches results to reduce lookup time
- **Query Types**:
  - **A**: IPv4 address (e.g., example.com → 93.184.216.34)
  - **AAAA**: IPv6 address
  - **CNAME**: Canonical name (alias)
  - **MX**: Mail server records (priority + hostname)
  - **TXT**: Text records (SPF, DKIM, domain verification)
  - **NS**: Nameserver records
  - **SOA**: Start of authority
  - **PTR**: Reverse lookup (IP → domain)
  - **SRV**: Service records
- **Configuration**:
  - `domain`: Domain name to lookup
  - `recordType`: A, AAAA, CNAME, MX, TXT, NS, SOA, PTR, SRV, ALL
  - `nameserver`: Custom DNS server (default: system DNS)
  - `timeout`: Query timeout
- **Output**:
  ```json
  {
    "domain": "example.com",
    "recordType": "A",
    "records": ["93.184.216.34"],
    "ttl": 86400
  }
  ```
- **Use Cases**:
  - Domain availability checking
  - Email validation (check MX records)
  - CDN detection
  - Network diagnostics
  - DNS monitoring
  - Subdomain discovery

**4. ping-test (Network Latency Check)**
- **Purpose**: Test network connectivity and measure latency to target host
- **Technical**:
  - ICMP echo request/reply (traditional ping)
  - TCP/HTTP ping for firewalled environments
  - Packet loss calculation
  - Jitter measurement (latency variance)
- **Configuration**:
  - `host`: Target hostname or IP address
  - `count`: Number of ping packets to send (default: 4)
  - `interval`: Milliseconds between packets (default: 1000)
  - `timeout`: Timeout per packet (default: 5000)
  - `packetSize`: Payload size in bytes (default: 32)
  - `ttl`: Time-to-live (max hops)
- **Metrics Collected**:
  - **Latency**: Round-trip time for each packet (min, max, avg)
  - **Packet Loss**: Percentage of lost packets
  - **Jitter**: Variation in latency
  - **Hop Count**: Number of network hops
- **Output**:
  ```json
  {
    "host": "example.com",
    "packetsTransmitted": 4,
    "packetsReceived": 4,
    "packetLoss": "0%",
    "latency": {
      "min": 23.4,
      "max": 45.2,
      "avg": 32.1,
      "jitter": 7.3
    }
  }
  ```
- **Use Cases**:
  - Network troubleshooting
  - Server monitoring
  - Connection quality testing
  - Load balancer health checks
  - ISP performance monitoring
  - Geographic latency mapping

#### Database Nodes

Database nodes provide connectivity to various database systems and caching mechanisms. Enable persistent storage and retrieval of structured data.

**1. mongodb-query (NoSQL Document Operations)**
- **Purpose**: Execute MongoDB operations for document-based data storage
- **Technical**:
  - MongoDB Node.js driver with connection pooling
  - Supports MongoDB 4.0+ (including MongoDB Atlas)
  - Automatic schema validation (optional)
  - Index optimization recommendations
- **Operations**:
  - **find**: Query documents with filters
    ```javascript
    { collection: "users", filter: { age: { $gt: 25 } }, sort: { name: 1 }, limit: 10 }
    ```
  - **findOne**: Retrieve single document
  - **insert**: Add new document(s)
  - **insertMany**: Bulk insert with ordered/unordered execution
  - **update**: Modify existing documents
  - **updateMany**: Bulk update with filters
  - **delete**: Remove documents
  - **deleteMany**: Bulk delete with filters
  - **aggregate**: Complex data transformations and analytics
    ```javascript
    [
      { $match: { status: "active" } },
      { $group: { _id: "$category", total: { $sum: "$amount" } } },
      { $sort: { total: -1 } }
    ]
    ```
  - **count**: Count documents matching filter
  - **distinct**: Get unique values for a field
- **Configuration**:
  - `connectionString`: MongoDB URI (mongodb://localhost:27017/dbname)
  - `database`: Database name
  - `collection`: Collection name
  - `operation`: find, insert, update, delete, aggregate, count, distinct
  - `filter`: Query filter (MongoDB query language)
  - `document`: Document to insert/update
  - `options`: Sort, limit, skip, projection
- **Advanced Features**:
  - Transactions (multi-document ACID operations)
  - Change streams (real-time data updates)
  - Geospatial queries ($near, $geoWithin)
  - Text search with full-text indexes
  - Array operations ($push, $pull, $addToSet)
- **Error Handling**: Connection failures, duplicate key errors, validation errors, timeout errors
- **Use Cases**:
  - User profile storage
  - Product catalogs
  - Log storage and analysis
  - Session management
  - Content management systems

**2. postgresql-query (Relational SQL Database)**
- **Purpose**: Execute SQL queries on PostgreSQL databases
- **Technical**:
  - pg (node-postgres) driver with prepared statements
  - Connection pooling (configurable pool size)
  - Automatic SQL injection prevention
  - Query result streaming for large datasets
  - Supports PostgreSQL 10+ (including cloud providers: AWS RDS, Google Cloud SQL, Azure)
- **Query Types**:
  - **SELECT**: Retrieve data with filters, joins, aggregations
    ```sql
    SELECT u.name, COUNT(o.id) as order_count
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.active = true
    GROUP BY u.id, u.name
    ORDER BY order_count DESC
    LIMIT 10
    ```
  - **INSERT**: Add new rows (with RETURNING clause)
  - **UPDATE**: Modify existing rows
  - **DELETE**: Remove rows
  - **CREATE**: Create tables, indexes, views
  - **ALTER**: Modify table schema
  - **TRANSACTION**: BEGIN, COMMIT, ROLLBACK for atomic operations
- **Configuration**:
  - `connectionString`: PostgreSQL URI (postgresql://user:pass@localhost:5432/dbname)
  - `query`: SQL query string
  - `parameters`: Parameterized query values (prevents SQL injection)
    ```json
    {
      "query": "SELECT * FROM users WHERE email = $1 AND age > $2",
      "parameters": ["user@example.com", 25]
    }
    ```
  - `timeout`: Query timeout in milliseconds
  - `streaming`: Stream results for large datasets
- **Advanced Features**:
  - JSON/JSONB operations (store and query JSON data)
  - Full-text search (to_tsvector, to_tsquery)
  - Array operations
  - Window functions (ROW_NUMBER, RANK, LAG, LEAD)
  - Common Table Expressions (WITH queries)
  - Stored procedures and functions
- **Transaction Support**:
  - Multi-query transactions
  - Savepoints for partial rollbacks
  - Isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE)
- **Output**: Array of row objects with type-safe values
- **Use Cases**:
  - Transactional systems (e-commerce, banking)
  - Analytics and reporting
  - User authentication
  - Inventory management
  - Relational data modeling

**3. cache-manager (In-Memory Caching)**
- **Purpose**: Store frequently accessed data in memory for ultra-fast retrieval
- **Technical**:
  - LRU (Least Recently Used) eviction policy
  - Optional persistence to disk (RDB snapshots)
  - Automatic expiration (TTL - Time To Live)
  - Memory limit enforcement
  - Supports multiple cache stores (in-memory, Redis, Memcached)
- **Operations**:
  - **set**: Store key-value pair with optional TTL
    ```javascript
    { key: "user:123", value: { name: "John" }, ttl: 3600 }
    ```
  - **get**: Retrieve value by key
  - **del**: Delete specific key
  - **clear**: Delete all keys
  - **has**: Check if key exists
  - **keys**: List all keys (or matching pattern)
  - **ttl**: Get remaining time-to-live
  - **expire**: Update TTL for existing key
- **Configuration**:
  - `store`: in-memory (default), redis, memcached
  - `maxSize`: Maximum memory usage (MB)
  - `defaultTTL`: Default expiration time (seconds)
  - `checkPeriod`: Interval to check for expired keys (seconds)
  - `redisUrl`: Redis connection string (if using Redis store)
- **Eviction Strategies**:
  - **LRU**: Evict least recently used items when memory full
  - **LFU**: Evict least frequently used items
  - **FIFO**: First in, first out
  - **TTL**: Remove expired items first
- **Cache Patterns**:
  - **Cache-Aside**: Application checks cache first, then database
  - **Write-Through**: Write to cache and database simultaneously
  - **Write-Behind**: Write to cache immediately, database asynchronously
- **Use Cases**:
  - API response caching
  - Session storage
  - Rate limiting counters
  - Computed results caching
  - Database query result caching
  - Reduce API call costs

**4. memory-node (Vector Database + Context Storage)**
- **Purpose**: Project-specific context storage and semantic search using vector embeddings
- **Technical**:
  - Integrated vector database (FAISS, Weaviate, Qdrant, or Chroma)
  - Embedding models (Sentence-BERT, OpenAI embeddings, Cohere)
  - Approximate nearest neighbor search (HNSW algorithm)
  - Multi-modal embeddings (text, images, audio)
- **Operations**:
  - **store**: Store text/data with automatic embedding generation
  - **retrieve**: Semantic search to find similar content
    ```javascript
    { query: "machine learning algorithms", k: 5, threshold: 0.7 }
    ```
  - **update**: Update existing stored content
  - **delete**: Remove specific entries
  - **clear**: Clear all project-specific memory
- **Configuration**:
  - `embeddingModel`: Model for generating embeddings
  - `dimensions`: Embedding vector dimensions (384, 768, 1536, etc.)
  - `similarityMetric`: Cosine, Euclidean, or Dot Product
  - `indexType`: Flat (exact search) or HNSW (approximate, faster)
  - `projectId`: Isolate memory by project
- **Metadata Storage**:
  - Store additional metadata with each vector
  - Filter search results by metadata
  - Example: Store document chunks with `{page: 5, chapter: "Introduction"}`
- **Use Cases**:
  - RAG (Retrieval-Augmented Generation) pipelines
  - Semantic document search
  - Chat history with context retrieval
  - Knowledge base queries
  - Similar content recommendations
  - Project-specific AI memory
- **Performance**:
  - Sub-millisecond search on millions of vectors
  - Horizontal scaling with sharding
  - Automatic index optimization

#### Authentication & Security Nodes

Security nodes handle authentication, authorization, and cryptographic operations essential for secure applications.

**1. jwt-generate (JSON Web Token Creation)**
- **Purpose**: Generate secure JWT tokens for stateless authentication
- **Technical**:
  - RFC 7519 compliant JWT implementation
  - Supports HS256 (HMAC + SHA-256), RS256 (RSA + SHA-256), ES256 (ECDSA + SHA-256)
  - Token structure: Header.Payload.Signature (base64url encoded)
- **Token Types**:
  - **Access Token**: Short-lived (5-15 minutes), contains user claims
  - **Refresh Token**: Long-lived (days/months), used to get new access tokens
  - **ID Token**: Contains user identity information (OpenID Connect)
- **Configuration**:
  - `payload`: Data to encode in token (user ID, roles, permissions, custom claims)
    ```json
    {
      "userId": "123",
      "email": "user@example.com",
      "roles": ["admin", "editor"],
      "customClaim": "value"
    }
    ```
  - `secret`: Signing key (for HS256) or private key (for RS256/ES256)
  - `algorithm`: HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384, ES512
  - `expiresIn`: Token lifetime ("15m", "7d", "90 days", or seconds)
  - `issuer`: Token issuer (iss claim)
  - `audience`: Intended recipient (aud claim)
  - `subject`: Subject identifier (sub claim)
  - `notBefore`: Token not valid before this time
- **Claims Included**:
  - **Registered Claims**: iss (issuer), sub (subject), aud (audience), exp (expiration), nbf (not before), iat (issued at), jti (JWT ID)
  - **Custom Claims**: Any additional data needed by application
- **Security Features**:
  - Automatic expiration checking
  - Signature verification prevents tampering
  - Token rotation support
  - Blacklist integration for revocation
- **Use Cases**:
  - User authentication after login
  - API authentication
  - Single Sign-On (SSO)
  - Stateless session management
  - Inter-service communication

**2. jwt-verify (Token Validation)**
- **Purpose**: Validate JWT tokens and extract payload data
- **Technical**:
  - Verifies signature using secret/public key
  - Checks expiration, not-before, and other time-based claims
  - Validates issuer, audience against expected values
  - Timing-safe string comparison prevents timing attacks
- **Validation Checks**:
  - **Signature**: Token hasn't been tampered with
  - **Expiration**: Token is still valid (exp claim)
  - **Not Before**: Token is already valid (nbf claim)
  - **Issuer**: Token from expected issuer (iss claim)
  - **Audience**: Token intended for this service (aud claim)
- **Configuration**:
  - `token`: JWT string to verify
  - `secret`: Signing key (for HS256) or public key (for RS256/ES256)
  - `algorithms`: Allowed algorithms (security: prevents algorithm confusion attacks)
  - `issuer`: Expected issuer (optional)
  - `audience`: Expected audience (optional)
  - `ignoreExpiration`: Skip expiration check (for testing only)
  - `clockTolerance`: Seconds of leeway for time-based checks (handles clock skew)
- **Output**:
  - **Success**: Decoded payload with all claims
  - **Failure**: Error with reason (expired, invalid signature, wrong audience, etc.)
- **Error Types**:
  - `TokenExpiredError`: Token past expiration time
  - `JsonWebTokenError`: Invalid token structure or signature
  - `NotBeforeError`: Token used before nbf time
- **Use Cases**:
  - Protect API endpoints
  - Extract user information from token
  - Validate tokens from external services
  - Implement authorization logic based on claims

**3. password-hash (Secure Password Storage)**
- **Purpose**: Hash passwords before storage to prevent plaintext leaks
- **Technical**:
  - One-way hash functions (impossible to reverse)
  - Automatic salt generation (prevents rainbow table attacks)
  - Configurable work factor (computational cost)
  - Timing-safe comparison prevents timing attacks
- **Algorithms**:
  - **bcrypt**: Industry standard, well-tested, automatic salt generation
    - Work factor (cost): 10-14 (higher = slower = more secure)
    - Recommended for most use cases
  - **argon2**: Winner of Password Hashing Competition, most secure
    - Types: Argon2i (optimized against side-channel attacks), Argon2d (optimized against GPU attacks), Argon2id (hybrid)
    - Memory cost, time cost, parallelism configurable
    - Best for high-security applications
  - **scrypt**: Memory-hard function, resistant to hardware attacks
    - CPU cost, memory cost, parallelization configurable
  - **PBKDF2**: Older but still acceptable, widely supported
    - Iteration count: 100,000+ recommended
- **Configuration**:
  - `password`: Plain text password to hash
  - `algorithm`: bcrypt (default), argon2, argon2i, argon2d, argon2id, scrypt, pbkdf2
  - `workFactor`: Computational cost (algorithm-specific)
    - bcrypt: 10-14 (rounds)
    - argon2: memory cost (KB), time cost (iterations), parallelism (threads)
    - scrypt: N (CPU/memory cost), r (block size), p (parallelization)
    - pbkdf2: iterations (100,000+)
- **Output**: Hashed password string (includes algorithm, salt, and hash)
  - Example: `$2b$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy`
- **Password Verification**: Use companion function to verify password against hash
  ```javascript
  const isValid = await verifyPassword(plainPassword, hashedPassword);
  ```
- **Security Best Practices**:
  - Never log or transmit passwords in plain text
  - Use HTTPS for password submission
  - Implement rate limiting on login attempts
  - Require strong passwords (length, complexity)
  - Consider multi-factor authentication
- **Use Cases**:
  - User registration (hash before saving)
  - Password changes
  - Admin password resets
  - Application secrets storage

#### Hardware & Sensor Nodes

Hardware nodes provide direct access to device sensors and peripherals, enabling IoT, mobile, and interactive applications.

**1. camera-capture (Image/Video Capture)**
- **Purpose**: Capture photos or video streams from device camera
- **Technical**:
  - MediaDevices API (browser) or platform-specific camera APIs
  - Supports front and rear cameras on mobile devices
  - Hardware acceleration when available
- **Capture Modes**:
  - **Photo**: Single image capture
  - **Burst**: Multiple photos in quick succession
  - **Video**: Record video stream to file
  - **Stream**: Continuous frame capture for real-time processing
- **Configuration**:
  - `facingMode`: user (front camera) or environment (rear camera)
  - `resolution`: Width x height (e.g., 1920x1080, 4K, 8K)
  - `frameRate`: FPS for video (15, 30, 60, 120)
  - `format`: JPEG, PNG, WebP for images; MP4, WebM for video
  - `quality`: Compression quality 0-100
  - `flashMode`: on, off, auto, torch (continuous light)
  - `focusMode`: auto, manual, continuous
  - `exposureCompensation`: EV adjustment (-2 to +2)
- **Features**:
  - Auto-focus and tap-to-focus
  - Digital zoom (pinch/slider)
  - Flash/torch control
  - Exposure and white balance adjustment
  - Face detection overlay
  - Grid lines and leveling guides
- **Use Cases**:
  - QR code scanning
  - Document scanning
  - Facial recognition
  - Augmented reality
  - Video conferencing
  - Photo editing apps

**2. microphone-record (Audio Input)**
- **Purpose**: Record audio from device microphone
- **Technical**:
  - Web Audio API or platform audio APIs
  - Real-time audio processing with low latency
  - Supports multiple audio input devices
- **Recording Options**:
  - **Duration**: Fixed duration or until stopped
  - **Quality**: Sample rate (8kHz-96kHz), bit depth (16-bit, 24-bit)
  - **Channels**: Mono (1), Stereo (2), Multi-channel (5.1, 7.1)
  - **Format**: WAV (uncompressed), MP3, OGG, AAC, FLAC
- **Configuration**:
  - `deviceId`: Specific microphone (if multiple available)
  - `sampleRate`: Audio sample rate (44100 Hz default, 48000 Hz for professional)
  - `bitDepth`: 16-bit or 24-bit
  - `channels`: 1 (mono) or 2 (stereo)
  - `format`: Output format (wav, mp3, ogg, aac)
  - `echoCancellation`: Remove echo for voice calls
  - `noiseSuppression`: Reduce background noise
  - `autoGainControl`: Normalize volume levels
- **Audio Processing**:
  - Real-time waveform visualization
  - Volume meter (dB levels)
  - Silence detection (auto-stop when silent)
  - Voice activity detection
  - Frequency analysis (FFT)
- **Use Cases**:
  - Voice commands
  - Speech-to-text
  - Voice notes
  - Podcasting
  - Music recording
  - Audio interviews

**3. screen-capture (Screenshot/Screen Recording)**
- **Purpose**: Capture screenshots or record screen activity
- **Technical**:
  - Screen Capture API (browser) or platform APIs
  - Captures entire screen, specific window, or browser tab
  - Hardware-accelerated encoding
- **Capture Modes**:
  - **Screenshot**: Single image of screen/window
  - **Recording**: Video of screen activity
  - **Streaming**: Real-time screen sharing
- **Configuration**:
  - `source`: fullscreen, window, browser-tab
  - `resolution`: Capture resolution (matches source or downscaled)
  - `cursor`: Include mouse cursor (true/false)
  - `audio`: Capture system audio and/or microphone
  - `format`: PNG, JPEG for screenshots; MP4, WebM for video
  - `frameRate`: Video FPS (15, 30, 60)
- **Use Cases**:
  - Tutorial videos
  - Bug reports with screenshots
  - Screen sharing/presentations
  - Compliance recording
  - Remote support

**4. geolocation-tracker (GPS Positioning)**
- **Purpose**: Get device location coordinates and track movement
- **Technical**:
  - GPS, WiFi triangulation, cell tower positioning
  - Accuracy varies by method and environment
  - Battery-efficient background tracking
- **Data Provided**:
  - **Coordinates**: Latitude, longitude (decimal degrees)
  - **Altitude**: Meters above sea level
  - **Accuracy**: Horizontal accuracy radius (meters)
  - **Heading**: Direction of travel (0-360 degrees, 0=North)
  - **Speed**: Current speed (meters/second)
  - **Timestamp**: When position was determined
- **Configuration**:
  - `enableHighAccuracy`: Use GPS (accurate but battery-intensive) vs WiFi/cell (less accurate but battery-friendly)
  - `timeout`: Maximum time to wait for position (milliseconds)
  - `maximumAge`: Accept cached position if fresher than this (milliseconds)
  - `trackingMode`: single (one-time position) or continuous (track movement)
  - `distanceFilter`: Only report new position if moved N meters
- **Use Cases**:
  - Maps and navigation
  - Location-based services
  - Geotagging photos/posts
  - Delivery tracking
  - Fitness tracking
  - Store/restaurant finders

**5. compass-reader (Magnetic Heading)**
- **Purpose**: Determine device orientation relative to magnetic north
- **Technical**: Magnetometer sensor readings
- **Data**:
  - **Heading**: Degrees from magnetic north (0-360)
  - **Accuracy**: Heading accuracy estimate
  - **NeedsCalibration**: Whether compass needs calibration
- **Use Cases**: Navigation, AR applications, panorama photo stitching

**6. accelerometer-reader (Motion Detection)**
- **Purpose**: Detect device acceleration and orientation changes
- **Technical**: MEMS accelerometer sensor (3-axis: x, y, z)
- **Data**:
  - **Acceleration**: m/s² on each axis (including gravity)
  - **Acceleration Without Gravity**: Linear acceleration only
  - **Rotation Rate**: Degrees/second for each axis
- **Use Cases**: Gesture controls, shake detection, step counting, fall detection, orientation detection

**7. gyroscope-reader (Rotation Tracking)**
- **Purpose**: Measure device rotation rate
- **Technical**: MEMS gyroscope sensor (3-axis angular velocity)
- **Data**: Rotation rate (degrees/second or radians/second) around x, y, z axes
- **Use Cases**: VR/AR tracking, image stabilization, 3D controls, rotation gestures

**8. battery-monitor (Power Status)**
- **Purpose**: Monitor device battery level and charging state
- **Technical**: Battery Status API
- **Data**:
  - **Level**: Battery percentage (0.0 to 1.0)
  - **Charging**: Boolean (plugged in or not)
  - **ChargingTime**: Minutes until fully charged (or Infinity if not charging)
  - **DischargingTime**: Minutes until battery depleted (or Infinity if charging)
- **Events**: Trigger on battery level change, charging state change
- **Use Cases**: Low battery warnings, power-saving mode triggers, battery health monitoring

**9. network-status (Connectivity Detection)**
- **Purpose**: Monitor network connection type and quality
- **Technical**: Network Information API
- **Data**:
  - **Type**: none, ethernet, wifi, cellular (2g, 3g, 4g, 5g), bluetooth
  - **Effective Type**: slow-2g, 2g, 3g, 4g (based on actual performance)
  - **Downlink**: Estimated bandwidth (Mbps)
  - **RTT**: Round-trip time (milliseconds)
  - **SaveData**: User's data saver preference
  - **Online**: Currently connected to network
- **Use Cases**: Adaptive quality (video streaming), offline mode activation, sync optimization, connection warnings

#### QR Code & Barcode Nodes

QR codes and barcodes enable quick data encoding/decoding for inventory, payments, authentication, and information sharing.

**1. qr-code-scanner (QR Code Reading)**
- **Purpose**: Decode QR codes from camera stream or image files
- **Technical**:
  - jsQR library for browser, ZXing for native
  - Real-time camera scanning with auto-focus
  - Image processing (contrast adjustment, rotation correction)
  - Multi-code detection (scan multiple QR codes in one image)
- **Data Extracted**:
  - **Text**: Plain text content
  - **URL**: Automatic URL detection
  - **Contact**: vCard format (name, phone, email)
  - **WiFi**: SSID, password, security type
  - **Email**: Recipient, subject, body
  - **SMS**: Phone number, message content
  - **Location**: Geo coordinates
- **Configuration**:
  - `inputSource`: camera (live stream) or image (file/URL)
  - `continuous`: Scan continuously until stopped
  - `beep`: Audible feedback on successful scan
  - `vibrate`: Haptic feedback (mobile devices)
  - `highlightCode`: Draw rectangle around detected code
- **Use Cases**: Product lookups, payment processing, ticket validation, WiFi sharing, contact exchange

**2. qr-code-generator (QR Code Creation)**
- **Purpose**: Generate QR codes encoding any data type
- **Technical**:
  - Error correction levels (L, M, Q, H) - up to 30% data recovery
  - Version auto-selection (1-40) based on data size
  - Customizable appearance and branding
- **Data Types**:
  - Text, URL, Email, SMS, Phone, WiFi, vCard, Event, Location, App Store link
- **Customization**:
  - `size`: Pixels (recommended: 200-1000)
  - `errorCorrection`: L (7%), M (15%), Q (25%), H (30%)
  - `foregroundColor`: QR code color (default: black)
  - `backgroundColor`: Background color (default: white)
  - `logo`: Embed logo in center (reduces scan reliability)
  - `quietZone`: White border around code (recommended: 4 modules)
  - `outputFormat`: PNG, SVG, PDF, Base64
- **Use Cases**: Share URLs, encode contact info, WiFi credentials, payment info, app deep links

**3. barcode-scanner (Linear Barcode Reading)**
- **Purpose**: Decode 1D and 2D barcodes from camera or images
- **Technical**: ZXing library supporting 20+ barcode formats
- **Supported Formats**:
  - **1D**: UPC-A, UPC-E, EAN-8, EAN-13, CODE-39, CODE-93, CODE-128, ITF, Codabar
  - **2D**: QR Code, Data Matrix, Aztec, PDF417
- **Configuration**:
  - `formats`: Specific formats to scan (improves speed)
  - `tryHarder`: More aggressive scanning (slower but more accurate)
  - `multiple`: Detect multiple barcodes in one image
- **Use Cases**: Inventory management, point-of-sale, library systems, shipping/logistics

**4. barcode-generator (Barcode Creation)**
- **Purpose**: Generate linear and 2D barcodes
- **Technical**: JsBarcode library with extensive format support
- **Formats Available**:
  - CODE128, CODE39, EAN13, EAN8, UPC, ITF14, MSI, Pharmacode
- **Configuration**:
  - `format`: Barcode type
  - `width`: Bar width (1-4 pixels)
  - `height`: Barcode height (pixels)
  - `displayValue`: Show human-readable text below barcode
  - `fontSize`: Text size
  - `margin`: White space around barcode
  - `outputFormat`: PNG, SVG, Base64
- **Use Cases**: Product labeling, shipping labels, inventory tags, asset tracking

---

#### Mapping & Geocoding Nodes

Location services enable map visualization, address resolution, and geographic data processing.

**1. map-renderer (Interactive Maps)**
- **Purpose**: Display interactive maps with markers, routes, and overlays
- **Technical**:
  - Supports Google Maps, Mapbox, OpenStreetMap (Leaflet)
  - Vector tiles for smooth zooming
  - GPU-accelerated rendering
  - Offline map support (pre-downloaded tiles)
- **Map Providers**:
  - **Google Maps**: Most accurate, comprehensive data, requires API key (paid)
  - **Mapbox**: Customizable styling, good performance, requires API key (paid tier for high usage)
  - **OpenStreetMap**: Free, open-source, community-maintained
- **Features**:
  - **Markers**: Custom pins with popups, clustering for many markers
  - **Polylines**: Draw routes, boundaries, trails
  - **Polygons**: Highlight areas, regions, zones
  - **Heatmaps**: Visualize density data
  - **Directions**: Turn-by-turn navigation
  - **Geocoding**: Search places by name
  - **Geofencing**: Trigger events when entering/exiting areas
- **Configuration**:
  - `provider`: google-maps, mapbox, openstreetmap
  - `center`: Initial map center (lat, lng)
  - `zoom`: Initial zoom level (1-20)
  - `markers`: Array of marker objects with coordinates and popups
  - `routes`: Array of coordinate paths to draw
  - `style`: Map theme (standard, satellite, terrain, dark, custom)
- **Use Cases**: Store locators, delivery tracking, geofencing, route planning, location visualization

**2. geocoding (Address ↔ Coordinates)**
- **Purpose**: Convert addresses to coordinates (geocoding) and coordinates to addresses (reverse geocoding)
- **Technical**:
  - Multiple providers: Google Maps, Mapbox, OpenStreetMap (Nominatim)
  - Caching to reduce API costs
  - Batch geocoding support
- **Operations**:
  - **Forward Geocoding**: Address → Coordinates
    - Input: "1600 Amphitheatre Parkway, Mountain View, CA"
    - Output: {lat: 37.4224764, lng: -122.0842499}
  - **Reverse Geocoding**: Coordinates → Address
    - Input: {lat: 37.4224764, lng: -122.0842499}
    - Output: "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA"
- **Configuration**:
  - `provider`: google, mapbox, nominatim
  - `address`: Address string for forward geocoding
  - `lat`, `lng`: Coordinates for reverse geocoding
  - `language`: Preferred language for results
  - `region`: Bias results to region (country code)
- **Response Details**:
  - Formatted address
  - Address components (street, city, state, zip, country)
  - Coordinates (lat, lng)
  - Place type (street address, city, landmark, etc.)
  - Bounding box
- **Use Cases**: Validate addresses, calculate distances, find nearby locations, display addresses on maps

---

#### Advanced Control Flow Nodes

These nodes implement sophisticated flow control patterns for complex business logic and system reliability.

**1. rules-engine (Business Rules)**
- **Purpose**: Execute complex business logic based on configurable rules
- **Technical**:
  - Rule evaluation engine with boolean logic
  - Priority-based rule execution
  - Conflict resolution strategies
- **Rule Structure**:
  ```json
  {
    "name": "VIP Discount Rule",
    "conditions": {
      "all": [
        { "fact": "userType", "operator": "equal", "value": "VIP" },
        { "fact": "orderTotal", "operator": "greaterThan", "value": 100 }
      ]
    },
    "actions": [
      { "type": "applyDiscount", "params": { "percent": 20 } },
      { "type": "sendEmail", "params": { "template": "vip-thank-you" } }
    ]
  }
  ```
- **Operators**: equal, notEqual, greaterThan, lessThan, contains, in, matches (regex)
- **Logic**: all (AND), any (OR), not (NOT)
- **Use Cases**: Pricing rules, approval workflows, eligibility checks, automated decisions

**2. state-machine (Finite State Machine)**
- **Purpose**: Model workflows with explicit states and transitions
- **Technical**:
  - Deterministic state transitions
  - State persistence across sessions
  - Transition guards (conditions for allowing transition)
  - Entry/exit actions for states
- **State Machine Definition**:
  ```json
  {
    "initial": "draft",
    "states": {
      "draft": {
        "on": { "submit": "pending_review" }
      },
      "pending_review": {
        "on": {
          "approve": "approved",
          "reject": "draft"
        }
      },
      "approved": {
        "on": { "publish": "published" }
      },
      "published": { "type": "final" }
    }
  }
  ```
- **Features**:
  - State history for audit trails
  - Parallel states (multiple substates active simultaneously)
  - Nested state machines (hierarchical states)
- **Use Cases**: Order processing, approval workflows, game states, document lifecycle, chatbot conversations

**3. task-scheduler (Cron Job Management)**
- **Purpose**: Schedule tasks to run at specific times or intervals
- **Technical**:
  - Cron expression parser (standard Unix cron syntax)
  - Persistent scheduling (survives server restarts)
  - Timezone support
  - Missed execution handling
- **Cron Syntax**:
  ```
  ┌─────────── second (0-59) [optional]
  │ ┌────────── minute (0-59)
  │ │ ┌──────── hour (0-23)
  │ │ │ ┌────── day of month (1-31)
  │ │ │ │ ┌──── month (1-12)
  │ │ │ │ │ ┌── day of week (0-7, 0/7 = Sunday)
  │ │ │ │ │ │
  * * * * * *
  ```
- **Examples**:
  - `0 0 * * *` - Daily at midnight
  - `*/15 * * * *` - Every 15 minutes
  - `0 9 * * 1-5` - Weekdays at 9 AM
  - `0 0 1 * *` - First day of every month
- **Features**:
  - One-time or recurring schedules
  - Start/end dates for schedules
  - Max executions limit
  - Execution history
- **Use Cases**: Data backups, report generation, cleanup tasks, reminder notifications, batch processing

**4. circuit-breaker (Fault Tolerance)**
- **Purpose**: Prevent cascading failures by stopping requests to failing services
- **Technical**:
  - Three states: Closed (normal), Open (failing), Half-Open (testing recovery)
  - Failure threshold triggers opening
  - Timeout for retry attempts
- **State Transitions**:
  - **Closed → Open**: After N consecutive failures
  - **Open → Half-Open**: After timeout period
  - **Half-Open → Closed**: After successful test request
  - **Half-Open → Open**: If test request fails
- **Configuration**:
  - `failureThreshold`: Failures before opening (default: 5)
  - `timeout`: Milliseconds before attempting half-open (default: 60000)
  - `successThreshold`: Successes in half-open before closing (default: 2)
- **Use Cases**: API resilience, database connection management, microservice communication, prevent overload

---

#### Scheduling & Event Triggers

Event-driven architecture enables workflows to react to external events automatically.

**1. Cron/Timer Triggers**
- Schedule workflows with cron expressions or intervals
- One-time or recurring execution
- Timezone-aware scheduling
- Example: Daily report generation, hourly data sync, monthly billing

**2. Webhooks**
- Expose HTTP endpoints that trigger workflows when called
- Validate webhook signatures (HMAC, JWT)
- Parse webhook payloads (JSON, form data, XML)
- Example: GitHub commit triggers CI/CD, Stripe payment triggers fulfillment

**3. File Watchers**
- Monitor directories for file changes (create, modify, delete)
- Filter by file extension or pattern
- Debounce rapid changes
- Example: Auto-process uploaded files, backup changed files

**4. Email Triggers**
- Trigger workflows on incoming emails
- Parse email content, attachments, headers
- Filter by sender, subject, body keywords
- Example: Support ticket creation, invoice processing, newsletter signups

**5. Queue Listeners**
- Subscribe to message queues (RabbitMQ, Kafka, Redis, SQS)
- Automatic message acknowledgment and retry
- Dead-letter queue for failed messages
- Example: Process orders from queue, handle async tasks, event sourcing

**6. Event-Based Scheduling UI**
- Visual interface for configuring triggers
- Retry policies: fixed delay, exponential backoff, max attempts
- Backoff strategies for rate-limited APIs
- Alert configuration for failed triggers
- Execution history and debugging

---

#### Notification Nodes

**notification (System Notifications)**
- **Purpose**: Display notifications to users via browser/system
- **Technical**:
  - Notification API (browser), native notifications (desktop/mobile)
  - Permission-based (user must grant notification permission)
- **Types**:
  - **Toast**: Brief popup message that auto-dismisses
  - **Persistent**: Remains until user dismisses
  - **Action**: Includes clickable buttons
- **Configuration**:
  - `title`: Notification title (required)
  - `body`: Message content
  - `icon`: Image URL for notification icon
  - `badge`: Badge icon for mobile devices
  - `sound`: Audio file to play (on supported platforms)
  - `actions`: Array of action buttons
  - `requireInteraction`: Keep visible until user interacts
  - `tag`: Group related notifications
- **Use Cases**: Task completion alerts, error notifications, reminder prompts, status updates

---

**Summary of Implemented Nodes:**
- **Text Processing**: 8 nodes for string manipulation and parsing
- **Data Manipulation**: 8 nodes for iteration, generation, and comparison
- **File & Media**: 8 nodes for file I/O and multimedia processing
- **Network & Web**: 4 nodes for HTTP and web operations
- **Database**: 4 nodes for data persistence and caching
- **Authentication**: 3 nodes for security and auth
- **Hardware & Sensors**: 9 nodes for device access
- **QR & Barcodes**: 4 nodes for code generation/scanning
- **Mapping**: 2 nodes for location services
- **Control Flow**: 4 nodes for advanced logic patterns
- **Scheduling**: 6 trigger types for event-driven workflows
- **Notifications**: 1 node for user alerts

**Total**: 61 production-ready nodes covering all major workflow requirements

### 1.3 Planned Nodes (From utilityNodesImplementation.json)

These nodes are planned for future implementation and will expand OLAI's integration ecosystem and workflow capabilities. Each node has been prioritized and scoped for development.

---

#### Database Nodes (Pending Implementation)

**1. mysql-query (MySQL Database Operations)**
- **Priority**: High | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Execute SQL queries against MySQL databases
- **Technical**:
  - MySQL2 driver with connection pooling
  - Supports MySQL 5.7+ and MariaDB
  - Prepared statements for SQL injection prevention
  - Transaction support with rollback
  - Query result streaming for large datasets
- **Operations**:
  - SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP
  - Stored procedures and functions
  - Bulk operations
  - Transactions (BEGIN, COMMIT, ROLLBACK)
- **Configuration**:
  - `connectionString`: MySQL connection URI
  - `query`: SQL query with parameterized placeholders
  - `parameters`: Array of values for prepared statements
  - `timeout`: Query timeout (milliseconds)
  - `multipleStatements`: Allow multiple SQL statements
- **Advanced Features**:
  - Master-slave replication support (read from replicas)
  - Connection retry with exponential backoff
  - Query logging and performance monitoring
  - Result pagination for large datasets
- **Use Cases**: E-commerce systems, CMS platforms, legacy system integration, transactional applications

**2. redis-query (Redis Key-Value Operations)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Perform operations on Redis in-memory data store
- **Technical**:
  - ioredis library with cluster and sentinel support
  - Pipelining for batch operations
  - Pub/Sub for real-time messaging
  - Lua script execution
  - Supports Redis 5.0+
- **Operations**:
  - **String**: GET, SET, INCR, DECR, APPEND
  - **Hash**: HGET, HSET, HGETALL, HDEL
  - **List**: LPUSH, RPUSH, LPOP, RPOP, LRANGE
  - **Set**: SADD, SREM, SMEMBERS, SINTER, SUNION
  - **Sorted Set**: ZADD, ZREM, ZRANGE, ZRANK
  - **Pub/Sub**: PUBLISH, SUBSCRIBE, PSUBSCRIBE
  - **Transactions**: MULTI, EXEC, WATCH
  - **Scripting**: EVAL (Lua scripts)
- **Configuration**:
  - `host`, `port`: Redis server connection
  - `password`: Authentication password
  - `database`: Database number (0-15)
  - `operation`: Command to execute
  - `key`: Key name
  - `value`: Value to store
  - `ttl`: Expiration time (seconds)
  - `cluster`: Enable cluster mode
- **Use Cases**: Session storage, real-time leaderboards, pub/sub messaging, rate limiting, distributed locks

**3. sqlite-query (Embedded Database)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Execute SQL queries on embedded SQLite databases
- **Technical**:
  - better-sqlite3 (synchronous) or sqlite3 (async)
  - File-based database (no server required)
  - ACID compliance
  - Full-text search support
  - JSON1 extension for JSON operations
- **Features**:
  - Zero configuration - just specify file path
  - Single-file database (easy backup and portability)
  - Supports up to 281 TB database size
  - Concurrent readers (single writer)
  - In-memory databases for testing (`:memory:`)
- **Configuration**:
  - `databasePath`: Path to SQLite file
  - `query`: SQL query string
  - `parameters`: Parameterized query values
  - `mode`: readonly, readwrite, or create
  - `enableWAL`: Write-Ahead Logging for better concurrency
- **Use Cases**: Mobile apps, desktop applications, local data storage, prototyping, embedded systems

**4. firebase-firestore (Cloud NoSQL Database)**
- **Priority**: High | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Read and write documents using Google Firebase Firestore
- **Technical**:
  - Firebase Admin SDK for server-side
  - Real-time listeners for data synchronization
  - Offline persistence
  - Automatic multi-region replication
  - Strong consistency guarantees
- **Operations**:
  - **get**: Retrieve document(s)
  - **set**: Create or overwrite document
  - **add**: Create document with auto-generated ID
  - **update**: Partially update document
  - **delete**: Remove document
  - **query**: Filter and sort collections
  - **transaction**: Atomic multi-document operations
  - **batch**: Batch write operations
- **Query Capabilities**:
  - Filter: `where('age', '>=', 18)`
  - Sort: `orderBy('name', 'asc')`
  - Limit: `limit(10)`
  - Pagination: `startAfter(lastDoc)`
  - Array operations: `array-contains`, `in`
- **Configuration**:
  - `serviceAccountKey`: Firebase credentials JSON
  - `collection`: Collection path
  - `documentId`: Specific document (optional)
  - `operation`: get, set, add, update, delete, query
  - `data`: Document data
  - `filters`: Query filters
- **Real-time Features**:
  - Listen to document/collection changes
  - Receive updates when data changes
  - Automatic conflict resolution
- **Use Cases**: Real-time applications, mobile backends, collaborative tools, chat systems, user-generated content

**5. firebase-auth (User Authentication)**
- **Priority**: High | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Authenticate users with Firebase (email/password, OAuth providers, phone)
- **Technical**:
  - Firebase Authentication SDK
  - JWT-based session management
  - Multi-factor authentication support
  - Built-in security rules
- **Authentication Methods**:
  - Email/password
  - Email link (passwordless)
  - Phone (SMS verification)
  - OAuth providers (Google, Facebook, Twitter, GitHub, Apple)
  - Anonymous authentication
  - Custom token authentication
- **Operations**:
  - Sign up new users
  - Sign in existing users
  - Sign out
  - Reset password
  - Verify email
  - Update profile (display name, photo URL)
  - Manage sessions
  - Delete user account
- **Configuration**:
  - `serviceAccountKey`: Firebase credentials
  - `operation`: signup, signin, signout, resetPassword, verifyEmail
  - `email`, `password`: User credentials
  - `provider`: OAuth provider (google, facebook, github, etc.)
  - `phoneNumber`: For phone authentication
- **Security Features**:
  - Built-in email verification
  - Account enumeration protection
  - Rate limiting on authentication attempts
  - Automatic token refresh
- **Use Cases**: User authentication, social login, mobile app auth, web app login, multi-tenant applications

**6. firebase-storage (Cloud File Storage)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Upload and download binary assets to Firebase Cloud Storage
- **Technical**:
  - Built on Google Cloud Storage
  - Client and server-side SDKs
  - Resumable uploads for large files
  - Automatic CDN distribution
- **Operations**:
  - Upload files (single, multipart, resumable)
  - Download files (URL, stream, buffer)
  - Delete files
  - List files in directory
  - Get metadata
  - Update metadata
  - Generate signed URLs (temporary access)
- **Configuration**:
  - `serviceAccountKey`: Firebase credentials
  - `bucket`: Storage bucket name
  - `path`: File path in storage
  - `operation`: upload, download, delete, list, getMetadata
  - `file`: File to upload
  - `contentType`: MIME type
  - `metadata`: Custom metadata
- **Security**:
  - Security rules for access control
  - Firebase Authentication integration
  - CORS configuration
  - Signed URLs for temporary access
- **Use Cases**: User uploads (photos, documents), CDN hosting, media storage, backups, file sharing

**7. supabase-query (Open-Source Firebase Alternative)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Run SQL queries and RPC calls against Supabase (PostgreSQL backend)
- **Technical**:
  - Built on PostgreSQL with REST API layer
  - Row-level security (RLS)
  - Real-time subscriptions
  - PostgREST for automatic API generation
- **Operations**:
  - SELECT, INSERT, UPDATE, DELETE (via API)
  - RPC (call PostgreSQL functions)
  - Real-time subscriptions
  - Full-text search
  - Filters, ordering, pagination
- **Configuration**:
  - `supabaseUrl`: Project URL
  - `supabaseKey`: API key (anon or service role)
  - `table`: Table name
  - `operation`: select, insert, update, delete, rpc
  - `filters`: Query filters
  - `data`: Data to insert/update
- **Use Cases**: Web applications, mobile backends, real-time dashboards, open-source alternatives to Firebase

**8. supabase-auth (Supabase Authentication)**
- **Priority**: High | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Handle Supabase user sign-up, sign-in, and session management
- **Technical**:
  - Built on GoTrue (open-source auth server)
  - JWT-based authentication
  - Magic link support
  - OAuth provider integration
- **Authentication Methods**:
  - Email/password
  - Magic link (passwordless)
  - Phone (SMS OTP)
  - OAuth (Google, GitHub, GitLab, Bitbucket, etc.)
  - SAML SSO (enterprise)
- **Configuration**:
  - `supabaseUrl`: Project URL
  - `supabaseKey`: API key
  - `operation`: signUp, signIn, signOut, resetPassword
  - `email`, `password`: User credentials
  - `provider`: OAuth provider
- **Use Cases**: User authentication for web/mobile apps, passwordless login, social authentication

---

#### Cloud Storage Nodes (Pending Implementation)

**1. google-cloud-storage (GCS File Storage)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Upload files to Google Cloud Storage buckets
- **Technical**:
  - @google-cloud/storage SDK
  - Multi-regional, dual-regional, and regional buckets
  - Lifecycle management
  - Object versioning
  - Customer-managed encryption keys (CMEK)
- **Operations**:
  - Upload (simple, multipart, resumable)
  - Download
  - Delete
  - Copy/move
  - List objects
  - Set permissions (ACL)
  - Generate signed URLs
- **Configuration**:
  - `keyFile`: Service account JSON
  - `bucketName`: GCS bucket
  - `destinationPath`: Object path
  - `file`: File to upload
  - `metadata`: Custom metadata
  - `storageClass`: STANDARD, NEARLINE, COLDLINE, ARCHIVE
  - `public`: Make file publicly accessible
- **Use Cases**: Large-scale file storage, CDN origin, data lakes, backup storage, media hosting

**2. dropbox-upload (Dropbox File Upload)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Upload files to Dropbox
- **Technical**:
  - Dropbox API v2
  - OAuth 2.0 authentication
  - Chunked uploading for large files
  - Automatic retry on failure
- **Configuration**:
  - `accessToken`: OAuth access token
  - `path`: Destination path in Dropbox
  - `file`: File to upload
  - `mode`: add (error if exists), overwrite, or update
  - `autorename`: Auto-rename if conflict
- **Use Cases**: User file backups, document storage, photo backup, collaborative file sharing

**3. onedrive-upload (Microsoft OneDrive Upload)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Upload files to OneDrive
- **Technical**:
  - Microsoft Graph API
  - OAuth 2.0 authentication
  - Resumable upload sessions for large files
  - Supports personal and business accounts
- **Configuration**:
  - `accessToken`: OAuth token
  - `path`: Destination path
  - `file`: File to upload
  - `conflictBehavior`: rename, replace, or fail
- **Use Cases**: Enterprise file storage, Office 365 integration, document management

**4. ipfs-upload (Decentralized Storage)**
- **Priority**: Low | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Store files and metadata on IPFS (InterPlanetary File System)
- **Technical**:
  - IPFS HTTP client or js-ipfs
  - Content-addressed storage (CID - Content Identifier)
  - Distributed file system
  - Pinning services for persistence (Pinata, Infura, Web3.Storage)
- **Operations**:
  - Add file to IPFS
  - Pin file (prevent garbage collection)
  - Retrieve file by CID
  - List pinned files
  - Unpin file
- **Configuration**:
  - `ipfsNode`: IPFS node URL or local node
  - `file`: File to upload
  - `pin`: Pin file for persistence
  - `wrapWithDirectory`: Preserve filename
  - `pinningService`: Pinata, Infura, Web3.Storage credentials
- **Output**: CID (Content Identifier) - immutable hash of content
- **Use Cases**: NFT metadata storage, decentralized apps, censorship-resistant storage, permanent web hosting

**5. json-file-storage (Structured File Persistence)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Persist structured data to local or remote JSON files
- **Technical**:
  - File-based JSON storage with atomic writes
  - Schema validation (optional)
  - Automatic formatting (pretty-print)
  - Supports nested object updates
- **Operations**:
  - Read entire JSON file
  - Write JSON data
  - Update specific keys/paths
  - Append to arrays
  - Query with JSON path expressions
- **Configuration**:
  - `filePath`: JSON file path
  - `operation`: read, write, update, append
  - `data`: Data to write/update
  - `jsonPath`: Path to specific key (e.g., `users[0].name`)
  - `createIfNotExists`: Auto-create file
  - `pretty`: Pretty-print JSON (default: true)
- **Use Cases**: Configuration files, simple databases, data export, testing fixtures, local caching

---

#### AI & Model Nodes (Pending Implementation)

**1. huggingface-inference (Model Inference)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Run inference on Hugging Face hosted models
- **Technical**:
  - Hugging Face Inference API
  - Supports 150,000+ models
  - Serverless inference (no model hosting required)
  - Automatic model loading and caching
- **Supported Tasks**:
  - Text generation, classification, summarization
  - Translation, question answering
  - Image classification, segmentation, object detection
  - Audio transcription, classification
  - Zero-shot classification
  - Feature extraction (embeddings)
- **Configuration**:
  - `apiKey`: Hugging Face API token
  - `model`: Model ID (e.g., `gpt2`, `bert-base-uncased`)
  - `task`: Task type (auto-detected from model)
  - `inputs`: Input text/image/audio
  - `parameters`: Model-specific parameters (temperature, max_length, etc.)
- **Use Cases**: Quick model prototyping, serverless AI features, model comparison, low-volume inference

**2. cohere-embed (Text Embeddings)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Generate text embeddings using Cohere API
- **Technical**:
  - Cohere Embed API
  - High-quality embeddings for semantic search
  - Multiple model sizes (small, large)
  - Batch processing support
- **Configuration**:
  - `apiKey`: Cohere API key
  - `texts`: Array of texts to embed
  - `model`: embed-english-v3.0, embed-multilingual-v3.0
  - `inputType`: search_document, search_query, classification, clustering
  - `truncate`: START, END, or NONE
- **Output**: Array of embedding vectors (768 or 1024 dimensions)
- **Use Cases**: Semantic search, document similarity, clustering, recommendation systems, RAG pipelines

---

#### Messaging & Communication Nodes (Pending Implementation)

**1. telegram-send-message (Telegram Bot)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Send messages via Telegram Bot API
- **Technical**:
  - Telegram Bot API
  - Supports text, images, videos, documents, locations
  - Inline keyboards and reply keyboards
  - Message editing and deletion
- **Message Types**:
  - Text (with Markdown/HTML formatting)
  - Photo, video, audio, document
  - Location, venue, contact
  - Poll, quiz
  - Sticker, animation
- **Configuration**:
  - `botToken`: Telegram bot token
  - `chatId`: Recipient chat ID
  - `message`: Text message
  - `parseMode`: Markdown, HTML, or none
  - `replyMarkup`: Inline keyboard buttons
  - `disableNotification`: Silent message
- **Use Cases**: Bot notifications, alerts, customer support, automated messages, monitoring alerts

**2. smtp-email (Email Sending)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Send transactional emails via SMTP servers
- **Technical**:
  - Nodemailer library
  - Supports all SMTP servers (Gmail, SendGrid, AWS SES, etc.)
  - HTML and plain text emails
  - Attachments support
  - Template rendering
- **Configuration**:
  - `host`: SMTP server hostname
  - `port`: SMTP port (25, 465, 587)
  - `secure`: Use TLS/SSL
  - `username`, `password`: SMTP credentials
  - `from`: Sender email and name
  - `to`: Recipient(s) (comma-separated)
  - `cc`, `bcc`: Carbon copy recipients
  - `subject`: Email subject
  - `html`: HTML body
  - `text`: Plain text alternative
  - `attachments`: Array of attachment objects
- **Use Cases**: Transactional emails, password resets, order confirmations, newsletters, notifications

**3. push-notification (Push Notifications)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Deliver push notifications through web or native channels
- **Technical**:
  - Web Push Protocol (service workers)
  - FCM (Firebase Cloud Messaging) for mobile
  - APNs (Apple Push Notification service) for iOS
  - VAPID authentication for web push
- **Channels**:
  - Web push (browser notifications)
  - Android (via FCM)
  - iOS (via APNs)
- **Configuration**:
  - `channel`: web, fcm, apns
  - `token`: Device/subscription token
  - `title`: Notification title
  - `body`: Notification body
  - `icon`: Icon URL
  - `data`: Custom payload
  - `actions`: Action buttons
  - `badge`: Badge count (mobile)
  - `sound`: Notification sound
- **Use Cases**: Mobile app notifications, browser alerts, real-time updates, engagement campaigns

**4. websocket-client (Real-time Communication)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Connect to WebSocket endpoints for real-time messaging
- **Technical**:
  - ws library or native WebSocket API
  - Bidirectional communication
  - Automatic reconnection
  - Ping/pong heartbeat
- **Operations**:
  - Connect to WebSocket server
  - Send messages
  - Receive messages (event-driven)
  - Close connection
  - Subscribe to events
- **Configuration**:
  - `url`: WebSocket URL (ws:// or wss://)
  - `protocols`: Subprotocols
  - `headers`: Custom headers
  - `reconnect`: Auto-reconnect on disconnect
  - `heartbeatInterval`: Ping interval (seconds)
- **Use Cases**: Chat applications, live dashboards, stock tickers, multiplayer games, collaborative editing

**5. mqtt-client (IoT Messaging)**
- **Priority**: Low | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Publish and subscribe to MQTT topics for IoT messaging
- **Technical**:
  - MQTT.js library
  - Lightweight pub/sub protocol
  - QoS (Quality of Service) levels 0, 1, 2
  - Last Will and Testament
  - Retained messages
- **Operations**:
  - Connect to MQTT broker
  - Publish message to topic
  - Subscribe to topic(s)
  - Unsubscribe from topic
  - Disconnect
- **Configuration**:
  - `brokerUrl`: MQTT broker URL (mqtt://, mqtts://)
  - `username`, `password`: Authentication
  - `clientId`: Unique client identifier
  - `topic`: Topic to publish/subscribe
  - `message`: Message payload
  - `qos`: Quality of Service (0, 1, 2)
  - `retain`: Retain message for new subscribers
- **Use Cases**: IoT device communication, smart home, sensor networks, telemetry, industrial automation

---

#### Payment Nodes (Pending Implementation)

**1. stripe-payment (Payment Processing)**
- **Priority**: Medium | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Create charges and manage customers via Stripe
- **Technical**:
  - Stripe Node.js SDK
  - PCI compliance handled by Stripe
  - Strong Customer Authentication (SCA) support
  - Webhook integration for event handling
- **Operations**:
  - Create payment intent
  - Create customer
  - Create subscription
  - Process charge
  - Refund payment
  - List transactions
  - Manage payment methods
- **Configuration**:
  - `secretKey`: Stripe secret key
  - `operation`: charge, createCustomer, createSubscription, refund
  - `amount`: Amount in cents
  - `currency`: Currency code (USD, EUR, etc.)
  - `customerId`: Stripe customer ID
  - `paymentMethodId`: Payment method ID
  - `description`: Payment description
- **Webhook Support**: Listen to payment events (succeeded, failed, refunded)
- **Use Cases**: E-commerce, SaaS billing, subscriptions, marketplace payments, donation platforms

**2. paypal-payment (PayPal Processing)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Process payments using PayPal APIs
- **Technical**:
  - PayPal REST API or SDK
  - Express Checkout for guest payments
  - Recurring payments support
  - Multi-currency support
- **Operations**:
  - Create payment order
  - Capture payment
  - Refund payment
  - Verify webhook signatures
- **Configuration**:
  - `clientId`, `clientSecret`: PayPal credentials
  - `mode`: sandbox or live
  - `amount`: Payment amount
  - `currency`: Currency code
  - `description`: Payment description
- **Use Cases**: Alternative payment method, international payments, mobile commerce

---

#### Authentication & User Management Nodes (Pending Implementation)

**1. oauth-login (OAuth 2.0 Authentication)**
- **Priority**: High | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Authenticate users with OAuth 2.0 providers (Google, GitHub, etc.)
- **Technical**:
  - OAuth 2.0 authorization code flow
  - PKCE (Proof Key for Code Exchange) for security
  - Token refresh mechanism
  - State parameter for CSRF protection
- **Supported Providers**:
  - Google, GitHub, GitLab, Bitbucket
  - Facebook, Twitter, LinkedIn
  - Microsoft, Apple
  - Custom OAuth providers
- **Configuration**:
  - `provider`: OAuth provider name
  - `clientId`, `clientSecret`: OAuth app credentials
  - `redirectUri`: Callback URL
  - `scope`: Requested permissions
  - `state`: CSRF token
- **Flow**:
  1. Redirect user to provider authorization page
  2. User grants permission
  3. Provider redirects back with authorization code
  4. Exchange code for access token
  5. Retrieve user profile
- **Use Cases**: Social login, single sign-on, third-party integrations

**2. user-profile (Profile Management)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Store and retrieve application user profile data
- **Technical**:
  - Database-backed user storage
  - Field validation
  - Privacy controls
  - Profile picture uploads
- **Operations**:
  - Create profile
  - Get profile by ID
  - Update profile fields
  - Delete profile
  - Search profiles
- **Configuration**:
  - `userId`: User identifier
  - `operation`: create, get, update, delete, search
  - `profileData`: Profile fields (name, email, avatar, bio, etc.)
  - `private`: Privacy settings
- **Use Cases**: User management, social profiles, customer data, team directories

**3. session-manager (Session Management)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Maintain user sessions with expiry, refresh, and storage helpers
- **Technical**:
  - Session store (memory, Redis, database)
  - JWT or session cookie based
  - Automatic expiration and cleanup
  - Concurrent session management
- **Operations**:
  - Create session
  - Validate session
  - Refresh session
  - Destroy session
  - List active sessions
- **Configuration**:
  - `userId`: User identifier
  - `sessionId`: Session identifier
  - `expiresIn`: Session duration
  - `refreshToken`: Refresh token for extending session
  - `metadata`: Device info, IP, location
- **Use Cases**: User authentication, "remember me" functionality, session tracking, security auditing

---

#### Security & Operations Nodes (Pending Implementation)

**1. secrets-manager (Credential Management)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Securely load and rotate sensitive credentials
- **Technical**:
  - Encrypted storage (AES-256)
  - Integration with HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
  - Automatic rotation support
  - Access logging
- **Operations**:
  - Store secret
  - Retrieve secret
  - Rotate secret
  - Delete secret
  - List secrets (names only)
- **Configuration**:
  - `secretName`: Secret identifier
  - `value`: Secret value
  - `operation`: get, set, rotate, delete
  - `encryption`: Encryption method
  - `externalProvider`: vault, aws, azure, gcp
- **Use Cases**: API key management, database credentials, encryption keys, certificate storage

**2. environment-config (Configuration Loader)**
- **Priority**: Medium | **Complexity**: Low | **Requires External**: No
- **Purpose**: Load environment-specific configuration values
- **Technical**:
  - dotenv integration
  - Multiple environment support (dev, staging, prod)
  - Type validation and coercion
  - Required field validation
- **Operations**:
  - Load .env file
  - Get config value
  - Validate config
  - Merge configurations
- **Configuration**:
  - `envFile`: Path to .env file
  - `environment`: dev, staging, production
  - `key`: Config key to retrieve
  - `default`: Default value if not found
  - `required`: Array of required keys
- **Use Cases**: Application configuration, feature toggles, service URLs, environment variables

**3. feature-flags (Feature Toggle System)**
- **Priority**: Low | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Toggle app behavior using feature flags and experiments
- **Technical**:
  - Database or config-backed flag storage
  - User/group targeting
  - Percentage rollouts
  - A/B testing support
  - Real-time flag updates
- **Operations**:
  - Check if flag is enabled
  - Enable/disable flag
  - Set flag percentage rollout
  - Target specific users/groups
- **Configuration**:
  - `flagName`: Feature flag identifier
  - `userId`: User to check flag for
  - `defaultValue`: Fallback value
  - `percentage`: Rollout percentage (0-100)
  - `targetUsers`: Array of user IDs with flag enabled
- **Use Cases**: Gradual feature rollouts, A/B testing, canary deployments, emergency kill switches

**4. log-aggregator (Log Collection)**
- **Priority**: Low | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Collect and forward application logs to centralized storage
- **Technical**:
  - Multiple log levels (debug, info, warn, error, fatal)
  - Structured logging (JSON format)
  - Log forwarding to Elasticsearch, Splunk, CloudWatch, Datadog
  - Log rotation and compression
- **Configuration**:
  - `level`: Minimum log level to capture
  - `destination`: console, file, elasticsearch, cloudwatch, datadog
  - `format`: text or json
  - `fields`: Additional fields to include
- **Use Cases**: Debugging, monitoring, compliance, security auditing

**5. error-tracking (Exception Reporting)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Report exceptions to services like Sentry or Rollbar
- **Technical**:
  - Automatic exception capture
  - Stack trace extraction
  - Source map support for minified code
  - Breadcrumbs for debugging context
  - Release tracking
- **Configuration**:
  - `service`: sentry, rollbar, bugsnag, airbrake
  - `dsn`: Service-specific DSN/API key
  - `environment`: Environment name
  - `release`: Release version
  - `tags`: Additional tags for filtering
- **Use Cases**: Production error monitoring, crash reporting, performance monitoring

---

#### Networking Nodes (Pending Implementation)

**1. graphql-request (GraphQL Client)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Query and mutate GraphQL APIs with variable support
- **Technical**:
  - graphql-request library
  - Support for queries, mutations, subscriptions
  - Variable interpolation
  - Fragment support
  - Batch requests
- **Configuration**:
  - `endpoint`: GraphQL API URL
  - `query`: GraphQL query or mutation
  - `variables`: Query variables
  - `headers`: HTTP headers (authorization, etc.)
  - `operation`: query, mutation, subscription
- **Query Example**:
  ```graphql
  query GetUser($id: ID!) {
    user(id: $id) {
      name
      email
      posts {
        title
      }
    }
  }
  ```
- **Use Cases**: API integration, data fetching, GitHub API, Shopify API, Hasura

---

#### DevOps Nodes (Pending Implementation)

**1. github-webhook (GitHub Event Handler)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Trigger workflows from GitHub events (push, PR, issues, releases)
- **Technical**:
  - GitHub Webhooks API
  - Signature verification (HMAC-SHA256)
  - Event filtering
  - Automatic payload parsing
- **Supported Events**:
  - push, pull_request, issues, release
  - star, fork, watch
  - deployment, status
  - workflow_run, check_suite
- **Configuration**:
  - `webhookSecret`: Secret for signature verification
  - `events`: Array of events to listen for
  - `repository`: Filter by repository
  - `branch`: Filter by branch
- **Use Cases**: CI/CD triggers, deployment automation, notification systems, issue tracking integration

**2. docker-build (Container Image Builder)**
- **Priority**: Low | **Complexity**: High | **Requires External**: Yes
- **Purpose**: Build Docker images from Dockerfile
- **Technical**:
  - Docker Engine API
  - Multi-stage build support
  - Build cache management
  - Image tagging and pushing to registries
- **Configuration**:
  - `dockerfilePath`: Path to Dockerfile
  - `context`: Build context directory
  - `imageName`: Image name and tag
  - `buildArgs`: Build-time variables
  - `registry`: Docker registry (Docker Hub, ECR, GCR, ACR)
  - `push`: Push image after build
- **Use Cases**: CI/CD pipelines, automated deployments, containerization workflows

---

#### Analytics Nodes (Pending Implementation)

**1. segment-event (Analytics Events)**
- **Priority**: Low | **Complexity**: Medium | **Requires External**: Yes
- **Purpose**: Send customer events through Segment for downstream analytics tools
- **Technical**:
  - Segment Analytics SDK
  - Event batching and retry
  - Multiple destination support (100+ integrations)
  - Real-time or batch processing
- **Event Types**:
  - **Track**: User actions (clicks, purchases, signups)
  - **Page**: Page views
  - **Identify**: User traits
  - **Group**: Group/organization traits
  - **Alias**: Link user identities
- **Configuration**:
  - `writeKey`: Segment write key
  - `eventType`: track, page, identify, group, alias
  - `userId`: User identifier
  - `eventName`: Event name (for track)
  - `properties`: Event properties
  - `traits`: User/group traits
- **Use Cases**: Product analytics, marketing attribution, user behavior tracking, customer data platform

---

#### Control Flow Nodes (Pending Implementation)

**1. rate-limiter (Request Throttling)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Control how frequently downstream nodes execute using token-bucket and sliding-window strategies
- **Technical**:
  - Multiple algorithms: token-bucket, leaky-bucket, fixed-window, sliding-window
  - Distributed rate limiting (Redis-backed)
  - Per-user, per-IP, or global limits
- **Algorithms**:
  - **Token Bucket**: Tokens refill at constant rate, burst allowed
  - **Leaky Bucket**: Smooth rate, no bursts
  - **Fixed Window**: Reset at fixed intervals
  - **Sliding Window**: Smooth rate over rolling window
- **Configuration**:
  - `algorithm`: token-bucket, leaky-bucket, fixed-window, sliding-window
  - `limit`: Maximum requests
  - `window`: Time window (seconds)
  - `key`: Identifier for limit (userId, IP, global)
  - `blockOnLimit`: Block or queue excess requests
- **Use Cases**: API rate limiting, protect external services, prevent abuse, cost control

**2. debounce-control (Event Debouncing)**
- **Priority**: Low | **Complexity**: Low | **Requires External**: No
- **Purpose**: Delay rapid-fire events and only process the final call after a quiet period
- **Technical**:
  - Timer-based debouncing
  - Trailing or leading edge triggering
  - Per-key debouncing
- **Configuration**:
  - `delay`: Milliseconds of quiet time required
  - `key`: Debounce key (group related events)
  - `mode`: trailing (execute after delay) or leading (execute immediately, block subsequent)
- **Use Cases**: Search-as-you-type, form validation, window resize handlers, API call reduction

**3. throttle-control (Action Throttling)**
- **Priority**: Low | **Complexity**: Low | **Requires External**: No
- **Purpose**: Ensure an action runs at most once within a specified time interval
- **Technical**:
  - Time-based throttling
  - Leading, trailing, or both edge execution
  - Per-key throttling
- **Configuration**:
  - `interval`: Milliseconds between executions
  - `key`: Throttle key
  - `mode`: leading, trailing, or both
- **Use Cases**: Button click protection, scroll handlers, API polling, animation frames

**4. retry-logic (Failure Recovery)**
- **Priority**: Medium | **Complexity**: Medium | **Requires External**: No
- **Purpose**: Automatically retry failed operations with linear, exponential, or custom backoff strategies
- **Technical**:
  - Multiple backoff strategies
  - Jitter to prevent thundering herd
  - Retry condition filtering (only retry on specific errors)
  - Circuit breaker integration
- **Backoff Strategies**:
  - **Fixed**: Same delay between retries
  - **Linear**: Increasing delay (1s, 2s, 3s, ...)
  - **Exponential**: Doubling delay (1s, 2s, 4s, 8s, ...)
  - **Exponential with Jitter**: Random variance to prevent synchronized retries
- **Configuration**:
  - `maxRetries`: Maximum retry attempts
  - `strategy`: fixed, linear, exponential, exponential-jitter
  - `initialDelay`: Starting delay (milliseconds)
  - `maxDelay`: Maximum delay cap
  - `retryOn`: Error types/codes to retry on
  - `timeout`: Per-attempt timeout
- **Use Cases**: Network request resilience, database connection recovery, external API calls, distributed systems

---

**Summary of Planned Nodes:**
- **Database**: 8 nodes (MySQL, Redis, SQLite, Firebase Firestore/Auth/Storage, Supabase Query/Auth)
- **Cloud Storage**: 5 nodes (GCS, Dropbox, OneDrive, IPFS, JSON File Storage)
- **AI/ML**: 2 nodes (Hugging Face Inference, Cohere Embed)
- **Messaging**: 5 nodes (Telegram, SMTP, Push Notifications, WebSocket, MQTT)
- **Payments**: 2 nodes (Stripe, PayPal)
- **Authentication**: 3 nodes (OAuth, User Profile, Session Manager)
- **Security/Operations**: 5 nodes (Secrets Manager, Environment Config, Feature Flags, Log Aggregator, Error Tracking)
- **Networking**: 1 node (GraphQL)
- **DevOps**: 2 nodes (GitHub Webhook, Docker Build)
- **Analytics**: 1 node (Segment)
- **Control Flow**: 4 nodes (Rate Limiter, Debounce, Throttle, Retry Logic)

**Total Planned**: 38 high-value integration and infrastructure nodes

**Implementation Priority**:
1. **High Priority** (8 nodes): MySQL, Firebase Firestore/Auth, Supabase Auth, OAuth
2. **Medium Priority** (21 nodes): Redis, SQLite, GCS, Firebase Storage, Supabase Query, JSON Storage, SMTP, Push Notifications, WebSocket, Stripe, User Profile, Session Manager, Secrets Manager, Environment Config, Error Tracking, GraphQL, Rate Limiter, Retry Logic
3. **Low Priority** (9 nodes): Cohere, Telegram, MQTT, PayPal, Dropbox, OneDrive, IPFS, Feature Flags, Log Aggregator, GitHub Webhook, Docker Build, Segment, Debounce, Throttle

### 1.4 Current Architecture Patterns

OLAI follows a **modular assembly architecture** where applications are composed from pre-built, reusable components rather than generating code from scratch. This approach ensures consistency, reliability, and rapid development while maintaining flexibility.

---

#### 1.4.1 Modular Assembly Approach

**Philosophy:**
- **No Code Generation from Scratch**: Applications are assembled from battle-tested templates
- **Template-Based Construction**: Every node is a pre-built, configurable template
- **Schema-Driven Development**: All components (nodes, routes, UI) are defined by schemas
- **Composability**: Complex applications built by connecting simple, single-purpose nodes
- **Reusability**: Same nodes used across different workflows and projects

**Benefits:**
- **Reliability**: Pre-tested templates reduce bugs
- **Speed**: Assembly is faster than generation
- **Consistency**: Standard patterns across all projects
- **Maintainability**: Template updates benefit all projects
- **Quality**: Professional-grade code without expertise

**Implementation:**
```typescript
// Node templates are defined as schemas
interface NodeTemplate {
  id: string;
  name: string;
  category: string;
  inputs: InputDefinition[];
  outputs: OutputDefinition[];
  config: ConfigSchema;
  handler: ExecutionHandler;
  validation: ValidationRules;
}

// Example: HTTP Request node template
const httpRequestTemplate: NodeTemplate = {
  id: 'http-request',
  name: 'HTTP Request',
  category: 'network',
  inputs: [
    { name: 'url', type: 'string', required: true },
    { name: 'method', type: 'enum', values: ['GET', 'POST', 'PUT', 'DELETE'] },
    { name: 'headers', type: 'object' },
    { name: 'body', type: 'any' }
  ],
  outputs: [
    { name: 'response', type: 'object' },
    { name: 'statusCode', type: 'number' },
    { name: 'headers', type: 'object' }
  ],
  config: { /* configuration schema */ },
  handler: async (inputs, config) => { /* execution logic */ },
  validation: { /* validation rules */ }
};
```

---

#### 1.4.2 Node Schema Structure

Each node in OLAI follows a standardized schema that defines its behavior, inputs, outputs, configuration, and execution logic.

**Complete Node Schema Definition:**

```typescript
interface NodeSchema {
  // Identity
  id: string;                    // Unique node identifier (e.g., 'http-request')
  name: string;                  // Display name (e.g., 'HTTP Request')
  version: string;               // Semantic version (e.g., '1.2.0')
  category: string;              // Category for organization (e.g., 'network')
  description: string;           // Brief description
  icon: string;                  // Icon identifier or SVG
  
  // Input/Output Definitions
  inputs: InputPort[];           // Input ports with types
  outputs: OutputPort[];         // Output ports with types
  
  // Configuration
  config: ConfigSchema;          // Configuration parameters
  defaults: Record<string, any>; // Default configuration values
  
  // Execution
  handler: ExecutionHandler;     // Main execution function
  validate: ValidationHandler;   // Input validation function
  transform: TransformHandler;   // Output transformation function
  
  // Lifecycle Hooks
  onInit?: InitHandler;          // Called when node is added to workflow
  onConnect?: ConnectHandler;    // Called when edges are connected
  onDisconnect?: DisconnectHandler;
  onDestroy?: DestroyHandler;    // Cleanup when node removed
  
  // Metadata
  tags: string[];                // Search tags
  documentation: string;         // Markdown documentation
  examples: Example[];           // Usage examples
  
  // Resource Requirements
  resources?: {
    cpu?: number;                // CPU cores required
    memory?: number;             // RAM in MB
    gpu?: boolean;               // Requires GPU
    external?: string[];         // External services (APIs, databases)
  };
  
  // Error Handling
  retryable?: boolean;           // Can be retried on failure
  timeout?: number;              // Execution timeout (ms)
  fallback?: FallbackHandler;    // Fallback on error
}

interface InputPort {
  name: string;                  // Port identifier
  type: DataType;                // Data type (string, number, object, array, any)
  required: boolean;             // Is input required
  default?: any;                 // Default value
  validation?: ValidationRule;   // Validation rules
  description?: string;          // Port description
  schema?: JSONSchema;           // JSON schema for complex types
}

interface OutputPort {
  name: string;
  type: DataType;
  description?: string;
  schema?: JSONSchema;
}

interface ConfigSchema {
  type: 'object';
  properties: Record<string, ConfigProperty>;
  required?: string[];
}

interface ConfigProperty {
  type: string;                  // string, number, boolean, enum, object, array
  title: string;                 // Display label
  description?: string;          // Help text
  default?: any;                 // Default value
  enum?: any[];                  // For enum types
  minimum?: number;              // For number types
  maximum?: number;
  pattern?: string;              // For string types (regex)
  items?: ConfigProperty;        // For array types
  properties?: Record<string, ConfigProperty>; // For object types
}
```

**Example: Complete HTTP Request Node Schema:**

```typescript
const httpRequestNode: NodeSchema = {
  id: 'http-request',
  name: 'HTTP Request',
  version: '1.0.0',
  category: 'network',
  description: 'Make HTTP requests to any URL',
  icon: 'Globe',
  
  inputs: [
    {
      name: 'url',
      type: 'string',
      required: true,
      description: 'Target URL',
      validation: { pattern: '^https?://' }
    },
    {
      name: 'method',
      type: 'string',
      required: false,
      default: 'GET',
      description: 'HTTP method'
    },
    {
      name: 'body',
      type: 'any',
      required: false,
      description: 'Request body'
    }
  ],
  
  outputs: [
    {
      name: 'response',
      type: 'object',
      description: 'Response data'
    },
    {
      name: 'status',
      type: 'number',
      description: 'HTTP status code'
    },
    {
      name: 'error',
      type: 'object',
      description: 'Error object if request failed'
    }
  ],
  
  config: {
    type: 'object',
    properties: {
      timeout: {
        type: 'number',
        title: 'Timeout',
        description: 'Request timeout in milliseconds',
        default: 30000,
        minimum: 1000,
        maximum: 300000
      },
      retries: {
        type: 'number',
        title: 'Retry Attempts',
        description: 'Number of retry attempts on failure',
        default: 3,
        minimum: 0,
        maximum: 10
      },
      followRedirects: {
        type: 'boolean',
        title: 'Follow Redirects',
        description: 'Automatically follow 3xx redirects',
        default: true
      }
    }
  },
  
  handler: async (inputs, config, context) => {
    // Execution logic
    const response = await axios({
      url: inputs.url,
      method: inputs.method,
      data: inputs.body,
      timeout: config.timeout,
      maxRedirects: config.followRedirects ? 5 : 0
    });
    
    return {
      response: response.data,
      status: response.status,
      error: null
    };
  },
  
  validate: (inputs) => {
    if (!inputs.url) {
      throw new Error('URL is required');
    }
    if (!inputs.url.match(/^https?:\/\//)) {
      throw new Error('URL must start with http:// or https://');
    }
  },
  
  resources: {
    external: ['network']
  },
  
  retryable: true,
  timeout: 60000,
  
  tags: ['network', 'http', 'api', 'rest'],
  documentation: '# HTTP Request Node\n\nMake HTTP requests...',
  examples: [
    {
      title: 'GET Request',
      description: 'Fetch data from an API',
      config: {
        url: 'https://api.example.com/data',
        method: 'GET'
      }
    }
  ]
};
```

---

#### 1.4.3 Backend Route Generation

Backend routes are automatically generated from node schemas, ensuring consistency between node definitions and API endpoints.

**Route Generation Process:**

```typescript
// Automatic route generation from node schema
function generateNodeRoutes(nodeSchema: NodeSchema): Express.Router {
  const router = express.Router();
  
  // POST /api/nodes/:nodeId/execute - Execute node
  router.post(`/api/nodes/${nodeSchema.id}/execute`, async (req, res) => {
    try {
      // 1. Validate inputs against schema
      const validationResult = validateInputs(req.body.inputs, nodeSchema.inputs);
      if (!validationResult.valid) {
        return res.status(400).json({ error: validationResult.errors });
      }
      
      // 2. Merge config with defaults
      const config = { ...nodeSchema.defaults, ...req.body.config };
      
      // 3. Execute node handler
      const context = {
        nodeId: req.body.nodeId,
        workflowId: req.body.workflowId,
        executionId: req.body.executionId,
        userId: req.user.id
      };
      
      const outputs = await nodeSchema.handler(
        req.body.inputs,
        config,
        context
      );
      
      // 4. Transform outputs
      const transformedOutputs = nodeSchema.transform
        ? nodeSchema.transform(outputs)
        : outputs;
      
      // 5. Return results
      res.json({
        success: true,
        outputs: transformedOutputs,
        metadata: {
          executionTime: Date.now() - context.startTime,
          nodeId: nodeSchema.id,
          version: nodeSchema.version
        }
      });
      
    } catch (error) {
      // Error handling with fallback
      if (nodeSchema.fallback && nodeSchema.retryable) {
        const fallbackResult = await nodeSchema.fallback(error, req.body.inputs);
        return res.json({ success: true, outputs: fallbackResult, fallback: true });
      }
      
      res.status(500).json({
        success: false,
        error: error.message,
        stack: process.env.NODE_ENV === 'development' ? error.stack : undefined
      });
    }
  });
  
  // GET /api/nodes/:nodeId/schema - Get node schema
  router.get(`/api/nodes/${nodeSchema.id}/schema`, (req, res) => {
    res.json({
      id: nodeSchema.id,
      name: nodeSchema.name,
      version: nodeSchema.version,
      inputs: nodeSchema.inputs,
      outputs: nodeSchema.outputs,
      config: nodeSchema.config,
      documentation: nodeSchema.documentation
    });
  });
  
  // GET /api/nodes/:nodeId/examples - Get usage examples
  router.get(`/api/nodes/${nodeSchema.id}/examples`, (req, res) => {
    res.json({ examples: nodeSchema.examples });
  });
  
  return router;
}

// Register all node routes
nodeSchemas.forEach(schema => {
  app.use(generateNodeRoutes(schema));
});
```

**Generated API Endpoints:**
- `POST /api/nodes/{nodeId}/execute` - Execute node with inputs
- `GET /api/nodes/{nodeId}/schema` - Retrieve node schema
- `GET /api/nodes/{nodeId}/examples` - Get usage examples
- `POST /api/nodes/{nodeId}/validate` - Validate inputs without execution
- `GET /api/nodes` - List all available nodes
- `GET /api/nodes?category={category}` - Filter nodes by category

---

#### 1.4.4 Frontend UI Generation

The frontend UI is dynamically generated from node schemas and workflow definitions, ensuring perfect synchronization between backend and frontend.

**Component Generation:**

```typescript
// Auto-generate React component for node configuration
function generateNodeConfigComponent(nodeSchema: NodeSchema): React.FC {
  return function NodeConfig({ node, onUpdate }) {
    const [config, setConfig] = useState(node.config || nodeSchema.defaults);
    
    // Generate form fields from config schema
    const renderConfigField = (key: string, property: ConfigProperty) => {
      switch (property.type) {
        case 'string':
          return (
            <TextField
              label={property.title}
              value={config[key] || property.default}
              onChange={(e) => setConfig({ ...config, [key]: e.target.value })}
              helperText={property.description}
              pattern={property.pattern}
            />
          );
          
        case 'number':
          return (
            <NumberField
              label={property.title}
              value={config[key] || property.default}
              onChange={(value) => setConfig({ ...config, [key]: value })}
              min={property.minimum}
              max={property.maximum}
              helperText={property.description}
            />
          );
          
        case 'boolean':
          return (
            <Switch
              label={property.title}
              checked={config[key] ?? property.default}
              onChange={(checked) => setConfig({ ...config, [key]: checked })}
              helperText={property.description}
            />
          );
          
        case 'enum':
          return (
            <Select
              label={property.title}
              value={config[key] || property.default}
              options={property.enum.map(v => ({ label: v, value: v }))}
              onChange={(value) => setConfig({ ...config, [key]: value })}
              helperText={property.description}
            />
          );
          
        case 'object':
          return (
            <ObjectEditor
              label={property.title}
              value={config[key] || property.default}
              schema={property.properties}
              onChange={(value) => setConfig({ ...config, [key]: value })}
            />
          );
          
        case 'array':
          return (
            <ArrayEditor
              label={property.title}
              value={config[key] || property.default}
              itemSchema={property.items}
              onChange={(value) => setConfig({ ...config, [key]: value })}
            />
          );
      }
    };
    
    return (
      <Card>
        <CardHeader>
          <Icon name={nodeSchema.icon} />
          <Title>{nodeSchema.name}</Title>
          <Description>{nodeSchema.description}</Description>
        </CardHeader>
        
        <CardBody>
          {Object.entries(nodeSchema.config.properties).map(([key, property]) => (
            <FormGroup key={key}>
              {renderConfigField(key, property)}
            </FormGroup>
          ))}
        </CardBody>
        
        <CardFooter>
          <Button onClick={() => onUpdate(config)}>Apply</Button>
          <Button variant="secondary" onClick={() => setConfig(nodeSchema.defaults)}>
            Reset to Defaults
          </Button>
        </CardFooter>
      </Card>
    );
  };
}

// Auto-generate ReactFlow node component
function generateReactFlowNode(nodeSchema: NodeSchema): React.FC {
  return function WorkflowNode({ data, selected }) {
    return (
      <div className={`node ${selected ? 'selected' : ''}`}>
        <div className="node-header">
          <Icon name={nodeSchema.icon} />
          <span className="node-title">{nodeSchema.name}</span>
          <StatusIndicator status={data.status} />
        </div>
        
        <div className="node-body">
          {/* Input handles */}
          {nodeSchema.inputs.map((input, idx) => (
            <Handle
              key={input.name}
              type="target"
              position="left"
              id={input.name}
              style={{ top: `${(idx + 1) * (100 / (nodeSchema.inputs.length + 1))}%` }}
              title={input.description}
            />
          ))}
          
          {/* Output handles */}
          {nodeSchema.outputs.map((output, idx) => (
            <Handle
              key={output.name}
              type="source"
              position="right"
              id={output.name}
              style={{ top: `${(idx + 1) * (100 / (nodeSchema.outputs.length + 1))}%` }}
              title={output.description}
            />
          ))}
          
          {/* Node content preview */}
          {data.preview && (
            <div className="node-preview">
              {renderPreview(data.preview, nodeSchema)}
            </div>
          )}
        </div>
        
        {data.error && (
          <div className="node-error">
            <AlertIcon />
            <span>{data.error}</span>
          </div>
        )}
      </div>
    );
  };
}
```

**UI Components Generated:**
1. **Node Palette**: Searchable list of all available nodes (categorized)
2. **Canvas Node**: Visual representation on workflow canvas
3. **Configuration Panel**: Dynamic form for node configuration
4. **Input/Output Ports**: Connection handles for data flow
5. **Status Indicators**: Visual feedback for execution state
6. **Error Display**: User-friendly error messages
7. **Documentation Panel**: Context-sensitive help

---

#### 1.4.5 Workflow Execution Engine

The execution engine processes workflows by resolving dependencies, executing nodes in the correct order, and managing state throughout execution.

**Execution Flow:**

```typescript
class WorkflowExecutionEngine {
  async execute(workflow: Workflow, inputs: Record<string, any>): Promise<ExecutionResult> {
    // 1. Build execution graph
    const graph = this.buildExecutionGraph(workflow);
    
    // 2. Topological sort for dependency resolution
    const executionOrder = this.topologicalSort(graph);
    
    // 3. Initialize execution context
    const context: ExecutionContext = {
      workflowId: workflow.id,
      executionId: generateId(),
      startTime: Date.now(),
      inputs,
      outputs: {},
      nodeStates: {},
      checkpoints: []
    };
    
    // 4. Execute nodes in order
    for (const nodeId of executionOrder) {
      try {
        // Check if node can execute (all dependencies complete)
        if (!this.canExecute(nodeId, context)) {
          context.nodeStates[nodeId] = { status: 'blocked', reason: 'waiting for dependencies' };
          continue;
        }
        
        // Update status
        context.nodeStates[nodeId] = { status: 'running', startTime: Date.now() };
        this.emitStatus(context, nodeId, 'running');
        
        // Get node inputs from connected edges
        const nodeInputs = this.resolveNodeInputs(nodeId, workflow, context);
        
        // Execute node
        const nodeOutputs = await this.executeNode(nodeId, nodeInputs, workflow, context);
        
        // Store outputs
        context.outputs[nodeId] = nodeOutputs;
        context.nodeStates[nodeId] = {
          status: 'completed',
          startTime: context.nodeStates[nodeId].startTime,
          endTime: Date.now(),
          outputs: nodeOutputs
        };
        
        // Create checkpoint
        if (workflow.checkpointEnabled) {
          await this.createCheckpoint(context);
        }
        
        // Emit success status
        this.emitStatus(context, nodeId, 'completed', nodeOutputs);
        
      } catch (error) {
        // Handle node failure
        context.nodeStates[nodeId] = {
          status: 'failed',
          error: error.message,
          endTime: Date.now()
        };
        
        this.emitStatus(context, nodeId, 'failed', { error: error.message });
        
        // Check if node has error handler
        if (workflow.nodes[nodeId].onError === 'continue') {
          continue;
        } else if (workflow.nodes[nodeId].onError === 'retry') {
          // Retry logic
          const retryResult = await this.retryNode(nodeId, nodeInputs, workflow, context);
          if (retryResult.success) {
            context.outputs[nodeId] = retryResult.outputs;
            continue;
          }
        }
        
        // Stop execution on failure
        throw new WorkflowExecutionError(`Node ${nodeId} failed: ${error.message}`, context);
      }
    }
    
    // 5. Return execution result
    return {
      success: true,
      executionId: context.executionId,
      outputs: context.outputs,
      duration: Date.now() - context.startTime,
      nodeStates: context.nodeStates
    };
  }
  
  // Topological sort for dependency resolution
  private topologicalSort(graph: ExecutionGraph): string[] {
    const sorted: string[] = [];
    const visited = new Set<string>();
    const visiting = new Set<string>();
    
    const visit = (nodeId: string) => {
      if (visited.has(nodeId)) return;
      if (visiting.has(nodeId)) {
        throw new Error(`Circular dependency detected at node: ${nodeId}`);
      }
      
      visiting.add(nodeId);
      
      // Visit dependencies first
      const dependencies = graph.dependencies[nodeId] || [];
      dependencies.forEach(depId => visit(depId));
      
      visiting.delete(nodeId);
      visited.add(nodeId);
      sorted.push(nodeId);
    };
    
    // Visit all nodes
    Object.keys(graph.nodes).forEach(nodeId => visit(nodeId));
    
    return sorted;
  }
  
  // Resolve node inputs from connected edges
  private resolveNodeInputs(
    nodeId: string,
    workflow: Workflow,
    context: ExecutionContext
  ): Record<string, any> {
    const inputs: Record<string, any> = {};
    
    // Get incoming edges
    const incomingEdges = workflow.edges.filter(edge => edge.target === nodeId);
    
    incomingEdges.forEach(edge => {
      // Get source node output
      const sourceOutput = context.outputs[edge.source]?.[edge.sourceHandle];
      
      // Apply edge transformation if specified
      const value = edge.transform
        ? edge.transform(sourceOutput)
        : sourceOutput;
      
      // Map to target input
      inputs[edge.targetHandle] = value;
    });
    
    // Merge with node's static inputs
    const node = workflow.nodes.find(n => n.id === nodeId);
    Object.assign(inputs, node.data.inputs);
    
    return inputs;
  }
  
  // Execute single node
  private async executeNode(
    nodeId: string,
    inputs: Record<string, any>,
    workflow: Workflow,
    context: ExecutionContext
  ): Promise<Record<string, any>> {
    const node = workflow.nodes.find(n => n.id === nodeId);
    const nodeSchema = getNodeSchema(node.type);
    
    // Validate inputs
    nodeSchema.validate(inputs);
    
    // Execute with timeout
    const result = await Promise.race([
      nodeSchema.handler(inputs, node.data.config, context),
      this.timeout(nodeSchema.timeout || 60000)
    ]);
    
    return result;
  }
  
  // Real-time status updates via WebSocket
  private emitStatus(
    context: ExecutionContext,
    nodeId: string,
    status: NodeStatus,
    data?: any
  ) {
    this.webSocket.emit('workflow:status', {
      workflowId: context.workflowId,
      executionId: context.executionId,
      nodeId,
      status,
      timestamp: Date.now(),
      data
    });
  }
  
  // Create checkpoint for long-running workflows
  private async createCheckpoint(context: ExecutionContext) {
    const checkpoint: Checkpoint = {
      executionId: context.executionId,
      timestamp: Date.now(),
      outputs: context.outputs,
      nodeStates: context.nodeStates
    };
    
    await this.checkpointStore.save(checkpoint);
    context.checkpoints.push(checkpoint);
  }
  
  // Resume from checkpoint
  async resumeFromCheckpoint(checkpointId: string): Promise<ExecutionResult> {
    const checkpoint = await this.checkpointStore.load(checkpointId);
    
    // Rebuild context from checkpoint
    const context: ExecutionContext = {
      executionId: checkpoint.executionId,
      outputs: checkpoint.outputs,
      nodeStates: checkpoint.nodeStates,
      checkpoints: [checkpoint]
    };
    
    // Continue execution from last successful node
    // ... (implementation continues)
  }
}
```

**Key Features:**
1. **Dependency Resolution**: Topological sort ensures correct execution order
2. **Parallel Execution**: Independent nodes run concurrently
3. **Real-time Updates**: WebSocket broadcasts status changes
4. **Error Handling**: Configurable error strategies (stop, continue, retry)
5. **Checkpointing**: Save state for long-running workflows
6. **Resume Capability**: Resume from checkpoints after crashes
7. **Timeout Protection**: Prevent runaway executions
8. **Circular Dependency Detection**: Validates workflow before execution

---

**Summary of Architecture Patterns:**
- ✅ **Modular Assembly**: Pre-built templates over code generation
- ✅ **Schema-Driven**: Everything defined by schemas
- ✅ **Auto-Generated Routes**: Backend APIs from schemas
- ✅ **Dynamic UI**: Frontend components from schemas
- ✅ **Smart Execution**: Dependency-aware workflow processing
- ✅ **Real-time Feedback**: Live status updates
- ✅ **Fault Tolerance**: Checkpointing and recovery
- ✅ **Type Safety**: Full TypeScript support throughout

---

## 2. Multi-Agent Architecture Plan

OLAI's multi-agent system functions as a **complete software company workforce replacement**, with specialized AI agents handling every aspect of software development from requirements gathering to deployment. Each agent is an expert in its domain, coordinating seamlessly to deliver production-ready applications.

---

### 2.1 Agent Overview & Detailed Responsibilities

#### **PM Agent (Project Manager) - The Orchestrator**

The PM Agent is the primary interface between the user and OLAI, acting as an intelligent project manager that understands goals, manages timelines, and coordinates all other agents.

**Core Responsibilities:**

1. **Chat-First Interface**
   - Natural language conversation with user
   - Understands project intent from descriptions
   - Explains technical decisions in plain language
   - Provides progress updates and status reports
   - Handles user feedback and change requests

2. **Requirements Gathering & Analysis**
   - **Initial Discovery**: Extracts core requirements from user description
   - **Intelligent Questioning**: Asks targeted clarifying questions
     - Project type detection: portfolio vs. AI-powered app vs. e-commerce
     - User constraints: budget, timeline, technical skills
     - Feature priorities: must-have vs. nice-to-have
   - **Minimal Questions Strategy**: Only asks what cannot be inferred
   - **Continuous Clarification**: Asks questions throughout project, not just at start
   - **Context Building**: Builds comprehensive project understanding over time

   - **Three-Document Requirements-First Flow**
     - As soon as the user shares their idea (prompt) and answers the PM Agent's initial questions, the PM Agent automatically starts generating a **three-document package** for clarity and alignment:
       1. **Single Page Idea Summary**
          - A concise, one-page narrative of the idea
          - Captures: problem statement, target audience, goals, core features, and expected outcome
          - Written in simple language so non-technical stakeholders can quickly understand the project
       2. **Detailed Technical Documentation**
          - A long-form, deeply technical document (similar to this OLAI planning document)
          - Includes: AI models to be used (if any), core algorithms, data flows, module breakdowns, external integrations, and non-functional requirements
          - Describes each module, service, and workflow so that all downstream agents (Architect, Coding, Testing, Builder, etc.) can rely on it as a **single source of truth**
       3. **Project Map (Nodular Tree View)**
          - A complete **tree/graph-style map** of the application
          - Nodes represent concrete elements: pages, components, APIs, background jobs, queues, models, databases, external services, etc.
          - Shows parent–child and dependency relationships so both humans and agents can visually and structurally understand the whole system

     - This documentation-first flow ensures that:
       - All required **questions, doubts, and missing data** are asked and collected early in the process
       - The PM Agent ties its clarifying questions directly to sections of these documents
       - The user can **review, approve, or correct** the Single Page Summary, Detailed Document, and Project Map before heavy implementation starts
       - Every later decision (architecture, code, deployment, optimization) is grounded in this shared documentation, reducing ambiguity and rework

3. **Project Scope Detection**
   - **Model Detection**: Determines if AI models are required
     - Pure UI/backend projects: Portfolio website, CRUD apps
     - AI-required projects: Patient monitoring, recommendation systems, chatbots
   - **Complexity Assessment**: Estimates project complexity (simple, medium, complex)
   - **Resource Planning**: Identifies required agents, models, and external services

4. **Time-Based Management**
   - **Deadline Management**: Works until specified deadline (e.g., "by 6:00 PM")
   - **Task Scheduling**: Allocates time to different phases
   - **Priority Management**: Focuses on high-priority features first
   - **Buffer Time**: Reserves time for testing, bug fixes, and polish

5. **Task Breakdown & Assignment**
   - Decomposes project into actionable tasks
   - Assigns tasks to appropriate specialized agents
   - Creates task dependencies and ordering
   - Monitors task progress and completion
   - Reassigns tasks if an agent is blocked

6. **Continuous Improvement Loop**
   - **Optimization Identification**: Finds areas for improvement
     - Server performance optimization
     - UI/UX enhancements
     - Feature additions
     - Code quality improvements
   - **Iterative Refinement**: Continuously improves until deadline or perfection
   - **Quality Gates**: Ensures minimum quality standards before moving forward

7. **Progress Monitoring & Reporting**
   - Real-time tracking of all agent activities
   - Deadline compliance monitoring
   - Bottleneck identification
   - User-facing progress reports
   - Risk assessment and mitigation

8. **Agent Coordination**
   - Inter-agent communication management
   - Conflict resolution between agents
   - Resource allocation across agents
   - Escalation handling for blocked tasks

**Decision-Making Examples:**

```yaml
# Example 1: Portfolio Website
User Input: "Build a portfolio website for my design work"

PM Analysis:
  - Project Type: Pure UI/Frontend
  - Complexity: Simple
  - AI Models Required: None
  - Timeline: 2-4 hours
  - Agents Needed: Architect, Coding, Review, Builder
  
PM Questions (Minimal):
  - "What sections do you want? (About, Portfolio, Contact, Blog?)"
  - "Do you have logo/images, or should I generate them?"
  - "Preferred color scheme?"
  
PM Plan:
  1. [Architect] Design single-page or multi-page layout
  2. [Coding] Build React components with responsive design
  3. [Review] Check accessibility and responsiveness
  4. [Builder] Generate web bundle
  5. [PM] Optimize and polish until deadline

# Example 2: AI-Powered Patient Monitoring System
User Input: "Create a patient monitoring system that predicts health deterioration"

PM Analysis:
  - Project Type: AI-Powered Application
  - Complexity: High
  - AI Models Required: Yes (4-5 models likely)
  - Timeline: 1-2 days
  - Hardware: Check user's GPU/RAM
  - Agents Needed: All agents + Research Agent for model selection
  
PM Questions (Targeted):
  - "What patient data do you have? (vitals, lab results, imaging?)"
  - "Real-time monitoring or batch analysis?"
  - "What's your hardware? (GPU/RAM for model selection)"
  - "Regulatory requirements? (HIPAA, GDPR?)"
  - "Who will use this? (doctors, nurses, patients?)"
  
PM Plan:
  1. [Research] Identify compatible models (vitals analysis, risk prediction, anomaly detection)
  2. [Research] Validate models can run simultaneously on user's hardware
  3. [Architect] Design data pipeline, model orchestration, alerting system
  4. [Coding] Implement backend with model integration, frontend dashboard
  5. [Testing] Generate synthetic patient data, validate predictions
  6. [Review] Security audit, HIPAA compliance check
  7. [Builder] Create deployable system
  8. [PM] Optimize model execution, improve dashboard, add features until deadline
```

**PM Agent Intelligence:**

```typescript
interface PMAgentContext {
  // Project Understanding
  projectType: 'ui-only' | 'backend-heavy' | 'ai-powered' | 'mixed';
  complexity: 'simple' | 'medium' | 'complex' | 'enterprise';
  requiredModels: ModelRequirement[];
  
  // Timeline Management
  deadline?: Date;
  estimatedDuration: number;  // hours
  currentPhase: ProjectPhase;
  timeRemaining: number;
  
  // Resource Planning
  activeAgents: Agent[];
  hardwareCapabilities: HardwareProfile;
  externalServices: ServiceRequirement[];
  
  // Progress Tracking
  completedTasks: Task[];
  inProgressTasks: Task[];
  blockedTasks: Task[];
  overallProgress: number;  // 0-100
  
  // Continuous Improvement
  optimizationOpportunities: Optimization[];
  qualityMetrics: QualityMetrics;
  userFeedback: Feedback[];
}

class PMAgent {
  async analyzeProject(userInput: string): Promise<ProjectAnalysis> {
    // 1. Extract core requirements using NLP
    const requirements = await this.extractRequirements(userInput);
    
    // 2. Detect project type and complexity
    const projectType = this.detectProjectType(requirements);
    const complexity = this.assessComplexity(requirements);
    
    // 3. Determine AI model requirements
    const modelRequirements = projectType.includes('ai')
      ? await this.determineModelNeeds(requirements)
      : [];
    
    // 4. Estimate timeline
    const timeline = this.estimateTimeline(complexity, modelRequirements);
    
    // 5. Generate targeted questions (only what's unclear)
    const questions = this.generateQuestions(requirements, projectType);
    
    return {
      projectType,
      complexity,
      modelRequirements,
      timeline,
      questions: questions.filter(q => q.priority === 'high')  // Ask only essential questions
    };
  }
  
  async createTaskBreakdown(analysis: ProjectAnalysis): Promise<Task[]> {
    const tasks: Task[] = [];
    
    // Phase 1: Architecture
    tasks.push({
      id: 'arch-1',
      agent: 'architect',
      title: 'Design system architecture',
      dependencies: [],
      estimatedTime: analysis.complexity === 'simple' ? 0.5 : 2,
      priority: 'critical'
    });
    
    // Phase 2: Research (if AI models needed)
    if (analysis.modelRequirements.length > 0) {
      tasks.push({
        id: 'research-1',
        agent: 'research',
        title: 'Identify and validate AI models',
        dependencies: ['arch-1'],
        estimatedTime: 1,
        priority: 'critical'
      });
    }
    
    // Phase 3: Implementation
    tasks.push({
      id: 'code-1',
      agent: 'coding',
      title: 'Implement backend',
      dependencies: ['arch-1'],
      estimatedTime: analysis.complexity === 'simple' ? 1 : 4,
      priority: 'critical'
    });
    
    tasks.push({
      id: 'code-2',
      agent: 'coding',
      title: 'Implement frontend',
      dependencies: ['arch-1'],
      estimatedTime: analysis.complexity === 'simple' ? 1 : 3,
      priority: 'critical'
    });
    
    // Continue task breakdown...
    return tasks;
  }
  
  async monitorProgress(context: PMAgentContext): Promise<void> {
    // Check if deadline approaching
    if (context.deadline && context.timeRemaining < 2 * 60 * 60 * 1000) { // 2 hours
      // Prioritize critical tasks only
      await this.reprioritizeTasks(context, 'critical-only');
    }
    
    // Identify optimization opportunities
    const optimizations = await this.identifyOptimizations(context);
    
    // Apply optimizations if time allows
    if (context.timeRemaining > context.estimatedDuration * 1.5) {
      for (const opt of optimizations) {
        await this.applyOptimization(opt, context);
      }
    }
  }
}
```

---

#### **Architect Agent - The System Designer**

The Architect Agent designs the technical architecture, making high-level decisions about structure, patterns, and technologies.

**Core Responsibilities:**

1. **System Architecture Design**
   - **Folder Structure**: Organizes project files logically
     ```
     project/
     ├── backend/
     │   ├── src/
     │   │   ├── routes/      # API endpoints
     │   │   ├── services/    # Business logic
     │   │   ├── models/      # Data models
     │   │   ├── utils/       # Utilities
     │   │   └── ai/          # AI model integrations
     │   ├── tests/
     │   └── config/
     ├── frontend/
     │   ├── src/
     │   │   ├── components/  # React components
     │   │   ├── pages/       # Page components
     │   │   ├── hooks/       # Custom hooks
     │   │   ├── services/    # API clients
     │   │   └── utils/
     │   └── public/
     └── mobile/
         └── src/
     ```
   
   - **API Architecture**: Designs RESTful or GraphQL APIs
     - Endpoint structure and naming conventions
     - Request/response schemas
     - Authentication and authorization flows
     - Rate limiting and caching strategies
   
   - **Client/Server Boundaries**: Decides what runs where
     - Server-side rendering vs. client-side rendering
     - API vs. direct database access
     - Real-time vs. polling
     - Edge functions vs. server functions

2. **AI Model Selection & Integration**
   - **Model Architecture Decisions**:
     - Local vs. API-based models
     - Model size vs. accuracy trade-offs
     - Quantization strategies (INT8, FP16, FP32)
     - Model chaining and orchestration
   
   - **Runtime Environment**:
     - Python backend for Hugging Face models
     - Node.js backend for Gemini/OpenAI APIs
     - ONNX Runtime for optimized inference
     - TensorFlow.js for browser models

3. **Database Schema Design**
   - **Database Selection**:
     - PostgreSQL for relational data
     - MongoDB for document storage
     - Redis for caching and sessions
     - Vector DB for embeddings (Weaviate, Pinecone, Chroma)
   
   - **Schema Design**:
     - Table/collection structure
     - Indexes for performance
     - Relationships and foreign keys
     - Denormalization strategies

4. **Caching Strategy**
   - **Multi-Level Caching**:
     - L1: In-memory (application-level)
     - L2: Redis (distributed cache)
     - L3: CDN (static assets)
   
   - **Cache Invalidation**: Strategies for keeping cache fresh
   - **Cache Warming**: Pre-populate cache with common queries

5. **Technology Stack Selection**
   - Frontend: React, Next.js, or Vue
   - Backend: Fastify, Express, or NestJS
   - Mobile: React Native, Flutter, or native
   - Database: Based on data model
   - Deployment: Docker, serverless, or VPS

6. **Design Patterns & Best Practices**
   - MVC/MVVM architecture
   - Repository pattern for data access
   - Service layer for business logic
   - Dependency injection
   - Error handling patterns

**Architecture Decision Example:**

```typescript
class ArchitectAgent {
  async designArchitecture(requirements: Requirements): Promise<Architecture> {
    // Analyze requirements
    const dataModel = this.analyzeDataModel(requirements);
    const userFlows = this.identifyUserFlows(requirements);
    const scalabilityNeeds = this.assessScalability(requirements);
    
    // Make technology decisions
    const stack = {
      frontend: this.selectFrontendTech(requirements),
      backend: this.selectBackendTech(requirements),
      database: this.selectDatabase(dataModel),
      cache: 'redis',
      cdn: requirements.hasStaticAssets ? 'cloudflare' : null,
      hosting: this.selectHosting(scalabilityNeeds)
    };
    
    // Design API structure
    const apiDesign = {
      style: 'REST',  // or GraphQL for complex queries
      versioning: 'url',  // /api/v1/...
      authentication: 'JWT',
      rateLimit: {
        window: 60000,  // 1 minute
        max: 100  // 100 requests per minute
      },
      endpoints: this.designEndpoints(userFlows)
    };
    
    // Design database schema
    const schema = this.designSchema(dataModel, stack.database);
    
    // Design folder structure
    const folderStructure = this.designFolderStructure(stack);
    
    return {
      stack,
      apiDesign,
      schema,
      folderStructure,
      patterns: ['repository', 'service-layer', 'dependency-injection']
    };
  }
  
  // AI Model Architecture Design
  async designModelArchitecture(
    modelRequirements: ModelRequirement[],
    hardware: HardwareProfile
  ): Promise<ModelArchitecture> {
    const selectedModels: SelectedModel[] = [];
    
    for (const req of modelRequirements) {
      // Select model based on hardware constraints
      const model = await this.selectOptimalModel(req, hardware);
      selectedModels.push(model);
    }
    
    // Design model orchestration
    const orchestration = this.designModelOrchestration(selectedModels);
    
    // Design model serving strategy
    const serving = {
      local: selectedModels.filter(m => m.type === 'local'),
      api: selectedModels.filter(m => m.type === 'api'),
      loadBalancing: orchestration.parallel ? 'round-robin' : null,
      caching: {
        enabled: true,
        ttl: 3600,  // 1 hour
        keyStrategy: 'input-hash'
      }
    };
    
    return {
      models: selectedModels,
      orchestration,
      serving
    };
  }
}
```

---

#### **Coding Agent - The Implementation Expert**

The Coding Agent writes all application code (backend, frontend, mobile) following the architecture and best practices.

**Core Responsibilities:**

1. **Backend Development**
   - **API Routes**: RESTful endpoints with Fastify/Express
   - **Business Logic**: Service layer implementation
   - **Database Access**: Repository pattern with ORMs (Prisma, TypeORM, Mongoose)
   - **AI Model Integration**: Model loading, inference, error handling
   - **Authentication**: JWT, OAuth, session management
   - **Validation**: Input validation with Zod, Joi, or class-validator
   - **Error Handling**: Consistent error responses and logging

2. **Frontend Development**
   - **React Components**: Functional components with hooks
   - **State Management**: Context API, Zustand, or Redux
   - **Routing**: React Router with protected routes
   - **API Integration**: Axios/Fetch with error handling and loading states
   - **Form Handling**: React Hook Form with validation
   - **Styling**: Tailwind CSS, styled-components, or CSS modules
   - **Responsive Design**: Mobile-first approach

3. **Mobile Development**
   - React Native or Flutter components
   - Native integrations (camera, sensors, push notifications)
   - Offline-first architecture
   - Platform-specific code (iOS/Android)

4. **Safe File Editing with AST Parsing**
   - **Partial Edits**: Only modify necessary parts
   - **AST-Based Editing**: Parse code, modify AST nodes, regenerate
   - **No Full Rewrites**: Preserve existing code and comments
   - **Format Preservation**: Maintain code style and formatting
   
   ```typescript
   class CodingAgent {
     async editFile(filePath: string, changes: CodeChange[]): Promise<void> {
       // 1. Parse file to AST
       const ast = this.parseToAST(filePath);
       
       // 2. Apply changes to specific AST nodes
       for (const change of changes) {
         const node = this.findNode(ast, change.selector);
         this.modifyNode(node, change.modification);
       }
       
       // 3. Regenerate code from AST
       const newCode = this.generateCode(ast);
       
       // 4. Write file
       await fs.writeFile(filePath, newCode);
     }
     
     // Example: Add new function to existing file
     async addFunction(filePath: string, functionCode: string): Promise<void> {
       const ast = this.parseToAST(filePath);
       
       // Parse new function to AST
       const funcAST = this.parseFunctionToAST(functionCode);
       
       // Find insertion point (e.g., before last export)
       const insertionIndex = this.findInsertionPoint(ast);
       
       // Insert function AST
       ast.program.body.splice(insertionIndex, 0, funcAST);
       
       // Regenerate and write
       await fs.writeFile(filePath, this.generateCode(ast));
     }
   }
   ```

5. **Code Generation (Cursor/Copilot Style)**
   - **Context-Aware Generation**: Understands project structure
   - **Inline Code Completion**: Suggests next lines
   - **Function Generation**: Generates complete functions from comments
   - **Test Generation**: Automatically generates tests for functions
   - **Documentation Generation**: Generates JSDoc comments

6. **Follows Architecture Rules**
   - Adheres to folder structure
   - Uses established patterns (repository, service layer)
   - Maintains consistent naming conventions
   - Follows code style guidelines
   - Implements proper error handling

**Code Generation Example:**

```typescript
class CodingAgent {
  async generateBackendRoute(endpoint: EndpointDefinition): Promise<string> {
    // Generate route with validation, error handling, and documentation
    return `
import { FastifyRequest, FastifyReply } from 'fastify';
import { z } from 'zod';
import { ${endpoint.service} } from '../services/${endpoint.service}';

// Input validation schema
const ${endpoint.name}Schema = z.object({
  ${endpoint.inputs.map(i => `${i.name}: z.${i.type}()${i.required ? '' : '.optional'()}'`).join(',\n  ')}
});

/**
 * ${endpoint.description}
 * @route ${endpoint.method} ${endpoint.path}
 */
export async function ${endpoint.handlerName}(
  request: FastifyRequest<{ Body: z.infer<typeof ${endpoint.name}Schema> }>,
  reply: FastifyReply
) {
  try {
    // Validate input
    const input = ${endpoint.name}Schema.parse(request.body);
    
    // Call service
    const result = await ${endpoint.service}.${endpoint.methodName}(input);
    
    // Return response
    return reply.code(200).send({
      success: true,
      data: result
    });
  } catch (error) {
    request.log.error(error);
    
    if (error instanceof z.ZodError) {
      return reply.code(400).send({
        success: false,
        error: 'Validation failed',
        details: error.errors
      });
    }
    
    return reply.code(500).send({
      success: false,
      error: 'Internal server error'
    });
  }
}
    `;
  }
  
  async generateReactComponent(component: ComponentDefinition): Promise<string> {
    return `
import React, { useState } from 'react';
${component.imports.join('\n')}

interface ${component.name}Props {
  ${component.props.map(p => `${p.name}${p.required ? '' : '?'}: ${p.type};`).join('\n  ')}
}

/**
 * ${component.description}
 */
export const ${component.name}: React.FC<${component.name}Props> = ({
  ${component.props.map(p => p.name).join(', ')}
}) => {
  ${component.state.map(s => `const [${s.name}, set${capitalize(s.name)}] = useState<${s.type}>(${s.initial});`).join('\n  ')}
  
  ${component.effects.map(e => `
  useEffect(() => {
    ${e.code}
  }, [${e.dependencies.join(', ')}]);
  `).join('\n')}
  
  ${component.handlers.map(h => `
  const ${h.name} = ${h.async ? 'async ' : ''}(${h.params.join(', ')}) => {
    ${h.code}
  };
  `).join('\n')}
  
  return (
    ${component.jsx}
  );
};
    `;
  }
}
```

---

#### **Research Agent - The Knowledge Expert**

The Research Agent identifies external resources, validates compatibility, and ensures optimal model selection.

**Core Responsibilities:**

1. **Library & API Discovery**
   - Searches npm, PyPI, GitHub for relevant packages
   - Reads API documentation
   - Compares alternatives
   - Checks license compatibility
   - Verifies maintenance status and security

2. **AI Model Research & Selection**
   - **Model Discovery**: Finds models on Hugging Face, Ollama, GitHub
   - **Capability Matching**: Matches model capabilities to requirements
   - **Hardware Validation**: Ensures models fit on user's hardware
   - **Performance Estimation**: Predicts inference time on user's hardware
   - **Multi-Model Compatibility**: Ensures 4-5 models can run simultaneously

3. **Multi-Model Planning**
   - **Compatibility Matrix**: Creates matrix showing which models can run together
   - **Memory Allocation**: Plans memory distribution across models
   - **Execution Strategy**: Sequential vs. parallel execution
   - **Resource Optimization**: Quantization, batching, model caching

4. **Hardware Capability Detection**
   - GPU: Type (NVIDIA, AMD, Apple Silicon), VRAM, CUDA version
   - CPU: Cores, architecture (x86, ARM)
   - RAM: Total and available memory
   - Disk: Available space for model storage

5. **Model Replacement Suggestions**
   - If model too large: Suggest smaller alternatives
   - If model too slow: Suggest faster alternatives
   - If model unavailable: Suggest equivalent models

**Research Example:**

```typescript
class ResearchAgent {
  async researchModels(requirements: ModelRequirement[], hardware: HardwareProfile): Promise<ModelPlan> {
    const modelPlans: ModelSelection[] = [];
    
    for (const req of requirements) {
      // Search for candidate models
      const candidates = await this.searchModels(req.task, req.modality);
      
      // Filter by hardware constraints
      const compatible = candidates.filter(model => 
        this.isCompatibleWithHardware(model, hardware)
      );
      
      // Rank by performance and accuracy
      const ranked = this.rankModels(compatible, hardware);
      
      // Select best model
      const selected = ranked[0];
      
      modelPlans.push({
        requirement: req,
        selectedModel: selected,
        alternatives: ranked.slice(1, 4),
        estimatedMemory: selected.memoryRequirement,
        estimatedInferenceTime: this.estimateInferenceTime(selected, hardware)
      });
    }
    
    // Validate multi-model compatibility
    const compatibility = this.validateMultiModelCompatibility(modelPlans, hardware);
    
    if (!compatibility.compatible) {
      // Apply optimization strategies
      modelPlans = this.optimizeForMultiModel(modelPlans, hardware);
    }
    
    return {
      models: modelPlans,
      totalMemory: modelPlans.reduce((sum, m) => sum + m.estimatedMemory, 0),
      compatibility,
      recommendations: this.generateRecommendations(modelPlans, hardware)
    };
  }
  
  // Compatibility Matrix
  private validateMultiModelCompatibility(
    models: ModelSelection[],
    hardware: HardwareProfile
  ): CompatibilityResult {
    const totalMemory = models.reduce((sum, m) => sum + m.estimatedMemory, 0);
    const availableMemory = hardware.gpu ? hardware.gpu.vram : hardware.ram * 0.5;
    
    if (totalMemory > availableMemory) {
      return {
        compatible: false,
        reason: 'Insufficient memory',
        required: totalMemory,
        available: availableMemory,
        suggestions: [
          'Use quantized models (INT8 instead of FP32)',
          'Use smaller model variants',
          'Execute models sequentially instead of parallel',
          'Offload some models to CPU'
        ]
      };
    }
    
    // Check for model conflicts (same port, same GPU device)
    const conflicts = this.detectModelConflicts(models);
    
    if (conflicts.length > 0) {
      return {
        compatible: false,
        reason: 'Model conflicts detected',
        conflicts,
        suggestions: ['Use model orchestration to queue requests']
      };
    }
    
    return {
      compatible: true,
      parallelExecution: true,
      estimatedSimultaneousModels: models.length
    };
  }
}
```

---

#### **Testing Agent - The Quality Assurance Expert**

The Testing Agent ensures code quality through comprehensive testing strategies and automated test generation.

**Core Responsibilities:**

1. **Unit Test Generation**
   - **Function-Level Tests**: Tests for individual functions and methods
   - **Component Tests**: Tests for React components (with React Testing Library)
   - **Mock Generation**: Automatic mock data and dependency mocking
   - **Edge Case Identification**: Tests boundary conditions and error scenarios
   
   ```typescript
   class TestingAgent {
     async generateUnitTests(functionCode: string, context: CodeContext): Promise<string> {
       // Parse function to understand inputs, outputs, dependencies
       const functionInfo = this.parseFunction(functionCode);
       
       // Generate test cases
       const testCases = [
         ...this.generateHappyPathTests(functionInfo),
         ...this.generateEdgeCaseTests(functionInfo),
         ...this.generateErrorCaseTests(functionInfo)
       ];
       
       return `
import { describe, it, expect, vi } from 'vitest';
import { ${functionInfo.name} } from './${functionInfo.fileName}';

describe('${functionInfo.name}', () => {
  ${testCases.map(tc => `
  it('${tc.description}', async () => {
    // Arrange
    ${tc.arrange}
    
    // Act
    ${tc.act}
    
    // Assert
    ${tc.assert}
  });
  `).join('\n')}
});
       `;
     }
   }
   ```

2. **Integration Test Generation**
   - **API Endpoint Tests**: Tests for REST/GraphQL endpoints
   - **Workflow Tests**: End-to-end workflow execution tests
   - **Database Integration Tests**: Tests with real database connections
   - **External Service Mocking**: Mock external APIs for reliable testing

3. **Test Dataset Generation**
   - **Synthetic Data**: Generates realistic test data
   - **Edge Cases**: Boundary values, null/undefined, empty arrays
   - **Performance Data**: Large datasets for performance testing
   - **Security Data**: SQL injection, XSS, CSRF test cases

4. **Test Execution & Reporting**
   - Runs all tests (unit, integration, e2e)
   - Generates coverage reports
   - Identifies failing tests
   - Provides detailed error messages and stack traces
   - Performance metrics (test duration, slowest tests)

5. **Code Coverage Validation**
   - Ensures minimum coverage thresholds (e.g., 80%)
   - Identifies untested code paths
   - Suggests additional test cases for low-coverage areas

6. **Synthetic Test Generator for Workflows**
   - Automatically creates test inputs for workflow nodes
   - Validates workflow outputs
   - Tests error handling and edge cases
   - Ensures workflow behaves correctly under various conditions

**Test Generation Example:**

```typescript
// Auto-generated integration test for API endpoint
import request from 'supertest';
import { app } from '../src/app';
import { db } from '../src/database';

describe('POST /api/users', () => {
  beforeEach(async () => {
    await db.users.deleteMany({});
  });
  
  it('should create a new user with valid data', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({
        name: 'John Doe',
        email: 'john@example.com',
        password: 'SecureP@ss123'
      })
      .expect(201);
    
    expect(response.body).toMatchObject({
      success: true,
      data: {
        id: expect.any(String),
        name: 'John Doe',
        email: 'john@example.com'
      }
    });
    
    // Verify user was created in database
    const user = await db.users.findOne({ email: 'john@example.com' });
    expect(user).toBeDefined();
    expect(user.password).not.toBe('SecureP@ss123'); // Password should be hashed
  });
  
  it('should return 400 for invalid email', async () => {
    await request(app)
      .post('/api/users')
      .send({
        name: 'John Doe',
        email: 'invalid-email',
        password: 'SecureP@ss123'
      })
      .expect(400);
  });
  
  it('should return 409 for duplicate email', async () => {
    // Create first user
    await request(app)
      .post('/api/users')
      .send({
        name: 'John Doe',
        email: 'john@example.com',
        password: 'SecureP@ss123'
      });
    
    // Attempt to create duplicate
    await request(app)
      .post('/api/users')
      .send({
        name: 'Jane Doe',
        email: 'john@example.com',
        password: 'AnotherP@ss123'
      })
      .expect(409);
  });
});
```

---

#### **Builder Agent - The Build Engineer**

The Builder Agent handles all build pipelines, optimizations, and multi-platform compilation.

**Core Responsibilities:**

1. **Build Pipeline Configuration**
   - **Web**: Vite, Webpack, or esbuild configuration
   - **Mobile**: React Native or Flutter build config
   - **Desktop**: Electron or Tauri configuration
   - **Build Scripts**: Automated build commands and hooks

2. **Multi-Platform Build Execution**
   - **Parallel Building**: Builds all platforms simultaneously
   - **Platform-Specific Optimizations**: Tailored builds for each platform
   - **Build Caching**: Reuse unchanged modules across builds
   - **Incremental Builds**: Only rebuild changed components
   
   ```typescript
   class BuilderAgent {
     async buildAllPlatforms(project: Project): Promise<BuildResults> {
       // Execute builds in parallel
       const results = await Promise.all([
         this.buildWeb(project),
         this.buildAndroid(project),
         this.buildWindows(project),
         this.buildMacOS(project)
       ]);
       
       return {
         web: results[0],
         android: results[1],
         windows: results[2],
         macOS: results[3],
         totalTime: Math.max(...results.map(r => r.duration)),
         totalSize: results.reduce((sum, r) => sum + r.size, 0)
       };
     }
     
     private async buildWeb(project: Project): Promise<BuildResult> {
       // 1. Install dependencies
       await this.installDependencies(project.webPath);
       
       // 2. Run build with optimizations
       const buildConfig = {
         minify: true,
         treeshake: true,
         splitting: true,  // Code splitting
         sourcemap: false,  // No sourcemaps in production
         target: ['es2020', 'chrome90', 'safari14'],
         define: {
           'process.env.NODE_ENV': '"production"'
         }
       };
       
       const startTime = Date.now();
       await this.runBuild('vite build', buildConfig);
       
       // 3. Analyze bundle
       const analysis = await this.analyzeBundleSize(project.webPath + '/dist');
       
       return {
         platform: 'web',
         success: true,
         outputPath: project.webPath + '/dist',
         size: analysis.totalSize,
         duration: Date.now() - startTime,
         assets: analysis.assets
       };
     }
   }
   ```

3. **Build Optimization**
   - **Code Splitting**: Lazy-load routes and components
   - **Tree Shaking**: Remove unused code
   - **Minification**: Compress JavaScript, CSS, HTML
   - **Image Optimization**: Compress and convert to modern formats (WebP, AVIF)
   - **Font Subsetting**: Include only used characters
   - **Preloading/Prefetching**: Optimize resource loading

4. **Android APK Build**
   - Gradle build configuration
   - Signing with keystore
   - ProGuard/R8 for code optimization and obfuscation
   - APK size optimization
   - Multi-architecture builds (ARM, x86)

5. **Windows EXE Build**
   - **Electron**: Full Chromium + Node.js runtime
   - **Tauri**: Lightweight with system WebView
   - **Installer Creation**: NSIS or WiX installer
   - **Code Signing**: Digital signature for Windows
   - **Auto-Update**: Built-in update mechanism

6. **macOS App Build**
   - DMG or PKG installer creation
   - Code signing with Apple Developer certificate
   - Notarization for macOS Gatekeeper
   - Universal binary (Intel + Apple Silicon)

7. **Build Validation**
   - Smoke tests on each build
   - Size checks (warning if bundle too large)
   - Dependency security audit
   - Performance benchmarks

---

#### **Review Agent - The Code Auditor**

The Review Agent performs comprehensive code quality checks, security audits, and suggests improvements.

**Core Responsibilities:**

1. **Code Quality Audit**
   - **Code Complexity**: Detects overly complex functions (cyclomatic complexity)
   - **Code Duplication**: Identifies repeated code blocks
   - **Naming Conventions**: Validates consistent naming
   - **Code Smells**: Detects anti-patterns and bad practices
   - **Documentation**: Ensures functions and classes have documentation

2. **Bug Detection**
   - **Static Analysis**: ESLint, TypeScript compiler errors
   - **Type Safety**: Validates TypeScript types
   - **Null Safety**: Detects potential null/undefined errors
   - **Logic Errors**: Identifies unreachable code, infinite loops
   - **Memory Leaks**: Detects common memory leak patterns

3. **Security Audit**
   - **OWASP Top 10**: Checks for common vulnerabilities
     - SQL Injection
     - XSS (Cross-Site Scripting)
     - CSRF (Cross-Site Request Forgery)
     - Authentication flaws
     - Insecure deserialization
   - **Dependency Vulnerabilities**: Scans npm/pip packages for known CVEs
   - **Secrets Detection**: Finds hardcoded API keys, passwords
   - **Security Headers**: Validates HTTP security headers

4. **Refactoring Suggestions**
   - **Extract Function**: Suggests breaking large functions into smaller ones
   - **Simplify Conditionals**: Suggests simplifying complex if/else chains
   - **Remove Dead Code**: Identifies unused variables and functions
   - **Optimize Algorithms**: Suggests more efficient implementations

5. **Code Style Validation**
   - **Formatting**: Prettier/ESLint formatting rules
   - **Conventions**: Project-specific style guide adherence
   - **Best Practices**: Enforces industry best practices

6. **Performance Analysis**
   - Identifies performance bottlenecks
   - Suggests caching opportunities
   - Detects N+1 query problems
   - Recommends database indexes

**Review Example:**

```typescript
class ReviewAgent {
  async reviewCode(codebase: Codebase): Promise<ReviewReport> {
    const issues: Issue[] = [];
    
    // 1. Run static analysis
    const lintIssues = await this.runLinter(codebase);
    issues.push(...lintIssues);
    
    // 2. Security scan
    const securityIssues = await this.runSecurityScan(codebase);
    issues.push(...securityIssues);
    
    // 3. Dependency audit
    const dependencyIssues = await this.auditDependencies(codebase);
    issues.push(...dependencyIssues);
    
    // 4. Code quality metrics
    const qualityMetrics = await this.analyzeQuality(codebase);
    
    // 5. Generate refactoring suggestions
    const refactorings = await this.suggestRefactorings(codebase, qualityMetrics);
    
    // 6. Prioritize issues
    const prioritized = this.prioritizeIssues(issues);
    
    return {
      summary: {
        totalIssues: issues.length,
        critical: issues.filter(i => i.severity === 'critical').length,
        high: issues.filter(i => i.severity === 'high').length,
        medium: issues.filter(i => i.severity === 'medium').length,
        low: issues.filter(i => i.severity === 'low').length
      },
      issues: prioritized,
      qualityMetrics,
      refactorings,
      overallScore: this.calculateScore(issues, qualityMetrics)
    };
  }
  
  // Example: Detect SQL injection vulnerability
  private detectSQLInjection(code: string): Issue[] {
    const issues: Issue[] = [];
    const ast = this.parseToAST(code);
    
    // Find all SQL query constructions
    const queries = this.findSQLQueries(ast);
    
    for (const query of queries) {
      if (query.usesStringConcatenation && query.includesUserInput) {
        issues.push({
          type: 'security',
          severity: 'critical',
          title: 'SQL Injection Vulnerability',
          description: 'User input concatenated directly into SQL query',
          file: query.file,
          line: query.line,
          fix: 'Use parameterized queries or prepared statements',
          example: `
// Vulnerable:
const query = \`SELECT * FROM users WHERE email = '\${userEmail}'\`;

// Fixed:
const query = 'SELECT * FROM users WHERE email = ?';
const results = await db.query(query, [userEmail]);
          `
        });
      }
    }
    
    return issues;
  }
}
```

---

#### **Release Agent - The Deployment Manager**

The Release Agent prepares final build artifacts, manages versioning, and creates deployment packages.

**Core Responsibilities:**

1. **Multi-Platform Artifact Preparation**
   - **Web**: Deployable bundle (static files or Docker image)
   - **Android**: Signed APK or AAB (Android App Bundle)
   - **Windows**: Signed EXE and installer
   - **macOS**: Signed DMG or PKG
   - **npm/PyPI**: Publishable packages

2. **Version Management**
   - **Semantic Versioning**: Automatically determines version bump (major, minor, patch)
   - **Changelog Generation**: Auto-generates changelog from commit messages
   - **Git Tagging**: Creates git tags for releases
   - **Version Embedding**: Updates version in package.json, pubspec.yaml, etc.

3. **Release Notes Generation**
   - **AI-Generated**: Summarizes changes in user-friendly language
   - **Categorization**: Groups changes (Features, Bug Fixes, Breaking Changes)
   - **Credit Attribution**: Lists contributors
   - **Migration Guides**: Instructions for breaking changes

4. **Deployment Manifest Creation**
   - **Docker**: Dockerfile and docker-compose.yml
   - **Kubernetes**: Deployment YAML files
   - **Serverless**: Vercel, Netlify, or AWS Lambda configuration
   - **Environment Variables**: .env.example file

5. **Export Validation**
   - **Integrity Checks**: Validates all builds are complete and error-free
   - **Size Checks**: Warns if builds are unexpectedly large
   - **Smoke Tests**: Quick tests on final builds
   - **Checksums**: Generates SHA-256 checksums for artifacts

6. **Distribution Preparation**
   - **CDN Upload**: Uploads static assets to CDN
   - **App Store Submission**: Prepares metadata for app stores
   - **Package Registry**: Publishes to npm, PyPI, Docker Hub
   - **GitHub Release**: Creates GitHub release with artifacts

**Release Process Example:**

```typescript
class ReleaseAgent {
  async prepareRelease(project: Project, builds: BuildResults): Promise<Release> {
    // 1. Determine version bump
    const currentVersion = await this.getCurrentVersion(project);
    const commits = await this.getCommitsSinceLastRelease(project);
    const newVersion = this.determineVersionBump(commits, currentVersion);
    
    // 2. Generate release notes
    const releaseNotes = await this.generateReleaseNotes(commits, newVersion);
    
    // 3. Update version in all package files
    await this.updateVersionFiles(project, newVersion);
    
    // 4. Create release artifacts
    const artifacts: ReleaseArtifact[] = [
      {
        platform: 'web',
        path: builds.web.outputPath,
        filename: `${project.name}-web-v${newVersion}.zip`,
        size: builds.web.size,
        checksum: await this.generateChecksum(builds.web.outputPath)
      },
      {
        platform: 'android',
        path: builds.android.outputPath,
        filename: `${project.name}-v${newVersion}.apk`,
        size: builds.android.size,
        checksum: await this.generateChecksum(builds.android.outputPath)
      },
      {
        platform: 'windows',
        path: builds.windows.outputPath,
        filename: `${project.name}-Setup-v${newVersion}.exe`,
        size: builds.windows.size,
        checksum: await this.generateChecksum(builds.windows.outputPath)
      },
      {
        platform: 'macos',
        path: builds.macOS.outputPath,
        filename: `${project.name}-v${newVersion}.dmg`,
        size: builds.macOS.size,
        checksum: await this.generateChecksum(builds.macOS.outputPath)
      }
    ];
    
    // 5. Create deployment manifests
    const manifests = {
      docker: await this.generateDockerfile(project),
      kubernetes: await this.generateK8sManifests(project),
      vercel: await this.generateVercelConfig(project),
      env: await this.generateEnvExample(project)
    };
    
    // 6. Git operations
    await this.gitCommit(project, `chore: release v${newVersion}`);
    await this.gitTag(project, `v${newVersion}`);
    
    return {
      version: newVersion,
      releaseNotes,
      artifacts,
      manifests,
      publishable: true,
      distributionUrls: {
        github: `https://github.com/${project.repo}/releases/tag/v${newVersion}`,
        cdn: `https://cdn.${project.domain}/releases/v${newVersion}`
      }
    };
  }
  
  // AI-generated release notes
  private async generateReleaseNotes(commits: Commit[], version: string): Promise<string> {
    // Group commits by type
    const features = commits.filter(c => c.type === 'feat');
    const fixes = commits.filter(c => c.type === 'fix');
    const breaking = commits.filter(c => c.breaking);
    
    return `
# Release v${version}

## 🎉 Features
${features.map(f => `- ${f.description} (${f.hash.substring(0, 7)})`).join('\n')}

## 🐛 Bug Fixes
${fixes.map(f => `- ${f.description} (${f.hash.substring(0, 7)})`).join('\n')}

${breaking.length > 0 ? `
## ⚠️ Breaking Changes
${breaking.map(b => `- ${b.description}\n  ${b.migrationGuide}`).join('\n')}
` : ''}

## 📦 Distribution

### Web Application
- Deploy to any static hosting (Vercel, Netlify, AWS S3)
- Download: \`${project.name}-web-v${version}.zip\`

### Android
- Install: \`${project.name}-v${version}.apk\`
- Requires Android 7.0+

### Windows
- Run installer: \`${project.name}-Setup-v${version}.exe\`
- Requires Windows 10+

### macOS
- Open DMG: \`${project.name}-v${version}.dmg\`
- Requires macOS 11+

## 🙏 Contributors
${this.getContributors(commits).map(c => `- @${c.username}`).join('\n')}
    `;
  }
}
```

---

### 2.1.1 Three-Document Requirements-First Flow Integration

**CRITICAL ARCHITECTURAL PATTERN:** The multi-agent system is built around a **three-document requirements-first flow** that serves as the single source of truth for all agents throughout the project lifecycle.

#### **Architectural Integration Points**

**1. Document Creation (PM Agent Phase)**
- **Idea Summary Document**: Created first, establishes project vision and scope
- **Technical Documentation**: Comprehensive specifications with AI models, algorithms, modules
- **Project Map**: Nodular tree structure showing all components and relationships

**2. Document Storage (Shared Memory Store)**
- All three documents are stored in the centralized SharedMemoryStore
- Documents are immutable once approved by user
- All agents access documents through standardized APIs
- Documents serve as the authoritative reference for all decisions

**3. Agent Consumption Pattern**
```typescript
interface AgentDocumentAccess {
  // All agents receive the three documents as context
  context: {
    ideaSummary: IdeaSummaryDocument;        // Project vision and goals
    technicalDocs: TechnicalDocumentation;   // Detailed specifications
    projectMap: ProjectMap;                  // Component relationships
  };

  // Agents can query specific sections
  queryDocuments(section: DocumentSection): DocumentContent;

  // Agents validate decisions against documents
  validateDecision(decision: any, documents: ThreeDocuments): ValidationResult;
}
```

**4. Decision-Making Grounded in Documents**
- **Architect Agent**: References technical documentation for architecture decisions
- **Coding Agent**: Uses project map for component relationships and technical docs for implementation details
- **Testing Agent**: Validates against technical specifications and project map
- **Builder Agent**: Uses project map for dependency resolution and build order
- **Review Agent**: Cross-references all three documents for comprehensive review

**5. Conflict Resolution**
- When agents have conflicting interpretations, documents serve as arbitration
- PM Agent mediates conflicts by referencing approved documents
- Changes require document updates and user approval

**6. Continuous Validation**
- All agent outputs are validated against the three documents
- Deviations trigger document review or PM intervention
- Ensures project stays aligned with original vision

#### **Benefits of Document-Centric Architecture**

- **Consistency**: All agents work from the same approved specifications
- **Traceability**: Every decision can be traced back to document requirements
- **User Control**: User approval of documents ensures alignment with vision
- **Scalability**: New agents can onboard by reading the three documents
- **Quality Assurance**: Documents provide comprehensive coverage before implementation begins

---

### 2.2 LLM Assignment Strategy (Expanded)

### 2.2 LLM Assignment Strategy (Comprehensive)

The choice of LLM for each agent is critical for performance, cost, and quality. OLAI uses a sophisticated model assignment strategy that balances capabilities, speed, cost, and privacy.

---

#### Model Selection Principles

1. **Task Complexity Matching**: Complex reasoning tasks get powerful models (Pro, R1), simple tasks get fast models (Flash, 8B)
2. **Context Requirements**: Long-context tasks (PM, Architect) get models with large context windows
3. **Speed vs. Quality Trade-off**: Iterative tasks prioritize speed, critical tasks prioritize quality
4. **Cost Optimization**: Use cheapest model that meets quality requirements
5. **Privacy Considerations**: Sensitive code uses local models when possible
6. **Fallback Strategy**: Every agent has fallback models for reliability

---

#### Detailed LLM Assignments

**PM Agent (Project Manager)**

**Primary: Gemini 1.5 Pro**
- **Context Window**: 1M tokens (perfect for long conversations)
- **Strengths**: 
  - Excellent conversation understanding
  - Long-term context retention
  - Natural language generation
  - Requirement extraction from informal descriptions
- **Cost**: Medium ($0.00125/1K input tokens, $0.005/1K output tokens)
- **When to Use**: All user conversations, requirement analysis, progress reports

**Fallback: DeepSeek R1**
- **Context Window**: 128K tokens
- **Strengths**: Strong reasoning, planning, task decomposition
- **Cost**: Low ($0.14/1M input tokens, $2.19/1M output tokens)
- **When to Use**: Complex project planning, multi-agent coordination

**Local Fallback: LLaMA 3 70B** (privacy-sensitive projects)
- **Context Window**: 8K-128K tokens (extended)
- **Strengths**: No external data transmission, good reasoning
- **Cost**: Hardware only (GPU/RAM)
- **When to Use**: Projects with privacy requirements, offline mode

**Model Switch Logic**:
```typescript
class PMAgentModelSelector {
  selectModel(context: PMContext): LLMModel {
    // Use local model if privacy required
    if (context.privacyMode || context.sensitiveData) {
      return LLaMA3_70B;
    }
    
    // Use DeepSeek for complex planning
    if (context.task === 'planning' && context.complexity === 'high') {
      return DeepSeekR1;
    }
    
    // Default to Gemini Pro for conversations
    return Gemini15Pro;
  }
}
```

---

**Architect Agent**

**Primary: Gemini 1.5 Pro**
- **Context Window**: 1M tokens (can analyze entire codebases)
- **Strengths**:
  - System design expertise
  - Understands design patterns and trade-offs
  - Can analyze existing codebases for integration
  - Multi-modal (can process architecture diagrams)
- **Cost**: Medium
- **When to Use**: Initial architecture design, system design decisions

**Secondary: Claude 3.5 Sonnet** (alternative for critical designs)
- **Context Window**: 200K tokens
- **Strengths**: Exceptional reasoning, structured output, attention to detail
- **Cost**: Medium-High ($3/1M input tokens, $15/1M output tokens)
- **When to Use**: Critical architecture decisions, complex system designs

**Local Fallback: LLaMA 3 70B**
- **When to Use**: Privacy-sensitive architectures, offline mode, cost constraints

---

**Coding Agent**

**Primary: DeepSeek R1** (70B)
- **Context Window**: 128K tokens
- **Strengths**:
  - **Best Code Generation**: Industry-leading code quality
  - Strong reasoning for complex algorithms
  - Understands context and intent
  - Can generate Cursor/Copilot-style completions
- **Cost**: Very Low (open-source, can run locally or cloud)
- **When to Use**: 
  - Complex business logic
  - Algorithm implementation
  - New feature development
  - AST-based code modifications

**Secondary: Gemini 1.5 Flash** (for speed)
- **Context Window**: 1M tokens
- **Strengths**: 
  - **Ultra-fast** (10x faster than Pro)
  - Good code completion
  - Low cost
- **Cost**: Very Low ($0.075/1M input tokens, $0.30/1M output tokens)
- **When to Use**:
  - Simple CRUD endpoints
  - Repetitive code (routes, models)
  - Quick fixes and small edits
  - Inline code completion

**Tertiary: CodeLLaMA 34B** (local)
- **Strengths**: Code-specific training, fast local inference
- **When to Use**: Simple edits, local development, privacy mode

**Quaternary: GPT-4 Turbo** (as quality check)
- **When to Use**: Complex algorithms requiring verification, critical code paths

**Model Selection Strategy**:
```typescript
class CodingAgentModelSelector {
  selectModel(task: CodingTask): LLMModel {
    // Critical code paths get best model
    if (task.critical || task.complexity === 'high') {
      return DeepSeekR1;  // Best reasoning
    }
    
    // Simple CRUD operations get fast model
    if (task.type === 'crud' || task.repetitive) {
      return Gemini15Flash;  // Fast and cheap
    }
    
    // Local development gets local model
    if (task.mode === 'local' || task.privateCode) {
      return CodeLLaMA34B;
    }
    
    // Default to DeepSeek for balance
    return DeepSeekR1;
  }
}
```

---

**Research Agent**

**Primary: Gemini 1.5 Pro**
- **Context Window**: 1M tokens
- **Strengths**:
  - **Grounding with Google Search**: Can search web for latest info
  - Reads and understands API documentation
  - Multi-modal (can process screenshots, diagrams)
  - Excellent at comparing alternatives
- **Cost**: Medium
- **When to Use**: API research, library comparison, model discovery

**Secondary: Perplexity AI** (specialized search)
- **Strengths**: Purpose-built for research, cites sources
- **Cost**: Low
- **When to Use**: Quick fact-checking, recent technology lookups

**Fallback: Gemini 1.5 Flash**
- **When to Use**: Quick lookups, simple queries, cached results

---

**Testing Agent**

**Primary: Gemini 1.5 Flash**
- **Context Window**: 1M tokens
- **Strengths**:
  - **Speed**: Generates tests quickly
  - Good pattern recognition (common test patterns)
  - Low cost for high-volume test generation
- **Cost**: Very Low
- **When to Use**: Unit test generation, simple integration tests

**Secondary: DeepSeek R1**
- **When to Use**: Complex test scenarios, edge case generation, test strategy planning

**Tertiary: GPT-4 Turbo** (for comprehensive test suites)
- **When to Use**: Critical system testing, security test generation

---

**Builder Agent**

**Primary: Gemini 1.5 Flash**
- **Strengths**: Fast configuration generation, build script creation
- **Cost**: Very Low
- **When to Use**: Build configuration, Dockerfile generation, CI/CD setup

**Local: LLaMA 3 8B**
- **When to Use**: Simple config edits, local builds

---

**Review Agent**

**Primary: DeepSeek R1**
- **Strengths**:
  - **Strong Reasoning**: Identifies subtle bugs and logic errors
  - Security-aware
  - Good at suggesting refactorings
- **Cost**: Low
- **When to Use**: Code review, security audit, refactoring suggestions

**Secondary: Gemini 1.5 Pro** (for comprehensive analysis)
- **When to Use**: Large codebase analysis, architectural reviews

**Tertiary: Claude 3.5 Sonnet** (for critical reviews)
- **Strengths**: Exceptional attention to detail, finds edge cases
- **When to Use**: Production code reviews, security-critical code

---

**Release Agent**

**Primary: Gemini 1.5 Flash**
- **Strengths**: Fast documentation generation, structured output
- **Cost**: Very Low
- **When to Use**: Release notes, changelog generation, version bumping

**Secondary: Claude 3.5 Sonnet** (for user-facing documentation)
- **When to Use**: User-facing release notes, migration guides, breaking change documentation

---

#### Hybrid Model Usage Strategies

**1. Browser-Based Operations (Gemini Nano)**
- **Use Cases**:
  - Client-side code suggestions
  - Inline documentation
  - Local node validation
  - Privacy-preserving features
- **Advantages**: No API calls, instant responses, works offline
- **Limitations**: Limited capabilities, smaller models

**2. Local Model Operations (LLaMA 3, CodeLLaMA, Mistral)**
- **Use Cases**:
  - Privacy-sensitive code
  - Offline development
  - High-volume operations (cost savings)
  - Sensitive data processing
- **Advantages**: No external data transmission, no API costs, unlimited usage
- **Limitations**: Requires hardware, slower than cloud models

**3. Cost-Optimized Operations**
- **Strategy**: Use cheapest model that meets quality bar
  ```typescript
  // Cost optimization logic
  if (task.qualityRequirement < 8/10 && task.volume > 100) {
    return Gemini15Flash;  // $0.30/1M output tokens
  } else if (task.qualityRequirement >= 9/10) {
    return GPT4Turbo;  // $30/1M output tokens (but highest quality)
  } else {
    return DeepSeekR1;  // $2.19/1M output tokens (good balance)
  }
  ```

**4. Quality-First Operations**
- **Use Cases**: Critical business logic, security code, production releases
- **Strategy**: Use best available model regardless of cost
- **Models**: GPT-4 Turbo, Claude 3.5 Sonnet, DeepSeek R1

**5. Speed-First Operations**
- **Use Cases**: Inline completions, live feedback, interactive features
- **Strategy**: Use fastest model with acceptable quality
- **Models**: Gemini 1.5 Flash, Local 8B models

---

#### Model Cost Comparison (per 1M tokens)

| Model | Input Cost | Output Cost | Speed | Quality | Context |
|-------|-----------|------------|-------|---------|---------|
| GPT-4 Turbo | $10 | $30 | Slow | ★★★★★ | 128K |
| Claude 3.5 Sonnet | $3 | $15 | Medium | ★★★★★ | 200K |
| Gemini 1.5 Pro | $1.25 | $5 | Medium | ★★★★ | 1M |
| DeepSeek R1 | $0.14 | $2.19 | Fast | ★★★★ | 128K |
| Gemini 1.5 Flash | $0.075 | $0.30 | Very Fast | ★★★ | 1M |
| LLaMA 3 70B (local) | $0 | $0 | Medium | ★★★ | 128K |
| LLaMA 3 8B (local) | $0 | $0 | Very Fast | ★★ | 128K |

---

#### Intelligent Model Switching

```typescript
class AgentModelOrchestrator {
  async selectOptimalModel(agent: Agent, task: Task, context: Context): Promise<LLMModel> {
    // 1. Check privacy requirements
    if (context.privacyMode || task.containsSensitiveData) {
      return this.selectLocalModel(agent, task);
    }
    
    // 2. Check cost constraints
    if (context.budget && context.budget.remaining < context.budget.threshold) {
      return this.selectCheapestModel(agent, task);
    }
    
    // 3. Check speed requirements
    if (task.interactive || task.deadline < 5000) { // 5 seconds
      return this.selectFastestModel(agent, task);
    }
    
    // 4. Check quality requirements
    if (task.critical || task.qualityThreshold > 0.9) {
      return this.selectBestModel(agent, task);
    }
    
    // 5. Default to balanced model
    return this.selectBalancedModel(agent, task);
  }
  
  // Dynamic model switching based on real-time performance
  async adaptiveModelSelection(agent: Agent, task: Task): Promise<LLMModel> {
    const history = await this.getAgentPerformanceHistory(agent);
    
    // If recent tasks have been failing, upgrade model
    if (history.recentFailureRate > 0.3) {
      return this.upgradeModel(agent.currentModel);
    }
    
    // If recent tasks have been succeeding with cheaper model, downgrade
    if (history.recentSuccessRate > 0.95 && history.avgQuality > 0.9) {
      const cheaperModel = this.downgradeModel(agent.currentModel);
      if (cheaperModel && cheaperModel.cost < agent.currentModel.cost * 0.5) {
        return cheaperModel;
      }
    }
    
    return agent.currentModel;
  }
}
```

---

### 2.3 Agent Communication Protocol (Expanded)

### 2.3 Agent Communication Protocol (Comprehensive)

Agents communicate through a standardized protocol that ensures reliable message passing, context sharing, and coordination. The protocol is designed for asynchronous, distributed agent operations with built-in resilience.

---

#### Message Format Specification

**Standard Message Structure:**

```typescript
interface AgentMessage {
  // Message Identity
  messageId: string;          // Unique message identifier (UUID)
  timestamp: number;          // Unix timestamp (milliseconds)
  
  // Sender & Receiver
  from: {
    agentId: string;          // Sender agent ID (e.g., 'pm-agent-1')
    agentType: AgentType;     // Agent type (PM, Architect, Coding, etc.)
    instanceId: string;       // Specific agent instance
  };
  to: {
    agentId?: string;         // Specific recipient (optional)
    agentType?: AgentType;    // Broadcast to agent type (optional)
    broadcast?: boolean;      // Broadcast to all agents
  };
  
  // Message Content
  type: MessageType;          // Message type (see below)
  priority: Priority;         // critical, high, medium, low
  payload: any;               // Message-specific data
  
  // Context & Tracing
  context: {
    projectId: string;        // Project identifier
    workflowId?: string;      // Workflow identifier
    taskId?: string;          // Task identifier
    chainId: string;          // Trace ID for end-to-end tracking
    parentMessageId?: string; // For response messages
  };
  
  // Metadata
  metadata: {
    retryCount?: number;      // Number of retries
    expiresAt?: number;       // Message expiration
    requiresAck?: boolean;    // Requires acknowledgment
    ackTimeout?: number;      // Acknowledgment timeout (ms)
  };
  
  // Attachments
  attachments?: Attachment[]; // File attachments, code snippets, etc.
}

interface Attachment {
  id: string;
  type: 'file' | 'code' | 'image' | 'data';
  name: string;
  contentType: string;
  size: number;
  url?: string;
  data?: any;
}
```

---

#### Message Types

**1. Task Assignment**
```typescript
interface TaskAssignmentMessage extends AgentMessage {
  type: 'task.assign';
  payload: {
    task: {
      id: string;
      title: string;
      description: string;
      assignee: string;        // Agent to assign task to
      priority: Priority;
      deadline?: Date;
      dependencies: string[];  // Task IDs this depends on
      estimatedDuration: number; // Minutes
    };
    context: {
      projectContext: ProjectContext;
      requirements: string[];
      constraints: string[];
    };
    resources: {
      files: string[];         // Relevant files
      apis: string[];          // APIs to use
      models: string[];        // AI models to use
    };
  };
}

// Example
const assignMessage: TaskAssignmentMessage = {
  messageId: 'msg-abc123',
  timestamp: Date.now(),
  from: { agentId: 'pm-1', agentType: 'PM', instanceId: 'pm-instance-1' },
  to: { agentId: 'architect-1', agentType: 'Architect' },
  type: 'task.assign',
  priority: 'high',
  payload: {
    task: {
      id: 'task-001',
      title: 'Design system architecture',
      description: 'Create folder structure, API design, and database schema for e-commerce platform',
      assignee: 'architect-1',
      priority: 'high',
      deadline: new Date('2025-01-20T18:00:00'),
      dependencies: [],
      estimatedDuration: 120
    },
    context: {
      projectContext: { /* ... */ },
      requirements: ['User authentication', 'Product catalog', 'Shopping cart'],
      constraints: ['Use PostgreSQL', 'RESTful API', 'React frontend']
    },
    resources: {
      files: [],
      apis: ['Stripe API', 'SendGrid API'],
      models: []
    }
  },
  context: {
    projectId: 'proj-123',
    chainId: 'chain-abc',
    taskId: 'task-001'
  },
  metadata: {
    requiresAck: true,
    ackTimeout: 30000  // 30 seconds
  }
};
```

**2. Task Completion**
```typescript
interface TaskCompletionMessage extends AgentMessage {
  type: 'task.complete';
  payload: {
    taskId: string;
    status: 'completed' | 'partially_completed';
    result: {
      artifacts: Artifact[];   // Generated files, documents, etc.
      outputs: Record<string, any>; // Structured outputs
      metrics: {
        duration: number;      // Actual time taken (ms)
        quality: number;       // Self-assessed quality (0-1)
        confidence: number;    // Confidence in result (0-1)
      };
    };
    notes?: string;            // Additional notes or findings
    followUpTasks?: Task[];    // Tasks that should be created next
  };
}
```

**3. Task Escalation**
```typescript
interface TaskEscalationMessage extends AgentMessage {
  type: 'task.escalate';
  payload: {
    taskId: string;
    reason: 'blocked' | 'insufficient_context' | 'out_of_scope' | 'error' | 'needs_decision';
    details: string;
    blockers?: {
      type: 'dependency' | 'resource' | 'information' | 'decision';
      description: string;
      resolution?: string;     // Suggested resolution
    }[];
    attemptedSolutions: string[]; // What agent already tried
    needsHumanInput?: boolean;    // Requires user intervention
  };
}
```

**4. Information Request**
```typescript
interface InformationRequestMessage extends AgentMessage {
  type: 'info.request';
  payload: {
    question: string;
    context: string;
    requestType: 'clarification' | 'data' | 'decision' | 'review';
    urgency: Priority;
    options?: string[];        // Multiple choice options (if applicable)
    deadline?: Date;
  };
}

interface InformationResponseMessage extends AgentMessage {
  type: 'info.response';
  payload: {
    requestMessageId: string;
    answer: string | any;
    confidence: number;        // 0-1
    sources?: string[];        // Citation sources
  };
}
```

**5. Agent Handoff**
```typescript
interface AgentHandoffMessage extends AgentMessage {
  type: 'agent.handoff';
  payload: {
    taskId: string;
    fromAgent: string;
    toAgent: string;
    reason: string;
    context: {
      workCompleted: string;   // What has been done
      workRemaining: string;   // What needs to be done
      artifacts: Artifact[];
      state: Record<string, any>;
    };
    instructions: string;
  };
}
```

**6. Status Update**
```typescript
interface StatusUpdateMessage extends AgentMessage {
  type: 'status.update';
  payload: {
    taskId?: string;
    status: 'idle' | 'busy' | 'blocked' | 'offline';
    currentActivity?: string;
    progress?: number;         // 0-100
    eta?: number;              // Estimated completion time (ms)
  };
}
```

**7. Error Notification**
```typescript
interface ErrorNotificationMessage extends AgentMessage {
  type: 'error.notify';
  payload: {
    taskId?: string;
    error: {
      code: string;
      message: string;
      stack?: string;
      severity: 'low' | 'medium' | 'high' | 'critical';
    };
    recovery: {
      attempted: boolean;
      successful?: boolean;
      strategy?: string;
    };
  };
}
```

---

#### Context Sharing Architecture

**1. Shared Memory Store**

The shared memory store is the single source of truth for project-wide context accessible to all agents.

```typescript
interface SharedMemoryStore {
  // Project Information
  project: {
    id: string;
    name: string;
    description: string;
    type: string;
    status: ProjectStatus;
    createdAt: Date;
    updatedAt: Date;
  };
  
  // Requirements & Specifications
  requirements: {
    functional: Requirement[];
    nonFunctional: Requirement[];
    constraints: Constraint[];
    priorities: Priority[];
  };
  
  // Architecture Decisions
  architecture: {
    decisions: ArchitectureDecision[];
    patterns: string[];
    stack: TechnologyStack;
    folderStructure: FolderStructure;
    apiDesign: APIDesign;
    dataModel: DataModel;
  };
  
  // Codebase State
  codebase: {
    files: FileTree;
    dependencies: Dependency[];
    configurations: Configuration[];
    lastModified: Date;
  };
  
  // Task Management
  tasks: {
    all: Task[];
    active: Task[];
    completed: Task[];
    blocked: Task[];
    dependencies: TaskDependencyGraph;
  };
  
  // Agent State
  agents: {
    active: AgentState[];
    idle: AgentState[];
    offline: AgentState[];
  };
  
  // Execution History
  history: {
    messages: AgentMessage[];
    decisions: Decision[];
    changes: Change[];
  };
}

class SharedMemory {
  private store: SharedMemoryStore;
  
  // Read operations
  async getProjectContext(): Promise<ProjectContext> {
    return {
      project: this.store.project,
      requirements: this.store.requirements,
      architecture: this.store.architecture
    };
  }
  
  async getTaskContext(taskId: string): Promise<TaskContext> {
    const task = this.store.tasks.all.find(t => t.id === taskId);
    const dependencies = this.getTaskDependencies(taskId);
    const relatedFiles = this.getRelatedFiles(task);
    
    return { task, dependencies, relatedFiles };
  }
  
  // Write operations
  async updateArchitecture(decision: ArchitectureDecision): Promise<void> {
    this.store.architecture.decisions.push(decision);
    this.store.project.updatedAt = new Date();
    await this.persist();
  }
  
  async addTask(task: Task): Promise<void> {
    this.store.tasks.all.push(task);
    this.store.tasks.active.push(task);
    await this.persist();
  }
  
  async updateTaskStatus(taskId: string, status: TaskStatus): Promise<void> {
    const task = this.store.tasks.all.find(t => t.id === taskId);
    if (task) {
      task.status = status;
      
      // Move task between lists
      this.store.tasks.active = this.store.tasks.active.filter(t => t.id !== taskId);
      this.store.tasks.completed = this.store.tasks.completed.filter(t => t.id !== taskId);
      this.store.tasks.blocked = this.store.tasks.blocked.filter(t => t.id !== taskId);
      
      if (status === 'completed') {
        this.store.tasks.completed.push(task);
      } else if (status === 'in_progress') {
        this.store.tasks.active.push(task);
      } else if (status === 'blocked') {
        this.store.tasks.blocked.push(task);
      }
      
      await this.persist();
    }
  }
  
  // Persistence
  private async persist(): Promise<void> {
    await db.sharedMemory.update({
      projectId: this.store.project.id,
      data: this.store
    });
  }
}
```

**2. Agent-Specific Memory**

Each agent maintains its own private memory for task history, learned patterns, and internal state.

```typescript
interface AgentMemory {
  agentId: string;
  agentType: AgentType;
  
  // Task History
  taskHistory: {
    completed: Task[];
    metrics: {
      totalTasks: number;
      successRate: number;
      avgDuration: number;
      qualityScore: number;
    };
  };
  
  // Learned Patterns
  learnedPatterns: {
    codePatterns: Pattern[];    // Common code patterns agent has seen
    architecturePatterns: Pattern[]; // Architecture patterns
    errorPatterns: Pattern[];   // Common errors and solutions
  };
  
  // Agent State
  state: {
    currentTask?: Task;
    queue: Task[];
    workingMemory: Record<string, any>; // Temporary data
    preferences: AgentPreferences;
  };
  
  // Performance Metrics
  performance: {
    responseTime: number[];      // Recent response times
    successRate: number;
    modelUsage: Record<string, number>; // Model usage stats
    costAccumulated: number;
  };
}

class AgentMemoryManager {
  async getRelevantContext(agent: Agent, task: Task): Promise<Context> {
    // Retrieve relevant past experiences
    const similarTasks = await this.findSimilarTasks(agent, task);
    const relevantPatterns = await this.findRelevantPatterns(agent, task);
    const sharedContext = await sharedMemory.getProjectContext();
    
    return {
      shared: sharedContext,
      personal: {
        similarTasks,
        relevantPatterns
      },
      current: task
    };
  }
  
  async recordTaskCompletion(agent: Agent, task: Task, result: TaskResult): Promise<void> {
    // Update task history
    agent.memory.taskHistory.completed.push(task);
    
    // Update metrics
    agent.memory.taskHistory.metrics.totalTasks++;
    agent.memory.taskHistory.metrics.successRate = 
      (agent.memory.taskHistory.metrics.successRate * (agent.memory.taskHistory.metrics.totalTasks - 1) + 
       (result.success ? 1 : 0)) / agent.memory.taskHistory.metrics.totalTasks;
    
    // Extract and store patterns
    const newPatterns = await this.extractPatterns(task, result);
    agent.memory.learnedPatterns.codePatterns.push(...newPatterns);
    
    await this.persist(agent.memory);
  }
}
```

**3. Cross-Agent Context Passing**

When agents hand off tasks or collaborate, context is explicitly passed to ensure continuity.

```typescript
class ContextPasser {
  async prepareHandoffContext(fromAgent: Agent, toAgent: Agent, task: Task): Promise<HandoffContext> {
    // Gather all relevant information
    const workCompleted = await this.summarizeWork(fromAgent, task);
    const artifacts = await this.gatherArtifacts(task);
    const decisions = await this.getDecisions(task);
    const blockers = await this.identifyBlockers(task);
    
    // Package context for receiving agent
    const context: HandoffContext = {
      task,
      workCompleted,
      artifacts,
      decisions,
      blockers,
      recommendations: await this.generateRecommendations(fromAgent, toAgent, task),
      questions: await this.generateQuestions(fromAgent, toAgent, task)
    };
    
    return context;
  }
}
```

---

#### Message Bus Architecture

**Implementation:**

```typescript
class AgentMessageBus {
  private subscribers: Map<AgentType | string, Agent[]> = new Map();
  private messageQueue: PriorityQueue<AgentMessage> = new PriorityQueue();
  private persistence: MessagePersistence;
  
  // Subscribe to messages
  subscribe(agent: Agent, filter?: MessageFilter): void {
    if (!this.subscribers.has(agent.id)) {
      this.subscribers.set(agent.id, []);
    }
    this.subscribers.get(agent.id)!.push(agent);
  }
  
  // Publish message
  async publish(message: AgentMessage): Promise<void> {
    // 1. Validate message
    this.validateMessage(message);
    
    // 2. Persist message
    await this.persistence.save(message);
    
    // 3. Add to queue (priority-based)
    this.messageQueue.enqueue(message, this.getPriority(message.priority));
    
    // 4. Deliver immediately if high priority
    if (message.priority === 'critical' || message.priority === 'high') {
      await this.deliverImmediately(message);
    }
  }
  
  // Deliver message to recipients
  private async deliverImmediately(message: AgentMessage): Promise<void> {
    const recipients = this.findRecipients(message);
    
    await Promise.all(
      recipients.map(async (agent) => {
        try {
          await agent.receiveMessage(message);
          
          // Send acknowledgment if required
          if (message.metadata.requiresAck) {
            await this.sendAcknowledgment(message, agent);
          }
        } catch (error) {
          // Handle delivery failure
          await this.handleDeliveryFailure(message, agent, error);
        }
      })
    );
  }
  
  // Process message queue
  async processQueue(): Promise<void> {
    while (!this.messageQueue.isEmpty()) {
      const message = this.messageQueue.dequeue();
      
      // Check if message expired
      if (message.metadata.expiresAt && Date.now() > message.metadata.expiresAt) {
        continue;
      }
      
      await this.deliverImmediately(message);
    }
  }
  
  // Handle delivery failures
  private async handleDeliveryFailure(
    message: AgentMessage,
    agent: Agent,
    error: Error
  ): Promise<void> {
    const retryCount = message.metadata.retryCount || 0;
    
    if (retryCount < 3) {
      // Retry with exponential backoff
      const delay = Math.pow(2, retryCount) * 1000;
      setTimeout(() => {
        message.metadata.retryCount = retryCount + 1;
        this.publish(message);
      }, delay);
    } else {
      // Escalate to PM agent
      await this.escalateDeliveryFailure(message, agent, error);
    }
  }
}
```

---

**Summary of Agent Communication:**
- ✅ **Standardized Messages**: Consistent format across all agents
- ✅ **Multiple Message Types**: Task assignment, completion, escalation, info requests, handoffs
- ✅ **Priority-Based Delivery**: Critical messages delivered immediately
- ✅ **Reliable Delivery**: Acknowledgments, retries, persistence
- ✅ **Context Sharing**: Shared memory, agent-specific memory, cross-agent context passing
- ✅ **Traceability**: ChainId for end-to-end tracking
- ✅ **Resilience**: Automatic retries, failure handling, escalation

---

## 3. System Architecture for Multi-Agent Coordination

The multi-agent coordination architecture is the backbone of OLAI's ability to function as a complete software workforce replacement. This section details the infrastructure, components, and mechanisms that enable seamless collaboration between specialized agents.

---

### 3.1 Core Components (Comprehensive)

#### **1. Shared Memory Store - Single Source of Truth**

The Shared Memory Store is a centralized, persistent data store that all agents access to maintain project state, requirements, decisions, and context.

**Architecture:**

```typescript
class SharedMemoryStore {
  private db: Database;  // PostgreSQL or MongoDB
  private cache: Redis;   // Hot data cache
  private vectorDB: VectorDatabase;  // For semantic search
  
  // Core data structures
  private projectData: Map<string, ProjectData>;
  private requirementsData: Map<string, Requirements>;
  private architectureData: Map<string, ArchitectureDecisions>;
  private codebaseData: Map<string, CodebaseState>;
  private taskData: Map<string, TaskState>;
  private agentData: Map<string, AgentState>;
  
  /**
   * Project Specifications and Requirements
   */
  async getProjectContext(projectId: string): Promise<ProjectContext> {
    // Check cache first
    const cached = await this.cache.get(`project:${projectId}`);
    if (cached) return JSON.parse(cached);
    
    // Fetch from database
    const project = await this.db.projects.findOne({ id: projectId });
    const requirements = await this.db.requirements.find({ projectId });
    const constraints = await this.db.constraints.find({ projectId });

    // CRITICAL: Fetch the three foundational documents
    const ideaSummary = await this.db.ideaSummaries.findOne({ projectId });
    const technicalDocs = await this.db.technicalDocs.findOne({ projectId });
    const projectMap = await this.db.projectMaps.findOne({ projectId });

    if (!ideaSummary || !technicalDocs || !projectMap) {
      throw new Error(`Project ${projectId} missing required documents. Three-document flow must be completed before proceeding.`);
    }

    const context: ProjectContext = {
      project: {
        id: project.id,
        name: project.name,
        description: project.description,
        type: project.type,  // 'ui-only', 'backend-heavy', 'ai-powered', 'mixed'
        status: project.status,
        createdAt: project.createdAt,
        deadline: project.deadline,
        owner: project.owner
      },
      requirements: {
        functional: requirements.filter(r => r.type === 'functional'),
        nonFunctional: requirements.filter(r => r.type === 'non-functional'),
        constraints: constraints,
        priorities: this.calculatePriorities(requirements)
      },
      /**
       * CRITICAL: Three-Document Requirements-First Flow
       * These documents are the single source of truth for all agents
       */
      projectDocuments: {
        ideaSummary: ideaSummary.document,        // Document 1: Single page idea summary
        technicalDocs: technicalDocs.document,    // Document 2: Detailed technical specifications
        projectMap: projectMap.document           // Document 3: Nodular tree project map
      },
      metadata: {
        lastUpdated: new Date(),
        completeness: this.calculateCompleteness(requirements),
        confidence: this.calculateConfidence(requirements)
      }
    };
    
    // Cache for 5 minutes
    await this.cache.set(`project:${projectId}`, JSON.stringify(context), 'EX', 300);
    
    return context;
  }
  
  /**
   * Architecture Decisions and Patterns
   */
  async getArchitectureDecisions(projectId: string): Promise<ArchitectureDecisions> {
    const decisions = await this.db.architectureDecisions.find({ projectId });
    
    return {
      folderStructure: decisions.find(d => d.type === 'folder-structure')?.data,
      apiDesign: decisions.find(d => d.type === 'api-design')?.data,
      databaseSchema: decisions.find(d => d.type === 'database-schema')?.data,
      technologyStack: decisions.find(d => d.type === 'tech-stack')?.data,
      modelArchitecture: decisions.find(d => d.type === 'model-architecture')?.data,
      cachingStrategy: decisions.find(d => d.type === 'caching-strategy')?.data,
      securityApproach: decisions.find(d => d.type === 'security-approach')?.data,
      scalabilityPlan: decisions.find(d => d.type === 'scalability-plan')?.data,
      decisions: decisions,  // All decisions with reasoning
      patterns: this.extractPatterns(decisions)
    };
  }
  
  async addArchitectureDecision(
    projectId: string,
    decision: ArchitectureDecision
  ): Promise<void> {
    // Validate decision
    this.validateArchitectureDecision(decision);
    
    // Store decision
    await this.db.architectureDecisions.create({
      projectId,
      ...decision,
      timestamp: new Date(),
      version: await this.getNextDecisionVersion(projectId, decision.type)
    });
    
    // Invalidate cache
    await this.cache.del(`architecture:${projectId}`);
    
    // Notify agents of architecture change
    await this.broadcastArchitectureChange(projectId, decision);
  }
  
  /**
   * Code Structure and File Mappings
   */
  async getCodebaseState(projectId: string): Promise<CodebaseState> {
    const state = {
      files: await this.getFileTree(projectId),
      dependencies: await this.getDependencies(projectId),
      configurations: await this.getConfigurations(projectId),
      lastModified: await this.getLastModifiedTime(projectId),
      health: await this.calculateCodebaseHealth(projectId),
      metrics: {
        totalFiles: 0,
        totalLines: 0,
        testCoverage: 0,
        technicalDebt: 0
      }
    };
    
    // Calculate metrics
    state.metrics = await this.calculateCodebaseMetrics(state.files);
    
    return state;
  }
  
  async updateFile(
    projectId: string,
    filePath: string,
    content: string,
    agentId: string
  ): Promise<void> {
    // Create file version
    await this.db.fileVersions.create({
      projectId,
      filePath,
      content,
      modifiedBy: agentId,
      timestamp: new Date()
    });
    
    // Update current file
    await this.db.files.upsert({
      where: { projectId, filePath },
      update: { content, modifiedBy: agentId, modifiedAt: new Date() },
      create: { projectId, filePath, content, createdBy: agentId }
    });
    
    // Invalidate codebase cache
    await this.cache.del(`codebase:${projectId}`);
  }
  
  /**
   * Task Assignments and Status
   */
  async getTaskState(projectId: string): Promise<TaskState> {
    const tasks = await this.db.tasks.find({ projectId });
    
    return {
      all: tasks,
      active: tasks.filter(t => t.status === 'in_progress'),
      completed: tasks.filter(t => t.status === 'completed'),
      blocked: tasks.filter(t => t.status === 'blocked'),
      failed: tasks.filter(t => t.status === 'failed'),
      pending: tasks.filter(t => t.status === 'pending'),
      dependencies: await this.buildDependencyGraph(tasks),
      criticalPath: await this.calculateCriticalPath(tasks),
      progress: {
        overall: this.calculateProgress(tasks),
        byPhase: this.calculatePhaseProgress(tasks),
        byAgent: this.calculateAgentProgress(tasks)
      }
    };
  }
  
  async updateTaskStatus(
    taskId: string,
    status: TaskStatus,
    agentId: string,
    metadata?: any
  ): Promise<void> {
    await this.db.tasks.update({
      where: { id: taskId },
      data: {
        status,
        lastModifiedBy: agentId,
        lastModifiedAt: new Date(),
        metadata: { ...metadata }
      }
    });
    
    // Emit status change event
    await this.emitTaskStatusChange(taskId, status, agentId);
    
    // Check if status change unblocks other tasks
    await this.checkBlockedTasks(taskId);
  }
  
  /**
   * Agent Conversation History
   */
  async getConversationHistory(
    projectId: string,
    options?: {
      agentId?: string;
      messageType?: MessageType;
      since?: Date;
      limit?: number;
    }
  ): Promise<AgentMessage[]> {
    let query = { projectId };
    
    if (options?.agentId) {
      query['$or'] = [
        { 'from.agentId': options.agentId },
        { 'to.agentId': options.agentId }
      ];
    }
    
    if (options?.messageType) {
      query['type'] = options.messageType;
    }
    
    if (options?.since) {
      query['timestamp'] = { $gte: options.since.getTime() };
    }
    
    const messages = await this.db.messages.find(query)
      .sort({ timestamp: -1 })
      .limit(options?.limit || 100);
    
    return messages;
  }
  
  /**
   * Semantic Search with Vector DB
   */
  async semanticSearch(
    projectId: string,
    query: string,
    type?: 'requirement' | 'decision' | 'code' | 'message'
  ): Promise<SearchResult[]> {
    // Generate query embedding
    const embedding = await this.generateEmbedding(query);
    
    // Search in vector DB
    const results = await this.vectorDB.search({
      vector: embedding,
      filter: {
        projectId,
        type: type || undefined
      },
      limit: 10,
      threshold: 0.7  // Similarity threshold
    });
    
    // Hydrate results with full data
    const hydratedResults = await Promise.all(
      results.map(async (result) => {
        const fullData = await this.getById(result.id, result.type);
        return {
          ...result,
          data: fullData
        };
      })
    );
    
    return hydratedResults;
  }
}
```

**Data Structures:**

```typescript
interface ProjectContext {
  project: {
    id: string;
    name: string;
    description: string;
    type: 'ui-only' | 'backend-heavy' | 'ai-powered' | 'mixed';
    status: 'planning' | 'in_progress' | 'testing' | 'deploying' | 'completed';
    createdAt: Date;
    deadline?: Date;
    owner: string;
  };
  requirements: {
    functional: Requirement[];
    nonFunctional: Requirement[];
    constraints: Constraint[];
    priorities: PriorityMap;
  };
  /**
   * CRITICAL: Three-Document Requirements-First Flow
   * These documents serve as the single source of truth for the entire project lifecycle
   */
  projectDocuments: {
    ideaSummary: IdeaSummaryDocument;        // Document 1: Single page idea summary
    technicalDocs: TechnicalDocumentation;   // Document 2: Detailed technical specifications
    projectMap: ProjectMap;                  // Document 3: Nodular tree project map
  };
  metadata: {
    lastUpdated: Date;
    completeness: number;  // 0-100%
    confidence: number;    // 0-100%
  };
}

interface ArchitectureDecisions {
  folderStructure: FolderStructure;
  apiDesign: APIDesign;
  databaseSchema: DatabaseSchema;
  technologyStack: TechnologyStack;
  modelArchitecture: ModelArchitecture;
  cachingStrategy: CachingStrategy;
  securityApproach: SecurityApproach;
  scalabilityPlan: ScalabilityPlan;
  decisions: ArchitectureDecision[];
  patterns: Pattern[];
}

interface CodebaseState {
  files: FileTree;
  dependencies: Dependency[];
  configurations: Configuration[];
  lastModified: Date;
  health: {
    score: number;  // 0-100
    issues: Issue[];
    warnings: Warning[];
  };
  metrics: {
    totalFiles: number;
    totalLines: number;
    testCoverage: number;
    technicalDebt: number;
  };
}

interface TaskState {
  all: Task[];
  active: Task[];
  completed: Task[];
  blocked: Task[];
  failed: Task[];
  pending: Task[];
  dependencies: DependencyGraph;
  criticalPath: Task[];
  progress: {
    overall: number;
    byPhase: Record<string, number>;
    byAgent: Record<string, number>;
  };
}
```

**Benefits:**
- ✅ **Single Source of Truth**: All agents access same data
- ✅ **Fast Access**: Redis caching for hot data
- ✅ **Semantic Search**: Vector DB for intelligent context retrieval
- ✅ **Version Control**: All changes tracked with history
- ✅ **Event-Driven**: Changes broadcast to interested agents
- ✅ **Scalable**: Sharded database for large projects

---

#### **2. Task Queue System - Priority-Based Orchestration**

The Task Queue System manages task scheduling, dependencies, priorities, and execution order across all agents.

**Architecture:**

```typescript
class TaskQueueSystem {
  private priorityQueue: PriorityQueue<Task>;
  private dependencyGraph: DependencyGraph;
  private taskRegistry: Map<string, Task>;
  private executingTasks: Set<string>;
  
  /**
   * Add task to queue with dependencies and priority
   */
  async enqueueTask(task: Task): Promise<void> {
    // Validate task
    this.validateTask(task);
    
    // Calculate priority score
    const priorityScore = this.calculatePriority(task);
    
    // Add to priority queue
    this.priorityQueue.enqueue(task, priorityScore);
    
    // Update dependency graph
    await this.dependencyGraph.addNode(task.id, task.dependencies);
    
    // Store in registry
    this.taskRegistry.set(task.id, task);
    
    // Emit task queued event
    await this.emitTaskQueued(task);
  }
  
  /**
   * Calculate task priority based on multiple factors
   */
  private calculatePriority(task: Task): number {
    let score = 0;
    
    // Base priority (critical=100, high=75, medium=50, low=25)
    const priorityScores = {
      critical: 100,
      high: 75,
      medium: 50,
      low: 25
    };
    score += priorityScores[task.priority];
    
    // Deadline urgency (closer deadline = higher priority)
    if (task.deadline) {
      const timeUntilDeadline = task.deadline.getTime() - Date.now();
      const hoursTillDeadline = timeUntilDeadline / (1000 * 60 * 60);
      if (hoursTillDeadline < 2) score += 50;  // Very urgent
      else if (hoursTillDeadline < 6) score += 30;
      else if (hoursTillDeadline < 24) score += 10;
    }
    
    // Dependency count (fewer dependencies = higher priority)
    score -= task.dependencies.length * 5;
    
    // Blocking count (more tasks blocked by this = higher priority)
    const blockingCount = this.countBlockedTasks(task.id);
    score += blockingCount * 10;
    
    // Estimated duration (shorter tasks = higher priority for quick wins)
    if (task.estimatedDuration < 30) score += 15;  // < 30 minutes
    else if (task.estimatedDuration < 60) score += 10;
    
    return Math.max(0, score);  // Ensure non-negative
  }
  
  /**
   * Get next executable task (with dependencies satisfied)
   */
  async getNextTask(): Promise<Task | null> {
    while (!this.priorityQueue.isEmpty()) {
      const task = this.priorityQueue.peek();
      
      // Check if dependencies are satisfied
      const dependenciesSatisfied = await this.areDependenciesSatisfied(task);
      
      if (dependenciesSatisfied) {
        // Remove from queue and mark as executing
        this.priorityQueue.dequeue();
        this.executingTasks.add(task.id);
        return task;
      } else {
        // Move to blocked state
        this.priorityQueue.dequeue();
        task.status = 'blocked';
        await this.updateTaskStatus(task.id, 'blocked');
      }
    }
    
    return null;  // No executable tasks available
  }
  
  /**
   * Check if all task dependencies are completed
   */
  private async areDependenciesSatisfied(task: Task): Promise<boolean> {
    if (task.dependencies.length === 0) return true;
    
    for (const depId of task.dependencies) {
      const depTask = this.taskRegistry.get(depId);
      if (!depTask || depTask.status !== 'completed') {
        return false;
      }
    }
    
    return true;
  }
  
  /**
   * Check and unblock tasks when a dependency completes
   */
  async checkBlockedTasks(completedTaskId: string): Promise<void> {
    // Find all tasks blocked by this task
    const blockedTasks = Array.from(this.taskRegistry.values())
      .filter(t => t.status === 'blocked' && t.dependencies.includes(completedTaskId));
    
    for (const task of blockedTasks) {
      // Check if all dependencies now satisfied
      const canExecute = await this.areDependenciesSatisfied(task);
      
      if (canExecute) {
        // Move back to queue
        task.status = 'pending';
        await this.enqueueTask(task);
        await this.updateTaskStatus(task.id, 'pending');
      }
    }
  }
  
  /**
   * Handle task completion
   */
  async completeTask(taskId: string, result: TaskResult): Promise<void> {
    this.executingTasks.delete(taskId);
    
    const task = this.taskRegistry.get(taskId);
    if (!task) throw new Error(`Task ${taskId} not found`);
    
    task.status = 'completed';
    task.result = result;
    task.completedAt = new Date();
    
    // Update in shared memory
    await sharedMemory.updateTaskStatus(taskId, 'completed', result.agentId, result);
    
    // Check if any blocked tasks can now execute
    await this.checkBlockedTasks(taskId);
    
    // Emit completion event
    await this.emitTaskCompleted(task, result);
  }
  
  /**
   * Handle task failure
   */
  async failTask(taskId: string, error: Error, agentId: string): Promise<void> {
    this.executingTasks.delete(taskId);
    
    const task = this.taskRegistry.get(taskId);
    if (!task) throw new Error(`Task ${taskId} not found`);
    
    task.status = 'failed';
    task.error = error;
    task.failureCount = (task.failureCount || 0) + 1;
    
    // Check if should retry
    if (task.retryable && task.failureCount < task.maxRetries) {
      // Re-queue with exponential backoff
      const delay = Math.pow(2, task.failureCount) * 1000;
      setTimeout(() => {
        task.status = 'pending';
        this.enqueueTask(task);
      }, delay);
    } else {
      // Permanent failure - escalate
      await this.escalateFailedTask(task, error, agentId);
    }
  }
  
  /**
   * Build critical path (longest path through dependencies)
   */
  async calculateCriticalPath(tasks: Task[]): Promise<Task[]> {
    const graph = this.buildTaskGraph(tasks);
    
    // Topological sort
    const sorted = this.topologicalSort(graph);
    
    // Calculate earliest start/finish times
    const earliestFinish = new Map<string, number>();
    for (const taskId of sorted) {
      const task = this.taskRegistry.get(taskId);
      const depFinishTimes = task.dependencies.map(d => earliestFinish.get(d) || 0);
      const earliestStart = Math.max(...depFinishTimes, 0);
      earliestFinish.set(taskId, earliestStart + task.estimatedDuration);
    }
    
    // Find critical path (tasks with zero slack)
    const criticalPath: Task[] = [];
    let currentTaskId = sorted[sorted.length - 1];  // Start from last task
    
    while (currentTaskId) {
      const task = this.taskRegistry.get(currentTaskId);
      criticalPath.unshift(task);
      
      // Find predecessor on critical path
      currentTaskId = this.findCriticalPredecessor(currentTaskId, earliestFinish);
    }
    
    return criticalPath;
  }
}
```

**Task Scheduling Strategies:**

```typescript
interface TaskSchedulingStrategy {
  // FIFO: First In, First Out
  fifo(): void {
    // Tasks executed in order added
  }
  
  // Priority-Based: Higher priority first
  priorityBased(): void {
    // Tasks executed by calculated priority
  }
  
  // Deadline-Driven: Closest deadline first
  deadlineDriven(): void {
    // Tasks with soonest deadlines executed first
  }
  
  // Shortest Job First: Quick wins
  shortestJobFirst(): void {
    // Short tasks executed first for momentum
  }
  
  // Critical Path: Focus on bottlenecks
  criticalPath(): void {
    // Tasks on critical path prioritized
  }
  
  // Load Balancing: Distribute across agents
  loadBalancing(): void {
    // Balance work across available agents
  }
}
```

**Benefits:**
- ✅ **Smart Scheduling**: Multi-factor priority calculation
- ✅ **Dependency Management**: Automatic dependency tracking and resolution
- ✅ **Blocked Task Handling**: Automatically unblock when dependencies complete
- ✅ **Retry Logic**: Automatic retry with exponential backoff
- ✅ **Critical Path**: Identifies and prioritizes bottlenecks
- ✅ **Scalable**: Handles thousands of tasks efficiently

---

#### **3. Message Bus - Event-Driven Communication**

The Message Bus enables real-time, asynchronous communication between agents with guaranteed delivery and ordering.

**Architecture:**

```typescript
class MessageBus {
  private broker: MessageBroker;  // RabbitMQ, Kafka, or Redis Streams
  private subscribers: Map<string, Set<MessageHandler>>;
  private persistence: MessagePersistence;
  
  /**
   * Publish message to bus
   */
  async publish(message: AgentMessage): Promise<void> {
    // 1. Validate message
    this.validateMessage(message);
    
    // 2. Assign message ID
    message.messageId = message.messageId || generateUUID();
    message.timestamp = message.timestamp || Date.now();
    
    // 3. Persist message
    await this.persistence.save(message);
    
    // 4. Publish to broker
    await this.broker.publish(this.getRoutingKey(message), message);
    
    // 5. Emit telemetry
    await this.emitMessagePublished(message);
  }
  
  /**
   * Subscribe to messages
   */
  subscribe(
    agentId: string,
    handler: MessageHandler,
    filter?: MessageFilter
  ): Subscription {
    // Create subscription
    const subscription: Subscription = {
      agentId,
      handler,
      filter,
      active: true
    };
    
    // Register handler
    if (!this.subscribers.has(agentId)) {
      this.subscribers.set(agentId, new Set());
    }
    this.subscribers.get(agentId).add(handler);
    
    // Subscribe to broker with routing key
    const routingKey = this.buildRoutingKey(agentId, filter);
    this.broker.subscribe(routingKey, async (message) => {
      await this.deliverMessage(message, handler, filter);
    });
    
    return subscription;
  }
  
  /**
   * Deliver message to handler
   */
  private async deliverMessage(
    message: AgentMessage,
    handler: MessageHandler,
    filter?: MessageFilter
  ): Promise<void> {
    // Apply filter
    if (filter && !this.matchesFilter(message, filter)) {
      return;
    }
    
    try {
      // Deliver to handler
      await handler(message);
      
      // Send acknowledgment if required
      if (message.metadata.requiresAck) {
        await this.sendAcknowledgment(message);
      }
      
      // Emit telemetry
      await this.emitMessageDelivered(message);
      
    } catch (error) {
      // Handle delivery failure
      await this.handleDeliveryFailure(message, error);
    }
  }
  
  /**
   * Get routing key for message
   */
  private getRoutingKey(message: AgentMessage): string {
    // Format: <message-type>.<from-agent-type>.<to-agent-type>
    return [
      message.type,
      message.from.agentType,
      message.to.agentType || '*'
    ].join('.');
  }
  
  /**
   * Build routing key pattern for subscription
   */
  private buildRoutingKey(agentId: string, filter?: MessageFilter): string {
    if (!filter) {
      // Subscribe to all messages for this agent
      return `*.*.${agentId}`;
    }
    
    // Build pattern based on filter
    return [
      filter.messageType || '*',
      filter.fromAgentType || '*',
      agentId
    ].join('.');
  }
}
```

**Message Delivery Guarantees:**

```typescript
enum DeliveryGuarantee {
  AT_MOST_ONCE = 'at-most-once',    // Fire and forget
  AT_LEAST_ONCE = 'at-least-once',  // May receive duplicates
  EXACTLY_ONCE = 'exactly-once'      // Guaranteed single delivery
}

class GuaranteedDelivery {
  /**
   * At-Least-Once: Retry until acknowledged
   */
  async atLeastOnce(message: AgentMessage): Promise<void> {
    let delivered = false;
    let retries = 0;
    const maxRetries = 5;
    
    while (!delivered && retries < maxRetries) {
      try {
        await this.deliver(message);
        await this.waitForAcknowledgment(message, 30000);  // 30s timeout
        delivered = true;
      } catch (error) {
        retries++;
        await this.delay(Math.pow(2, retries) * 1000);  // Exponential backoff
      }
    }
    
    if (!delivered) {
      throw new Error(`Failed to deliver message ${message.messageId} after ${maxRetries} attempts`);
    }
  }
  
  /**
   * Exactly-Once: Idempotent delivery with deduplication
   */
  async exactlyOnce(message: AgentMessage): Promise<void> {
    // Check if already delivered
    const alreadyDelivered = await this.checkDeliveryStatus(message.messageId);
    if (alreadyDelivered) {
      return;  // Skip duplicate
    }
    
    // Deliver with transaction
    await this.deliverWithTransaction(message);
    
    // Mark as delivered
    await this.markDelivered(message.messageId);
  }
}
```

---

#### **4. Agent Registry - Capability & Health Management**

The Agent Registry maintains real-time information about all agents, their capabilities, availability, and performance metrics.

**Architecture:**

```typescript
class AgentRegistry {
  private agents: Map<string, AgentRegistration>;
  private healthMonitor: HealthMonitor;
  
  /**
   * Register agent with capabilities
   */
  async registerAgent(registration: AgentRegistration): Promise<void> {
    // Validate registration
    this.validateRegistration(registration);
    
    // Store registration
    this.agents.set(registration.agentId, {
      ...registration,
      registeredAt: new Date(),
      lastHeartbeat: new Date(),
      status: 'online'
    });
    
    // Start health monitoring
    await this.healthMonitor.startMonitoring(registration.agentId);
    
    // Emit agent registered event
    await this.emitAgentRegistered(registration);
  }
  
  /**
   * Find agent with required capabilities
   */
  async findAgent(requirements: AgentRequirements): Promise<AgentRegistration | null> {
    const candidates = Array.from(this.agents.values())
      .filter(agent => agent.status === 'online')
      .filter(agent => this.matchesRequirements(agent, requirements))
      .filter(agent => agent.currentLoad < agent.maxConcurrency);
    
    if (candidates.length === 0) return null;
    
    // Select agent with lowest load
    return candidates.reduce((best, current) => 
      current.currentLoad < best.currentLoad ? current : best
    );
  }
  
  /**
   * Update agent health status
   */
  async updateHealth(agentId: string, health: HealthStatus): Promise<void> {
    const agent = this.agents.get(agentId);
    if (!agent) return;
    
    agent.health = health;
    agent.lastHeartbeat = new Date();
    
    // Check if agent became unhealthy
    if (health.status === 'unhealthy') {
      await this.handleUnhealthyAgent(agent);
    }
  }
  
  /**
   * Get agent performance metrics
   */
  async getPerformanceMetrics(agentId: string): Promise<AgentMetrics> {
    const agent = this.agents.get(agentId);
    if (!agent) throw new Error(`Agent ${agentId} not found`);
    
    return {
      totalTasks: agent.metrics.totalTasks,
      successRate: agent.metrics.successRate,
      avgDuration: agent.metrics.avgDuration,
      avgQuality: agent.metrics.avgQuality,
      currentLoad: agent.currentLoad,
      maxConcurrency: agent.maxConcurrency,
      uptime: Date.now() - agent.registeredAt.getTime(),
      lastActive: agent.lastHeartbeat
    };
  }
}

interface AgentRegistration {
  agentId: string;
  agentType: AgentType;
  capabilities: Capability[];
  maxConcurrency: number;
  currentLoad: number;
  status: 'online' | 'offline' | 'busy';
  health: HealthStatus;
  metrics: AgentMetrics;
  registeredAt: Date;
  lastHeartbeat: Date;
}

interface Capability {
  name: string;
  version: string;
  proficiency: number;  // 0-100
}
```

**Benefits:**
- ✅ **Dynamic Discovery**: Find agents with required capabilities
- ✅ **Load Balancing**: Distribute work based on agent load
- ✅ **Health Monitoring**: Detect and handle unhealthy agents
- ✅ **Performance Tracking**: Monitor agent efficiency and quality
- ✅ **Automatic Failover**: Reassign tasks from failed agents

---

**Summary of Core Components:**
- ✅ **Shared Memory Store**: Centralized project state and context
- ✅ **Task Queue System**: Priority-based task scheduling with dependency management
- ✅ **Message Bus**: Real-time, reliable inter-agent communication
- ✅ **Agent Registry**: Capability management and health monitoring
- ✅ **Scalable Architecture**: Handles large projects with multiple agents
- ✅ **Fault Tolerant**: Automatic retry, fallback, and recovery mechanisms

### 3.2 Task Lifecycle State Machine (Comprehensive)

The Task Lifecycle State Machine governs how tasks transition through their execution lifecycle, from creation to completion or failure, ensuring proper state management and traceability.

---

#### **State Definitions**

```typescript
enum TaskStatus {
  PENDING = 'pending',           // Task created, waiting to be assigned
  ASSIGNED = 'assigned',         // Assigned to agent, not yet started
  IN_PROGRESS = 'in_progress',   // Agent actively working on task
  BLOCKED = 'blocked',           // Waiting for dependencies or external input
  COMPLETED = 'completed',       // Successfully finished
  FAILED = 'failed',             // Encountered unrecoverable error
  ESCALATED = 'escalated',       // Requires human intervention
  CANCELLED = 'cancelled'        // Manually cancelled by user/PM
}

interface TaskState {
  taskId: string;
  status: TaskStatus;
  assignedAgent?: string;
  startTime?: Date;
  endTime?: Date;
  progress: number;  // 0-100
  metadata: {
    retryCount: number;
    blockReason?: string;
    errorMessage?: string;
    escalationReason?: string;
  };
  history: StateTransition[];
}

interface StateTransition {
  from: TaskStatus;
  to: TaskStatus;
  timestamp: Date;
  triggeredBy: string;  // Agent ID or system
  reason: string;
  metadata?: Record<string, any>;
}
```

---

#### **State Transition Rules**

```typescript
class TaskStateMachine {
  // Valid transitions map
  private validTransitions: Map<TaskStatus, Set<TaskStatus>> = new Map([
    [TaskStatus.PENDING, new Set([TaskStatus.ASSIGNED, TaskStatus.CANCELLED])],
    [TaskStatus.ASSIGNED, new Set([TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED])],
    [TaskStatus.IN_PROGRESS, new Set([
      TaskStatus.BLOCKED,
      TaskStatus.COMPLETED,
      TaskStatus.FAILED,
      TaskStatus.ESCALATED,
      TaskStatus.CANCELLED
    ])],
    [TaskStatus.BLOCKED, new Set([
      TaskStatus.IN_PROGRESS,
      TaskStatus.FAILED,
      TaskStatus.ESCALATED,
      TaskStatus.CANCELLED
    ])],
    [TaskStatus.FAILED, new Set([
      TaskStatus.ASSIGNED,  // Retry
      TaskStatus.ESCALATED,
      TaskStatus.CANCELLED
    ])],
    [TaskStatus.ESCALATED, new Set([
      TaskStatus.ASSIGNED,  // After human resolution
      TaskStatus.CANCELLED
    ])],
    [TaskStatus.COMPLETED, new Set([])],  // Terminal state
    [TaskStatus.CANCELLED, new Set([])]   // Terminal state
  ]);
  
  /**
   * Transition task to new state
   */
  async transition(
    taskId: string,
    newStatus: TaskStatus,
    triggeredBy: string,
    reason: string,
    metadata?: Record<string, any>
  ): Promise<void> {
    // 1. Get current state
    const currentState = await this.getTaskState(taskId);
    
    // 2. Validate transition
    if (!this.isValidTransition(currentState.status, newStatus)) {
      throw new Error(
        `Invalid state transition: ${currentState.status} -> ${newStatus}`
      );
    }
    
    // 3. Execute pre-transition hooks
    await this.executePreTransitionHooks(taskId, currentState.status, newStatus);
    
    // 4. Update state
    const transition: StateTransition = {
      from: currentState.status,
      to: newStatus,
      timestamp: new Date(),
      triggeredBy,
      reason,
      metadata
    };
    
    currentState.status = newStatus;
    currentState.history.push(transition);
    
    // Update timestamps
    if (newStatus === TaskStatus.IN_PROGRESS && !currentState.startTime) {
      currentState.startTime = new Date();
    }
    if ([TaskStatus.COMPLETED, TaskStatus.FAILED, TaskStatus.CANCELLED].includes(newStatus)) {
      currentState.endTime = new Date();
    }
    
    // 5. Persist state
    await this.saveTaskState(taskId, currentState);
    
    // 6. Execute post-transition hooks
    await this.executePostTransitionHooks(taskId, currentState.status, newStatus);
    
    // 7. Emit state change event
    await this.emitStateChange(taskId, transition);
  }
  
  /**
   * Check if transition is valid
   */
  private isValidTransition(from: TaskStatus, to: TaskStatus): boolean {
    const validNextStates = this.validTransitions.get(from);
    return validNextStates ? validNextStates.has(to) : false;
  }
  
  /**
   * Execute hooks before transition
   */
  private async executePreTransitionHooks(
    taskId: string,
    from: TaskStatus,
    to: TaskStatus
  ): Promise<void> {
    // Pre-transition logic based on target state
    switch (to) {
      case TaskStatus.ASSIGNED:
        // Ensure agent is available
        await this.validateAgentAvailable(taskId);
        break;
        
      case TaskStatus.IN_PROGRESS:
        // Ensure dependencies are met
        await this.validateDependenciesMet(taskId);
        // Reserve resources
        await this.reserveResources(taskId);
        break;
        
      case TaskStatus.BLOCKED:
        // Identify blocking reason
        await this.identifyBlocker(taskId);
        break;
        
      case TaskStatus.ESCALATED:
        // Prepare escalation context
        await this.prepareEscalationContext(taskId);
        break;
    }
  }
  
  /**
   * Execute hooks after transition
   */
  private async executePostTransitionHooks(
    taskId: string,
    from: TaskStatus,
    to: TaskStatus
  ): Promise<void> {
    switch (to) {
      case TaskStatus.COMPLETED:
        // Unblock dependent tasks
        await this.unblockDependentTasks(taskId);
        // Release resources
        await this.releaseResources(taskId);
        // Update agent metrics
        await this.updateAgentMetrics(taskId, true);
        break;
        
      case TaskStatus.FAILED:
        // Check retry logic
        await this.handleTaskFailure(taskId);
        // Update agent metrics
        await this.updateAgentMetrics(taskId, false);
        break;
        
      case TaskStatus.BLOCKED:
        // Move to blocked queue
        await this.moveToBlockedQueue(taskId);
        break;
        
      case TaskStatus.ESCALATED:
        // Notify user
        await this.notifyUserEscalation(taskId);
        break;
    }
  }
  
  /**
   * Get task execution history
   */
  async getTaskHistory(taskId: string): Promise<StateTransition[]> {
    const state = await this.getTaskState(taskId);
    return state.history;
  }
  
  /**
   * Calculate task duration
   */
  calculateDuration(state: TaskState): number | null {
    if (!state.startTime) return null;
    const endTime = state.endTime || new Date();
    return endTime.getTime() - state.startTime.getTime();
  }
}
```

---

#### **ChainId & Distributed Tracing System**

The ChainId and tracing system provides end-to-end observability across all agents, nodes, and workflow threads.

```typescript
interface TraceContext {
  // Trace identifiers
  chainId: string;           // Unique ID for entire execution chain
  traceId: string;           // Current trace segment ID
  spanId: string;            // Current operation span ID
  parentSpanId?: string;     // Parent span for nested operations
  
  // Context metadata
  projectId: string;
  workflowId: string;
  taskId?: string;
  agentId?: string;
  nodeId?: string;
  threadId?: string;         // Thread/edge ID for node connections
  
  // Timing information
  startTime: number;
  endTime?: number;
  duration?: number;
  
  // Additional context
  metadata: Record<string, any>;
  tags: Record<string, string>;
  logs: TraceLog[];
  baggage: Record<string, string>;  // Cross-service context
}

interface TraceLog {
  timestamp: number;
  level: 'debug' | 'info' | 'warn' | 'error';
  message: string;
  fields?: Record<string, any>;
}

class DistributedTracing {
  private tracer: Tracer;  // OpenTelemetry or similar
  
  /**
   * Start new trace for agent chain
   */
  async startChain(projectId: string, workflowId: string): Promise<TraceContext> {
    const chainId = generateUUID();
    const traceId = generateUUID();
    const spanId = generateUUID();
    
    const context: TraceContext = {
      chainId,
      traceId,
      spanId,
      projectId,
      workflowId,
      startTime: Date.now(),
      metadata: {},
      tags: {
        'project.id': projectId,
        'workflow.id': workflowId
      },
      logs: [],
      baggage: {}
    };
    
    // Create root span
    const span = this.tracer.startSpan('agent-chain', {
      attributes: context.tags
    });
    
    // Store context
    await this.storeContext(chainId, context);
    
    return context;
  }
  
  /**
   * Create child span for agent operation
   */
  async startAgentSpan(
    parentContext: TraceContext,
    agentId: string,
    taskId: string,
    operation: string
  ): Promise<TraceContext> {
    const childContext: TraceContext = {
      ...parentContext,
      spanId: generateUUID(),
      parentSpanId: parentContext.spanId,
      agentId,
      taskId,
      startTime: Date.now(),
      logs: []
    };
    
    // Create child span
    const span = this.tracer.startSpan(operation, {
      parent: parentContext.spanId,
      attributes: {
        'agent.id': agentId,
        'agent.type': this.getAgentType(agentId),
        'task.id': taskId,
        'operation': operation
      }
    });
    
    return childContext;
  }
  
  /**
   * Add thread-level tracing
   */
  async traceThread(
    context: TraceContext,
    sourceNodeId: string,
    targetNodeId: string,
    threadId: string,
    data: any
  ): Promise<void> {
    // Create thread span
    const threadSpan = this.tracer.startSpan('thread-execution', {
      parent: context.spanId,
      attributes: {
        'thread.id': threadId,
        'source.node': sourceNodeId,
        'target.node': targetNodeId,
        'data.size': JSON.stringify(data).length
      }
    });
    
    // Log thread execution
    context.logs.push({
      timestamp: Date.now(),
      level: 'info',
      message: `Thread ${threadId}: ${sourceNodeId} -> ${targetNodeId}`,
      fields: {
        sourceNode: sourceNodeId,
        targetNode: targetNodeId,
        dataKeys: Object.keys(data)
      }
    });
    
    // Store thread metadata for orchestration
    await this.storeThreadMetadata(context.chainId, threadId, {
      sourceNodeId,
      targetNodeId,
      timestamp: Date.now(),
      data: this.serializeData(data)
    });
    
    threadSpan.end();
  }
  
  /**
   * Complete trace span
   */
  async endSpan(context: TraceContext, success: boolean, error?: Error): Promise<void> {
    context.endTime = Date.now();
    context.duration = context.endTime - context.startTime;
    
    // Add final log
    context.logs.push({
      timestamp: Date.now(),
      level: success ? 'info' : 'error',
      message: success ? 'Span completed successfully' : `Span failed: ${error?.message}`,
      fields: {
        success,
        duration: context.duration,
        error: error ? {
          name: error.name,
          message: error.message,
          stack: error.stack
        } : undefined
      }
    });
    
    // End span in tracer
    const span = this.tracer.getSpan(context.spanId);
    if (span) {
      if (error) {
        span.setStatus({ code: 'ERROR', message: error.message });
      }
      span.end();
    }
    
    // Persist trace context
    await this.storeContext(context.chainId, context);
  }
  
  /**
   * Query traces for debugging and analysis
   */
  async queryTraces(filters: {
    chainId?: string;
    projectId?: string;
    agentId?: string;
    taskId?: string;
    startTime?: number;
    endTime?: number;
    errorOnly?: boolean;
  }): Promise<TraceContext[]> {
    // Query trace storage (e.g., Jaeger, Zipkin, or custom DB)
    const traces = await this.traceStore.query(filters);
    return traces;
  }
  
  /**
   * Visualize execution flow
   */
  async visualizeChain(chainId: string): Promise<ExecutionVisualization> {
    const traces = await this.queryTraces({ chainId });
    
    // Build execution graph
    const graph: ExecutionVisualization = {
      chainId,
      nodes: [],
      edges: [],
      timeline: []
    };
    
    // Process traces into visualization
    for (const trace of traces) {
      // Add node for each agent/task
      if (trace.agentId && trace.taskId) {
        graph.nodes.push({
          id: trace.spanId,
          type: 'agent',
          agentId: trace.agentId,
          taskId: trace.taskId,
          startTime: trace.startTime,
          duration: trace.duration,
          success: !trace.logs.some(l => l.level === 'error')
        });
      }
      
      // Add edges for parent-child relationships
      if (trace.parentSpanId) {
        graph.edges.push({
          from: trace.parentSpanId,
          to: trace.spanId,
          type: 'parent-child'
        });
      }
      
      // Add timeline events
      graph.timeline.push({
        timestamp: trace.startTime,
        event: 'span-start',
        spanId: trace.spanId,
        label: trace.metadata.operation || 'unknown'
      });
      
      if (trace.endTime) {
        graph.timeline.push({
          timestamp: trace.endTime,
          event: 'span-end',
          spanId: trace.spanId
        });
      }
    }
    
    // Sort timeline
    graph.timeline.sort((a, b) => a.timestamp - b.timestamp);
    
    return graph;
  }
}
```

**Benefits:**
- ✅ **Full Observability**: Track execution across all agents and nodes
- ✅ **Thread-Level Tracing**: See data flow through workflow edges
- ✅ **Performance Analysis**: Identify bottlenecks and slow operations
- ✅ **Error Attribution**: Pinpoint exact failure location
- ✅ **Visual Debugging**: Execution graph visualization
- ✅ **Production Ready**: OpenTelemetry compatible

---

**Summary of Task Lifecycle:**
- ✅ **8 States**: Comprehensive lifecycle coverage
- ✅ **Validated Transitions**: Only valid state changes allowed
- ✅ **Pre/Post Hooks**: Custom logic at transition points
- ✅ **Complete History**: Full audit trail of state changes
- ✅ **ChainId Tracing**: End-to-end execution tracking
- ✅ **Thread-Level Observability**: Track data flow between nodes

### 3.3 Agent Handoff Protocol (Comprehensive)

The Agent Handoff Protocol defines how work transitions between specialized agents, ensuring context preservation, artifact transfer, and seamless collaboration.

---

#### **Handoff Architecture**

```typescript
interface HandoffRequest {
  handoffId: string;
  fromAgent: {
    agentId: string;
    agentType: AgentType;
  };
  toAgent: {
    agentId?: string;      // Specific agent (optional)
    agentType: AgentType;  // Required agent type
    capabilities?: string[]; // Required capabilities
  };
  task: {
    taskId: string;
    title: string;
    description: string;
    priority: Priority;
    deadline?: Date;
  };
  context: HandoffContext;
  acknowledgmentRequired: boolean;
  timeout: number;  // Acknowledgment timeout (ms)
}

interface HandoffContext {
  // Work completed so far
  workCompleted: {
    summary: string;
    artifacts: Artifact[];
    decisions: Decision[];
    duration: number;
    quality: number;
  };
  
  // Work remaining
  workRemaining: {
    description: string;
    estimatedDuration: number;
    dependencies: string[];
    risks: Risk[];
  };
  
  // Project context
  projectContext: {
    projectId: string;
    requirements: Requirement[];
    architecture: ArchitectureDecisions;
    codebase: CodebaseSnapshot;
  };
  
  // Communication
  instructions: string;
  questions: string[];
  recommendations: Recommendation[];
  
  // Metadata
  chainId: string;
  traceContext: TraceContext;
  metadata: Record<string, any>;
}

interface Artifact {
  id: string;
  type: 'file' | 'document' | 'code' | 'design' | 'data';
  name: string;
  path?: string;
  content?: string;
  url?: string;
  metadata: Record<string, any>;
}
```

---

#### **Standard Handoff Scenarios**

```typescript
class AgentHandoffOrchestrator {
  /**
   * 1. PM → Architect Handoff
   * When: Requirements gathering complete
   * Purpose: Begin system design
   */
  async handoffToArchitect(
    requirements: Requirement[],
    constraints: Constraint[]
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: 'Requirements gathered and validated',
        artifacts: [
          {
            id: 'requirements-doc',
            type: 'document',
            name: 'Project Requirements',
            content: JSON.stringify(requirements),
            metadata: {
              completeness: this.calculateCompleteness(requirements),
              confidence: this.calculateConfidence(requirements)
            }
          }
        ],
        decisions: [
          {
            type: 'scope',
            description: 'Project scope defined',
            reasoning: 'Based on user requirements and constraints'
          }
        ],
        duration: 0,
        quality: 0.95
      },
      workRemaining: {
        description: 'Design system architecture, folder structure, API design, database schema, and technology stack',
        estimatedDuration: 120,  // 2 hours
        dependencies: [],
        risks: [
          {
            description: 'Technology choices may affect scalability',
            probability: 0.3,
            impact: 'medium'
          }
        ]
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Please design the complete system architecture based on the requirements.
        Focus on:
        1. Folder structure and project organization
        2. API design (RESTful or GraphQL)
        3. Database schema
        4. AI model integration architecture (if needed)
        5. Caching and performance strategies
        
        Consider scalability, maintainability, and best practices.
      `,
      questions: [],
      recommendations: [
        {
          type: 'architecture',
          description: 'Consider microservices if project complexity is high',
          reasoning: 'Enables independent scaling and deployment'
        }
      ],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: {}
    };
    
    return this.createHandoffRequest('PM', 'Architect', context);
  }
  
  /**
   * 2. Architect → Coding Handoff
   * When: Architecture design complete
   * Purpose: Begin implementation
   */
  async handoffToCoding(
    architecture: ArchitectureDecisions,
    designDocuments: Document[]
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: 'System architecture designed and validated',
        artifacts: [
          {
            id: 'architecture-doc',
            type: 'document',
            name: 'Architecture Design',
            content: JSON.stringify(architecture),
            metadata: {}
          },
          {
            id: 'folder-structure',
            type: 'design',
            name: 'Folder Structure',
            content: JSON.stringify(architecture.folderStructure),
            metadata: {}
          },
          {
            id: 'api-design',
            type: 'design',
            name: 'API Design',
            content: JSON.stringify(architecture.apiDesign),
            metadata: {}
          }
        ],
        decisions: architecture.decisions,
        duration: 7200000,  // 2 hours
        quality: 0.92
      },
      workRemaining: {
        description: 'Implement backend services, frontend components, and integrate all systems',
        estimatedDuration: 240,  // 4 hours
        dependencies: [],
        risks: [
          {
            description: 'Complex business logic may take longer than estimated',
            probability: 0.4,
            impact: 'high'
          }
        ]
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Implement the system according to the architecture design.
        
        Backend Tasks:
        - Create folder structure
        - Set up Fastify server
        - Implement API routes
        - Create database models and migrations
        - Implement business logic services
        - Add authentication and authorization
        
        Frontend Tasks:
        - Set up React project
        - Create component structure
        - Implement pages and routing
        - Connect to backend APIs
        - Add state management
        - Style with Tailwind CSS
        
        Follow the architecture patterns and best practices defined.
        Use AST-based editing for safe file modifications.
      `,
      questions: [],
      recommendations: [
        {
          type: 'implementation',
          description: 'Start with backend API, then frontend',
          reasoning: 'Ensures API is ready for frontend integration'
        }
      ],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: { architecture }
    };
    
    return this.createHandoffRequest('Architect', 'Coding', context);
  }
  
  /**
   * 3. Coding → Testing Handoff
   * When: Code implementation complete
   * Purpose: Validate functionality
   */
  async handoffToTesting(
    codeArtifacts: Artifact[],
    implementationSummary: string
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: implementationSummary,
        artifacts: codeArtifacts,
        decisions: [],
        duration: 14400000,  // 4 hours
        quality: 0.88
      },
      workRemaining: {
        description: 'Write and execute comprehensive test suite',
        estimatedDuration: 90,  // 1.5 hours
        dependencies: [],
        risks: []
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Create comprehensive test suite:
        1. Unit tests for all functions and methods
        2. Integration tests for API endpoints
        3. Component tests for React components
        4. End-to-end workflow tests
        5. Generate test datasets for edge cases
        
        Execute tests and generate coverage report.
        Aim for 80%+ code coverage.
      `,
      questions: [],
      recommendations: [],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: {}
    };
    
    return this.createHandoffRequest('Coding', 'Testing', context);
  }
  
  /**
   * 4. Testing → Review Handoff
   * When: Tests complete
   * Purpose: Code review and quality audit
   */
  async handoffToReview(
    testResults: TestResults,
    coverageReport: CoverageReport
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: `Tests completed with ${coverageReport.percentage}% coverage`,
        artifacts: [
          {
            id: 'test-results',
            type: 'data',
            name: 'Test Results',
            content: JSON.stringify(testResults),
            metadata: { passed: testResults.passed, failed: testResults.failed }
          },
          {
            id: 'coverage-report',
            type: 'document',
            name: 'Coverage Report',
            content: JSON.stringify(coverageReport),
            metadata: { coverage: coverageReport.percentage }
          }
        ],
        decisions: [],
        duration: 5400000,  // 1.5 hours
        quality: 0.91
      },
      workRemaining: {
        description: 'Review code quality, security, and suggest improvements',
        estimatedDuration: 60,  // 1 hour
        dependencies: [],
        risks: []
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Perform comprehensive code review:
        1. Code quality audit (complexity, duplication, smells)
        2. Security audit (OWASP Top 10, dependency vulnerabilities)
        3. Performance analysis
        4. Suggest refactorings and improvements
        5. Validate code style and conventions
        
        Focus on critical issues that must be fixed before deployment.
      `,
      questions: [],
      recommendations: [],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: { testResults, coverageReport }
    };
    
    return this.createHandoffRequest('Testing', 'Review', context);
  }
  
  /**
   * 5. Review → Builder Handoff
   * When: Review passed (or issues resolved)
   * Purpose: Build deployment artifacts
   */
  async handoffToBuilder(
    reviewReport: ReviewReport,
    codebaseSnapshot: CodebaseSnapshot
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: `Code review complete. Quality score: ${reviewReport.overallScore}/100`,
        artifacts: [
          {
            id: 'review-report',
            type: 'document',
            name: 'Code Review Report',
            content: JSON.stringify(reviewReport),
            metadata: { score: reviewReport.overallScore }
          }
        ],
        decisions: [],
        duration: 3600000,  // 1 hour
        quality: reviewReport.overallScore / 100
      },
      workRemaining: {
        description: 'Build all platform artifacts in parallel',
        estimatedDuration: 45,  // 45 minutes
        dependencies: [],
        risks: [
          {
            description: 'Build failures on specific platforms',
            probability: 0.2,
            impact: 'medium'
          }
        ]
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Build deployment artifacts for all platforms:
        1. Web application (production bundle)
        2. Android APK (signed release)
        3. Windows EXE (Electron or Tauri)
        4. macOS DMG (signed app bundle)
        
        Optimize builds for production:
        - Code splitting and tree shaking
        - Asset compression and minification
        - Source map generation
        - Build validation and smoke tests
        
        Execute builds in parallel for efficiency.
      `,
      questions: [],
      recommendations: [
        {
          type: 'build',
          description: 'Use Tauri for Windows build if bundle size is a concern',
          reasoning: 'Tauri produces ~10MB builds vs ~100MB for Electron'
        }
      ],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: { reviewReport, codebaseSnapshot }
    };
    
    return this.createHandoffRequest('Review', 'Builder', context);
  }
  
  /**
   * 6. Builder → Release Handoff
   * When: All builds complete successfully
   * Purpose: Prepare release and deployment
   */
  async handoffToRelease(
    buildResults: BuildResults,
    artifacts: BuildArtifact[]
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: `All platform builds completed successfully`,
        artifacts: artifacts.map(artifact => ({
          id: artifact.id,
          type: 'file',
          name: artifact.filename,
          path: artifact.path,
          url: artifact.url,
          metadata: {
            platform: artifact.platform,
            size: artifact.size,
            checksum: artifact.checksum
          }
        })),
        decisions: [],
        duration: 2700000,  // 45 minutes
        quality: 0.94
      },
      workRemaining: {
        description: 'Prepare release artifacts and deployment manifests',
        estimatedDuration: 30,  // 30 minutes
        dependencies: [],
        risks: []
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Prepare final release:
        1. Determine version number (semantic versioning)
        2. Generate release notes (AI-generated)
        3. Create deployment manifests (Docker, K8s, Vercel config)
        4. Validate all build artifacts
        5. Create GitHub release (or equivalent)
        6. Generate checksums and signatures
        
        Ensure all artifacts are properly signed and validated.
      `,
      questions: [],
      recommendations: [],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: { buildResults, artifacts }
    };
    
    return this.createHandoffRequest('Builder', 'Release', context);
  }
  
  /**
   * 7. Any → Research Handoff
   * When: External information needed
   * Purpose: Gather knowledge/resources
   */
  async handoffToResearch(
    fromAgent: AgentType,
    researchQuery: ResearchQuery
  ): Promise<HandoffRequest> {
    const context: HandoffContext = {
      workCompleted: {
        summary: 'Identified need for external research',
        artifacts: [],
        decisions: [],
        duration: 0,
        quality: 1.0
      },
      workRemaining: {
        description: researchQuery.description,
        estimatedDuration: 30,  // 30 minutes
        dependencies: [],
        risks: []
      },
      projectContext: await this.getProjectContext(),
      instructions: `
        Research request: ${researchQuery.query}
        
        Tasks:
        ${researchQuery.tasks.map((t, i) => `${i + 1}. ${t}`).join('\n')}
        
        Deliverables:
        - Findings document
        - Recommended solutions
        - Compatibility analysis
        - Security assessment
      `,
      questions: [],
      recommendations: [],
      chainId: generateChainId(),
      traceContext: await this.createTraceContext(),
      metadata: { researchQuery }
    };
    
    return this.createHandoffRequest(fromAgent, 'Research', context);
  }
}
```

---

#### **Handoff Execution Protocol**

```typescript
class HandoffExecutor {
  /**
   * Execute handoff with acknowledgment
   */
  async executeHandoff(request: HandoffRequest): Promise<HandoffResult> {
    // 1. Find suitable target agent
    const targetAgent = await this.findTargetAgent(request.toAgent);
    
    if (!targetAgent) {
      throw new Error(`No available ${request.toAgent.agentType} agent found`);
    }
    
    // 2. Send handoff request
    const handoffMessage: AgentMessage = {
      messageId: generateUUID(),
      timestamp: Date.now(),
      from: request.fromAgent,
      to: { agentId: targetAgent.agentId, agentType: request.toAgent.agentType },
      type: 'agent.handoff',
      priority: request.task.priority,
      payload: {
        handoffId: request.handoffId,
        task: request.task,
        context: request.context
      },
      context: {
        projectId: request.context.projectContext.projectId,
        chainId: request.context.chainId,
        taskId: request.task.taskId
      },
      metadata: {
        requiresAck: request.acknowledgmentRequired,
        ackTimeout: request.timeout
      }
    };
    
    await messageBus.publish(handoffMessage);
    
    // 3. Wait for acknowledgment
    if (request.acknowledgmentRequired) {
      const ack = await this.waitForAcknowledgment(
        request.handoffId,
        request.timeout
      );
      
      if (!ack) {
        throw new Error('Handoff acknowledgment timeout');
      }
    }
    
    // 4. Mark task as handed off
    await taskQueue.updateTaskStatus(
      request.task.taskId,
      TaskStatus.ASSIGNED,
      targetAgent.agentId
    );
    
    // 5. Update trace
    await tracing.recordHandoff(request.context.chainId, {
      from: request.fromAgent.agentId,
      to: targetAgent.agentId,
      taskId: request.task.taskId,
      timestamp: Date.now()
    });
    
    return {
      success: true,
      handoffId: request.handoffId,
      targetAgent: targetAgent.agentId,
      acknowledgedAt: Date.now()
    };
  }
  
  /**
   * Handle handoff reception (target agent side)
   */
  async receiveHandoff(message: AgentMessage): Promise<void> {
    const { handoffId, task, context } = message.payload;
    
    // 1. Validate agent can handle task
    const canHandle = await this.validateCapabilities(task, context);
    
    if (!canHandle) {
      // Reject handoff
      await this.rejectHandoff(handoffId, 'Insufficient capabilities');
      return;
    }
    
    // 2. Load context into agent memory
    await this.loadHandoffContext(context);
    
    // 3. Accept handoff
    await this.acceptHandoff(handoffId);
    
    // 4. Start working on task
    await this.startTask(task, context);
  }
}
```

**Benefits:**
- ✅ **Context Preservation**: Complete work history transferred
- ✅ **Artifact Management**: All files and documents transferred
- ✅ **Acknowledgment Protocol**: Guaranteed handoff receipt
- ✅ **Standard Scenarios**: Well-defined handoff patterns
- ✅ **Traceability**: Full handoff audit trail
- ✅ **Flexible**: Support for any agent-to-agent handoff

---

### 3.4 Long-Running Task Persistence (Comprehensive)

Long-running tasks (spanning hours or days) require robust persistence mechanisms to handle interruptions, crashes, and multi-session workflows.

---

#### **Checkpoint System Architecture**

```typescript
interface Checkpoint {
  checkpointId: string;
  taskId: string;
  agentId: string;
  timestamp: Date;
  sequenceNumber: number;  // Incremental checkpoint number
  
  // State snapshot
  state: {
    status: TaskStatus;
    progress: number;
    currentPhase: string;
    workCompleted: WorkSummary;
    workRemaining: WorkSummary;
  };
  
  // Data snapshot
  data: {
    inputs: Record<string, any>;
    outputs: Record<string, any>;
    intermediateResults: Record<string, any>;
    variables: Record<string, any>;
  };
  
  // Execution context
  context: {
    executionPath: string[];  // Sequence of operations executed
    pendingOperations: Operation[];
    errors: Error[];
    warnings: Warning[];
  };
  
  // Artifacts
  artifacts: {
    files: FileSnapshot[];
    codeChanges: CodeChange[];
    databaseMigrations: Migration[];
  };
  
  // Metadata
  metadata: {
    duration: number;
    resourceUsage: ResourceUsage;
    quality: number;
  };
}

class CheckpointManager {
  private storage: CheckpointStorage;
  private interval: number = 300000;  // 5 minutes
  
  /**
   * Create checkpoint for long-running task
   */
  async createCheckpoint(
    taskId: string,
    agentId: string,
    state: TaskExecutionState
  ): Promise<Checkpoint> {
    const checkpoint: Checkpoint = {
      checkpointId: generateUUID(),
      taskId,
      agentId,
      timestamp: new Date(),
      sequenceNumber: await this.getNextSequenceNumber(taskId),
      state: {
        status: state.status,
        progress: state.progress,
        currentPhase: state.currentPhase,
        workCompleted: this.summarizeWork(state.completedOperations),
        workRemaining: this.estimateRemainingWork(state.pendingOperations)
      },
      data: {
        inputs: state.inputs,
        outputs: state.outputs,
        intermediateResults: state.intermediateResults,
        variables: state.variables
      },
      context: {
        executionPath: state.executionPath,
        pendingOperations: state.pendingOperations,
        errors: state.errors,
        warnings: state.warnings
      },
      artifacts: await this.snapshotArtifacts(taskId),
      metadata: {
        duration: Date.now() - state.startTime,
        resourceUsage: await this.captureResourceUsage(agentId),
        quality: state.qualityScore
      }
    };
    
    // Persist checkpoint
    await this.storage.save(checkpoint);
    
    // Emit checkpoint created event
    await this.emitCheckpointCreated(checkpoint);
    
    return checkpoint;
  }
  
  /**
   * Start automatic checkpointing for task
   */
  startAutomaticCheckpointing(
    taskId: string,
    agentId: string,
    stateProvider: () => Promise<TaskExecutionState>
  ): CheckpointHandle {
    const intervalId = setInterval(async () => {
      try {
        const state = await stateProvider();
        await this.createCheckpoint(taskId, agentId, state);
      } catch (error) {
        console.error('Checkpoint creation failed:', error);
      }
    }, this.interval);
    
    return {
      taskId,
      intervalId,
      stop: () => clearInterval(intervalId)
    };
  }
  
  /**
   * Resume task from latest checkpoint
   */
  async resumeFromCheckpoint(taskId: string): Promise<TaskExecutionState> {
    // Get latest checkpoint
    const checkpoint = await this.storage.getLatest(taskId);
    
    if (!checkpoint) {
      throw new Error(`No checkpoint found for task ${taskId}`);
    }
    
    // Restore file artifacts
    await this.restoreArtifacts(checkpoint.artifacts);
    
    // Reconstruct execution state
    const state: TaskExecutionState = {
      taskId: checkpoint.taskId,
      agentId: checkpoint.agentId,
      status: checkpoint.state.status,
      progress: checkpoint.state.progress,
      currentPhase: checkpoint.state.currentPhase,
      startTime: checkpoint.timestamp.getTime(),
      inputs: checkpoint.data.inputs,
      outputs: checkpoint.data.outputs,
      intermediateResults: checkpoint.data.intermediateResults,
      variables: checkpoint.data.variables,
      executionPath: checkpoint.context.executionPath,
      completedOperations: this.reconstructCompletedOperations(checkpoint),
      pendingOperations: checkpoint.context.pendingOperations,
      errors: checkpoint.context.errors,
      warnings: checkpoint.context.warnings,
      qualityScore: checkpoint.metadata.quality
    };
    
    // Emit resumed event
    await this.emitTaskResumed(taskId, checkpoint.checkpointId);
    
    return state;
  }
  
  /**
   * Resume from specific checkpoint (not just latest)
   */
  async resumeFromSpecificCheckpoint(checkpointId: string): Promise<TaskExecutionState> {
    const checkpoint = await this.storage.getById(checkpointId);
    
    if (!checkpoint) {
      throw new Error(`Checkpoint ${checkpointId} not found`);
    }
    
    return this.resumeFromCheckpoint(checkpoint.taskId);
  }
  
  /**
   * List all checkpoints for task
   */
  async listCheckpoints(taskId: string): Promise<Checkpoint[]> {
    return await this.storage.findAll({ taskId });
  }
  
  /**
   * Clean up old checkpoints (retention policy)
   */
  async cleanupCheckpoints(taskId: string): Promise<void> {
    const checkpoints = await this.listCheckpoints(taskId);
    
    // Keep last 10 checkpoints, delete older ones
    if (checkpoints.length > 10) {
      const toDelete = checkpoints
        .sort((a, b) => b.sequenceNumber - a.sequenceNumber)
        .slice(10);
      
      for (const checkpoint of toDelete) {
        await this.storage.delete(checkpoint.checkpointId);
      }
    }
  }
}
```

---

#### **Multi-Session Workflow Support**

```typescript
class MultiSessionWorkflowManager {
  /**
   * Pause workflow for later resumption
   */
  async pauseWorkflow(
    workflowId: string,
    reason: string
  ): Promise<PauseHandle> {
    // 1. Create checkpoint for all active tasks
    const activeTasks = await taskQueue.getActiveTasks(workflowId);
    
    const checkpoints = await Promise.all(
      activeTasks.map(task => 
        checkpointManager.createCheckpoint(task.id, task.assignedAgent, task.state)
      )
    );
    
    // 2. Save workflow state
    const workflowState = await this.captureWorkflowState(workflowId);
    
    await workflowStorage.save({
      workflowId,
      status: 'paused',
      pausedAt: new Date(),
      reason,
      checkpoints: checkpoints.map(c => c.checkpointId),
      state: workflowState
    });
    
    // 3. Stop all agents
    for (const task of activeTasks) {
      await agentRegistry.stopAgent(task.assignedAgent);
    }
    
    return {
      workflowId,
      checkpoints: checkpoints.map(c => c.checkpointId),
      pausedAt: new Date()
    };
  }
  
  /**
   * Resume paused workflow
   */
  async resumeWorkflow(workflowId: string): Promise<void> {
    // 1. Load workflow state
    const workflow = await workflowStorage.findOne({ workflowId });
    
    if (!workflow || workflow.status !== 'paused') {
      throw new Error(`Workflow ${workflowId} cannot be resumed`);
    }
    
    // 2. Restore all checkpoints
    for (const checkpointId of workflow.checkpoints) {
      const state = await checkpointManager.resumeFromSpecificCheckpoint(checkpointId);
      
      // Restart task with restored state
      await this.restartTask(state);
    }
    
    // 3. Update workflow status
    await workflowStorage.update(
      { workflowId },
      { status: 'running', resumedAt: new Date() }
    );
  }
  
  /**
   * Handle agent crash and recovery
   */
  async handleAgentCrash(agentId: string): Promise<void> {
    // 1. Find all tasks assigned to crashed agent
    const tasks = await taskQueue.getTasksByAgent(agentId);
    
    // 2. For each task, resume from last checkpoint
    for (const task of tasks) {
      try {
        const state = await checkpointManager.resumeFromCheckpoint(task.id);
        
        // 3. Reassign to different agent
        const newAgent = await agentRegistry.findAgent({
          agentType: task.agentType,
          capabilities: task.requiredCapabilities,
          exclude: [agentId]  // Exclude crashed agent
        });
        
        if (newAgent) {
          await taskQueue.reassignTask(task.id, newAgent.agentId);
          await this.restartTask(state);
        } else {
          // No available agent, mark as blocked
          await taskQueue.updateTaskStatus(task.id, TaskStatus.BLOCKED, agentId);
        }
      } catch (error) {
        console.error(`Failed to recover task ${task.id}:`, error);
        await taskQueue.failTask(task.id, error, agentId);
      }
    }
    
    // 4. Mark agent as crashed and remove from registry
    await agentRegistry.markAsCrashed(agentId);
  }
}
```

---

#### **State Storage Strategy**

```typescript
class StateStorageManager {
  /**
   * Multi-tier storage strategy
   */
  private storageStrategy = {
    // Tier 1: In-memory cache (Redis)
    cache: {
      storage: RedisCache,
      use: 'hot data',
      ttl: 3600,  // 1 hour
      maxSize: '1GB'
    },
    
    // Tier 2: Database (PostgreSQL)
    database: {
      storage: PostgreSQL,
      use: 'persistent state',
      tables: ['tasks', 'checkpoints', 'workflows', 'agents']
    },
    
    // Tier 3: File system (S3/Local)
    fileSystem: {
      storage: S3Storage,
      use: 'large artifacts',
      path: '/olai/artifacts/',
      compression: true
    },
    
    // Tier 4: Version control (Git)
    versionControl: {
      storage: GitRepository,
      use: 'code changes',
      repo: '/olai/projects/'
    }
  };
  
  /**
   * Store state with appropriate storage tier
   */
  async storeState(key: string, value: any, options?: StorageOptions): Promise<void> {
    const size = this.calculateSize(value);
    
    // Small, hot data → Cache
    if (size < 1024 * 100 && options?.hot) {  // < 100KB
      await this.cache.set(key, value, { ttl: options.ttl || 3600 });
    }
    
    // Structured data → Database
    if (options?.persistent) {
      await this.database.save(options.table, key, value);
    }
    
    // Large files → File system
    if (size > 1024 * 1024) {  // > 1MB
      const path = await this.fileSystem.save(key, value, {
        compress: true,
        encrypt: options?.encrypt
      });
      
      // Store reference in database
      await this.database.save('file_references', key, { path, size });
    }
    
    // Code files → Version control
    if (options?.versionControl) {
      await this.versionControl.commit(key, value, {
        message: options.commitMessage,
        author: options.author
      });
    }
  }
  
  /**
   * Retrieve state from appropriate tier
   */
  async retrieveState(key: string): Promise<any> {
    // Try cache first
    const cached = await this.cache.get(key);
    if (cached) return cached;
    
    // Try database
    const dbValue = await this.database.findOne({ key });
    if (dbValue) {
      // Update cache
      await this.cache.set(key, dbValue, { ttl: 3600 });
      return dbValue;
    }
    
    // Try file system
    const fileRef = await this.database.findOne('file_references', { key });
    if (fileRef) {
      const value = await this.fileSystem.load(fileRef.path);
      return value;
    }
    
    // Try version control
    const vcValue = await this.versionControl.read(key);
    if (vcValue) return vcValue;
    
    return null;
  }
}
```

**Benefits:**
- ✅ **Crash Recovery**: Resume from last checkpoint after crashes
- ✅ **Multi-Session**: Pause and resume workflows across sessions
- ✅ **Automatic Checkpointing**: Periodic state snapshots
- ✅ **Efficient Storage**: Multi-tier storage strategy
- ✅ **Version Control**: Code changes tracked in Git
- ✅ **Granular Recovery**: Resume from specific checkpoint

---

### 3.5 Escalation Mechanism (Comprehensive)

The Escalation Mechanism ensures that blocked or critical situations are promptly brought to human attention for resolution.

---

#### **Escalation Triggers**

```typescript
enum EscalationTrigger {
  AGENT_STUCK = 'agent_stuck',                  // Agent unable to proceed
  RETRY_EXHAUSTED = 'retry_exhausted',          // All retries failed
  AMBIGUOUS_REQUIREMENTS = 'ambiguous_requirements',  // Unclear specifications
  RESOURCE_CONSTRAINTS = 'resource_constraints',      // Insufficient resources
  SECURITY_CONCERNS = 'security_concerns',      // Security issue detected
  CONFLICTING_DECISIONS = 'conflicting_decisions',    // Agent decisions conflict
  DEADLINE_RISK = 'deadline_risk',              // Likely to miss deadline
  QUALITY_THRESHOLD = 'quality_threshold',      // Quality below acceptable
  EXTERNAL_DEPENDENCY = 'external_dependency',  // Blocked by external service
  USER_INPUT_REQUIRED = 'user_input_required'   // Needs user decision
}

interface EscalationEvent {
  escalationId: string;
  trigger: EscalationTrigger;
  severity: 'low' | 'medium' | 'high' | 'critical';
  taskId: string;
  agentId: string;
  timestamp: Date;
  
  // Context
  issue: {
    summary: string;
    description: string;
    impact: string;
    possibleCauses: string[];
  };
  
  // Current state
  state: {
    taskStatus: TaskStatus;
    progress: number;
    attemptsCount: number;
    timeElapsed: number;
    timeRemaining?: number;
  };
  
  // Options and recommendations
  options: EscalationOption[];
  recommendation: string;
  
  // Artifacts
  artifacts: {
    logs: Log[];
    errorTraces: ErrorTrace[];
    screenshots?: string[];
    relevantCode?: CodeSnippet[];
  };
  
  // Resolution tracking
  resolution?: {
    resolvedBy: string;
    resolvedAt: Date;
    solution: string;
    actionTaken: string;
  };
}

interface EscalationOption {
  id: string;
  title: string;
  description: string;
  pros: string[];
  cons: string[];
  estimatedTime: number;
  risk: 'low' | 'medium' | 'high';
}
```

---

#### **Escalation Detection & Creation**

```typescript
class EscalationManager {
  /**
   * Detect when escalation is needed
   */
  async detectEscalationNeeded(
    taskId: string,
    agentId: string
  ): Promise<EscalationTrigger | null> {
    const task = await taskQueue.getTask(taskId);
    const agent = await agentRegistry.getAgent(agentId);
    
    // Check 1: Agent stuck (no progress for extended period)
    if (this.isAgentStuck(task, agent)) {
      return EscalationTrigger.AGENT_STUCK;
    }
    
    // Check 2: Retry exhausted
    if (task.retryCount >= task.maxRetries) {
      return EscalationTrigger.RETRY_EXHAUSTED;
    }
    
    // Check 3: Deadline risk
    if (task.deadline) {
      const timeRemaining = task.deadline.getTime() - Date.now();
      const estimatedCompletion = this.estimateCompletionTime(task);
      
      if (estimatedCompletion > timeRemaining) {
        return EscalationTrigger.DEADLINE_RISK;
      }
    }
    
    // Check 4: Quality threshold
    if (task.qualityScore < task.minQualityThreshold) {
      return EscalationTrigger.QUALITY_THRESHOLD;
    }
    
    // Check 5: Resource constraints
    const resources = await this.checkResourceAvailability(task);
    if (!resources.sufficient) {
      return EscalationTrigger.RESOURCE_CONSTRAINTS;
    }
    
    return null;
  }
  
  /**
   * Create escalation event
   */
  async createEscalation(
    taskId: string,
    agentId: string,
    trigger: EscalationTrigger
  ): Promise<EscalationEvent> {
    const task = await taskQueue.getTask(taskId);
    const agent = await agentRegistry.getAgent(agentId);
    
    // Generate escalation context
    const context = await this.generateEscalationContext(task, agent, trigger);
    
    // Determine severity
    const severity = this.calculateSeverity(trigger, task);
    
    // Generate options and recommendation
    const options = await this.generateOptions(task, agent, trigger);
    const recommendation = await this.generateRecommendation(options, context);
    
    // Create escalation event
    const escalation: EscalationEvent = {
      escalationId: generateUUID(),
      trigger,
      severity,
      taskId,
      agentId,
      timestamp: new Date(),
      issue: context.issue,
      state: context.state,
      options,
      recommendation,
      artifacts: await this.gatherArtifacts(taskId, agentId)
    };
    
    // Store escalation
    await this.storage.save(escalation);
    
    // Notify user
    await this.notifyUser(escalation);
    
    // Update task status
    await taskQueue.transition(taskId, TaskStatus.ESCALATED, 'system', trigger);
    
    return escalation;
  }
  
  /**
   * Generate escalation options
   */
  private async generateOptions(
    task: Task,
    agent: Agent,
    trigger: EscalationTrigger
  ): Promise<EscalationOption[]> {
    const options: EscalationOption[] = [];
    
    switch (trigger) {
      case EscalationTrigger.AGENT_STUCK:
        options.push({
          id: 'retry-different-approach',
          title: 'Retry with different approach',
          description: 'Reset and try alternative implementation strategy',
          pros: ['May succeed with new approach', 'Learn from failure'],
          cons: ['Time consuming', 'May fail again'],
          estimatedTime: 60,
          risk: 'medium'
        });
        
        options.push({
          id: 'reassign-agent',
          title: 'Reassign to different agent',
          description: 'Assign task to another agent with same capabilities',
          pros: ['Fresh perspective', 'Different strengths'],
          cons: ['Context transfer needed', 'Original agent wasted time'],
          estimatedTime: 30,
          risk: 'low'
        });
        
        options.push({
          id: 'simplify-requirements',
          title: 'Simplify requirements',
          description: 'Reduce scope or complexity of task',
          pros: ['More achievable', 'Faster completion'],
          cons: ['Reduced functionality', 'May not meet needs'],
          estimatedTime: 45,
          risk: 'low'
        });
        break;
        
      case EscalationTrigger.DEADLINE_RISK:
        options.push({
          id: 'extend-deadline',
          title: 'Extend deadline',
          description: 'Request more time to complete properly',
          pros: ['Maintain quality', 'Reduce pressure'],
          cons: ['Delays delivery', 'May not be acceptable'],
          estimatedTime: 0,
          risk: 'low'
        });
        
        options.push({
          id: 'reduce-scope',
          title: 'Reduce scope',
          description: 'Remove non-critical features to meet deadline',
          pros: ['Meet deadline', 'Deliver core functionality'],
          cons: ['Incomplete features', 'Technical debt'],
          estimatedTime: 15,
          risk: 'medium'
        });
        
        options.push({
          id: 'add-resources',
          title: 'Add more agents',
          description: 'Parallelize work with additional agents',
          pros: ['Faster completion', 'Maintain scope'],
          cons: ['Coordination overhead', 'May not scale linearly'],
          estimatedTime: 20,
          risk: 'medium'
        });
        break;
        
      case EscalationTrigger.AMBIGUOUS_REQUIREMENTS:
        options.push({
          id: 'clarify-requirements',
          title: 'Request clarification',
          description: 'Ask user specific questions to clarify ambiguity',
          pros: ['Clear understanding', 'Correct implementation'],
          cons: ['Requires user time', 'Delays progress'],
          estimatedTime: 30,
          risk: 'low'
        });
        
        options.push({
          id: 'make-assumptions',
          title: 'Make reasonable assumptions',
          description: 'Proceed with best-guess interpretation',
          pros: ['No delay', 'Can iterate later'],
          cons: ['May be wrong', 'Rework needed'],
          estimatedTime: 0,
          risk: 'high'
        });
        break;
    }
    
    return options;
  }
  
  /**
   * Resolve escalation with user input
   */
  async resolveEscalation(
    escalationId: string,
    selectedOption: string,
    userInput: string
  ): Promise<void> {
    const escalation = await this.storage.get(escalationId);
    
    // Record resolution
    escalation.resolution = {
      resolvedBy: 'user',
      resolvedAt: new Date(),
      solution: selectedOption,
      actionTaken: userInput
    };
    
    await this.storage.update(escalationId, escalation);
    
    // Execute resolution action
    await this.executeResolution(escalation, selectedOption, userInput);
    
    // Resume task
    await taskQueue.transition(
      escalation.taskId,
      TaskStatus.ASSIGNED,
      'user',
      `Escalation resolved: ${selectedOption}`
    );
  }
}
```

---

#### **User Notification System**

```typescript
class EscalationNotifier {
  /**
   * Notify user of escalation via multiple channels
   */
  async notifyUser(escalation: EscalationEvent): Promise<void> {
    // Channel 1: In-app notification (immediate)
    await this.sendInAppNotification(escalation);
    
    // Channel 2: WebSocket push (real-time)
    await this.sendWebSocketNotification(escalation);
    
    // Channel 3: Email (for high/critical severity)
    if (['high', 'critical'].includes(escalation.severity)) {
      await this.sendEmailNotification(escalation);
    }
    
    // Channel 4: SMS (for critical severity only)
    if (escalation.severity === 'critical') {
      await this.sendSMSNotification(escalation);
    }
  }
  
  /**
   * Send in-app notification
   */
  private async sendInAppNotification(escalation: EscalationEvent): Promise<void> {
    const notification = {
      type: 'escalation',
      severity: escalation.severity,
      title: this.getNotificationTitle(escalation.trigger),
      message: escalation.issue.summary,
      actionUrl: `/escalations/${escalation.escalationId}`,
      timestamp: escalation.timestamp
    };
    
    await notificationService.send(escalation.taskId, notification);
  }
  
  /**
   * Send email notification
   */
  private async sendEmailNotification(escalation: EscalationEvent): Promise<void> {
    const user = await this.getUserForProject(escalation.taskId);
    
    const emailContent = `
      <h2>🚨 OLAI Escalation: ${this.getNotificationTitle(escalation.trigger)}</h2>
      
      <p><strong>Severity:</strong> ${escalation.severity.toUpperCase()}</p>
      <p><strong>Task:</strong> ${escalation.taskId}</p>
      <p><strong>Time:</strong> ${escalation.timestamp.toLocaleString()}</p>
      
      <h3>Issue Summary</h3>
      <p>${escalation.issue.description}</p>
      
      <h3>Impact</h3>
      <p>${escalation.issue.impact}</p>
      
      <h3>Recommended Action</h3>
      <p>${escalation.recommendation}</p>
      
      <p>
        <a href="${process.env.APP_URL}/escalations/${escalation.escalationId}">
          View Full Details and Resolve
        </a>
      </p>
    `;
    
    await emailService.send({
      to: user.email,
      subject: `[OLAI] ${escalation.severity.toUpperCase()}: ${this.getNotificationTitle(escalation.trigger)}`,
      html: emailContent
    });
  }
}
```

**Benefits:**
- ✅ **Automatic Detection**: Identifies issues requiring human intervention
- ✅ **Contextual Information**: Complete context for informed decisions
- ✅ **Multiple Options**: Presents alternatives with pros/cons
- ✅ **Multi-Channel Notifications**: In-app, WebSocket, email, SMS
- ✅ **Resolution Tracking**: Records decisions and outcomes
- ✅ **Task Resumption**: Automatically resumes after resolution

---

### 3.6 Progress Reporting (Comprehensive)

Progress Reporting keeps users informed about project status through real-time updates, summaries, and alerts.

---

#### **Report Types**

```typescript
enum ReportType {
  REALTIME_STATUS = 'realtime_status',      // Live updates as they happen
  PROGRESS_SUMMARY = 'progress_summary',    // Periodic comprehensive summaries
  MILESTONE = 'milestone',                  // Milestone achievements
  ERROR_ALERT = 'error_alert',              // Error notifications
  WARNING_ALERT = 'warning_alert',          // Warning notifications
  DEADLINE_REMINDER = 'deadline_reminder',  // Deadline approaching
  COMPLETION = 'completion'                 // Project/task completion
}

interface ProgressReport {
  reportId: string;
  type: ReportType;
  projectId: string;
  timestamp: Date;
  
  // Overall progress
  progress: {
    overall: number;          // 0-100
    byPhase: PhaseProgress[];
    byAgent: AgentProgress[];
    timeline: TimelineEvent[];
  };
  
  // Current activities
  activeWork: {
    inProgress: TaskSummary[];
    recentCompleted: TaskSummary[];
    blocked: TaskSummary[];
    upcoming: TaskSummary[];
  };
  
  // Metrics
  metrics: {
    tasksCompleted: number;
    tasksRemaining: number;
    totalDuration: number;
    estimatedCompletion: Date;
    quality: number;
    efficiency: number;
  };
  
  // Issues and risks
  issues: {
    errors: ErrorSummary[];
    warnings: WarningSummary[];
    blockers: Blocker[];
    risks: Risk[];
  };
  
  // Next steps
  nextSteps: string[];
  
  // Visualization data
  visualization: {
    ganttChart: GanttData;
    burndownChart: BurndownData;
    agentActivity: AgentActivityData;
  };
}

interface PhaseProgress {
  phase: string;
  status: 'not_started' | 'in_progress' | 'completed';
  progress: number;
  startTime?: Date;
  endTime?: Date;
  duration?: number;
}

interface AgentProgress {
  agentId: string;
  agentType: AgentType;
  tasksAssigned: number;
  tasksCompleted: number;
  currentTask?: string;
  efficiency: number;
  quality: number;
}
```

---

#### **Real-Time Progress Updates (WebSocket)**

```typescript
class RealtimeProgressReporter {
  private wsServer: WebSocketServer;
  
  /**
   * Send real-time status update
   */
  async sendRealtimeUpdate(projectId: string, update: StatusUpdate): Promise<void> {
    const message = {
      type: 'progress.update',
      projectId,
      timestamp: Date.now(),
      data: update
    };
    
    // Broadcast to all connected clients for this project
    await this.wsServer.broadcast(`project:${projectId}`, message);
  }
  
  /**
   * Stream agent activity
   */
  async streamAgentActivity(
    projectId: string,
    agentId: string,
    activity: AgentActivity
  ): Promise<void> {
    await this.sendRealtimeUpdate(projectId, {
      type: 'agent.activity',
      agentId,
      activity: {
        action: activity.action,
        taskId: activity.taskId,
        progress: activity.progress,
        message: activity.message,
        timestamp: Date.now()
      }
    });
  }
  
  /**
   * Stream task status changes
   */
  async streamTaskStatus(
    projectId: string,
    taskId: string,
    oldStatus: TaskStatus,
    newStatus: TaskStatus
  ): Promise<void> {
    await this.sendRealtimeUpdate(projectId, {
      type: 'task.status',
      taskId,
      oldStatus,
      newStatus,
      timestamp: Date.now()
    });
  }
  
  /**
   * Stream progress percentage updates
   */
  async streamProgressUpdate(
    projectId: string,
    progress: number
  ): Promise<void> {
    await this.sendRealtimeUpdate(projectId, {
      type: 'progress.percentage',
      progress,
      timestamp: Date.now()
    });
  }
}
```

---

#### **Periodic Progress Summaries**

```typescript
class ProgressSummaryGenerator {
  /**
   * Generate comprehensive progress summary
   */
  async generateSummary(projectId: string): Promise<ProgressReport> {
    // Gather all project data
    const project = await sharedMemory.getProjectContext(projectId);
    const tasks = await taskQueue.getTaskState(projectId);
    const agents = await agentRegistry.getActiveAgents(projectId);
    
    // Calculate overall progress
    const overallProgress = this.calculateOverallProgress(tasks);
    
    // Calculate phase progress
    const phaseProgress = this.calculatePhaseProgress(tasks);
    
    // Calculate agent progress
    const agentProgress = agents.map(agent => this.calculateAgentProgress(agent, tasks));
    
    // Identify issues
    const issues = await this.identifyIssues(tasks);
    
    // Generate next steps
    const nextSteps = await this.generateNextSteps(tasks, project);
    
    // Generate visualization data
    const visualization = {
      ganttChart: this.generateGanttData(tasks),
      burndownChart: this.generateBurndownData(tasks),
      agentActivity: this.generateAgentActivityData(agents, tasks)
    };
    
    const report: ProgressReport = {
      reportId: generateUUID(),
      type: ReportType.PROGRESS_SUMMARY,
      projectId,
      timestamp: new Date(),
      progress: {
        overall: overallProgress,
        byPhase: phaseProgress,
        byAgent: agentProgress,
        timeline: await this.generateTimeline(tasks)
      },
      activeWork: {
        inProgress: tasks.active.map(t => this.summarizeTask(t)),
        recentCompleted: tasks.completed.slice(-5).map(t => this.summarizeTask(t)),
        blocked: tasks.blocked.map(t => this.summarizeTask(t)),
        upcoming: this.getUpcomingTasks(tasks, 5)
      },
      metrics: {
        tasksCompleted: tasks.completed.length,
        tasksRemaining: tasks.all.length - tasks.completed.length,
        totalDuration: this.calculateTotalDuration(tasks),
        estimatedCompletion: this.estimateCompletion(tasks),
        quality: this.calculateAverageQuality(tasks.completed),
        efficiency: this.calculateEfficiency(tasks)
      },
      issues,
      nextSteps,
      visualization
    };
    
    return report;
  }
  
  /**
   * Generate user-friendly progress message
   */
  async generateProgressMessage(report: ProgressReport): Promise<string> {
    const { progress, metrics, activeWork } = report;
    
    return `
📊 **Project Progress Update**

**Overall Progress:** ${Math.round(progress.overall)}% complete

**Current Status:**
- ✅ ${metrics.tasksCompleted} tasks completed
- 🔄 ${activeWork.inProgress.length} tasks in progress
- ⏳ ${metrics.tasksRemaining} tasks remaining

**Active Work:**
${activeWork.inProgress.map(t => `- ${t.title} (${Math.round(t.progress)}%)`).join('\n')}

**Recent Completions:**
${activeWork.recentCompleted.map(t => `- ✓ ${t.title}`).join('\n')}

**Estimated Completion:** ${metrics.estimatedCompletion.toLocaleString()}

${report.issues.blockers.length > 0 ? `
⚠️ **Blockers:**
${report.issues.blockers.map(b => `- ${b.description}`).join('\n')}
` : ''}

**Next Steps:**
${report.nextSteps.map((step, i) => `${i + 1}. ${step}`).join('\n')}
    `.trim();
  }
}
```

---

#### **Report Channels**

```typescript
class ProgressReportDistributor {
  /**
   * Distribute report via all appropriate channels
   */
  async distribute(report: ProgressReport): Promise<void> {
    // Channel 1: WebSocket (real-time)
    await this.sendViaWebSocket(report);
    
    // Channel 2: REST API (queryable)
    await this.saveForAPIAccess(report);
    
    // Channel 3: Dashboard update
    await this.updateDashboard(report);
    
    // Channel 4: Email (for summaries only)
    if (report.type === ReportType.PROGRESS_SUMMARY) {
      await this.sendViaEmail(report);
    }
    
    // Channel 5: SMS (for critical alerts only)
    if (report.type === ReportType.ERROR_ALERT && report.issues.errors.some(e => e.severity === 'critical')) {
      await this.sendViaSMS(report);
    }
  }
  
  /**
   * Store report for REST API access
   */
  private async saveForAPIAccess(report: ProgressReport): Promise<void> {
    await reportsStorage.save(report);
    
    // Make available at GET /api/projects/:projectId/reports/:reportId
    // and GET /api/projects/:projectId/reports/latest
  }
  
  /**
   * Update real-time dashboard
   */
  private async updateDashboard(report: ProgressReport): Promise<void> {
    await dashboardService.update(report.projectId, {
      progress: report.progress,
      metrics: report.metrics,
      activeWork: report.activeWork,
      visualization: report.visualization,
      lastUpdated: report.timestamp
    });
  }
}
```

**Benefits:**
- ✅ **Real-Time Updates**: Instant status via WebSocket
- ✅ **Comprehensive Summaries**: Detailed periodic reports
- ✅ **Visual Progress**: Gantt charts, burndown charts, agent activity
- ✅ **Multi-Channel**: WebSocket, API, email, SMS, dashboard
- ✅ **Actionable Information**: Next steps and recommendations
- ✅ **Issue Tracking**: Errors, warnings, blockers, risks

---

**Summary of Section 3 (Multi-Agent Coordination):**
- ✅ **Core Components**: Shared memory, task queue, message bus, agent registry
- ✅ **Task Lifecycle**: 8-state machine with full tracing
- ✅ **Agent Handoff**: 7 standard scenarios with context transfer
- ✅ **Persistence**: Checkpointing and multi-session support
- ✅ **Escalation**: Automatic detection and resolution workflow
- ✅ **Progress Reporting**: Real-time updates and comprehensive summaries

---

## 4. Implementation Plan for Chat-first PM

The Chat-first PM implementation transforms natural language conversations into fully functional applications through intelligent requirement gathering, project management, and agent coordination.

---

### 4.0 Chat-First Interface Architecture (Comprehensive)

The chat interface is the primary entry point for all users, providing a conversational, intuitive way to build complete applications without technical expertise.

---

#### **Interface Architecture**

```typescript
interface ChatInterface {
  // Core components
  components: {
    chatInput: ChatInputComponent;
    conversationHistory: ConversationHistoryComponent;
    agentActivityFeed: AgentActivityFeedComponent;
    progressTimeline: ProgressTimelineComponent;
    deadlineCountdown: DeadlineCountdownComponent;
    buildStatusIndicator: BuildStatusIndicatorComponent;
    visualCanvas: WorkflowCanvasComponent;  // Optional, shown on demand
  };
  
  // State management
  state: {
    conversationId: string;
    projectId: string;
    messages: Message[];
    agentActivities: AgentActivity[];
    progress: ProjectProgress;
    deadline?: Date;
    buildStatus: BuildStatus;
  };
  
  // Event handlers
  handlers: {
    onUserMessage: (message: string) => Promise<void>;
    onAgentMessage: (message: AgentMessage) => void;
    onProgressUpdate: (progress: ProjectProgress) => void;
    onBuildStatusChange: (status: BuildStatus) => void;
    onShowVisualEditor: () => void;
  };
}

interface Message {
  id: string;
  type: 'user' | 'agent' | 'system';
  sender: string;
  content: string;
  timestamp: Date;
  metadata?: {
    requiresResponse?: boolean;
    options?: string[];  // For multiple-choice questions
    attachments?: Attachment[];
    codeSnippets?: CodeSnippet[];
    visualizations?: Visualization[];
  };
}

class ChatInterfaceManager {
  /**
   * Initialize chat session
   */
  async initializeSession(userId: string): Promise<ChatSession> {
    const conversationId = generateUUID();
    
    // Create session
    const session: ChatSession = {
      conversationId,
      userId,
      startedAt: new Date(),
      state: 'active',
      messages: [],
      context: {
        projectType: null,
        requirements: [],
        decisions: [],
        currentPhase: 'discovery'
      }
    };
    
    // Send welcome message
    await this.sendWelcomeMessage(session);
    
    return session;
  }
  
  /**
   * Send welcome message with context-aware prompts
   */
  private async sendWelcomeMessage(session: ChatSession): Promise<void> {
    const welcomeMessage = {
      type: 'agent',
      sender: 'PM Agent',
      content: `
👋 Hi! I'm your AI Project Manager. I'll help you build your application from start to finish.

**What I can do:**
- 🎯 Understand your requirements through conversation
- 🏗️ Design and architect your application
- 💻 Write all the code (backend, frontend, mobile)
- ✅ Test everything thoroughly
- 📦 Build for multiple platforms (Web, Android, Windows, macOS)
- 🚀 Deploy your application

**Just describe your idea**, and I'll handle the rest!

Some examples to get started:
• "Build a portfolio website to showcase my design work"
• "Create a patient monitoring system that predicts health risks"
• "Make an e-commerce site for my handmade jewelry business"

What would you like to build today?
      `.trim(),
      timestamp: new Date(),
      metadata: {
        requiresResponse: true,
        suggestedPrompts: [
          'Build a portfolio website',
          'Create a business dashboard',
          'Make a mobile app'
        ]
      }
    };
    
    await this.addMessage(session, welcomeMessage);
  }
  
  /**
   * Handle user message
   */
  async handleUserMessage(
    session: ChatSession,
    message: string
  ): Promise<void> {
    // 1. Add user message to history
    await this.addMessage(session, {
      type: 'user',
      sender: 'User',
      content: message,
      timestamp: new Date()
    });
    
    // 2. Show typing indicator
    await this.showTypingIndicator(session);
    
    // 3. Process message with PM Agent
    const response = await this.processWithPMAgent(session, message);
    
    // 4. Hide typing indicator
    await this.hideTypingIndicator(session);
    
    // 5. Send agent response
    await this.addMessage(session, response);
    
    // 6. Update session context
    await this.updateSessionContext(session, response);
  }
  
  /**
   * Process message with PM Agent (NLP + LLM)
   */
  private async processWithPMAgent(
    session: ChatSession,
    message: string
  ): Promise<Message> {
    // Extract intent and entities
    const analysis = await this.analyzeMessage(message, session.context);
    
    // Determine response based on current phase
    switch (session.context.currentPhase) {
      case 'discovery':
        return await this.handleDiscoveryPhase(session, analysis);
        
      case 'requirements':
        return await this.handleRequirementsPhase(session, analysis);
        
      case 'confirmation':
        return await this.handleConfirmationPhase(session, analysis);
        
      case 'execution':
        return await this.handleExecutionPhase(session, analysis);
        
      case 'completed':
        return await this.handleCompletedPhase(session, analysis);
        
      default:
        return await this.handleDefaultPhase(session, analysis);
    }
  }
  
  /**
   * Handle discovery phase (initial project understanding)
   */
  private async handleDiscoveryPhase(
    session: ChatSession,
    analysis: MessageAnalysis
  ): Promise<Message> {
    // Extract project type
    const projectType = this.detectProjectType(analysis);
    
    // Extract core requirements
    const requirements = this.extractRequirements(analysis);
    
    // Detect deadline if mentioned
    const deadline = this.extractDeadline(analysis);
    
    // Store in context
    session.context.projectType = projectType;
    session.context.requirements.push(...requirements);
    if (deadline) session.context.deadline = deadline;
    
    // Generate response
    const response = await this.generateDiscoveryResponse(
      session,
      projectType,
      requirements,
      deadline
    );
    
    // Move to requirements phase if enough information
    if (this.hasEnoughInitialInfo(session.context)) {
      session.context.currentPhase = 'requirements';
    }
    
    return response;
  }
}
```

---

#### **Visual Components**

```tsx
// React component for chat interface
const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const [progress, setProgress] = useState<ProjectProgress | null>(null);
  const [deadline, setDeadline] = useState<Date | null>(null);
  
  // Real-time updates via WebSocket
  useEffect(() => {
    const ws = new WebSocket(`wss://api.olai.dev/ws/${sessionId}`);
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      
      switch (data.type) {
        case 'agent.message':
          setMessages(prev => [...prev, data.message]);
          break;
          
        case 'agent.typing':
          setIsTyping(true);
          break;
          
        case 'agent.typing_stopped':
          setIsTyping(false);
          break;
          
        case 'progress.update':
          setProgress(data.progress);
          break;
          
        case 'deadline.set':
          setDeadline(new Date(data.deadline));
          break;
      }
    };
    
    return () => ws.close();
  }, [sessionId]);
  
  const handleSend = async () => {
    if (!input.trim()) return;
    
    // Add user message
    const userMessage: Message = {
      id: generateId(),
      type: 'user',
      sender: 'You',
      content: input,
      timestamp: new Date()
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsTyping(true);
    
    // Send to backend
    await fetch('/api/chat/message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sessionId,
        message: input
      })
    });
  };
  
  return (
    <div className="chat-interface">
      {/* Header with progress */}
      <ChatHeader progress={progress} deadline={deadline} />
      
      {/* Messages */}
      <div className="messages-container">
        {messages.map(msg => (
          <MessageBubble key={msg.id} message={msg} />
        ))}
        
        {isTyping && <TypingIndicator />}
        
        <div ref={messagesEndRef} />
      </div>
      
      {/* Agent activity feed (sidebar) */}
      <AgentActivityFeed sessionId={sessionId} />
      
      {/* Input area */}
      <div className="input-container">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault();
              handleSend();
            }
          }}
          placeholder="Describe what you want to build..."
          rows={3}
        />
        
        <button onClick={handleSend} disabled={!input.trim()}>
          Send
        </button>
      </div>
      
      {/* Quick actions */}
      <QuickActions
        onShowVisual={() => setShowVisualEditor(true)}
        onExportCode={() => handleExportCode()}
        onViewLogs={() => setShowLogs(true)}
      />
    </div>
  );
};

// Message bubble component
const MessageBubble: React.FC<{ message: Message }> = ({ message }) => {
  const isUser = message.type === 'user';
  
  return (
    <div className={`message ${isUser ? 'user' : 'agent'}`}>
      <div className="message-header">
        <span className="sender">{message.sender}</span>
        <span className="timestamp">
          {formatTime(message.timestamp)}
        </span>
      </div>
      
      <div className="message-content">
        <ReactMarkdown>{message.content}</ReactMarkdown>
        
        {/* Code snippets */}
        {message.metadata?.codeSnippets?.map((snippet, i) => (
          <CodeSnippet key={i} code={snippet} />
        ))}
        
        {/* Multiple choice options */}
        {message.metadata?.options && (
          <OptionsSelector options={message.metadata.options} />
        )}
        
        {/* Visualizations */}
        {message.metadata?.visualizations?.map((viz, i) => (
          <Visualization key={i} data={viz} />
        ))}
      </div>
    </div>
  );
};

// Agent activity feed component
const AgentActivityFeed: React.FC<{ sessionId: string }> = ({ sessionId }) => {
  const [activities, setActivities] = useState<AgentActivity[]>([]);
  
  useEffect(() => {
    const ws = new WebSocket(`wss://api.olai.dev/ws/${sessionId}/activities`);
    
    ws.onmessage = (event) => {
      const activity = JSON.parse(event.data);
      setActivities(prev => [activity, ...prev].slice(0, 20));
    };
    
    return () => ws.close();
  }, [sessionId]);
  
  return (
    <div className="activity-feed">
      <h3>Agent Activity</h3>
      
      {activities.map(activity => (
        <div key={activity.id} className="activity-item">
          <div className="activity-icon">
            {getAgentIcon(activity.agentType)}
          </div>
          
          <div className="activity-content">
            <span className="agent-name">{activity.agentName}</span>
            <span className="activity-message">{activity.message}</span>
            <span className="activity-time">
              {formatRelativeTime(activity.timestamp)}
            </span>
          </div>
          
          {activity.progress !== undefined && (
            <div className="activity-progress">
              <ProgressBar value={activity.progress} />
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

// Deadline countdown component
const DeadlineCountdown: React.FC<{ deadline: Date }> = ({ deadline }) => {
  const [timeRemaining, setTimeRemaining] = useState('');
  
  useEffect(() => {
    const interval = setInterval(() => {
      const now = Date.now();
      const remaining = deadline.getTime() - now;
      
      if (remaining <= 0) {
        setTimeRemaining('Deadline reached');
        clearInterval(interval);
      } else {
        setTimeRemaining(formatDuration(remaining));
      }
    }, 1000);
    
    return () => clearInterval(interval);
  }, [deadline]);
  
  const getUrgencyClass = () => {
    const remaining = deadline.getTime() - Date.now();
    const hours = remaining / (1000 * 60 * 60);
    
    if (hours < 2) return 'urgent';
    if (hours < 6) return 'warning';
    return 'normal';
  };
  
  return (
    <div className={`deadline-countdown ${getUrgencyClass()}`}>
      <ClockIcon />
      <span>Time remaining: {timeRemaining}</span>
      <span className="deadline-time">
        Deadline: {deadline.toLocaleString()}
      </span>
    </div>
  );
};
```

**Benefits:**
- ✅ **Conversational**: Natural language interaction
- ✅ **Real-Time**: Live updates via WebSocket
- ✅ **Visual Feedback**: Progress, agent activity, countdown
- ✅ **Rich Messages**: Code snippets, visualizations, options
- ✅ **Responsive**: Mobile-friendly chat interface
- ✅ **Context-Aware**: Understands conversation flow

---

### 4.1 User Prompt Processing (Comprehensive)

User prompts are analyzed using advanced NLP and LLM techniques to extract intent, requirements, and context for accurate project understanding.

---

#### **Natural Language Processing Pipeline**

```typescript
interface MessageAnalysis {
  // Intent classification
  intent: {
    primary: Intent;
    confidence: number;
    secondary?: Intent[];
  };
  
  // Extracted entities
  entities: {
    projectType: ProjectType;
    features: Feature[];
    platforms: Platform[];
    technologies: Technology[];
    deadline?: Date;
    budget?: number;
    targetUsers?: string[];
  };
  
  // Requirements extraction
  requirements: {
    functional: Requirement[];
    nonFunctional: Requirement[];
    constraints: Constraint[];
  };
  
  // Ambiguities and missing information
  ambiguities: Ambiguity[];
  missingInfo: MissingInformation[];
  
  // Sentiment and complexity
  sentiment: 'positive' | 'neutral' | 'negative';
  complexity: 'simple' | 'medium' | 'complex' | 'enterprise';
  confidence: number;  // Overall analysis confidence
}

enum Intent {
  NEW_PROJECT = 'new_project',
  MODIFY_REQUIREMENT = 'modify_requirement',
  ASK_QUESTION = 'ask_question',
  PROVIDE_INFORMATION = 'provide_information',
  APPROVE_DECISION = 'approve_decision',
  REJECT_DECISION = 'reject_decision',
  REQUEST_STATUS = 'request_status',
  CHANGE_DEADLINE = 'change_deadline',
  VIEW_CODE = 'view_code',
  EXPORT_PROJECT = 'export_project'
}

class PromptProcessor {
  private nlp: NLPEngine;
  private llm: LLMClient;
  
  /**
   * Process user prompt with NLP + LLM
   */
  async processPrompt(
    prompt: string,
    context: ConversationContext
  ): Promise<MessageAnalysis> {
    // 1. Pre-process text
    const cleanedPrompt = this.preprocessText(prompt);
    
    // 2. Extract intent using NLP
    const intent = await this.extractIntent(cleanedPrompt, context);
    
    // 3. Extract entities using NER (Named Entity Recognition)
    const entities = await this.extractEntities(cleanedPrompt);
    
    // 4. Extract requirements using LLM
    const requirements = await this.extractRequirements(cleanedPrompt, context);
    
    // 5. Detect ambiguities
    const ambiguities = await this.detectAmbiguities(cleanedPrompt, entities, requirements);
    
    // 6. Identify missing information
    const missingInfo = await this.identifyMissingInfo(entities, requirements, context);
    
    // 7. Assess complexity
    const complexity = await this.assessComplexity(requirements, entities);
    
    // 8. Calculate overall confidence
    const confidence = this.calculateConfidence(intent, entities, requirements);
    
    return {
      intent,
      entities,
      requirements,
      ambiguities,
      missingInfo,
      sentiment: this.analyzeSentiment(cleanedPrompt),
      complexity,
      confidence
    };
  }
  
  /**
   * Extract intent from prompt
   */
  private async extractIntent(
    prompt: string,
    context: ConversationContext
  ): Promise<{ primary: Intent; confidence: number; secondary?: Intent[] }> {
    // Use LLM to classify intent
    const classification = await this.llm.complete({
      model: 'gemini-1.5-flash',  // Fast intent classification
      prompt: `
You are an intent classifier for a project management system.

Conversation context:
${JSON.stringify(context, null, 2)}

User message: "${prompt}"

Classify the user's primary intent from these options:
- new_project: Starting a new project
- modify_requirement: Changing existing requirements
- ask_question: Asking a question
- provide_information: Providing requested information
- approve_decision: Approving a suggestion
- reject_decision: Rejecting a suggestion
- request_status: Asking for project status
- change_deadline: Modifying deadline
- view_code: Requesting to see code
- export_project: Exporting/downloading project

Respond in JSON format:
{
  "primary": "intent_name",
  "confidence": 0.95,
  "secondary": ["other_intent"],
  "reasoning": "explanation"
}
      `,
      temperature: 0.1  // Low temperature for classification
    });
    
    const result = JSON.parse(classification);
    return {
      primary: result.primary as Intent,
      confidence: result.confidence,
      secondary: result.secondary
    };
  }
  
  /**
   * Extract entities using NER
   */
  private async extractEntities(prompt: string): Promise<any> {
    const entities: any = {
      projectType: null,
      features: [],
      platforms: [],
      technologies: [],
      deadline: null,
      budget: null,
      targetUsers: []
    };
    
    // Use LLM for entity extraction
    const extraction = await this.llm.complete({
      model: 'gemini-1.5-pro',  // Better for complex extraction
      prompt: `
Extract structured information from this project description:

"${prompt}"

Extract the following:
1. Project type (web app, mobile app, desktop app, API, AI system, etc.)
2. Features mentioned (list all)
3. Target platforms (web, iOS, Android, Windows, macOS)
4. Technologies or frameworks mentioned
5. Deadline (if any, parse date/time)
6. Budget or cost constraints
7. Target users or audience

Respond in JSON format:
{
  "projectType": "type",
  "features": ["feature1", "feature2"],
  "platforms": ["web", "mobile"],
  "technologies": ["React", "Node.js"],
  "deadline": "ISO date or null",
  "budget": number or null,
  "targetUsers": ["description"]
}
      `,
      temperature: 0.2
    });
    
    const extracted = JSON.parse(extraction);
    
    // Parse deadline if present
    if (extracted.deadline) {
      entities.deadline = this.parseDeadline(extracted.deadline);
    }
    
    return { ...entities, ...extracted };
  }
  
  /**
   * Parse deadline from natural language
   */
  private parseDeadline(deadlineText: string): Date | null {
    // Handle various formats:
    // - "by 6:00 PM"
    // - "by tomorrow"
    // - "in 3 hours"
    // - "by next Friday"
    // - "2024-01-20 18:00"
    
    const now = new Date();
    
    // Relative time patterns
    const patterns = {
      // "by 6:00 PM" or "by 6pm"
      timeToday: /by (\d{1,2})(?::(\d{2}))?\s*(am|pm)/i,
      
      // "in X hours/days"
      relativeTime: /in (\d+)\s*(hour|day|week)s?/i,
      
      // "tomorrow", "today"
      relativeDay: /(today|tomorrow|tonight)/i,
      
      // "next Monday", "this Friday"
      namedDay: /(next|this)\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)/i,
      
      // ISO date
      isoDate: /^\d{4}-\d{2}-\d{2}/
    };
    
    // Try time today
    let match = deadlineText.match(patterns.timeToday);
    if (match) {
      const hour = parseInt(match[1]);
      const minute = match[2] ? parseInt(match[2]) : 0;
      const isPM = match[3].toLowerCase() === 'pm';
      
      const deadline = new Date(now);
      deadline.setHours(isPM && hour !== 12 ? hour + 12 : hour);
      deadline.setMinutes(minute);
      deadline.setSeconds(0);
      
      // If time has passed today, assume tomorrow
      if (deadline < now) {
        deadline.setDate(deadline.getDate() + 1);
      }
      
      return deadline;
    }
    
    // Try relative time
    match = deadlineText.match(patterns.relativeTime);
    if (match) {
      const amount = parseInt(match[1]);
      const unit = match[2].toLowerCase();
      
      const deadline = new Date(now);
      
      switch (unit) {
        case 'hour':
          deadline.setHours(deadline.getHours() + amount);
          break;
        case 'day':
          deadline.setDate(deadline.getDate() + amount);
          break;
        case 'week':
          deadline.setDate(deadline.getDate() + amount * 7);
          break;
      }
      
      return deadline;
    }
    
    // Try ISO date
    try {
      const date = new Date(deadlineText);
      if (!isNaN(date.getTime())) {
        return date;
      }
    } catch {}
    
    return null;
  }
  
  /**
   * Extract requirements using LLM
   */
  private async extractRequirements(
    prompt: string,
    context: ConversationContext
  ): Promise<{ functional: Requirement[]; nonFunctional: Requirement[]; constraints: Constraint[] }> {
    const analysis = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Analyze this project description and extract requirements:

"${prompt}"

Previous context:
${JSON.stringify(context.requirements, null, 2)}

Extract:
1. Functional requirements (what the system should do)
2. Non-functional requirements (performance, security, usability)
3. Constraints (technical, budget, time)

For each requirement, assess:
- Priority (critical, high, medium, low)
- Clarity (clear, ambiguous, missing details)
- Feasibility (easy, medium, complex, needs research)

Respond in JSON:
{
  "functional": [
    {
      "id": "req-1",
      "description": "User authentication with email/password",
      "priority": "critical",
      "clarity": "clear",
      "feasibility": "easy"
    }
  ],
  "nonFunctional": [...],
  "constraints": [
    {
      "type": "technical",
      "description": "Must work on mobile devices",
      "impact": "high"
    }
  ]
}
      `,
      temperature: 0.3
    });
    
    return JSON.parse(analysis);
  }
  
  /**
   * Detect ambiguities in requirements
   */
  private async detectAmbiguities(
    prompt: string,
    entities: any,
    requirements: any
  ): Promise<Ambiguity[]> {
    const ambiguities: Ambiguity[] = [];
    
    // Check for vague terms
    const vagueTerms = ['modern', 'user-friendly', 'fast', 'secure', 'scalable', 'nice', 'good'];
    for (const term of vagueTerms) {
      if (prompt.toLowerCase().includes(term)) {
        ambiguities.push({
          type: 'vague_term',
          term,
          suggestion: `What specifically do you mean by "${term}"?`,
          severity: 'low'
        });
      }
    }
    
    // Check for missing platforms
    if (!entities.platforms || entities.platforms.length === 0) {
      ambiguities.push({
        type: 'missing_platform',
        suggestion: 'Which platforms should this run on? (Web, iOS, Android, Desktop)',
        severity: 'high'
      });
    }
    
    // Check for unclear scope
    if (requirements.functional.length < 3) {
      ambiguities.push({
        type: 'unclear_scope',
        suggestion: 'Could you describe more features or what users should be able to do?',
        severity: 'high'
      });
    }
    
    return ambiguities;
  }
  
  /**
   * Identify missing critical information
   */
  private async identifyMissingInfo(
    entities: any,
    requirements: any,
    context: ConversationContext
  ): Promise<MissingInformation[]> {
    const missing: MissingInformation[] = [];
    
    // Critical information checklist
    if (!entities.projectType) {
      missing.push({
        field: 'projectType',
        importance: 'critical',
        question: 'What type of application are you building?'
      });
    }
    
    if (!entities.targetUsers || entities.targetUsers.length === 0) {
      missing.push({
        field: 'targetUsers',
        importance: 'high',
        question: 'Who will be using this application?'
      });
    }
    
    if (!entities.deadline) {
      missing.push({
        field: 'deadline',
        importance: 'medium',
        question: 'Do you have a deadline for this project?'
      });
    }
    
    // Domain-specific questions
    if (entities.projectType === 'e-commerce') {
      if (!this.mentionsPayment(requirements)) {
        missing.push({
          field: 'payment',
          importance: 'critical',
          question: 'How should customers pay? (Credit card, PayPal, etc.)'
        });
      }
    }
    
    if (entities.projectType === 'ai-powered') {
      if (!this.mentionsModels(requirements)) {
        missing.push({
          field: 'aiModels',
          importance: 'critical',
          question: 'What AI capabilities do you need? (e.g., text generation, image analysis, predictions)'
        });
      }
    }
    
    return missing;
  }
  
  /**
   * Assess project complexity
   */
  private async assessComplexity(
    requirements: any,
    entities: any
  ): Promise<'simple' | 'medium' | 'complex' | 'enterprise'> {
    let score = 0;
    
    // Factor 1: Number of requirements
    score += requirements.functional.length * 2;
    score += requirements.nonFunctional.length;
    score += requirements.constraints.length;
    
    // Factor 2: Platform count
    score += (entities.platforms?.length || 0) * 5;
    
    // Factor 3: Special features
    if (entities.projectType === 'ai-powered') score += 20;
    if (this.requiresAuth(requirements)) score += 10;
    if (this.requiresPayments(requirements)) score += 15;
    if (this.requiresRealtime(requirements)) score += 10;
    
    // Factor 4: Scale indicators
    if (this.mentionsScale(requirements)) score += 15;
    
    // Classify based on score
    if (score < 20) return 'simple';
    if (score < 50) return 'medium';
    if (score < 100) return 'complex';
    return 'enterprise';
  }
}
```

**Benefits:**
- ✅ **Intent Classification**: Accurate understanding of user intent
- ✅ **Entity Extraction**: Identifies all project entities automatically
- ✅ **Requirement Extraction**: Structured functional and non-functional requirements
- ✅ **Ambiguity Detection**: Identifies vague or unclear information
- ✅ **Missing Info Identification**: Knows what questions to ask
- ✅ **Deadline Parsing**: Handles natural language deadlines
- ✅ **Complexity Assessment**: Automatic project complexity scoring

---

### 4.2 Requirements Gathering (Comprehensive)

The requirements gathering system uses intelligent questioning strategies to extract complete project specifications through natural conversation, adapting to project type and user expertise level.

---

#### **Continuous Questioning Strategy**

```typescript
interface QuestioningStrategy {
  phases: {
    initial: InitialQuestions;
    contextual: ContextualQuestions;
    clarification: ClarificationQuestions;
    validation: ValidationQuestions;
  };
  rules: {
    minimalQuestions: boolean;
    avoidRedundancy: boolean;
    adaptToProjectType: boolean;
    completeUnderstandingRequired: boolean;
  };
}

enum QuestionPhase {
  INITIAL = 'initial',           // First set of questions
  CONTEXTUAL = 'contextual',     // Questions during development
  CLARIFICATION = 'clarification', // Ambiguity resolution
  VALIDATION = 'validation'      // Confirm understanding
}

interface Question {
  id: string;
  phase: QuestionPhase;
  text: string;
  importance: 'critical' | 'high' | 'medium' | 'low';
  context: string;  // Why this question is being asked
  options?: string[];  // Multiple choice options
  defaultValue?: any;
  validation?: ValidationRule;
  dependsOn?: string[];  // Other question IDs this depends on
  skipConditions?: SkipCondition[];
}

interface QuestioningContext {
  projectType: ProjectType;
  askedQuestions: Set<string>;
  answeredQuestions: Map<string, any>;
  currentPhase: QuestionPhase;
  remainingGaps: InformationGap[];
  userExpertiseLevel: 'beginner' | 'intermediate' | 'expert';
}

class RequirementsGatherer {
  private questionGenerator: QuestionGenerator;
  private contextAnalyzer: ContextAnalyzer;
  private gapIdentifier: GapIdentifier;
  
  /**
   * Main requirements gathering orchestrator
   */
  /**
   * CRITICAL: Three-Document Requirements-First Flow Implementation
   *
   * Before ANY implementation begins, this method creates three comprehensive documents
   * that serve as the single source of truth for the entire project lifecycle.
   */
  async gatherRequirements(
    projectDescription: string,
    conversationContext: ConversationContext
  ): Promise<RequirementsSpec> {
    // ===== PHASE 1: INITIAL ANALYSIS =====
    const initialAnalysis = await this.analyzeInitialInput(projectDescription);

    // ===== PHASE 2: THREE-DOCUMENT CREATION =====

    // 2.1 Document 1: Single Page Idea Summary
    console.log('📄 Creating Document 1: Single Page Idea Summary...');
    const ideaSummary = await this.generateIdeaSummary({
      projectDescription,
      initialAnalysis,
      conversationContext,
      format: 'single-page'
    });

    // 2.2 Document 2: Detailed Technical Documentation
    console.log('📚 Creating Document 2: Detailed Technical Documentation...');
    const technicalDocs = await this.generateTechnicalDocumentation({
      ideaSummary,
      initialAnalysis,
      includeDetails: {
        aiModels: true,
        algorithms: true,
        modules: true,
        workflows: true,
        services: true,
        apis: true,
        dataFlows: true,
        integrations: true
      }
    });

    // 2.3 Document 3: Project Map (Nodular Tree View)
    console.log('🗺️  Creating Document 3: Project Map (Nodular Tree)...');
    const projectMap = await this.generateProjectMap({
      technicalDocumentation: technicalDocs,
      initialAnalysis,
      structure: 'nodular-tree',
      includeDependencies: true,
      includeRelationships: true
    });

    // ===== PHASE 3: USER REVIEW & APPROVAL =====
    console.log('👀 Presenting documents for user review...');

    const userApproval = await this.presentDocumentsForUserApproval(
      ideaSummary,
      technicalDocs,
      projectMap,
      conversationContext
    );

    if (!userApproval.approved) {
      // Handle user feedback and iterate
      const revisedDocuments = await this.iterateOnDocumentsBasedOnFeedback(
        userApproval.feedback,
        ideaSummary,
        technicalDocs,
        projectMap
      );

      // Present revised documents again
      const finalApproval = await this.presentDocumentsForUserApproval(
        revisedDocuments.ideaSummary,
        revisedDocuments.technicalDocs,
        revisedDocuments.projectMap,
        conversationContext
      );

      if (!finalApproval.approved) {
        throw new Error('User did not approve project documents. Cannot proceed.');
      }

      // Use revised documents
      ideaSummary = revisedDocuments.ideaSummary;
      technicalDocs = revisedDocuments.technicalDocs;
      projectMap = revisedDocuments.projectMap;
    }

    // ===== PHASE 4: REQUIREMENTS EXTRACTION FROM DOCUMENTS =====
    const requirements = await this.extractRequirementsFromApprovedDocuments(
      ideaSummary,
      technicalDocs,
      projectMap
    );

    // ===== PHASE 5: STORE DOCUMENTS FOR FUTURE REFERENCE =====
    await this.storeProjectDocuments({
      ideaSummary,
      technicalDocs,
      projectMap,
      requirements
    });

    return requirements;
  }

  /**
   * Generates Document 1: Single Page Idea Summary
   */
  private async generateIdeaSummary(params: IdeaSummaryParams): Promise<IdeaSummaryDocument> {
    return await this.pmAgent.generateIdeaSummary({
      projectDescription: params.projectDescription,
      analysis: params.initialAnalysis,
      format: params.format,
      targetAudience: 'user-review'
    });
  }

  /**
   * Generates Document 2: Comprehensive Technical Documentation
   */
  private async generateTechnicalDocumentation(params: TechnicalDocParams): Promise<TechnicalDocumentation> {
    return await this.pmAgent.generateTechnicalDocumentation({
      ideaSummary: params.ideaSummary,
      analysis: params.initialAnalysis,
      includeDetails: params.includeDetails,
      depth: 'comprehensive'
    });
  }

  /**
   * Generates Document 3: Project Map (Nodular Tree Structure)
   */
  private async generateProjectMap(params: ProjectMapParams): Promise<ProjectMap> {
    return await this.pmAgent.generateProjectMap({
      technicalDocumentation: params.technicalDocumentation,
      analysis: params.initialAnalysis,
      structure: params.structure,
      includeDependencies: params.includeDependencies,
      includeRelationships: params.includeRelationships
    });
  }

  /**
   * Presents all three documents for user review and approval
   */
  private async presentDocumentsForUserApproval(
    ideaSummary: IdeaSummaryDocument,
    technicalDocs: TechnicalDocumentation,
    projectMap: ProjectMap,
    conversationContext: ConversationContext
  ): Promise<UserApproval> {
    // Present documents in UI and get user feedback
    const approvalMessage = `
📋 **Document Review Required**

I've created three comprehensive documents for your project:

**📄 Document 1: Idea Summary**
- One-page overview of your project idea
- Target users, goals, and success criteria

**📚 Document 2: Technical Documentation**
- Complete technical specifications
- AI models, algorithms, modules, and workflows
- Architecture and implementation details

**🗺️ Document 3: Project Map**
- Complete nodular tree of your application
- All components, APIs, services, and relationships

Please review these documents. Do they accurately capture your vision?
Would you like me to make any changes before we proceed with implementation?

Reply with:
- ✅ **"APPROVE"** to proceed
- 🔄 **"REVISE"** with your feedback
    `;

    return await this.getUserResponse(approvalMessage, conversationContext);
  }

  /**
   * Extracts final requirements from approved documents
   */
  private async extractRequirementsFromApprovedDocuments(
    ideaSummary: IdeaSummaryDocument,
    technicalDocs: TechnicalDocumentation,
    projectMap: ProjectMap
  ): Promise<RequirementsSpec> {
    return {
      projectType: ideaSummary.projectType,
      features: technicalDocs.features,
      constraints: technicalDocs.constraints,
      technicalStack: technicalDocs.technicalStack,
      aiModels: technicalDocs.aiModels,
      architecture: technicalDocs.architecture,
      projectMap: projectMap,
      sourceDocuments: {
        ideaSummary,
        technicalDocs,
        projectMap
      }
    };
  }
  
  /**
   * Generate initial questions based on project type
   */
  private async generateInitialQuestions(
    analysis: InitialAnalysis
  ): Promise<Question[]> {
    const questions: Question[] = [];
    
    // Detect project type
    const projectType = analysis.projectType;
    
    // Universal questions (all projects)
    questions.push(...this.getUniversalQuestions());
    
    // Project-type specific questions
    switch (projectType) {
      case 'portfolio':
        questions.push(...await this.getPortfolioQuestions());
        break;
        
      case 'e-commerce':
        questions.push(...await this.getEcommerceQuestions());
        break;
        
      case 'ai-powered':
        questions.push(...await this.getAIPoweredQuestions());
        break;
        
      case 'dashboard':
        questions.push(...await this.getDashboardQuestions());
        break;
        
      case 'mobile-app':
        questions.push(...await this.getMobileAppQuestions());
        break;
        
      case 'api':
        questions.push(...await this.getAPIQuestions());
        break;
        
      default:
        questions.push(...await this.getGenericQuestions());
    }
    
    // Filter based on what's already known
    const filteredQuestions = questions.filter(q => 
      !this.alreadyAnswered(q, analysis)
    );
    
    // Prioritize and limit
    const prioritized = this.prioritizeQuestions(filteredQuestions);
    
    // Return top N most important questions (minimize user burden)
    return prioritized.slice(0, 5);  // Max 5 initial questions
  }
  
  /**
   * Universal questions for all projects
   */
  private getUniversalQuestions(): Question[] {
    return [
      {
        id: 'target-users',
        phase: QuestionPhase.INITIAL,
        text: 'Who will be using this application?',
        importance: 'high',
        context: 'Understanding the target audience helps design appropriate UX and features.',
        validation: {
          minLength: 10,
          maxLength: 500
        }
      },
      {
        id: 'primary-goal',
        phase: QuestionPhase.INITIAL,
        text: 'What is the main goal or problem this application solves?',
        importance: 'critical',
        context: 'The core purpose drives all design decisions.',
        validation: {
          minLength: 20,
          maxLength: 1000
        }
      },
      {
        id: 'platforms',
        phase: QuestionPhase.INITIAL,
        text: 'Which platforms should this run on?',
        importance: 'critical',
        context: 'Platform choice affects architecture and build process.',
        options: [
          'Web (browser)',
          'iOS (iPhone/iPad)',
          'Android (phone/tablet)',
          'Windows Desktop',
          'macOS Desktop',
          'All platforms'
        ]
      }
    ];
  }
  
  /**
   * Portfolio-specific questions
   */
  private async getPortfolioQuestions(): Promise<Question[]> {
    return [
      {
        id: 'portfolio-name',
        phase: QuestionPhase.INITIAL,
        text: 'What\'s your name or professional title?',
        importance: 'critical',
        context: 'This will be displayed prominently on your portfolio.',
        validation: {
          minLength: 2,
          maxLength: 100
        }
      },
      {
        id: 'portfolio-profession',
        phase: QuestionPhase.INITIAL,
        text: 'What\'s your profession or area of expertise?',
        importance: 'critical',
        context: 'E.g., "UI/UX Designer", "Full Stack Developer", "Data Scientist"',
        validation: {
          minLength: 5,
          maxLength: 100
        }
      },
      {
        id: 'portfolio-projects',
        phase: QuestionPhase.INITIAL,
        text: 'How many projects would you like to showcase? (Or should I create placeholder projects?)',
        importance: 'high',
        context: 'I can create example projects or use your actual work.',
        options: [
          'Create 3-5 placeholder projects',
          'I\'ll provide my actual projects',
          'Mix of both'
        ]
      },
      {
        id: 'portfolio-contact',
        phase: QuestionPhase.INITIAL,
        text: 'How should visitors contact you?',
        importance: 'high',
        context: 'Email, social media links, contact form, etc.',
        validation: {
          minLength: 10,
          maxLength: 500
        }
      },
      {
        id: 'portfolio-style',
        phase: QuestionPhase.INITIAL,
        text: 'What style do you prefer for your portfolio?',
        importance: 'medium',
        context: 'Visual aesthetic and layout preferences.',
        options: [
          'Minimalist & Clean',
          'Bold & Creative',
          'Professional & Corporate',
          'Dark & Modern',
          'Colorful & Playful',
          'Surprise me (AI decides)'
        ],
        defaultValue: 'Minimalist & Clean'
      }
    ];
  }
  
  /**
   * AI-powered application questions
   */
  private async getAIPoweredQuestions(): Promise<Question[]> {
    return [
      {
        id: 'ai-capabilities',
        phase: QuestionPhase.INITIAL,
        text: 'What AI capabilities does your application need?',
        importance: 'critical',
        context: 'This determines which models to integrate.',
        options: [
          'Text generation (chatbot, content creation)',
          'Image generation (create images from text)',
          'Image analysis (classify, detect objects)',
          'Speech recognition (voice input)',
          'Text-to-speech (voice output)',
          'Predictions/forecasting (ML models)',
          'Natural language understanding',
          'Document analysis (extract info from PDFs/images)',
          'Sentiment analysis',
          'Other (please specify)'
        ]
      },
      {
        id: 'ai-model-preference',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'Do you prefer cloud-based AI models or local models?',
        importance: 'high',
        context: 'Cloud models (API) are easier but cost money. Local models run on your device but need good hardware.',
        options: [
          'Cloud-based (easier, costs per use)',
          'Local (free, requires GPU)',
          'Hybrid (use both depending on task)',
          'You decide based on my hardware'
        ],
        defaultValue: 'You decide based on my hardware'
      },
      {
        id: 'ai-use-cases',
        phase: QuestionPhase.INITIAL,
        text: 'Can you describe a typical scenario where a user would use the AI feature?',
        importance: 'high',
        context: 'Understanding the use case helps optimize the AI integration.',
        validation: {
          minLength: 30,
          maxLength: 1000
        }
      },
      {
        id: 'ai-input-type',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'What type of input will users provide to the AI?',
        importance: 'high',
        context: 'Determines input processing pipeline.',
        options: [
          'Text only',
          'Images',
          'Audio/voice',
          'Video',
          'Documents (PDF, Word, etc.)',
          'Multiple types'
        ]
      },
      {
        id: 'ai-response-time',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'How fast should AI responses be?',
        importance: 'medium',
        context: 'Faster responses may require simpler models or more computing power.',
        options: [
          'Real-time (< 1 second)',
          'Quick (1-3 seconds)',
          'Standard (3-10 seconds)',
          'Batch processing (minutes)',
          'Not critical'
        ],
        defaultValue: 'Standard (3-10 seconds)'
      }
    ];
  }
  
  /**
   * E-commerce specific questions
   */
  private async getEcommerceQuestions(): Promise<Question[]> {
    return [
      {
        id: 'ecom-products',
        phase: QuestionPhase.INITIAL,
        text: 'What types of products will you sell?',
        importance: 'critical',
        context: 'Product type affects catalog structure and features.',
        validation: {
          minLength: 10,
          maxLength: 500
        }
      },
      {
        id: 'ecom-payment',
        phase: QuestionPhase.INITIAL,
        text: 'How should customers pay?',
        importance: 'critical',
        context: 'Payment integration is essential for e-commerce.',
        options: [
          'Credit/Debit cards (Stripe)',
          'PayPal',
          'Multiple payment methods',
          'Cash on delivery',
          'I\'ll decide later'
        ]
      },
      {
        id: 'ecom-inventory',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'Do you need inventory management?',
        importance: 'high',
        context: 'Track stock levels, low stock alerts, etc.',
        options: [
          'Yes, full inventory tracking',
          'Basic stock tracking',
          'No, digital products only',
          'Not needed'
        ]
      },
      {
        id: 'ecom-shipping',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'Will you ship physical products?',
        importance: 'high',
        context: 'Determines if shipping calculator and tracking are needed.',
        options: [
          'Yes, integrate shipping',
          'Manual shipping (I handle it)',
          'Digital products only',
          'Local pickup only'
        ]
      },
      {
        id: 'ecom-users',
        phase: QuestionPhase.CONTEXTUAL,
        text: 'Should customers create accounts?',
        importance: 'medium',
        context: 'User accounts enable order history, wishlists, etc.',
        options: [
          'Required (must register)',
          'Optional (guest checkout available)',
          'Guest checkout only',
          'You decide'
        ],
        defaultValue: 'Optional (guest checkout available)'
      }
    ];
  }
  
  /**
   * Ask questions interactively via chat
   */
  private async askQuestionsInteractively(
    questions: Question[],
    context: ConversationContext
  ): Promise<Map<string, any>> {
    const answers = new Map<string, any>();
    
    for (const question of questions) {
      // Skip if already answered or conditions not met
      if (this.shouldSkipQuestion(question, answers)) {
        continue;
      }
      
      // Format question message
      const message = this.formatQuestionMessage(question);
      
      // Send to user via chat
      await this.sendChatMessage(context, message);
      
      // Wait for answer
      const answer = await this.waitForAnswer(context, question);
      
      // Validate answer
      if (question.validation) {
        const isValid = await this.validateAnswer(answer, question.validation);
        if (!isValid) {
          // Ask again with validation error
          const retryMessage = this.formatValidationError(question);
          await this.sendChatMessage(context, retryMessage);
          const retryAnswer = await this.waitForAnswer(context, question);
          answers.set(question.id, retryAnswer);
        } else {
          answers.set(question.id, answer);
        }
      } else {
        answers.set(question.id, answer);
      }
      
      // Show acknowledgment
      await this.sendChatMessage(context, {
        type: 'agent',
        content: this.getAcknowledgment(question, answer)
      });
    }
    
    return answers;
  }
  
  /**
   * Format question as chat message
   */
  private formatQuestionMessage(question: Question): Message {
    let content = `**${question.text}**\n\n`;
    
    // Add context (why we're asking)
    content += `_${question.context}_\n\n`;
    
    // Add options if multiple choice
    if (question.options) {
      content += '**Options:**\n';
      question.options.forEach((opt, i) => {
        content += `${i + 1}. ${opt}\n`;
      });
      
      if (question.defaultValue) {
        const defaultIndex = question.options.indexOf(question.defaultValue);
        if (defaultIndex >= 0) {
          content += `\n_If you're not sure, I recommend option ${defaultIndex + 1}_`;
        }
      }
    }
    
    // Add importance indicator
    if (question.importance === 'critical') {
      content = '🔴 ' + content;  // Red circle for critical
    } else if (question.importance === 'high') {
      content = '🟡 ' + content;  // Yellow circle for high
    }
    
    return {
      id: generateUUID(),
      type: 'agent',
      sender: 'PM Agent',
      content,
      timestamp: new Date(),
      metadata: {
        requiresResponse: true,
        questionId: question.id,
        options: question.options
      }
    };
  }
  
  /**
   * Generate contextual questions based on information gaps
   */
  private async generateContextualQuestions(
    gaps: InformationGap[]
  ): Promise<Question[]> {
    const questions: Question[] = [];
    
    for (const gap of gaps) {
      // Use LLM to generate natural question
      const question = await this.llm.complete({
        model: 'gemini-1.5-flash',
        prompt: `
Generate a natural, conversational question to gather this missing information:

Gap: ${gap.field}
Importance: ${gap.importance}
Context: ${gap.context}

The question should be:
1. Clear and specific
2. Easy to answer
3. Explain why we need this information
4. Include examples if helpful

Respond in JSON:
{
  "text": "Your question here",
  "context": "Why this matters",
  "options": ["option1", "option2"] or null,
  "defaultValue": "default" or null
}
        `,
        temperature: 0.4
      });
      
      const generated = JSON.parse(question);
      
      questions.push({
        id: `contextual-${gap.field}`,
        phase: QuestionPhase.CONTEXTUAL,
        text: generated.text,
        importance: gap.importance,
        context: generated.context,
        options: generated.options,
        defaultValue: generated.defaultValue
      });
    }
    
    return questions;
  }
  
  /**
   * Identify information gaps
   */
  private async identifyGaps(
    requirements: RequirementsSpec
  ): Promise<InformationGap[]> {
    const gaps: InformationGap[] = [];
    
    // Check functional requirements completeness
    if (requirements.functional.length < 3) {
      gaps.push({
        field: 'functional-requirements',
        importance: 'high',
        context: 'We need more details about what the application should do'
      });
    }
    
    // Check technical requirements
    if (!requirements.technical.database && this.needsDatabase(requirements)) {
      gaps.push({
        field: 'database',
        importance: 'high',
        context: 'This type of application typically needs a database'
      });
    }
    
    // Check user authentication
    if (!requirements.hasUserAuth && this.shouldHaveAuth(requirements)) {
      gaps.push({
        field: 'authentication',
        importance: 'medium',
        context: 'Should users be able to create accounts and log in?'
      });
    }
    
    // Use LLM to identify subtle gaps
    const llmGaps = await this.identifyGapsWithLLM(requirements);
    gaps.push(...llmGaps);
    
    return gaps;
  }
}
```

**Benefits:**
- ✅ **Adaptive Questioning**: Questions adapt to project type and context
- ✅ **Minimal Burden**: Max 5 initial questions, more only if needed
- ✅ **Natural Conversation**: Questions feel like natural chat, not forms
- ✅ **Smart Defaults**: Suggests sensible defaults for non-critical choices
- ✅ **Validation**: Ensures answer quality before proceeding
- ✅ **Gap Detection**: Automatically identifies missing information
- ✅ **Priority-Based**: Critical questions first, optional questions later

---

### 4.3 Specification Completion (Comprehensive)

The specification completion system validates, consolidates, and structures all gathered requirements into a complete, consistent, and actionable project specification.

---

#### **Specification Building Engine**

```typescript
interface RequirementsSpec {
  // Meta information
  id: string;
  projectName: string;
  projectType: ProjectType;
  createdAt: Date;
  lastUpdated: Date;
  completeness: number;  // 0-100%
  confidence: number;    // 0-100%
  
  // Project overview
  overview: {
    description: string;
    primaryGoal: string;
    targetUsers: string[];
    problemSolved: string;
    successCriteria: string[];
  };
  
  // Functional requirements
  functional: FunctionalRequirement[];
  
  // Non-functional requirements
  nonFunctional: {
    performance: PerformanceRequirement[];
    security: SecurityRequirement[];
    usability: UsabilityRequirement[];
    reliability: ReliabilityRequirement[];
    scalability: ScalabilityRequirement[];
  };
  
  // Technical requirements
  technical: {
    platforms: Platform[];
    database?: DatabaseRequirement;
    authentication?: AuthRequirement;
    apis: APIRequirement[];
    aiModels?: AIModelRequirement[];
    thirdPartyIntegrations: Integration[];
  };
  
  // Architecture preferences
  architecture: {
    frontend: ArchitectureChoice;
    backend: ArchitectureChoice;
    deployment: DeploymentChoice;
    hosting: HostingChoice;
  };
  
  // Timeline and milestones
  timeline: {
    deadline?: Date;
    estimatedDuration: number;  // hours
    milestones: Milestone[];
    criticalPath: Task[];
  };
  
  // Resource constraints
  constraints: {
    budget?: number;
    hardware: HardwareConstraints;
    team: TeamConstraints;
    technical: TechnicalConstraints;
  };
  
  // Validation status
  validation: {
    isComplete: boolean;
    isConsistent: boolean;
    hasConflicts: boolean;
    conflicts: Conflict[];
    warnings: Warning[];
  };
}

interface FunctionalRequirement {
  id: string;
  title: string;
  description: string;
  priority: 'critical' | 'high' | 'medium' | 'low';
  category: string;  // 'user-management', 'content', 'payment', etc.
  userStory: string;  // "As a [user], I want [feature] so that [benefit]"
  acceptanceCriteria: string[];
  dependencies: string[];  // IDs of other requirements
  estimatedEffort: number;  // hours
  technicalNotes: string;
}

class SpecificationBuilder {
  private validator: SpecValidator;
  private consistencyChecker: ConsistencyChecker;
  private conflictResolver: ConflictResolver;
  
  /**
   * Build complete specification from gathered information
   */
  async buildSpecification(
    answers: Map<string, any>,
    initialAnalysis: InitialAnalysis
  ): Promise<RequirementsSpec> {
    // 1. Create base specification
    const spec: RequirementsSpec = {
      id: generateUUID(),
      projectName: this.extractProjectName(answers, initialAnalysis),
      projectType: initialAnalysis.projectType,
      createdAt: new Date(),
      lastUpdated: new Date(),
      completeness: 0,
      confidence: 0,
      overview: await this.buildOverview(answers, initialAnalysis),
      functional: [],
      nonFunctional: {
        performance: [],
        security: [],
        usability: [],
        reliability: [],
        scalability: []
      },
      technical: {
        platforms: [],
        apis: [],
        thirdPartyIntegrations: []
      },
      architecture: await this.determineArchitecture(answers),
      timeline: await this.buildTimeline(answers),
      constraints: await this.buildConstraints(answers),
      validation: {
        isComplete: false,
        isConsistent: true,
        hasConflicts: false,
        conflicts: [],
        warnings: []
      }
    };
    
    // 2. Extract functional requirements
    spec.functional = await this.extractFunctionalRequirements(
      answers,
      initialAnalysis,
      spec.projectType
    );
    
    // 3. Infer non-functional requirements
    spec.nonFunctional = await this.inferNonFunctionalRequirements(spec);
    
    // 4. Determine technical requirements
    spec.technical = await this.determineTechnicalRequirements(spec, answers);
    
    // 5. Validate completeness
    spec.completeness = await this.calculateCompleteness(spec);
    
    // 6. Check consistency
    await this.checkConsistency(spec);
    
    // 7. Resolve conflicts if any
    if (spec.validation.hasConflicts) {
      await this.resolveConflicts(spec);
    }
    
    // 8. Calculate confidence
    spec.confidence = await this.calculateConfidence(spec);
    
    return spec;
  }
  
  /**
   * Build project overview
   */
  private async buildOverview(
    answers: Map<string, any>,
    analysis: InitialAnalysis
  ): Promise<any> {
    return {
      description: analysis.description,
      primaryGoal: answers.get('primary-goal') || analysis.primaryGoal,
      targetUsers: this.extractTargetUsers(answers),
      problemSolved: analysis.problemSolved,
      successCriteria: await this.generateSuccessCriteria(answers, analysis)
    };
  }
  
  /**
   * Extract functional requirements using LLM
   */
  private async extractFunctionalRequirements(
    answers: Map<string, any>,
    analysis: InitialAnalysis,
    projectType: ProjectType
  ): Promise<FunctionalRequirement[]> {
    // Use LLM to generate structured requirements
    const llmAnalysis = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
You are a product manager creating a requirements specification.

Project type: ${projectType}
Project description: ${analysis.description}

User answers:
${JSON.stringify(Array.from(answers.entries()), null, 2)}

Generate a comprehensive list of functional requirements.

For each requirement, provide:
1. Title (short, descriptive)
2. Description (detailed explanation)
3. Priority (critical/high/medium/low)
4. Category (user-management, content, payment, etc.)
5. User story (As a [user], I want [feature] so that [benefit])
6. Acceptance criteria (list of conditions that must be met)
7. Estimated effort in hours

Respond in JSON array format:
[
  {
    "title": "User Authentication",
    "description": "Users can create accounts and log in securely",
    "priority": "critical",
    "category": "user-management",
    "userStory": "As a user, I want to create an account so that I can save my preferences",
    "acceptanceCriteria": [
      "Users can register with email/password",
      "Users can log in with credentials",
      "Password must be encrypted",
      "Forgot password functionality"
    ],
    "estimatedEffort": 8
  }
]
      `,
      temperature: 0.3
    });
    
    const requirements = JSON.parse(llmAnalysis);
    
    // Add IDs and dependencies
    return requirements.map((req, index) => ({
      id: `func-${index + 1}`,
      ...req,
      dependencies: this.identifyDependencies(req, requirements),
      technicalNotes: ''
    }));
  }
  
  /**
   * Infer non-functional requirements
   */
  private async inferNonFunctionalRequirements(
    spec: RequirementsSpec
  ): Promise<any> {
    const nonFunctional: any = {
      performance: [],
      security: [],
      usability: [],
      reliability: [],
      scalability: []
    };
    
    // Performance requirements
    if (spec.technical.aiModels && spec.technical.aiModels.length > 0) {
      nonFunctional.performance.push({
        requirement: 'AI response time',
        target: '< 3 seconds for typical requests',
        measurement: 'Time from user input to AI response',
        priority: 'high'
      });
    }
    
    if (spec.projectType === 'e-commerce') {
      nonFunctional.performance.push({
        requirement: 'Page load time',
        target: '< 2 seconds',
        measurement: 'First contentful paint',
        priority: 'high'
      });
    }
    
    // Security requirements
    if (spec.technical.authentication) {
      nonFunctional.security.push({
        requirement: 'Password security',
        target: 'Bcrypt with salt, min 8 characters',
        measurement: 'Password encryption standard',
        priority: 'critical'
      });
      
      nonFunctional.security.push({
        requirement: 'Session management',
        target: 'JWT tokens with 24h expiry',
        measurement: 'Token-based authentication',
        priority: 'critical'
      });
    }
    
    if (spec.projectType === 'e-commerce') {
      nonFunctional.security.push({
        requirement: 'Payment security',
        target: 'PCI DSS compliance via Stripe',
        measurement: 'No card data stored locally',
        priority: 'critical'
      });
    }
    
    // Usability requirements
    nonFunctional.usability.push({
      requirement: 'Mobile responsiveness',
      target: 'Works on all screen sizes',
      measurement: 'Responsive design breakpoints',
      priority: 'high'
    });
    
    nonFunctional.usability.push({
      requirement: 'Accessibility',
      target: 'WCAG 2.1 AA compliance',
      measurement: 'Screen reader support, keyboard navigation',
      priority: 'medium'
    });
    
    // Reliability requirements
    nonFunctional.reliability.push({
      requirement: 'Uptime',
      target: '99.9% availability',
      measurement: 'Server uptime monitoring',
      priority: 'high'
    });
    
    nonFunctional.reliability.push({
      requirement: 'Error handling',
      target: 'Graceful degradation',
      measurement: 'No crashes, user-friendly error messages',
      priority: 'high'
    });
    
    // Scalability requirements (if needed)
    if (this.requiresScalability(spec)) {
      nonFunctional.scalability.push({
        requirement: 'Concurrent users',
        target: '1000+ simultaneous users',
        measurement: 'Load testing',
        priority: 'medium'
      });
    }
    
    return nonFunctional;
  }
  
  /**
   * Determine technical requirements
   */
  private async determineTechnicalRequirements(
    spec: RequirementsSpec,
    answers: Map<string, any>
  ): Promise<any> {
    const technical: any = {
      platforms: answers.get('platforms') || ['web'],
      apis: [],
      thirdPartyIntegrations: []
    };
    
    // Database requirement
    if (this.needsDatabase(spec)) {
      technical.database = {
        type: this.chooseDatabaseType(spec),
        reason: this.explainDatabaseChoice(spec),
        schema: await this.generateDatabaseSchema(spec)
      };
    }
    
    // Authentication requirement
    if (this.needsAuthentication(spec)) {
      technical.authentication = {
        method: 'JWT',
        provider: 'custom',  // or 'Firebase', 'Auth0', etc.
        features: ['login', 'register', 'forgot-password', 'email-verification']
      };
    }
    
    // AI models requirement
    if (spec.projectType === 'ai-powered') {
      technical.aiModels = await this.selectAIModels(spec, answers);
    }
    
    // Third-party integrations
    if (spec.projectType === 'e-commerce') {
      technical.thirdPartyIntegrations.push({
        service: 'Stripe',
        purpose: 'Payment processing',
        required: true
      });
    }
    
    return technical;
  }
  
  /**
   * Check specification consistency
   */
  private async checkConsistency(spec: RequirementsSpec): Promise<void> {
    const conflicts: Conflict[] = [];
    const warnings: Warning[] = [];
    
    // Check platform vs features consistency
    if (spec.technical.platforms.includes('mobile') && 
        !spec.technical.platforms.includes('ios') &&
        !spec.technical.platforms.includes('android')) {
      conflicts.push({
        type: 'platform-mismatch',
        severity: 'high',
        description: 'Mobile platform specified but no specific mobile OS chosen',
        resolution: 'Clarify: iOS, Android, or both?'
      });
    }
    
    // Check deadline vs complexity
    if (spec.timeline.deadline) {
      const estimatedHours = this.calculateTotalEffort(spec);
      const availableHours = this.calculateAvailableHours(spec.timeline.deadline);
      
      if (estimatedHours > availableHours * 1.5) {
        warnings.push({
          type: 'tight-deadline',
          severity: 'high',
          description: `Estimated ${estimatedHours}h of work, only ${availableHours}h available`,
          recommendation: 'Consider reducing scope or extending deadline'
        });
      }
    }
    
    // Check dependencies
    for (const req of spec.functional) {
      for (const depId of req.dependencies) {
        const dep = spec.functional.find(r => r.id === depId);
        if (!dep) {
          conflicts.push({
            type: 'missing-dependency',
            severity: 'high',
            description: `Requirement "${req.title}" depends on missing requirement ${depId}`,
            resolution: 'Add missing requirement or remove dependency'
          });
        }
      }
    }
    
    // Update validation status
    spec.validation.conflicts = conflicts;
    spec.validation.warnings = warnings;
    spec.validation.hasConflicts = conflicts.length > 0;
    spec.validation.isConsistent = conflicts.length === 0;
  }
  
  /**
   * Calculate specification completeness
   */
  private async calculateCompleteness(spec: RequirementsSpec): Promise<number> {
    let score = 0;
    let maxScore = 100;
    
    // Overview (20 points)
    if (spec.overview.description) score += 5;
    if (spec.overview.primaryGoal) score += 5;
    if (spec.overview.targetUsers.length > 0) score += 5;
    if (spec.overview.successCriteria.length > 0) score += 5;
    
    // Functional requirements (30 points)
    if (spec.functional.length >= 3) score += 10;
    if (spec.functional.length >= 5) score += 10;
    if (spec.functional.every(r => r.acceptanceCriteria.length > 0)) score += 10;
    
    // Technical requirements (20 points)
    if (spec.technical.platforms.length > 0) score += 10;
    if (spec.technical.database || !this.needsDatabase(spec)) score += 5;
    if (spec.technical.authentication || !this.needsAuthentication(spec)) score += 5;
    
    // Architecture (15 points)
    if (spec.architecture.frontend) score += 5;
    if (spec.architecture.backend) score += 5;
    if (spec.architecture.deployment) score += 5;
    
    // Timeline (15 points)
    if (spec.timeline.estimatedDuration > 0) score += 5;
    if (spec.timeline.milestones.length > 0) score += 5;
    if (spec.timeline.criticalPath.length > 0) score += 5;
    
    return Math.round((score / maxScore) * 100);
  }
  
  /**
   * Calculate confidence in specification
   */
  private async calculateConfidence(spec: RequirementsSpec): Promise<number> {
    let confidence = 100;
    
    // Reduce confidence for conflicts
    confidence -= spec.validation.conflicts.length * 10;
    
    // Reduce confidence for warnings
    confidence -= spec.validation.warnings.length * 5;
    
    // Reduce confidence for incomplete spec
    if (spec.completeness < 80) {
      confidence -= (80 - spec.completeness) / 2;
    }
    
    // Reduce confidence for ambiguous requirements
    const ambiguousCount = spec.functional.filter(r => 
      r.description.length < 50 || r.acceptanceCriteria.length < 2
    ).length;
    confidence -= ambiguousCount * 3;
    
    return Math.max(0, Math.min(100, Math.round(confidence)));
  }
}
```

**Benefits:**
- ✅ **Structured Specification**: Complete, organized requirements document
- ✅ **Automatic Inference**: Non-functional requirements inferred from functional ones
- ✅ **Consistency Checking**: Detects conflicts and inconsistencies
- ✅ **Completeness Validation**: Measures specification completeness
- ✅ **Confidence Scoring**: Indicates reliability of specification
- ✅ **Dependency Tracking**: Identifies requirement dependencies
- ✅ **Conflict Resolution**: Automatic resolution suggestions

---

### 4.4 Work Breakdown (Comprehensive)

The work breakdown system decomposes the project specification into executable tasks with dependencies, priorities, and resource assignments.

---

#### **Task Decomposition Engine**

```typescript
interface Task {
  id: string;
  title: string;
  description: string;
  type: TaskType;
  phase: ProjectPhase;
  priority: Priority;
  status: TaskStatus;
  
  // Assignment
  assignedAgent: AgentType;
  estimatedEffort: number;  // hours
  actualEffort?: number;
  
  // Dependencies
  dependencies: string[];  // Task IDs that must complete first
  blockedBy: string[];     // Task IDs currently blocking this
  blocks: string[];        // Task IDs this task blocks
  
  // Timeline
  plannedStart?: Date;
  plannedEnd?: Date;
  actualStart?: Date;
  actualEnd?: Date;
  
  // Deliverables
  deliverables: Deliverable[];
  acceptanceCriteria: string[];
  
  // Context
  requirementIds: string[];  // Links to requirements
  artifacts: Artifact[];
  notes: string;
}

enum TaskType {
  RESEARCH = 'research',
  DESIGN = 'design',
  ARCHITECTURE = 'architecture',
  IMPLEMENTATION = 'implementation',
  TESTING = 'testing',
  BUILD = 'build',
  DEPLOYMENT = 'deployment',
  DOCUMENTATION = 'documentation',
  REVIEW = 'review',
  OPTIMIZATION = 'optimization'
}

enum ProjectPhase {
  PLANNING = 'planning',
  DESIGN = 'design',
  DEVELOPMENT = 'development',
  TESTING = 'testing',
  DEPLOYMENT = 'deployment',
  IMPROVEMENT = 'improvement'
}

enum TaskStatus {
  PENDING = 'pending',
  READY = 'ready',
  ASSIGNED = 'assigned',
  IN_PROGRESS = 'in_progress',
  BLOCKED = 'blocked',
  REVIEW = 'review',
  COMPLETED = 'completed',
  FAILED = 'failed'
}

class WorkBreakdownEngine {
  private taskGenerator: TaskGenerator;
  private dependencyAnalyzer: DependencyAnalyzer;
  private criticalPathCalculator: CriticalPathCalculator;
  
  /**
   * Decompose specification into tasks
   */
  async decomposeProject(
    spec: RequirementsSpec
  ): Promise<WorkBreakdownStructure> {
    const wbs: WorkBreakdownStructure = {
      projectId: spec.id,
      phases: [],
      tasks: [],
      criticalPath: [],
      totalEstimatedEffort: 0,
      parallelizableWork: []
    };
    
    // 1. Generate tasks for each phase
    wbs.phases.push(await this.generatePlanningPhase(spec));
    wbs.phases.push(await this.generateDesignPhase(spec));
    wbs.phases.push(await this.generateDevelopmentPhase(spec));
    wbs.phases.push(await this.generateTestingPhase(spec));
    wbs.phases.push(await this.generateDeploymentPhase(spec));
    
    // 2. Flatten all tasks
    wbs.tasks = wbs.phases.flatMap(phase => phase.tasks);
    
    // 3. Analyze dependencies
    await this.analyzeDependencies(wbs.tasks);
    
    // 4. Calculate critical path
    wbs.criticalPath = await this.calculateCriticalPath(wbs.tasks);
    
    // 5. Identify parallelizable work
    wbs.parallelizableWork = await this.identifyParallelWork(wbs.tasks);
    
    // 6. Calculate total effort
    wbs.totalEstimatedEffort = wbs.tasks.reduce(
      (sum, task) => sum + task.estimatedEffort,
      0
    );
    
    // 7. Assign initial priorities
    await this.assignPriorities(wbs.tasks, wbs.criticalPath);
    
    return wbs;
  }
  
  /**
   * Generate planning phase tasks
   */
  private async generatePlanningPhase(
    spec: RequirementsSpec
  ): Promise<Phase> {
    const tasks: Task[] = [];
    
    // Research tasks
    if (spec.technical.aiModels) {
      tasks.push({
        id: 'task-research-ai-models',
        title: 'Research AI Models',
        description: 'Identify and validate AI models compatible with requirements and hardware',
        type: TaskType.RESEARCH,
        phase: ProjectPhase.PLANNING,
        priority: Priority.CRITICAL,
        status: TaskStatus.PENDING,
        assignedAgent: AgentType.RESEARCH,
        estimatedEffort: 2,
        dependencies: [],
        blockedBy: [],
        blocks: ['task-integrate-ai'],
        deliverables: [
          { type: 'document', name: 'AI Model Selection Report' }
        ],
        acceptanceCriteria: [
          'List of compatible models with hardware requirements',
          'Performance benchmarks',
          'Cost analysis (if API-based)'
        ],
        requirementIds: spec.functional
          .filter(r => r.category === 'ai-features')
          .map(r => r.id),
        artifacts: [],
        notes: ''
      });
    }
    
    if (spec.technical.thirdPartyIntegrations.length > 0) {
      tasks.push({
        id: 'task-research-integrations',
        title: 'Research Third-Party Integrations',
        description: 'Identify APIs and SDKs for required integrations',
        type: TaskType.RESEARCH,
        phase: ProjectPhase.PLANNING,
        priority: Priority.HIGH,
        status: TaskStatus.PENDING,
        assignedAgent: AgentType.RESEARCH,
        estimatedEffort: 1.5,
        dependencies: [],
        blockedBy: [],
        blocks: ['task-implement-integrations'],
        deliverables: [
          { type: 'document', name: 'Integration Requirements' }
        ],
        acceptanceCriteria: [
          'List of APIs with documentation',
          'Authentication requirements',
          'Rate limits and costs'
        ],
        requirementIds: [],
        artifacts: [],
        notes: ''
      });
    }
    
    return {
      name: 'Planning',
      phase: ProjectPhase.PLANNING,
      tasks,
      estimatedDuration: tasks.reduce((sum, t) => sum + t.estimatedEffort, 0),
      status: 'pending'
    };
  }
  
  /**
   * Generate design phase tasks
   */
  private async generateDesignPhase(
    spec: RequirementsSpec
  ): Promise<Phase> {
    const tasks: Task[] = [];
    
    // Architecture design
    tasks.push({
      id: 'task-design-architecture',
      title: 'Design System Architecture',
      description: 'Design overall system architecture, folder structure, and component boundaries',
      type: TaskType.ARCHITECTURE,
      phase: ProjectPhase.DESIGN,
      priority: Priority.CRITICAL,
      status: TaskStatus.PENDING,
      assignedAgent: AgentType.ARCHITECT,
      estimatedEffort: 3,
      dependencies: ['task-research-ai-models', 'task-research-integrations'],
      blockedBy: [],
      blocks: ['task-implement-backend', 'task-implement-frontend'],
      deliverables: [
        { type: 'diagram', name: 'System Architecture Diagram' },
        { type: 'document', name: 'Architecture Decision Records' }
      ],
      acceptanceCriteria: [
        'Complete folder structure defined',
        'API endpoints documented',
        'Database schema designed',
        'Component hierarchy planned'
      ],
      requirementIds: spec.functional.map(r => r.id),
      artifacts: [],
      notes: ''
    });
    
    // Database schema
    if (spec.technical.database) {
      tasks.push({
        id: 'task-design-database',
        title: 'Design Database Schema',
        description: 'Design database tables, relationships, and indexes',
        type: TaskType.DESIGN,
        phase: ProjectPhase.DESIGN,
        priority: Priority.CRITICAL,
        status: TaskStatus.PENDING,
        assignedAgent: AgentType.ARCHITECT,
        estimatedEffort: 2,
        dependencies: ['task-design-architecture'],
        blockedBy: [],
        blocks: ['task-implement-backend'],
        deliverables: [
          { type: 'diagram', name: 'ER Diagram' },
          { type: 'code', name: 'Migration Scripts' }
        ],
        acceptanceCriteria: [
          'All entities identified',
          'Relationships defined',
          'Indexes planned for performance'
        ],
        requirementIds: [],
        artifacts: [],
        notes: ''
      });
    }
    
    // UI/UX design
    tasks.push({
      id: 'task-design-ui',
      title: 'Design UI/UX',
      description: 'Design user interface layouts, components, and user flows',
      type: TaskType.DESIGN,
      phase: ProjectPhase.DESIGN,
      priority: Priority.HIGH,
      status: TaskStatus.PENDING,
      assignedAgent: AgentType.ARCHITECT,
      estimatedEffort: 4,
      dependencies: ['task-design-architecture'],
      blockedBy: [],
      blocks: ['task-implement-frontend'],
      deliverables: [
        { type: 'design', name: 'UI Mockups' },
        { type: 'document', name: 'Component Library Spec' }
      ],
      acceptanceCriteria: [
        'All screens designed',
        'User flows documented',
        'Component reusability considered'
      ],
      requirementIds: spec.functional.map(r => r.id),
      artifacts: [],
      notes: ''
    });
    
    return {
      name: 'Design',
      phase: ProjectPhase.DESIGN,
      tasks,
      estimatedDuration: tasks.reduce((sum, t) => sum + t.estimatedEffort, 0),
      status: 'pending'
    };
  }
  
  /**
   * Generate development phase tasks (largest phase)
   */
  private async generateDevelopmentPhase(
    spec: RequirementsSpec
  ): Promise<Phase> {
    const tasks: Task[] = [];
    
    // Backend implementation
    tasks.push({
      id: 'task-implement-backend',
      title: 'Implement Backend',
      description: 'Build backend API, database integration, business logic',
      type: TaskType.IMPLEMENTATION,
      phase: ProjectPhase.DEVELOPMENT,
      priority: Priority.CRITICAL,
      status: TaskStatus.PENDING,
      assignedAgent: AgentType.CODING,
      estimatedEffort: this.estimateBackendEffort(spec),
      dependencies: ['task-design-architecture', 'task-design-database'],
      blockedBy: [],
      blocks: ['task-implement-frontend', 'task-test-backend'],
      deliverables: [
        { type: 'code', name: 'Backend Source Code' },
        { type: 'document', name: 'API Documentation' }
      ],
      acceptanceCriteria: [
        'All API endpoints implemented',
        'Database operations working',
        'Error handling in place',
        'Logging implemented'
      ],
      requirementIds: spec.functional.map(r => r.id),
      artifacts: [],
      notes: ''
    });
    
    // Frontend implementation
    tasks.push({
      id: 'task-implement-frontend',
      title: 'Implement Frontend',
      description: 'Build user interface components and integrate with backend',
      type: TaskType.IMPLEMENTATION,
      phase: ProjectPhase.DEVELOPMENT,
      priority: Priority.CRITICAL,
      status: TaskStatus.PENDING,
      assignedAgent: AgentType.CODING,
      estimatedEffort: this.estimateFrontendEffort(spec),
      dependencies: ['task-design-ui', 'task-implement-backend'],
      blockedBy: [],
      blocks: ['task-test-frontend'],
      deliverables: [
        { type: 'code', name: 'Frontend Source Code' },
        { type: 'code', name: 'Component Library' }
      ],
      acceptanceCriteria: [
        'All screens implemented',
        'Responsive design working',
        'API integration complete',
        'Error states handled'
      ],
      requirementIds: spec.functional.map(r => r.id),
      artifacts: [],
      notes: ''
    });
    
    // AI integration (if needed)
    if (spec.technical.aiModels) {
      tasks.push({
        id: 'task-integrate-ai',
        title: 'Integrate AI Models',
        description: 'Integrate selected AI models and implement AI features',
        type: TaskType.IMPLEMENTATION,
        phase: ProjectPhase.DEVELOPMENT,
        priority: Priority.CRITICAL,
        status: TaskStatus.PENDING,
        assignedAgent: AgentType.CODING,
        estimatedEffort: 6,
        dependencies: ['task-research-ai-models', 'task-implement-backend'],
        blockedBy: [],
        blocks: ['task-test-ai-features'],
        deliverables: [
          { type: 'code', name: 'AI Integration Code' },
          { type: 'document', name: 'AI Model Configuration' }
        ],
        acceptanceCriteria: [
          'Models loading correctly',
          'Inference working',
          'Error handling for AI failures',
          'Performance acceptable'
        ],
        requirementIds: spec.functional
          .filter(r => r.category === 'ai-features')
          .map(r => r.id),
        artifacts: [],
        notes: ''
      });
    }
    
    return {
      name: 'Development',
      phase: ProjectPhase.DEVELOPMENT,
      tasks,
      estimatedDuration: tasks.reduce((sum, t) => sum + t.estimatedEffort, 0),
      status: 'pending'
    };
  }
  
  /**
   * Calculate critical path using PERT/CPM algorithm
   */
  private async calculateCriticalPath(tasks: Task[]): Promise<Task[]> {
    // Build dependency graph
    const graph = this.buildDependencyGraph(tasks);
    
    // Forward pass (calculate earliest start/finish)
    for (const task of tasks) {
      if (task.dependencies.length === 0) {
        task.earliestStart = 0;
      } else {
        const dependencyFinishes = task.dependencies.map(depId => {
          const dep = tasks.find(t => t.id === depId);
          return dep ? (dep.earliestFinish || 0) : 0;
        });
        task.earliestStart = Math.max(...dependencyFinishes);
      }
      task.earliestFinish = task.earliestStart + task.estimatedEffort;
    }
    
    // Backward pass (calculate latest start/finish)
    const projectEnd = Math.max(...tasks.map(t => t.earliestFinish || 0));
    for (let i = tasks.length - 1; i >= 0; i--) {
      const task = tasks[i];
      if (task.blocks.length === 0) {
        task.latestFinish = projectEnd;
      } else {
        const blockStarts = task.blocks.map(blockId => {
          const block = tasks.find(t => t.id === blockId);
          return block ? (block.latestStart || projectEnd) : projectEnd;
        });
        task.latestFinish = Math.min(...blockStarts);
      }
      task.latestStart = task.latestFinish - task.estimatedEffort;
    }
    
    // Identify critical path (tasks with zero slack)
    const criticalPath = tasks.filter(task => {
      const slack = (task.latestStart || 0) - (task.earliestStart || 0);
      task.slack = slack;
      return slack === 0;
    });
    
    return criticalPath.sort((a, b) => 
      (a.earliestStart || 0) - (b.earliestStart || 0)
    );
  }
  
  /**
   * Identify work that can be done in parallel
   */
  private async identifyParallelWork(tasks: Task[]): Promise<ParallelGroup[]> {
    const groups: ParallelGroup[] = [];
    const processed = new Set<string>();
    
    for (const task of tasks) {
      if (processed.has(task.id)) continue;
      
      // Find tasks that can run in parallel
      const parallel = tasks.filter(t => 
        t.id !== task.id &&
        !processed.has(t.id) &&
        !this.hasDependency(t, task, tasks) &&
        !this.hasDependency(task, t, tasks) &&
        this.canRunInParallel(t, task)
      );
      
      if (parallel.length > 0) {
        const group: ParallelGroup = {
          tasks: [task, ...parallel],
          estimatedDuration: Math.max(...[task, ...parallel].map(t => t.estimatedEffort)),
          sequentialDuration: [task, ...parallel].reduce((sum, t) => sum + t.estimatedEffort, 0),
          timeSaved: 0
        };
        group.timeSaved = group.sequentialDuration - group.estimatedDuration;
        
        groups.push(group);
        processed.add(task.id);
        parallel.forEach(t => processed.add(t.id));
      }
    }
    
    return groups.sort((a, b) => b.timeSaved - a.timeSaved);
  }
}
```

**Benefits:**
- ✅ **Automatic Decomposition**: Breaks down project into executable tasks
- ✅ **Dependency Analysis**: Identifies task dependencies automatically
- ✅ **Critical Path**: Calculates project timeline and critical tasks
- ✅ **Parallel Work**: Identifies tasks that can run simultaneously
- ✅ **Effort Estimation**: Estimates time for each task
- ✅ **Agent Assignment**: Assigns appropriate agent to each task

---

### 4.5 Deadline Management (Comprehensive)

The deadline management system tracks project timelines, allocates time across tasks, monitors progress, and dynamically adjusts priorities to meet user-specified deadlines.

---

#### **Deadline Management System**

```typescript
interface ProjectDeadline {
  id: string;
  projectId: string;
  deadline: Date;
  timezone: string;
  setAt: Date;
  source: 'user' | 'system';  // User-specified or system-generated
  
  // Time allocation
  totalAvailableHours: number;
  totalEstimatedHours: number;
  bufferHours: number;
  
  // Tracking
  hoursSpent: number;
  hoursRemaining: number;
  percentTimeUsed: number;
  percentWorkComplete: number;
  
  // Status
  status: 'on-track' | 'at-risk' | 'critical' | 'missed';
  urgencyLevel: number;  // 0-10
  
  // Milestones
  milestones: DeadlineMilestone[];
  
  // Adjustments
  adjustmentHistory: DeadlineAdjustment[];
}

interface DeadlineMilestone {
  id: string;
  name: string;
  targetTime: Date;
  actualTime?: Date;
  percentComplete: number;
  status: 'pending' | 'in-progress' | 'completed' | 'missed';
  tasksIncluded: string[];  // Task IDs
}

class DeadlineManager {
  private timeAllocator: TimeAllocator;
  private progressTracker: ProgressTracker;
  private urgencyCalculator: UrgencyCalculator;
  
  /**
   * Set project deadline
   */
  async setDeadline(
    projectId: string,
    deadline: Date,
    wbs: WorkBreakdownStructure
  ): Promise<ProjectDeadline> {
    const now = new Date();
    const totalAvailableMs = deadline.getTime() - now.getTime();
    const totalAvailableHours = totalAvailableMs / (1000 * 60 * 60);
    
    // Calculate buffer time (20% of available time or 2 hours, whichever is larger)
    const bufferHours = Math.max(2, totalAvailableHours * 0.2);
    
    // Check if deadline is feasible
    const totalEstimatedHours = wbs.totalEstimatedEffort;
    const feasibility = this.assessFeasibility(
      totalAvailableHours,
      totalEstimatedHours,
      bufferHours
    );
    
    if (!feasibility.isFeasible && feasibility.severity === 'impossible') {
      throw new Error(
        `Deadline is not feasible. Need ${totalEstimatedHours}h but only ${totalAvailableHours}h available. Minimum deadline: ${feasibility.minimumDeadline}`
      );
    }
    
    // Create deadline object
    const projectDeadline: ProjectDeadline = {
      id: generateUUID(),
      projectId,
      deadline,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      setAt: now,
      source: 'user',
      totalAvailableHours,
      totalEstimatedHours,
      bufferHours,
      hoursSpent: 0,
      hoursRemaining: totalAvailableHours,
      percentTimeUsed: 0,
      percentWorkComplete: 0,
      status: 'on-track',
      urgencyLevel: 0,
      milestones: await this.generateMilestones(wbs, deadline),
      adjustmentHistory: []
    };
    
    // Allocate time to tasks
    await this.allocateTimeToTasks(wbs.tasks, projectDeadline);
    
    // Send notification to user
    await this.notifyDeadlineSet(projectDeadline, feasibility);
    
    return projectDeadline;
  }
  
  /**
   * Assess deadline feasibility
   */
  private assessFeasibility(
    availableHours: number,
    estimatedHours: number,
    bufferHours: number
  ): FeasibilityAssessment {
    const workableHours = availableHours - bufferHours;
    const ratio = workableHours / estimatedHours;
    
    if (ratio < 0.5) {
      return {
        isFeasible: false,
        severity: 'impossible',
        message: 'Deadline is too tight. Not enough time even with scope reduction.',
        minimumDeadline: new Date(Date.now() + estimatedHours * 2 * 60 * 60 * 1000),
        recommendations: [
          'Extend deadline significantly',
          'Reduce scope by at least 50%'
        ]
      };
    }
    
    if (ratio < 0.8) {
      return {
        isFeasible: true,
        severity: 'challenging',
        message: 'Deadline is tight. Will require focused work and may need scope adjustments.',
        recommendations: [
          'Prioritize critical features only',
          'Consider extending deadline by a few hours',
          'Prepare for scope cuts if delays occur'
        ]
      };
    }
    
    if (ratio < 1.2) {
      return {
        isFeasible: true,
        severity: 'reasonable',
        message: 'Deadline is achievable with steady progress.',
        recommendations: [
          'Stay on track with tasks',
          'Monitor progress regularly'
        ]
      };
    }
    
    return {
      isFeasible: true,
      severity: 'comfortable',
      message: 'Plenty of time available for quality work and improvements.',
      recommendations: [
        'Focus on quality',
        'Add polish and extra features',
        'Thorough testing'
      ]
    };
  }
  
  /**
   * Generate milestones based on project phases
   */
  private async generateMilestones(
    wbs: WorkBreakdownStructure,
    deadline: Date
  ): Promise<DeadlineMilestone[]> {
    const milestones: DeadlineMilestone[] = [];
    const now = Date.now();
    const totalDuration = deadline.getTime() - now;
    
    // Calculate phase durations
    const phaseDurations = wbs.phases.map(phase => phase.estimatedDuration);
    const totalPhaseDuration = phaseDurations.reduce((sum, d) => sum + d, 0);
    
    // Generate milestone for each phase
    let cumulativeTime = 0;
    for (let i = 0; i < wbs.phases.length; i++) {
      const phase = wbs.phases[i];
      const phaseDuration = phase.estimatedDuration;
      const phaseTimeRatio = phaseDuration / totalPhaseDuration;
      const phaseTimeMs = totalDuration * phaseTimeRatio;
      
      cumulativeTime += phaseTimeMs;
      
      milestones.push({
        id: `milestone-${phase.name.toLowerCase()}`,
        name: `Complete ${phase.name} Phase`,
        targetTime: new Date(now + cumulativeTime),
        percentComplete: 0,
        status: 'pending',
        tasksIncluded: phase.tasks.map(t => t.id)
      });
    }
    
    return milestones;
  }
  
  /**
   * Allocate time to individual tasks
   */
  private async allocateTimeToTasks(
    tasks: Task[],
    deadline: ProjectDeadline
  ): Promise<void> {
    const now = new Date();
    const availableTimeMs = deadline.deadline.getTime() - now.getTime();
    const totalEstimatedHours = tasks.reduce((sum, t) => sum + t.estimatedEffort, 0);
    
    // Calculate time multiplier
    const timeMultiplier = (availableTimeMs / (1000 * 60 * 60)) / totalEstimatedHours;
    
    // Allocate time to each task based on dependency order
    const sorted = this.topologicalSort(tasks);
    let currentTime = now.getTime();
    
    for (const task of sorted) {
      task.plannedStart = new Date(currentTime);
      task.plannedEnd = new Date(
        currentTime + task.estimatedEffort * timeMultiplier * 60 * 60 * 1000
      );
      currentTime = task.plannedEnd.getTime();
    }
  }
  
  /**
   * Monitor deadline progress in real-time
   */
  async monitorProgress(
    projectId: string,
    deadline: ProjectDeadline
  ): Promise<void> {
    const interval = setInterval(async () => {
      // Update time remaining
      const now = Date.now();
      const remainingMs = deadline.deadline.getTime() - now;
      deadline.hoursRemaining = remainingMs / (1000 * 60 * 60);
      deadline.percentTimeUsed = 
        ((deadline.totalAvailableHours - deadline.hoursRemaining) / deadline.totalAvailableHours) * 100;
      
      // Calculate urgency level
      deadline.urgencyLevel = this.calculateUrgency(deadline);
      
      // Update status
      deadline.status = this.determineStatus(deadline);
      
      // Check milestones
      await this.checkMilestones(deadline);
      
      // Send updates if status changed
      if (deadline.status === 'at-risk' || deadline.status === 'critical') {
        await this.sendUrgencyAlert(projectId, deadline);
      }
      
      // Adjust priorities if needed
      if (deadline.urgencyLevel > 7) {
        await this.escalatePriorities(projectId, deadline);
      }
      
      // Stop monitoring if deadline passed or project complete
      if (remainingMs <= 0 || deadline.percentWorkComplete >= 100) {
        clearInterval(interval);
      }
    }, 60000);  // Check every minute
  }
  
  /**
   * Calculate urgency level (0-10 scale)
   */
  private calculateUrgency(deadline: ProjectDeadline): number {
    const timeProgress = deadline.percentTimeUsed;
    const workProgress = deadline.percentWorkComplete;
    
    // Ideal: work progress should match or exceed time progress
    const progressGap = timeProgress - workProgress;
    
    // Base urgency on progress gap
    let urgency = 0;
    
    if (progressGap < -20) {
      urgency = 0;  // Well ahead of schedule
    } else if (progressGap < 0) {
      urgency = 2;  // Ahead of schedule
    } else if (progressGap < 10) {
      urgency = 4;  // On track
    } else if (progressGap < 20) {
      urgency = 6;  // Slightly behind
    } else if (progressGap < 30) {
      urgency = 8;  // Behind schedule
    } else {
      urgency = 10;  // Critically behind
    }
    
    // Increase urgency as deadline approaches
    if (deadline.hoursRemaining < 2) {
      urgency = Math.max(urgency, 9);
    } else if (deadline.hoursRemaining < 6) {
      urgency = Math.max(urgency, 7);
    }
    
    return Math.min(10, urgency);
  }
  
  /**
   * Determine overall deadline status
   */
  private determineStatus(
    deadline: ProjectDeadline
  ): 'on-track' | 'at-risk' | 'critical' | 'missed' {
    if (deadline.hoursRemaining < 0) {
      return 'missed';
    }
    
    if (deadline.urgencyLevel >= 8) {
      return 'critical';
    }
    
    if (deadline.urgencyLevel >= 6) {
      return 'at-risk';
    }
    
    return 'on-track';
  }
  
  /**
   * Send urgency alert to user
   */
  private async sendUrgencyAlert(
    projectId: string,
    deadline: ProjectDeadline
  ): Promise<void> {
    const message = {
      type: 'agent',
      sender: 'PM Agent',
      content: this.formatUrgencyMessage(deadline),
      timestamp: new Date(),
      metadata: {
        urgency: deadline.urgencyLevel,
        status: deadline.status
      }
    };
    
    await chatService.sendMessage(projectId, message);
    
    // Also send notification
    await notificationService.send({
      projectId,
      type: 'deadline-alert',
      priority: 'high',
      title: 'Deadline Alert',
      body: `Project is ${deadline.status}. ${deadline.hoursRemaining.toFixed(1)} hours remaining.`
    });
  }
  
  /**
   * Format urgency message for chat
   */
  private formatUrgencyMessage(deadline: ProjectDeadline): string {
    const hoursRemaining = deadline.hoursRemaining.toFixed(1);
    const percentComplete = deadline.percentWorkComplete.toFixed(0);
    
    let message = '';
    
    if (deadline.status === 'critical') {
      message = `⚠️ **CRITICAL: Deadline Alert**\n\n`;
    } else if (deadline.status === 'at-risk') {
      message = `⚡ **WARNING: Project At Risk**\n\n`;
    }
    
    message += `**Time Remaining:** ${hoursRemaining} hours\n`;
    message += `**Work Complete:** ${percentComplete}%\n`;
    message += `**Status:** ${deadline.status.toUpperCase()}\n\n`;
    
    if (deadline.urgencyLevel >= 8) {
      message += `I'm prioritizing critical tasks and working as fast as possible. Some non-essential features may be delayed or removed to meet the deadline.\n\n`;
    }
    
    message += `**Next Milestone:** ${this.getNextMilestone(deadline)}\n`;
    
    return message.trim();
  }
  
  /**
   * Escalate task priorities as deadline approaches
   */
  private async escalatePriorities(
    projectId: string,
    deadline: ProjectDeadline
  ): Promise<void> {
    const tasks = await taskQueue.getProjectTasks(projectId);
    
    // Sort by criticality and dependency
    const criticalPath = tasks.filter(t => t.slack === 0);
    
    // Increase priority of critical path tasks
    for (const task of criticalPath) {
      if (task.status === 'pending' || task.status === 'ready') {
        task.priority = Priority.CRITICAL;
        await taskQueue.updateTask(task);
      }
    }
    
    // Deprioritize non-essential tasks
    const nonEssential = tasks.filter(t => 
      t.priority === 'low' || t.priority === 'medium'
    );
    
    for (const task of nonEssential) {
      if (task.status === 'pending') {
        task.status = TaskStatus.DEFERRED;
        await taskQueue.updateTask(task);
      }
    }
  }
}
```

**Benefits:**
- ✅ **Feasibility Assessment**: Validates if deadline is achievable
- ✅ **Automatic Time Allocation**: Distributes time across tasks
- ✅ **Real-Time Monitoring**: Tracks progress every minute
- ✅ **Urgency Calculation**: Dynamic priority adjustment
- ✅ **Milestone Tracking**: Phase-based progress checkpoints
- ✅ **Alert System**: Notifies user of deadline risks
- ✅ **Priority Escalation**: Increases task priorities as deadline nears

---

### 4.6 Agent Triggering (Comprehensive)

The agent triggering system orchestrates when and how specialized agents are activated to execute tasks, ensuring prerequisites are met and work flows smoothly.

---

#### **Agent Trigger System**

```typescript
interface TriggerConditions {
  // Prerequisites
  specificationComplete: boolean;
  dependenciesResolved: boolean;
  resourcesAvailable: boolean;
  approvalReceived: boolean;
  timeAvailable: boolean;
  
  // Context
  requiredContext: string[];
  availableContext: string[];
  
  // Constraints
  hardwareReady: boolean;
  thirdPartyAPIsConfigured: boolean;
  environmentSetup: boolean;
}

interface AgentTrigger {
  taskId: string;
  agentType: AgentType;
  trigger: {
    when: TriggerConditions;
    priority: Priority;
    deadline?: Date;
    retryPolicy: RetryPolicy;
  };
  context: AgentContext;
  execution: {
    canRunInParallel: boolean;
    mustRunSequentially: boolean;
    blockedBy: string[];
  };
}

class AgentTriggerOrchestrator {
  private conditionEvaluator: ConditionEvaluator;
  private contextBuilder: ContextBuilder;
  private parallelExecutor: ParallelExecutor;
  
  /**
   * Evaluate and trigger agents for ready tasks
   */
  async evaluateAndTrigger(projectId: string): Promise<void> {
    // 1. Get all pending/ready tasks
    const tasks = await taskQueue.getPendingTasks(projectId);
    
    // 2. Evaluate trigger conditions for each task
    const readyTasks: Task[] = [];
    for (const task of tasks) {
      const conditions = await this.evaluateTriggerConditions(task);
      if (conditions.allMet) {
        readyTasks.push(task);
      } else {
        // Log why task isn't ready
        await this.logBlockedReason(task, conditions);
      }
    }
    
    // 3. Group tasks by parallelization possibilities
    const groups = await this.groupForParallelExecution(readyTasks);
    
    // 4. Trigger agents
    for (const group of groups) {
      if (group.parallel) {
        // Trigger all in parallel
        await Promise.all(
          group.tasks.map(task => this.triggerAgent(task))
        );
      } else {
        // Trigger sequentially
        for (const task of group.tasks) {
          await this.triggerAgent(task);
        }
      }
    }
  }
  
  /**
   * Evaluate if all trigger conditions are met
   */
  private async evaluateTriggerConditions(
    task: Task
  ): Promise<{ allMet: boolean; details: Record<string, boolean> }> {
    const conditions: Record<string, boolean> = {};
    
    // 1. Check specification completeness
    conditions.specificationComplete = await this.checkSpecificationComplete(task);
    
    // 2. Check dependencies
    conditions.dependenciesResolved = await this.checkDependencies(task);
    
    // 3. Check resources
    conditions.resourcesAvailable = await this.checkResources(task);
    
    // 4. Check approval (if needed)
    conditions.approvalReceived = await this.checkApproval(task);
    
    // 5. Check time availability
    conditions.timeAvailable = await this.checkTimeAvailable(task);
    
    // 6. Check hardware (for AI tasks)
    if (task.type === TaskType.AI_INTEGRATION) {
      conditions.hardwareReady = await this.checkHardware(task);
    }
    
    // 7. Check environment setup
    conditions.environmentSetup = await this.checkEnvironment(task);
    
    const allMet = Object.values(conditions).every(v => v);
    
    return { allMet, details: conditions };
  }
  
  /**
   * Check if specification has enough detail for task
   */
  private async checkSpecificationComplete(task: Task): Promise<boolean> {
    const spec = await specService.getSpecification(task.projectId);
    
    // Get requirements related to this task
    const relatedReqs = spec.functional.filter(r => 
      task.requirementIds.includes(r.id)
    );
    
    // Check if all related requirements are complete
    return relatedReqs.every(req => 
      req.description.length >= 50 &&
      req.acceptanceCriteria.length >= 2 &&
      req.priority !== undefined
    );
  }
  
  /**
   * Check if all task dependencies are resolved
   */
  private async checkDependencies(task: Task): Promise<boolean> {
    if (task.dependencies.length === 0) {
      return true;
    }
    
    // Check if all dependency tasks are completed
    for (const depId of task.dependencies) {
      const depTask = await taskQueue.getTask(depId);
      if (!depTask || depTask.status !== TaskStatus.COMPLETED) {
        return false;
      }
    }
    
    return true;
  }
  
  /**
   * Check if required resources are available
   */
  private async checkResources(task: Task): Promise<boolean> {
    // Check agent availability
    const agent = await agentRegistry.getAgent(task.assignedAgent);
    if (!agent || agent.status !== 'available') {
      return false;
    }
    
    // Check if agent has capacity
    const currentLoad = await agentRegistry.getAgentLoad(task.assignedAgent);
    if (currentLoad.activeTasks >= currentLoad.maxConcurrent) {
      return false;
    }
    
    return true;
  }
  
  /**
   * Check if approval is needed and received
   */
  private async checkApproval(task: Task): Promise<boolean> {
    // Critical architectural decisions need user approval
    if (task.type === TaskType.ARCHITECTURE && task.priority === Priority.CRITICAL) {
      const approval = await approvalService.getApproval(task.id);
      return approval?.status === 'approved';
    }
    
    // Auto-approve non-critical tasks
    return true;
  }
  
  /**
   * Check if enough time before deadline
   */
  private async checkTimeAvailable(task: Task): Promise<boolean> {
    const deadline = await deadlineManager.getProjectDeadline(task.projectId);
    if (!deadline) {
      return true;  // No deadline, always enough time
    }
    
    const now = Date.now();
    const remainingMs = deadline.deadline.getTime() - now;
    const remainingHours = remainingMs / (1000 * 60 * 60);
    
    // Need at least 1.5x the estimated effort remaining
    return remainingHours >= task.estimatedEffort * 1.5;
  }
  
  /**
   * Trigger agent to execute task
   */
  private async triggerAgent(task: Task): Promise<void> {
    // 1. Build execution context
    const context = await this.buildExecutionContext(task);
    
    // 2. Update task status
    task.status = TaskStatus.ASSIGNED;
    task.actualStart = new Date();
    await taskQueue.updateTask(task);
    
    // 3. Send task to agent via message bus
    await messageBus.send({
      type: MessageType.TASK_ASSIGNMENT,
      from: AgentType.PM,
      to: task.assignedAgent,
      chainId: generateChainId(),
      priority: task.priority,
      payload: {
        task,
        context,
        deadline: task.plannedEnd
      }
    });
    
    // 4. Start monitoring task execution
    await this.monitorExecution(task);
    
    // 5. Notify user
    await this.notifyTaskStarted(task);
  }
  
  /**
   * Build execution context for agent
   */
  private async buildExecutionContext(task: Task): Promise<AgentContext> {
    const spec = await specService.getSpecification(task.projectId);
    const architecture = await architectureService.getArchitecture(task.projectId);
    
    // Get completed dependency artifacts
    const dependencyArtifacts: Artifact[] = [];
    for (const depId of task.dependencies) {
      const depTask = await taskQueue.getTask(depId);
      if (depTask) {
        dependencyArtifacts.push(...depTask.artifacts);
      }
    }
    
    return {
      projectId: task.projectId,
      taskId: task.id,
      specification: spec,
      architecture,
      requirements: spec.functional.filter(r => 
        task.requirementIds.includes(r.id)
      ),
      dependencyArtifacts,
      constraints: {
        deadline: task.plannedEnd,
        priority: task.priority,
        qualityLevel: this.determineQualityLevel(task)
      },
      environment: await this.getEnvironmentInfo(task),
      previousWork: await this.getPreviousWork(task)
    };
  }
  
  /**
   * Group tasks for parallel execution
   */
  private async groupForParallelExecution(
    tasks: Task[]
  ): Promise<ExecutionGroup[]> {
    const groups: ExecutionGroup[] = [];
    const processed = new Set<string>();
    
    for (const task of tasks) {
      if (processed.has(task.id)) continue;
      
      // Find tasks that can run in parallel with this one
      const parallelTasks = tasks.filter(t => 
        t.id !== task.id &&
        !processed.has(t.id) &&
        this.canRunInParallel(task, t) &&
        this.hasSameOrCompatibleAgents(task, t)
      );
      
      if (parallelTasks.length > 0) {
        // Create parallel execution group
        groups.push({
          parallel: true,
          tasks: [task, ...parallelTasks],
          estimatedDuration: Math.max(
            task.estimatedEffort,
            ...parallelTasks.map(t => t.estimatedEffort)
          )
        });
        
        processed.add(task.id);
        parallelTasks.forEach(t => processed.add(t.id));
      } else {
        // Single task group
        groups.push({
          parallel: false,
          tasks: [task],
          estimatedDuration: task.estimatedEffort
        });
        processed.add(task.id);
      }
    }
    
    return groups;
  }
  
  /**
   * Check if two tasks can run in parallel
   */
  private canRunInParallel(task1: Task, task2: Task): boolean {
    // Can't run in parallel if one depends on the other
    if (task1.dependencies.includes(task2.id) || 
        task2.dependencies.includes(task1.id)) {
      return false;
    }
    
    // Can't run in parallel if they modify the same files
    if (this.hasFileConflicts(task1, task2)) {
      return false;
    }
    
    // Backend and frontend can usually run in parallel
    if (task1.type === TaskType.BACKEND && task2.type === TaskType.FRONTEND) {
      return true;
    }
    
    // Different agents can work in parallel
    if (task1.assignedAgent !== task2.assignedAgent) {
      return true;
    }
    
    return false;
  }
  
  /**
   * Monitor task execution
   */
  private async monitorExecution(task: Task): Promise<void> {
    const checkInterval = setInterval(async () => {
      const updated = await taskQueue.getTask(task.id);
      
      if (!updated) {
        clearInterval(checkInterval);
        return;
      }
      
      // Check for timeout
      if (task.plannedEnd && Date.now() > task.plannedEnd.getTime()) {
        await this.handleTimeout(updated);
      }
      
      // Check for stuck task
      if (this.isStuck(updated)) {
        await this.handleStuckTask(updated);
      }
      
      // Stop monitoring if complete or failed
      if (updated.status === TaskStatus.COMPLETED || 
          updated.status === TaskStatus.FAILED) {
        clearInterval(checkInterval);
        
        // Trigger dependent tasks
        if (updated.status === TaskStatus.COMPLETED) {
          await this.triggerDependentTasks(updated);
        }
      }
    }, 30000);  // Check every 30 seconds
  }
}
```

**Benefits:**
- ✅ **Condition Validation**: Ensures all prerequisites met before triggering
- ✅ **Parallel Execution**: Triggers multiple agents simultaneously when safe
- ✅ **Context Building**: Provides agents with complete execution context
- ✅ **Resource Management**: Checks agent availability and capacity
- ✅ **Execution Monitoring**: Tracks task progress and handles issues
- ✅ **Automatic Retry**: Handles failures with retry policies

---

### 4.7 Continuous Improvement Loop (Comprehensive)

The continuous improvement system automatically identifies, prioritizes, and implements enhancements after the initial working version is complete, maximizing quality within deadline constraints.

---

#### **Continuous Improvement Engine**

```typescript
interface ImprovementOpportunity {
  id: string;
  category: ImprovementCategory;
  title: string;
  description: string;
  currentState: string;
  proposedState: string;
  
  // Impact assessment
  impact: {
    performance?: number;  // 0-100
    usability?: number;
    reliability?: number;
    maintainability?: number;
    overall: number;  // Weighted average
  };
  
  // Effort estimation
  estimatedEffort: number;  // hours
  complexity: 'low' | 'medium' | 'high';
  risk: 'low' | 'medium' | 'high';
  
  // Prioritization
  priority: Priority;
  impactEffortRatio: number;
  
  // Implementation
  assignedAgent: AgentType;
  status: 'identified' | 'approved' | 'in-progress' | 'completed' | 'skipped';
}

enum ImprovementCategory {
  PERFORMANCE = 'performance',
  UI_UX = 'ui_ux',
  CODE_QUALITY = 'code_quality',
  FEATURE_ENHANCEMENT = 'feature_enhancement',
  SECURITY = 'security',
  ACCESSIBILITY = 'accessibility',
  SEO = 'seo',
  TESTING = 'testing',
  DOCUMENTATION = 'documentation'
}

class ContinuousImprovementEngine {
  private reviewAgent: ReviewAgent;
  private prioritizer: ImprovementPrioritizer;
  private implementer: ImprovementImplementer;
  
  /**
   * Main improvement loop
   */
  async runImprovementCycle(projectId: string): Promise<void> {
    // 1. Wait for initial build to complete
    await this.waitForInitialBuild(projectId);
    
    // 2. Start improvement loop
    while (true) {
      // Check if we should continue improving
      const shouldContinue = await this.shouldContinueImproving(projectId);
      if (!shouldContinue) {
        break;
      }
      
      // 3. Identify improvement opportunities
      const opportunities = await this.identifyOpportunities(projectId);
      
      if (opportunities.length === 0) {
        // No more improvements possible
        break;
      }
      
      // 4. Prioritize opportunities
      const prioritized = await this.prioritizeOpportunities(
        opportunities,
        projectId
      );
      
      // 5. Select top improvements to implement
      const selected = await this.selectImprovements(prioritized, projectId);
      
      if (selected.length === 0) {
        // No improvements feasible within constraints
        break;
      }
      
      // 6. Implement improvements
      for (const improvement of selected) {
        await this.implementImprovement(improvement, projectId);
      }
      
      // 7. Validate improvements
      await this.validateImprovements(selected, projectId);
      
      // 8. Notify user of progress
      await this.notifyImprovements(selected, projectId);
    }
    
    // Final notification
    await this.notifyImprovementComplete(projectId);
  }
  
  /**
   * Identify improvement opportunities
   */
  private async identifyOpportunities(
    projectId: string
  ): Promise<ImprovementOpportunity[]> {
    const opportunities: ImprovementOpportunity[] = [];
    
    // 1. Performance analysis
    const perfOpportunities = await this.analyzePerformance(projectId);
    opportunities.push(...perfOpportunities);
    
    // 2. UI/UX analysis
    const uxOpportunities = await this.analyzeUIUX(projectId);
    opportunities.push(...uxOpportunities);
    
    // 3. Code quality analysis
    const codeOpportunities = await this.analyzeCodeQuality(projectId);
    opportunities.push(...codeOpportunities);
    
    // 4. Feature completeness analysis
    const featureOpportunities = await this.analyzeFeatures(projectId);
    opportunities.push(...featureOpportunities);
    
    // 5. Security analysis
    const securityOpportunities = await this.analyzeSecurity(projectId);
    opportunities.push(...securityOpportunities);
    
    // 6. Accessibility analysis
    const accessibilityOpportunities = await this.analyzeAccessibility(projectId);
    opportunities.push(...accessibilityOpportunities);
    
    return opportunities;
  }
  
  /**
   * Analyze performance and identify optimizations
   */
  private async analyzePerformance(
    projectId: string
  ): Promise<ImprovementOpportunity[]> {
    const opportunities: ImprovementOpportunity[] = [];
    
    // Get performance metrics
    const metrics = await performanceAnalyzer.analyze(projectId);
    
    // Database query optimization
    if (metrics.database.slowQueries.length > 0) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.PERFORMANCE,
        title: 'Optimize Database Queries',
        description: `${metrics.database.slowQueries.length} slow database queries detected`,
        currentState: `Queries taking ${metrics.database.avgQueryTime}ms average`,
        proposedState: 'Add indexes, optimize queries, implement caching',
        impact: {
          performance: 80,
          overall: 80
        },
        estimatedEffort: 2,
        complexity: 'medium',
        risk: 'low',
        priority: Priority.HIGH,
        impactEffortRatio: 40,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Frontend bundle size
    if (metrics.frontend.bundleSize > 500000) {  // > 500KB
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.PERFORMANCE,
        title: 'Reduce Frontend Bundle Size',
        description: 'Large bundle size affecting load time',
        currentState: `Bundle size: ${(metrics.frontend.bundleSize / 1024).toFixed(0)}KB`,
        proposedState: 'Code splitting, tree shaking, lazy loading',
        impact: {
          performance: 60,
          usability: 40,
          overall: 50
        },
        estimatedEffort: 1.5,
        complexity: 'low',
        risk: 'low',
        priority: Priority.MEDIUM,
        impactEffortRatio: 33,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Image optimization
    if (metrics.frontend.unoptimizedImages > 0) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.PERFORMANCE,
        title: 'Optimize Images',
        description: `${metrics.frontend.unoptimizedImages} unoptimized images found`,
        currentState: 'Large uncompressed images',
        proposedState: 'Compress, convert to WebP, add lazy loading',
        impact: {
          performance: 50,
          overall: 50
        },
        estimatedEffort: 1,
        complexity: 'low',
        risk: 'low',
        priority: Priority.MEDIUM,
        impactEffortRatio: 50,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Caching opportunities
    if (!metrics.backend.hasCaching) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.PERFORMANCE,
        title: 'Implement Response Caching',
        description: 'No caching layer detected',
        currentState: 'All requests hit database',
        proposedState: 'Add Redis caching for frequently accessed data',
        impact: {
          performance: 70,
          overall: 70
        },
        estimatedEffort: 3,
        complexity: 'medium',
        risk: 'medium',
        priority: Priority.HIGH,
        impactEffortRatio: 23,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    return opportunities;
  }
  
  /**
   * Analyze UI/UX and identify enhancements
   */
  private async analyzeUIUX(projectId: string): Promise<ImprovementOpportunity[]> {
    const opportunities: ImprovementOpportunity[] = [];
    
    const analysis = await uxAnalyzer.analyze(projectId);
    
    // Loading states
    if (!analysis.hasLoadingStates) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.UI_UX,
        title: 'Add Loading States',
        description: 'Missing loading indicators for async operations',
        currentState: 'No feedback during loading',
        proposedState: 'Add spinners, skeletons, progress indicators',
        impact: {
          usability: 70,
          overall: 70
        },
        estimatedEffort: 1.5,
        complexity: 'low',
        risk: 'low',
        priority: Priority.HIGH,
        impactEffortRatio: 47,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Error handling UI
    if (!analysis.hasErrorUI) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.UI_UX,
        title: 'Improve Error Messages',
        description: 'Generic or missing error messages',
        currentState: 'Technical error messages shown to users',
        proposedState: 'User-friendly error messages with actions',
        impact: {
          usability: 80,
          overall: 80
        },
        estimatedEffort: 2,
        complexity: 'low',
        risk: 'low',
        priority: Priority.HIGH,
        impactEffortRatio: 40,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Animations and transitions
    if (!analysis.hasAnimations) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.UI_UX,
        title: 'Add Animations & Transitions',
        description: 'No animations for smoother UX',
        currentState: 'Abrupt state changes',
        proposedState: 'Smooth transitions, micro-interactions',
        impact: {
          usability: 40,
          overall: 40
        },
        estimatedEffort: 2,
        complexity: 'low',
        risk: 'low',
        priority: Priority.LOW,
        impactEffortRatio: 20,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    // Mobile responsiveness
    if (analysis.responsiveScore < 90) {
      opportunities.push({
        id: generateUUID(),
        category: ImprovementCategory.UI_UX,
        title: 'Improve Mobile Responsiveness',
        description: `Responsive score: ${analysis.responsiveScore}/100`,
        currentState: 'Some layout issues on mobile',
        proposedState: 'Perfect mobile layout and touch interactions',
        impact: {
          usability: 85,
          overall: 85
        },
        estimatedEffort: 3,
        complexity: 'medium',
        risk: 'low',
        priority: Priority.HIGH,
        impactEffortRatio: 28,
        assignedAgent: AgentType.CODING,
        status: 'identified'
      });
    }
    
    return opportunities;
  }
  
  /**
   * Prioritize opportunities based on impact, effort, and constraints
   */
  private async prioritizeOpportunities(
    opportunities: ImprovementOpportunity[],
    projectId: string
  ): Promise<ImprovementOpportunity[]> {
    // Calculate impact/effort ratio for each
    opportunities.forEach(opp => {
      opp.impactEffortRatio = opp.impact.overall / opp.estimatedEffort;
    });
    
    // Get project constraints
    const deadline = await deadlineManager.getProjectDeadline(projectId);
    const timeRemaining = deadline ? deadline.hoursRemaining : Infinity;
    
    // Filter out opportunities that take too long
    const feasible = opportunities.filter(opp => 
      opp.estimatedEffort < timeRemaining * 0.3  // Use max 30% of remaining time per improvement
    );
    
    // Sort by priority, then impact/effort ratio
    feasible.sort((a, b) => {
      // Priority first
      const priorityOrder = {
        [Priority.CRITICAL]: 4,
        [Priority.HIGH]: 3,
        [Priority.MEDIUM]: 2,
        [Priority.LOW]: 1
      };
      
      const priorityDiff = priorityOrder[b.priority] - priorityOrder[a.priority];
      if (priorityDiff !== 0) return priorityDiff;
      
      // Then by impact/effort ratio
      return b.impactEffortRatio - a.impactEffortRatio;
    });
    
    return feasible;
  }
  
  /**
   * Select improvements to implement
   */
  private async selectImprovements(
    opportunities: ImprovementOpportunity[],
    projectId: string
  ): Promise<ImprovementOpportunity[]> {
    const selected: ImprovementOpportunity[] = [];
    const deadline = await deadlineManager.getProjectDeadline(projectId);
    const timeRemaining = deadline ? deadline.hoursRemaining : Infinity;
    
    let timeAllocated = 0;
    const maxTimeForImprovements = timeRemaining * 0.5;  // Use max 50% of remaining time
    
    for (const opp of opportunities) {
      if (timeAllocated + opp.estimatedEffort <= maxTimeForImprovements) {
        selected.push(opp);
        timeAllocated += opp.estimatedEffort;
      }
      
      // Stop after selecting 5 improvements
      if (selected.length >= 5) {
        break;
      }
    }
    
    return selected;
  }
  
  /**
   * Determine if improvement cycle should continue
   */
  private async shouldContinueImproving(projectId: string): Promise<boolean> {
    const deadline = await deadlineManager.getProjectDeadline(projectId);
    
    // Stop if deadline passed
    if (deadline && deadline.hoursRemaining <= 0) {
      return false;
    }
    
    // Stop if less than 1 hour remaining
    if (deadline && deadline.hoursRemaining < 1) {
      return false;
    }
    
    // Stop if project is at risk
    if (deadline && deadline.status === 'critical') {
      return false;
    }
    
    // Stop if build is failing
    const buildStatus = await buildService.getStatus(projectId);
    if (buildStatus.status === 'failing') {
      return false;
    }
    
    return true;
  }
  
  /**
   * Notify user of improvements
   */
  private async notifyImprovements(
    improvements: ImprovementOpportunity[],
    projectId: string
  ): Promise<void> {
    const message = {
      type: 'agent',
      sender: 'PM Agent',
      content: `
✨ **Improvements Completed**

I've made ${improvements.length} improvements to your application:

${improvements.map((imp, i) => `${i + 1}. **${imp.title}**\n   ${imp.description}`).join('\n\n')}

The application is now faster, more polished, and more reliable!
      `.trim(),
      timestamp: new Date()
    };
    
    await chatService.sendMessage(projectId, message);
  }
}
```

**Benefits:**
- ✅ **Automatic Identification**: Finds improvement opportunities automatically
- ✅ **Impact Analysis**: Measures improvement impact on performance, UX, etc.
- ✅ **Smart Prioritization**: Ranks by impact/effort ratio within time constraints
- ✅ **Iterative Enhancement**: Continues until deadline or no more improvements
- ✅ **Category Coverage**: Performance, UI/UX, code quality, security, accessibility
- ✅ **Time-Aware**: Respects deadline and only improves when feasible
- ✅ **User Notification**: Keeps user informed of improvements made

---

**Summary of Section 4 (Chat-first PM Implementation):**
- ✅ **4.0**: Complete chat interface architecture with React components
- ✅ **4.1**: NLP/LLM prompt processing with intent and entity extraction
- ✅ **4.2**: Adaptive requirements gathering with project-specific questions
- ✅ **4.3**: Specification building with validation and conflict resolution
- ✅ **4.4**: Work breakdown with dependency analysis and critical path
- ✅ **4.5**: Deadline management with urgency tracking and priority escalation
- ✅ **4.6**: Agent triggering with condition evaluation and parallel execution
- ✅ **4.7**: Continuous improvement loop with automatic optimization

---

---

## 5. Code Generation System Design

The code generation system automatically transforms visual workflows into production-ready, type-safe, and tested code across backend, frontend, and mobile platforms.

---

### 5.1 Node to Backend Function Mapping (Comprehensive)

The node-to-backend mapping system ensures every visual node has a corresponding backend service that can execute its logic safely and efficiently.

---

#### **Node Mapping Architecture**

```typescript
interface NodeMapping {
  // Node identification
  nodeType: string;
  category: string;
  version: string;
  
  // Backend mapping
  serviceClass: string;
  routePath: string;
  httpMethod: 'POST' | 'GET' | 'PUT' | 'DELETE';
  
  // Execution configuration
  execution: {
    timeout: number;
    retryPolicy: RetryPolicy;
    rateLimits: RateLimits;
    caching: CachingPolicy;
    authentication: AuthRequirement;
  };
  
  // Input/Output schema
  inputSchema: JSONSchema;
  outputSchema: JSONSchema;
  
  // Dependencies
  dependencies: {
    packages: string[];
    models?: string[];
    apis?: string[];
    hardware?: HardwareRequirement[];
  };
}

interface NodeService {
  // Service identification
  name: string;
  version: string;
  
  // Execution methods
  execute(input: any, context: ExecutionContext): Promise<any>;
  validate(input: any): ValidationResult;
  preCheck(context: ExecutionContext): Promise<PreCheckResult>;
  
  // Lifecycle hooks
  beforeExecute?(input: any, context: ExecutionContext): Promise<void>;
  afterExecute?(output: any, context: ExecutionContext): Promise<void>;
  onError?(error: Error, context: ExecutionContext): Promise<void>;
  
  // Metadata
  getMetadata(): ServiceMetadata;
  getHealthStatus(): ServiceHealth;
}

class NodeMappingEngine {
  private serviceRegistry: Map<string, NodeService>;
  private routeRegistry: Map<string, RouteConfig>;
  
  /**
   * Register node type with backend service
   */
  registerNodeMapping(
    nodeType: string,
    serviceClass: new () => NodeService,
    config: NodeMappingConfig
  ): void {
    // 1. Instantiate service
    const service = new serviceClass();
    
    // 2. Validate service implementation
    this.validateService(service);
    
    // 3. Register service
    this.serviceRegistry.set(nodeType, service);
    
    // 4. Generate and register routes
    const routes = this.generateRoutes(nodeType, service, config);
    routes.forEach(route => {
      this.routeRegistry.set(route.path, route);
      this.registerRouteWithFastify(route);
    });
    
    // 5. Initialize dependencies
    await this.initializeDependencies(config.dependencies);
  }
  
  /**
   * Generate backend routes for node type
   */
  private generateRoutes(
    nodeType: string,
    service: NodeService,
    config: NodeMappingConfig
  ): RouteConfig[] {
    const routes: RouteConfig[] = [];
    
    // Main execution route
    routes.push({
      path: `/api/nodes/${nodeType}/execute`,
      method: 'POST',
      handler: async (request, reply) => {
        return await this.handleExecution(service, request, reply);
      },
      schema: {
        body: config.inputSchema,
        response: {
          200: config.outputSchema,
          400: errorSchema,
          500: errorSchema
        }
      },
      preHandler: [
        authMiddleware,
        rateLimitMiddleware(config.execution.rateLimits),
        validationMiddleware(config.inputSchema)
      ]
    });
    
    // Validation route
    routes.push({
      path: `/api/nodes/${nodeType}/validate`,
      method: 'POST',
      handler: async (request, reply) => {
        const result = service.validate(request.body);
        return reply.send(result);
      },
      schema: {
        body: config.inputSchema,
        response: {
          200: validationResultSchema
        }
      }
    });
    
    // Pre-check route (hardware, dependencies, etc.)
    routes.push({
      path: `/api/nodes/${nodeType}/precheck`,
      method: 'POST',
      handler: async (request, reply) => {
        const context = await this.buildExecutionContext(request);
        const result = await service.preCheck(context);
        return reply.send(result);
      },
      schema: {
        response: {
          200: preCheckResultSchema
        }
      }
    });
    
    // Status/health route
    routes.push({
      path: `/api/nodes/${nodeType}/health`,
      method: 'GET',
      handler: async (request, reply) => {
        const health = service.getHealthStatus();
        return reply.send(health);
      }
    });
    
    return routes;
  }
  
  /**
   * Handle node execution with full lifecycle
   */
  private async handleExecution(
    service: NodeService,
    request: FastifyRequest,
    reply: FastifyReply
  ): Promise<any> {
    const executionId = generateUUID();
    const startTime = Date.now();
    
    try {
      // 1. Build execution context
      const context: ExecutionContext = await this.buildExecutionContext(request);
      context.executionId = executionId;
      
      // 2. Pre-execution hook
      if (service.beforeExecute) {
        await service.beforeExecute(request.body, context);
      }
      
      // 3. Execute node logic
      const output = await service.execute(request.body, context);
      
      // 4. Post-execution hook
      if (service.afterExecute) {
        await service.afterExecute(output, context);
      }
      
      // 5. Log execution metrics
      await this.logExecution({
        executionId,
        nodeType: service.name,
        duration: Date.now() - startTime,
        status: 'success',
        input: request.body,
        output
      });
      
      // 6. Return standardized response
      return reply.send({
        success: true,
        executionId,
        output,
        metadata: {
          duration: Date.now() - startTime,
          timestamp: new Date().toISOString()
        }
      });
      
    } catch (error) {
      // Handle error
      if (service.onError) {
        await service.onError(error, context);
      }
      
      // Log error
      await this.logExecution({
        executionId,
        nodeType: service.name,
        duration: Date.now() - startTime,
        status: 'error',
        error: error.message,
        stack: error.stack
      });
      
      // Return error response
      return reply.status(error.statusCode || 500).send({
        success: false,
        executionId,
        error: {
          message: error.message,
          code: error.code,
          details: error.details
        }
      });
    }
  }
  
  /**
   * Build execution context with all required information
   */
  private async buildExecutionContext(
    request: FastifyRequest
  ): Promise<ExecutionContext> {
    return {
      executionId: generateUUID(),
      userId: request.user?.id,
      projectId: request.body?.projectId,
      workflowId: request.body?.workflowId,
      nodeId: request.body?.nodeId,
      environment: process.env.NODE_ENV,
      timestamp: new Date(),
      
      // Hardware context
      hardware: await hardwareDetector.detect(),
      
      // User preferences
      preferences: await userPreferences.get(request.user?.id),
      
      // Previous node outputs (for chaining)
      previousOutputs: request.body?.previousOutputs || {},
      
      // Shared memory
      sharedMemory: await sharedMemory.get(request.body?.workflowId)
    };
  }
}

/**
 * Example: Text Processing Node Service
 */
class TextTransformService implements NodeService {
  name = 'text-transform';
  version = '1.0.0';
  
  /**
   * Execute text transformation
   */
  async execute(input: any, context: ExecutionContext): Promise<any> {
    const { text, operation } = input;
    
    let result: string;
    
    switch (operation) {
      case 'uppercase':
        result = text.toUpperCase();
        break;
        
      case 'lowercase':
        result = text.toLowerCase();
        break;
        
      case 'capitalize':
        result = this.capitalize(text);
        break;
        
      case 'reverse':
        result = text.split('').reverse().join('');
        break;
        
      case 'trim':
        result = text.trim();
        break;
        
      default:
        throw new Error(`Unknown operation: ${operation}`);
    }
    
    return {
      originalText: text,
      transformedText: result,
      operation,
      length: result.length
    };
  }
  
  /**
   * Validate input
   */
  validate(input: any): ValidationResult {
    const errors: string[] = [];
    
    if (!input.text) {
      errors.push('text is required');
    } else if (typeof input.text !== 'string') {
      errors.push('text must be a string');
    }
    
    if (!input.operation) {
      errors.push('operation is required');
    } else if (!['uppercase', 'lowercase', 'capitalize', 'reverse', 'trim'].includes(input.operation)) {
      errors.push(`Invalid operation: ${input.operation}`);
    }
    
    return {
      valid: errors.length === 0,
      errors
    };
  }
  
  /**
   * Pre-execution check
   */
  async preCheck(context: ExecutionContext): Promise<PreCheckResult> {
    // No special requirements for text transformation
    return {
      ready: true,
      checks: {
        dependencies: { status: 'ok' },
        hardware: { status: 'ok' },
        permissions: { status: 'ok' }
      }
    };
  }
  
  /**
   * Get service metadata
   */
  getMetadata(): ServiceMetadata {
    return {
      name: this.name,
      version: this.version,
      description: 'Transform text using various operations',
      operations: ['uppercase', 'lowercase', 'capitalize', 'reverse', 'trim'],
      inputSchema: {
        type: 'object',
        required: ['text', 'operation'],
        properties: {
          text: { type: 'string' },
          operation: { type: 'string', enum: ['uppercase', 'lowercase', 'capitalize', 'reverse', 'trim'] }
        }
      },
      outputSchema: {
        type: 'object',
        properties: {
          originalText: { type: 'string' },
          transformedText: { type: 'string' },
          operation: { type: 'string' },
          length: { type: 'number' }
        }
      }
    };
  }
  
  /**
   * Get health status
   */
  getHealthStatus(): ServiceHealth {
    return {
      status: 'healthy',
      uptime: process.uptime(),
      lastCheck: new Date()
    };
  }
  
  private capitalize(text: string): string {
    return text.split(' ').map(word => 
      word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    ).join(' ');
  }
}

/**
 * One-Line Workflow Execution API
 */
class WorkflowExecutor {
  /**
   * Execute entire workflow with simple API
   */
  async run(
    workflowName: string,
    input: any,
    options?: ExecutionOptions
  ): Promise<WorkflowResult> {
    // 1. Load workflow definition
    const workflow = await workflowRegistry.get(workflowName);
    
    // 2. Resolve dependencies automatically
    await this.resolveDependencies(workflow);
    
    // 3. Execute workflow
    const result = await this.executeWorkflow(workflow, input, options);
    
    return result;
  }
  
  /**
   * Resolve all workflow dependencies
   */
  private async resolveDependencies(workflow: Workflow): Promise<void> {
    // Check and install packages
    for (const pkg of workflow.dependencies.packages) {
      if (!await packageManager.isInstalled(pkg)) {
        console.log(`Installing package: ${pkg}`);
        await packageManager.install(pkg);
      }
    }
    
    // Download and load AI models
    for (const model of workflow.dependencies.models || []) {
      if (!await modelManager.isDownloaded(model)) {
        console.log(`Downloading model: ${model}`);
        await modelManager.download(model, {
          onProgress: (progress) => console.log(`Progress: ${progress}%`)
        });
      }
    }
    
    // Verify API keys
    for (const api of workflow.dependencies.apis || []) {
      if (!await apiKeyManager.hasKey(api)) {
        throw new Error(`Missing API key for: ${api}`);
      }
    }
  }
}
```

**Benefits:**
- ✅ **Automatic Mapping**: Visual nodes automatically map to backend services
- ✅ **Type Safety**: Full TypeScript type checking for inputs/outputs
- ✅ **Standard Routes**: Consistent REST API endpoints for all nodes
- ✅ **Lifecycle Hooks**: Before/after execution hooks for custom logic
- ✅ **Error Handling**: Comprehensive error handling and logging
- ✅ **One-Line Execution**: Simple `flow.run()` API for developers
- ✅ **Dependency Resolution**: Automatic installation and configuration

---

### 5.2 Backend Route Generation (Comprehensive)

The route generation system automatically creates REST API endpoints for all nodes, complete with authentication, validation, rate limiting, and error handling.

---

#### **Dynamic Route Generation**

```typescript
interface RouteConfig {
  path: string;
  method: HTTPMethod;
  handler: RouteHandler;
  schema?: RouteSchema;
  preHandler?: PreHandler[];
  config?: RouteOptions;
}

interface RouteSchema {
  body?: JSONSchema;
  querystring?: JSONSchema;
  params?: JSONSchema;
  response?: Record<number, JSONSchema>;
  headers?: JSONSchema;
}

class RouteGenerator {
  private fastify: FastifyInstance;
  private templateEngine: TemplateEngine;
  
  /**
   * Generate routes from node schema
   */
  async generateRoutesFromSchema(
    nodeSchema: NodeSchema
  ): Promise<GeneratedRoutes> {
    const routes: RouteConfig[] = [];
    
    // 1. Generate execution route
    routes.push(this.generateExecutionRoute(nodeSchema));
    
    // 2. Generate validation route
    routes.push(this.generateValidationRoute(nodeSchema));
    
    // 3. Generate status route
    routes.push(this.generateStatusRoute(nodeSchema));
    
    // 4. Generate configuration route
    routes.push(this.generateConfigRoute(nodeSchema));
    
    // 5. Generate health check route
    routes.push(this.generateHealthRoute(nodeSchema));
    
    // 6. Register all routes with Fastify
    for (const route of routes) {
      await this.registerRoute(route);
    }
    
    return {
      nodeType: nodeSchema.type,
      routes,
      baseUrl: `/api/nodes/${nodeSchema.type}`
    };
  }
  
  /**
   * Generate execution route
   */
  private generateExecutionRoute(schema: NodeSchema): RouteConfig {
    return {
      path: `/api/nodes/${schema.type}/execute`,
      method: 'POST',
      handler: this.createExecutionHandler(schema),
      schema: {
        body: this.convertToJSONSchema(schema.inputs),
        response: {
          200: this.convertToJSONSchema(schema.outputs),
          400: errorResponseSchema,
          401: unauthorizedSchema,
          429: rateLimitSchema,
          500: internalErrorSchema
        },
        tags: [schema.category, schema.type],
        description: schema.description,
        summary: `Execute ${schema.label} node`
      },
      preHandler: [
        this.authenticationMiddleware,
        this.rateLimitMiddleware(schema.rateLimits),
        this.validationMiddleware,
        this.quotaCheckMiddleware
      ],
      config: {
        timeout: schema.timeout || 30000,
        rateLimit: schema.rateLimits,
        cache: schema.caching
      }
    };
  }
  
  /**
   * Create execution handler from template
   */
  private createExecutionHandler(schema: NodeSchema): RouteHandler {
    return async (request: FastifyRequest, reply: FastifyReply) => {
      const executionId = generateUUID();
      const startTime = Date.now();
      
      try {
        // 1. Extract and validate input
        const input = request.body as any;
        const userId = request.user.id;
        const projectId = input.projectId;
        
        // 2. Create execution context
        const context: ExecutionContext = {
          executionId,
          userId,
          projectId,
          nodeType: schema.type,
          timestamp: new Date(),
          environment: process.env.NODE_ENV || 'development'
        };
        
        // 3. Log execution start
        await executionLogger.log({
          executionId,
          nodeType: schema.type,
          userId,
          status: 'started',
          timestamp: new Date()
        });
        
        // 4. Execute node service
        const service = serviceRegistry.get(schema.type);
        if (!service) {
          throw new NodeServiceNotFoundError(schema.type);
        }
        
        const output = await service.execute(input, context);
        
        // 5. Log execution completion
        await executionLogger.log({
          executionId,
          nodeType: schema.type,
          userId,
          status: 'completed',
          duration: Date.now() - startTime,
          timestamp: new Date()
        });
        
        // 6. Update usage metrics
        await metricsService.recordExecution({
          userId,
          nodeType: schema.type,
          duration: Date.now() - startTime,
          success: true
        });
        
        // 7. Return response
        return reply.code(200).send({
          success: true,
          executionId,
          output,
          metadata: {
            duration: Date.now() - startTime,
            nodeType: schema.type,
            timestamp: new Date().toISOString()
          }
        });
        
      } catch (error) {
        // Handle execution error
        await executionLogger.log({
          executionId,
          nodeType: schema.type,
          status: 'failed',
          error: error.message,
          stack: error.stack,
          duration: Date.now() - startTime,
          timestamp: new Date()
        });
        
        // Determine error status code
        const statusCode = this.getErrorStatusCode(error);
        
        return reply.code(statusCode).send({
          success: false,
          executionId,
          error: {
            code: error.code || 'EXECUTION_ERROR',
            message: error.message,
            details: error.details || {}
          }
        });
      }
    };
  }
  
  /**
   * Generate route handler code as TypeScript file
   */
  async generateRouteHandlerFile(
    schema: NodeSchema,
    outputPath: string
  ): Promise<string> {
    const template = await this.templateEngine.load('route-handler.hbs');
    
    const code = template.render({
      nodeType: schema.type,
      label: schema.label,
      category: schema.category,
      inputs: schema.inputs,
      outputs: schema.outputs,
      serviceClass: this.generateServiceClassName(schema.type),
      hasAuthentication: true,
      hasRateLimit: !!schema.rateLimits,
      hasValidation: true,
      timeout: schema.timeout || 30000
    });
    
    // Format generated code
    const formatted = await this.formatCode(code);
    
    // Write to file
    await fs.writeFile(outputPath, formatted, 'utf-8');
    
    return outputPath;
  }
  
  /**
   * Register route with Fastify
   */
  private async registerRoute(route: RouteConfig): Promise<void> {
    this.fastify.route({
      method: route.method,
      url: route.path,
      handler: route.handler,
      schema: route.schema,
      preHandler: route.preHandler,
      config: route.config
    });
    
    console.log(`✓ Registered route: ${route.method} ${route.path}`);
  }
  
  /**
   * Generate authentication middleware
   */
  private authenticationMiddleware: PreHandler = async (request, reply) => {
    const token = request.headers.authorization?.replace('Bearer ', '');
    
    if (!token) {
      return reply.code(401).send({
        error: 'Unauthorized',
        message: 'Missing authentication token'
      });
    }
    
    try {
      const decoded = await jwtService.verify(token);
      request.user = decoded;
    } catch (error) {
      return reply.code(401).send({
        error: 'Unauthorized',
        message: 'Invalid or expired token'
      });
    }
  };
  
  /**
   * Generate rate limiting middleware
   */
  private rateLimitMiddleware(limits?: RateLimits): PreHandler {
    if (!limits) {
      // Default rate limits
      limits = {
        max: 100,
        timeWindow: '1 minute'
      };
    }
    
    return async (request, reply) => {
      const userId = request.user?.id;
      const key = `rate-limit:${userId}:${request.url}`;
      
      const count = await redis.incr(key);
      
      if (count === 1) {
        await redis.expire(key, this.parseTimeWindow(limits.timeWindow));
      }
      
      if (count > limits.max) {
        return reply.code(429).send({
          error: 'Too Many Requests',
          message: `Rate limit exceeded. Max ${limits.max} requests per ${limits.timeWindow}`,
          retryAfter: await redis.ttl(key)
        });
      }
      
      // Add rate limit headers
      reply.header('X-RateLimit-Limit', limits.max);
      reply.header('X-RateLimit-Remaining', Math.max(0, limits.max - count));
      reply.header('X-RateLimit-Reset', await redis.ttl(key));
    };
  }
}

/**
 * Route Template System
 */
class RouteTemplateEngine {
  /**
   * Handlebars template for route handler
   */
  private routeHandlerTemplate = `
import { FastifyRequest, FastifyReply } from 'fastify';
import { {{serviceClass}} } from '../services/{{serviceFile}}';
import { ExecutionContext } from '../types';
import { generateUUID } from '../utils';

/**
 * {{label}} Route Handler
 * Category: {{category}}
 * Auto-generated on {{generatedAt}}
 */
export async function {{handlerName}}(
  request: FastifyRequest,
  reply: FastifyReply
): Promise<void> {
  const executionId = generateUUID();
  const startTime = Date.now();
  
  try {
    // Extract input from request body
    const input = request.body as {{inputType}};
    
    // Build execution context
    const context: ExecutionContext = {
      executionId,
      userId: request.user.id,
      projectId: input.projectId,
      nodeType: '{{nodeType}}',
      timestamp: new Date(),
      environment: process.env.NODE_ENV
    };
    
    // Execute service
    const service = new {{serviceClass}}();
    const output = await service.execute(input, context);
    
    // Return success response
    return reply.code(200).send({
      success: true,
      executionId,
      output,
      metadata: {
        duration: Date.now() - startTime,
        nodeType: '{{nodeType}}',
        timestamp: new Date().toISOString()
      }
    });
    
  } catch (error) {
    // Handle error
    return reply.code(error.statusCode || 500).send({
      success: false,
      executionId,
      error: {
        code: error.code || 'EXECUTION_ERROR',
        message: error.message
      }
    });
  }
}

/**
 * Route configuration
 */
export const {{configName}} = {
  method: 'POST' as const,
  url: '/api/nodes/{{nodeType}}/execute',
  handler: {{handlerName}},
  schema: {
    body: {{inputSchemaJSON}},
    response: {
      200: {{outputSchemaJSON}}
    }
  },
  {{#if hasAuthentication}}
  preHandler: [authMiddleware, rateLimitMiddleware],
  {{/if}}
  config: {
    timeout: {{timeout}},
    rateLimit: {{rateLimitConfig}}
  }
};
  `.trim();
  
  /**
   * Render template with data
   */
  render(template: string, data: any): string {
    const handlebars = require('handlebars');
    const compiled = handlebars.compile(template);
    return compiled(data);
  }
}
```

**Benefits:**
- ✅ **Automatic Generation**: Routes auto-generated from node schemas
- ✅ **Consistent API**: All routes follow same patterns and conventions
- ✅ **Type Safety**: Full TypeScript typing for all routes
- ✅ **Built-in Security**: Authentication, rate limiting, validation included
- ✅ **Error Handling**: Comprehensive error handling and logging
- ✅ **Code Templates**: Generate readable, maintainable route handler code
- ✅ **Documentation**: Auto-generated API documentation with schemas

---

### 5.3 Frontend Component Scaffolding (Comprehensive)

The frontend scaffolding system automatically generates React components for each node type, complete with configuration panels, validation, state management, and AI-assisted code editing.

---

#### **Component Generation System**

```typescript
interface ComponentScaffold {
  // Component metadata
  name: string;
  nodeType: string;
  category: string;
  
  // Component files
  files: {
    component: string;      // Main React component
    styles: string;         // CSS/styled-components
    types: string;          // TypeScript interfaces
    config: string;         // Configuration panel
    hooks: string;          // Custom hooks
    utils: string;          // Utility functions
  };
  
  // Component structure
  structure: {
    props: ComponentProps;
    state: ComponentState;
    hooks: ComponentHooks;
    handlers: EventHandlers;
  };
}

class ComponentScaffolder {
  private templateEngine: TemplateEngine;
  private codeGenerator: AICodeGenerator;
  
  /**
   * Generate complete React component from node schema
   */
  async generateComponent(
    schema: NodeSchema
  ): Promise<ComponentScaffold> {
    // 1. Generate component types
    const types = await this.generateTypes(schema);
    
    // 2. Generate main component
    const component = await this.generateMainComponent(schema, types);
    
    // 3. Generate configuration panel
    const config = await this.generateConfigPanel(schema);
    
    // 4. Generate custom hooks
    const hooks = await this.generateHooks(schema);
    
    // 5. Generate styles
    const styles = await this.generateStyles(schema);
    
    // 6. Generate utilities
    const utils = await this.generateUtils(schema);
    
    return {
      name: this.getComponentName(schema.type),
      nodeType: schema.type,
      category: schema.category,
      files: {
        component,
        styles,
        types,
        config,
        hooks,
        utils
      },
      structure: {
        props: this.extractProps(schema),
        state: this.extractState(schema),
        hooks: this.extractHooks(schema),
        handlers: this.extractHandlers(schema)
      }
    };
  }
  
  /**
   * Generate TypeScript interfaces for component
   */
  private async generateTypes(schema: NodeSchema): Promise<string> {
    const template = `
import { Node, NodeProps } from 'reactflow';

/**
 * ${schema.label} Node Data
 */
export interface ${this.getComponentName(schema.type)}Data {
  ${schema.inputs.map(input => `
  // ${input.description || input.label}
  ${input.name}: ${this.mapToTypeScript(input.type)};
  `).join('\n')}
  
  // Output data
  output?: {
    ${schema.outputs.map(output => `
    ${output.name}: ${this.mapToTypeScript(output.type)};
    `).join('\n')}
  };
  
  // Execution state
  status?: 'idle' | 'running' | 'success' | 'error';
  error?: string;
}

/**
 * ${schema.label} Node Props
 */
export interface ${this.getComponentName(schema.type)}Props extends NodeProps {
  data: ${this.getComponentName(schema.type)}Data;
}

/**
 * ${schema.label} Configuration Props
 */
export interface ${this.getComponentName(schema.type)}ConfigProps {
  nodeId: string;
  data: ${this.getComponentName(schema.type)}Data;
  onUpdate: (data: Partial<${this.getComponentName(schema.type)}Data>) => void;
  onClose: () => void;
}
    `.trim();
    
    return await this.formatCode(template);
  }
  
  /**
   * Generate main React component
   */
  private async generateMainComponent(
    schema: NodeSchema,
    types: string
  ): Promise<string> {
    const componentName = this.getComponentName(schema.type);
    
    const template = `
import React, { useState, useCallback, useEffect } from 'react';
import { Handle, Position } from 'reactflow';
import { ${componentName}Props, ${componentName}Data } from './types';
import { ${componentName}Config } from './config';
import { useNodeExecution } from '../../hooks/useNodeExecution';
import { IconComponent } from '../icons';
import './styles.css';

/**
 * ${schema.label} Node Component
 * ${schema.description || ''}
 * 
 * Category: ${schema.category}
 * Auto-generated on ${new Date().toISOString()}
 */
export const ${componentName}: React.FC<${componentName}Props> = ({ 
  id, 
  data, 
  selected 
}) => {
  const [showConfig, setShowConfig] = useState(false);
  const { execute, status, output, error } = useNodeExecution(id);
  
  /**
   * Handle node execution
   */
  const handleExecute = useCallback(async () => {
    try {
      const result = await execute({
        nodeType: '${schema.type}',
        input: data
      });
      
      // Update node data with output
      if (result.output) {
        // Emit event to update node data
        window.dispatchEvent(new CustomEvent('node-output-updated', {
          detail: {
            nodeId: id,
            output: result.output
          }
        }));
      }
    } catch (err) {
      console.error('Node execution failed:', err);
    }
  }, [id, data, execute]);
  
  /**
   * Validate node configuration
   */
  const isValid = useCallback(() => {
    ${schema.inputs.filter(i => i.required).map(input => `
    if (!data.${input.name}) return false;
    `).join('\n')}
    return true;
  }, [data]);
  
  /**
   * Get status color
   */
  const getStatusColor = () => {
    switch (status) {
      case 'running': return '#3b82f6';  // blue
      case 'success': return '#10b981';  // green
      case 'error': return '#ef4444';    // red
      default: return '#6b7280';         // gray
    }
  };
  
  return (
    <>
      <div 
        className={\`node-container \${selected ? 'selected' : ''} \${status}\`}
        style={{ borderColor: getStatusColor() }}
      >
        {/* Node Header */}
        <div className="node-header">
          <IconComponent name="${schema.icon || 'default'}" />
          <span className="node-title">${schema.label}</span>
          <button 
            className="config-button"
            onClick={() => setShowConfig(true)}
            aria-label="Configure node"
          >
            ⚙️
          </button>
        </div>
        
        {/* Node Body */}
        <div className="node-body">
          {/* Input Summary */}
          <div className="input-summary">
            ${schema.inputs.slice(0, 2).map(input => `
            <div className="input-field">
              <label>${input.label}</label>
              <span className="input-value">
                {data.${input.name} || 'Not set'}
              </span>
            </div>
            `).join('\n')}
          </div>
          
          {/* Status Indicator */}
          {status && (
            <div className={\`status-indicator \${status}\`}>
              {status === 'running' && <div className="spinner" />}
              {status === 'success' && '✓'}
              {status === 'error' && '✗'}
              <span>{status}</span>
            </div>
          )}
          
          {/* Error Message */}
          {error && (
            <div className="error-message">
              {error}
            </div>
          )}
        </div>
        
        {/* Input Handles */}
        ${schema.inputs.filter(i => i.connection).map((input, idx) => `
        <Handle
          type="target"
          position={Position.Left}
          id="${input.name}"
          style={{ top: ${20 + idx * 20} }}
          title="${input.label}"
        />
        `).join('\n')}
        
        {/* Output Handles */}
        ${schema.outputs.map((output, idx) => `
        <Handle
          type="source"
          position={Position.Right}
          id="${output.name}"
          style={{ top: ${20 + idx * 20} }}
          title="${output.label}"
        />
        `).join('\n')}
      </div>
      
      {/* Configuration Panel */}
      {showConfig && (
        <${componentName}Config
          nodeId={id}
          data={data}
          onUpdate={(updates) => {
            // Emit event to update node data
            window.dispatchEvent(new CustomEvent('node-data-updated', {
              detail: {
                nodeId: id,
                data: { ...data, ...updates }
              }
            }));
          }}
          onClose={() => setShowConfig(false)}
        />
      )}
    </>
  );
};
    `.trim();
    
    return await this.formatCode(template);
  }
  
  /**
   * Generate configuration panel component
   */
  private async generateConfigPanel(schema: NodeSchema): Promise<string> {
    const componentName = this.getComponentName(schema.type);
    
    const template = `
import React, { useState } from 'react';
import { ${componentName}ConfigProps } from './types';
import { Modal, Button, Input, Select, Checkbox } from '../../ui';

/**
 * ${schema.label} Configuration Panel
 */
export const ${componentName}Config: React.FC<${componentName}ConfigProps> = ({
  nodeId,
  data,
  onUpdate,
  onClose
}) => {
  const [formData, setFormData] = useState(data);
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  /**
   * Validate form
   */
  const validate = (): boolean => {
    const newErrors: Record<string, string> = {};
    
    ${schema.inputs.filter(i => i.required).map(input => `
    if (!formData.${input.name}) {
      newErrors.${input.name} = '${input.label} is required';
    }
    `).join('\n')}
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
  
  /**
   * Handle save
   */
  const handleSave = () => {
    if (validate()) {
      onUpdate(formData);
      onClose();
    }
  };
  
  return (
    <Modal
      title="${schema.label} Configuration"
      onClose={onClose}
      width="600px"
    >
      <div className="config-form">
        ${schema.inputs.map(input => this.generateInputField(input)).join('\n')}
        
        <div className="form-actions">
          <Button variant="secondary" onClick={onClose}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleSave}>
            Save
          </Button>
        </div>
      </div>
    </Modal>
  );
};
    `.trim();
    
    return await this.formatCode(template);
  }
  
  /**
   * Generate input field based on type
   */
  private generateInputField(input: NodeInput): string {
    switch (input.type) {
      case 'string':
      case 'text':
        return `
        <Input
          label="${input.label}"
          value={formData.${input.name} || ''}
          onChange={(value) => setFormData({ ...formData, ${input.name}: value })}
          placeholder="${input.placeholder || ''}"
          required={${input.required}}
          error={errors.${input.name}}
          helperText="${input.description || ''}"
        />
        `;
        
      case 'number':
        return `
        <Input
          type="number"
          label="${input.label}"
          value={formData.${input.name} || 0}
          onChange={(value) => setFormData({ ...formData, ${input.name}: Number(value) })}
          required={${input.required}}
          error={errors.${input.name}}
        />
        `;
        
      case 'boolean':
        return `
        <Checkbox
          label="${input.label}"
          checked={formData.${input.name} || false}
          onChange={(checked) => setFormData({ ...formData, ${input.name}: checked })}
          helperText="${input.description || ''}"
        />
        `;
        
      case 'select':
        return `
        <Select
          label="${input.label}"
          value={formData.${input.name}}
          onChange={(value) => setFormData({ ...formData, ${input.name}: value })}
          options={${JSON.stringify(input.options || [])}}
          required={${input.required}}
          error={errors.${input.name}}
        />
        `;
        
      default:
        return `
        <Input
          label="${input.label}"
          value={formData.${input.name}}
          onChange={(value) => setFormData({ ...formData, ${input.name}: value })}
          required={${input.required}}
        />
        `;
    }
  }
}

/**
 * Custom Code Node with AI Assistance
 */
class CustomCodeNodeGenerator {
  /**
   * Generate custom code node with AI assistance
   */
  async generateCustomCodeNode(
    language: 'python' | 'javascript',
    prompt: string,
    context: ProjectContext
  ): Promise<CustomCodeNode> {
    // Use AI to generate code
    const code = await aiCodeGenerator.generate({
      language,
      prompt,
      context,
      style: 'production-ready',
      includeTests: true,
      includeDocumentation: true
    });
    
    // Validate syntax
    const validation = await this.validateSyntax(code, language);
    if (!validation.valid) {
      throw new Error(`Generated code has syntax errors: ${validation.errors.join(', ')}`);
    }
    
    // Generate sandboxed execution wrapper
    const wrapper = await this.generateSandbox(code, language);
    
    return {
      id: generateUUID(),
      language,
      code,
      wrapper,
      validated: true,
      createdAt: new Date()
    };
  }
  
  /**
   * Validate code syntax
   */
  private async validateSyntax(
    code: string,
    language: string
  ): Promise<ValidationResult> {
    switch (language) {
      case 'javascript':
      case 'typescript':
        return await this.validateJavaScript(code);
        
      case 'python':
        return await this.validatePython(code);
        
      default:
        return { valid: true, errors: [] };
    }
  }
}
```

**Benefits:**
- ✅ **Automatic Generation**: Complete React components from schemas
- ✅ **Type Safety**: Full TypeScript interfaces and type checking
- ✅ **Configuration Panels**: Auto-generated config UI for each node
- ✅ **State Management**: Built-in state handling and validation
- ✅ **Custom Code Nodes**: AI-assisted Python/JavaScript blocks
- ✅ **Sandboxed Execution**: Safe execution of custom code
- ✅ **Visual Consistency**: All nodes follow same design patterns

---

### 5.4 Visual-to-Code Parity (Comprehensive)

The visual-to-code parity system enables seamless bidirectional synchronization between the visual workflow editor and executable code, allowing both developers and non-developers to work in their preferred mode.

---

#### **Bidirectional Synchronization**

```typescript
interface CodeSyncEngine {
  // Sync direction
  direction: 'visual-to-code' | 'code-to-visual' | 'bidirectional';
  
  // Sync mode
  mode: 'real-time' | 'on-save' | 'on-demand';
  
  // Code representation
  codeFormat: 'typescript' | 'javascript' | 'python';
  
  // Sync state
  inSync: boolean;
  lastSync: Date;
  conflicts: SyncConflict[];
}

class VisualCodeSyncEngine {
  private workflowStore: WorkflowStore;
  private codeGenerator: CodeGenerator;
  private codeParser: CodeParser;
  
  /**
   * Sync visual workflow to code
   */
  async syncVisualToCode(
    workflowId: string,
    format: 'typescript' | 'javascript' | 'python' = 'typescript'
  ): Promise<GeneratedCode> {
    // 1. Get workflow definition
    const workflow = await this.workflowStore.get(workflowId);
    
    // 2. Generate code from workflow
    const code = await this.codeGenerator.generate(workflow, {
      format,
      includeComments: true,
      includeTypes: format === 'typescript',
      includeTests: true,
      style: 'production'
    });
    
    // 3. Format code
    const formatted = await this.formatCode(code, format);
    
    // 4. Save code
    await this.saveCode(workflowId, formatted);
    
    // 5. Update sync status
    await this.updateSyncStatus(workflowId, 'visual-to-code');
    
    return formatted;
  }
  
  /**
   * Sync code to visual workflow
   */
  async syncCodeToVisual(
    workflowId: string,
    code: string,
    format: 'typescript' | 'javascript' | 'python'
  ): Promise<Workflow> {
    // 1. Parse code into AST
    const ast = await this.codeParser.parse(code, format);
    
    // 2. Extract workflow structure from AST
    const workflow = await this.extractWorkflowFromAST(ast);
    
    // 3. Validate workflow
    const validation = await this.validateWorkflow(workflow);
    if (!validation.valid) {
      throw new ValidationError('Code cannot be converted to valid workflow', validation.errors);
    }
    
    // 4. Update visual workflow
    await this.workflowStore.update(workflowId, workflow);
    
    // 5. Update sync status
    await this.updateSyncStatus(workflowId, 'code-to-visual');
    
    return workflow;
  }
  
  /**
   * Enable real-time bidirectional sync
   */
  async enableRealtimeSync(workflowId: string): Promise<void> {
    // Watch for visual changes
    this.workflowStore.watch(workflowId, async (workflow) => {
      await this.syncVisualToCode(workflowId);
    });
    
    // Watch for code changes
    this.codeWatcher.watch(workflowId, async (code) => {
      await this.syncCodeToVisual(workflowId, code, 'typescript');
    });
  }
  
  /**
   * Generate inline code preview for node
   */
  async generateNodeCodePreview(
    nodeId: string,
    workflowId: string
  ): Promise<string> {
    const workflow = await this.workflowStore.get(workflowId);
    const node = workflow.nodes.find(n => n.id === nodeId);
    
    if (!node) {
      throw new Error(`Node ${nodeId} not found`);
    }
    
    // Generate code just for this node
    const code = await this.codeGenerator.generateNodeCode(node, {
      includeComments: true,
      standalone: true
    });
    
    return code;
  }
}

/**
 * Project Scaffold Generator
 */
class ProjectScaffoldGenerator {
  /**
   * Generate complete project scaffold
   */
  async generateProjectScaffold(
    workflow: Workflow,
    options: ScaffoldOptions
  ): Promise<ProjectScaffold> {
    const scaffold: ProjectScaffold = {
      files: {},
      metadata: {
        name: workflow.name,
        version: '1.0.0',
        generatedAt: new Date()
      }
    };
    
    // 1. Generate server file
    scaffold.files['src/server.ts'] = await this.generateServerFile(workflow);
    
    // 2. Generate dependency manifest
    scaffold.files['package.json'] = await this.generatePackageJson(workflow);
    
    // 3. Generate model loader
    if (workflow.usesAIModels) {
      scaffold.files['src/models/loader.ts'] = await this.generateModelLoader(workflow);
    }
    
    // 4. Generate test script
    scaffold.files['src/__tests__/workflow.test.ts'] = await this.generateTestScript(workflow);
    
    // 5. Generate README
    scaffold.files['README.md'] = await this.generateReadme(workflow);
    
    // 6. Generate Dockerfile (optional)
    if (options.includeDocker) {
      scaffold.files['Dockerfile'] = await this.generateDockerfile(workflow);
      scaffold.files['docker-compose.yml'] = await this.generateDockerCompose(workflow);
    }
    
    // 7. Generate environment file
    scaffold.files['.env.example'] = await this.generateEnvFile(workflow);
    
    // 8. Generate TypeScript config
    scaffold.files['tsconfig.json'] = await this.generateTsConfig();
    
    // 9. Generate ESLint config
    scaffold.files['.eslintrc.json'] = await this.generateEslintConfig();
    
    // 10. Generate workflow execution file
    scaffold.files['src/workflow.ts'] = await this.generateWorkflowFile(workflow);
    
    return scaffold;
  }
  
  /**
   * Generate server.ts file
   */
  private async generateServerFile(workflow: Workflow): Promise<string> {
    return `
import Fastify from 'fastify';
import { executeWorkflow } from './workflow';

const fastify = Fastify({
  logger: true
});

/**
 * Execute workflow endpoint
 */
fastify.post('/api/workflow/execute', async (request, reply) => {
  try {
    const result = await executeWorkflow(request.body);
    return reply.send({
      success: true,
      result
    });
  } catch (error) {
    return reply.status(500).send({
      success: false,
      error: error.message
    });
  }
});

/**
 * Health check endpoint
 */
fastify.get('/health', async (request, reply) => {
  return { status: 'ok' };
});

/**
 * Start server
 */
const start = async () => {
  try {
    await fastify.listen({ port: 3000, host: '0.0.0.0' });
    console.log('Server running on http://localhost:3000');
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
    `.trim();
  }
  
  /**
   * Generate workflow execution file
   */
  private async generateWorkflowFile(workflow: Workflow): Promise<string> {
    const code = await this.codeGenerator.generate(workflow, {
      format: 'typescript',
      includeComments: true,
      includeTypes: true,
      style: 'production'
    });
    
    return code;
  }
  
  /**
   * Generate package.json
   */
  private async generatePackageJson(workflow: Workflow): Promise<string> {
    const dependencies = await this.extractDependencies(workflow);
    
    const packageJson = {
      name: workflow.name.toLowerCase().replace(/\s+/g, '-'),
      version: '1.0.0',
      description: workflow.description || 'Generated by OLAI',
      main: 'dist/server.js',
      scripts: {
        dev: 'ts-node src/server.ts',
        build: 'tsc',
        start: 'node dist/server.js',
        test: 'jest',
        lint: 'eslint src/**/*.ts'
      },
      dependencies,
      devDependencies: {
        '@types/node': '^20.0.0',
        'typescript': '^5.0.0',
        'ts-node': '^10.9.1',
        'eslint': '^8.0.0',
        'jest': '^29.0.0',
        '@types/jest': '^29.0.0'
      }
    };
    
    return JSON.stringify(packageJson, null, 2);
  }
  
  /**
   * Generate README.md
   */
  private async generateReadme(workflow: Workflow): Promise<string> {
    return `
# ${workflow.name}

${workflow.description || 'Workflow generated by OLAI'}

## Setup

\`\`\`bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Run development server
npm run dev
\`\`\`

## Workflow Description

${this.generateWorkflowDescription(workflow)}

## API Endpoints

### Execute Workflow

\`\`\`bash
POST /api/workflow/execute
Content-Type: application/json

{
  "input": "your input here"
}
\`\`\`

### Health Check

\`\`\`bash
GET /health
\`\`\`

## Testing

\`\`\`bash
npm test
\`\`\`

## Building

\`\`\`bash
npm run build
\`\`\`

## Deployment

\`\`\`bash
npm start
\`\`\`

---

Generated by OLAI on ${new Date().toLocaleString()}
    `.trim();
  }
  
  /**
   * Generate Dockerfile
   */
  private async generateDockerfile(workflow: Workflow): Promise<string> {
    return `
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY dist ./dist

EXPOSE 3000

CMD ["node", "dist/server.js"]
    `.trim();
  }
  
  /**
   * Export project as downloadable bundle
   */
  async exportProject(
    workflowId: string,
    format: 'zip' | 'tar' = 'zip'
  ): Promise<Buffer> {
    const workflow = await this.workflowStore.get(workflowId);
    const scaffold = await this.generateProjectScaffold(workflow, {
      includeDocker: true
    });
    
    // Create archive
    if (format === 'zip') {
      return await this.createZip(scaffold);
    } else {
      return await this.createTar(scaffold);
    }
  }
}

/**
 * One-Click Actions
 */
class OneClickActions {
  /**
   * Convert chat to visual workflow
   */
  async convertChatToVisual(
    conversationId: string
  ): Promise<Workflow> {
    // Extract workflow from chat conversation
    const messages = await chatService.getMessages(conversationId);
    const workflow = await aiAnalyzer.extractWorkflow(messages);
    
    // Create visual workflow
    return await workflowStore.create(workflow);
  }
  
  /**
   * Publish workflow as API
   */
  async publishAsAPI(
    workflowId: string,
    options: PublishOptions
  ): Promise<PublishedAPI> {
    const workflow = await workflowStore.get(workflowId);
    
    // Generate API endpoint
    const apiEndpoint = await apiPublisher.publish(workflow, {
      authentication: options.requireAuth,
      rateLimit: options.rateLimit,
      cors: options.cors
    });
    
    return {
      url: apiEndpoint.url,
      apiKey: apiEndpoint.apiKey,
      documentation: apiEndpoint.docs
    };
  }
}
```

**Benefits:**
- ✅ **Bidirectional Sync**: Edit visually or in code, changes sync both ways
- ✅ **Real-Time Updates**: Changes reflect instantly
- ✅ **Complete Project Export**: Full deployable project with all files
- ✅ **Developer-Friendly**: Developers can work in code, non-developers in UI
- ✅ **VS Code Integration**: Full synchronization with VS Code
- ✅ **One-Click Actions**: Instant conversion, publishing, and export

---

### 5.5 Code Template System (Comprehensive)

**Template Management:**

```typescript
class CodeTemplateEngine {
  private templateStore: TemplateStore;
  private handlebars: Handlebars;
  
  /**
   * Generate code from template
   */
  async generateFromTemplate(
    templateName: string,
    data: TemplateData
  ): Promise<string> {
    // Load template with inheritance
    const template = await this.templateStore.load(templateName);
    
    // Apply parameter substitution
    const compiled = this.handlebars.compile(template.content);
    const code = compiled(data);
    
    // Format generated code
    return await this.formatCode(code, template.language);
  }
  
  /**
   * Template inheritance system
   */
  async loadTemplateWithInheritance(
    templateName: string
  ): Promise<Template> {
    const template = await this.templateStore.get(templateName);
    
    if (template.extends) {
      const parent = await this.loadTemplateWithInheritance(template.extends);
      return this.mergeTemplates(parent, template);
    }
    
    return template;
  }
}
```

**Template Types:**
- Backend service templates with error handling
- Frontend component templates with hooks
- Route handler templates with middleware
- Test templates with mocks and fixtures
- Configuration templates with environment variables

---

### 5.6 Safe File Editing (Comprehensive)

**AST-Based Editing System:**

```typescript
class SafeFileEditor {
  /**
   * Edit file using AST transformations
   */
  async editFile(
    filePath: string,
    edits: FileEdit[]
  ): Promise<EditResult> {
    // 1. Backup original file
    const backup = await this.backup(filePath);
    
    try {
      // 2. Parse file to AST
      const ast = await this.parseFile(filePath);
      
      // 3. Apply edits to AST
      for (const edit of edits) {
        await this.applyEditToAST(ast, edit);
      }
      
      // 4. Regenerate code from AST
      const code = await this.generateCode(ast);
      
      // 5. Validate syntax
      const validation = await this.validateSyntax(code);
      if (!validation.valid) {
        throw new ValidationError('Generated code has syntax errors');
      }
      
      // 6. Run tests
      const testResult = await this.runTests(filePath);
      if (!testResult.passed) {
        throw new TestError('Tests failed after edit');
      }
      
      // 7. Write to file
      await fs.writeFile(filePath, code);
      
      // 8. Remove backup
      await this.removeBackup(backup);
      
      return { success: true, changes: edits };
      
    } catch (error) {
      // Rollback on failure
      await this.restore(backup, filePath);
      throw error;
    }
  }
  
  /**
   * Apply edit to AST
   */
  private async applyEditToAST(
    ast: AST,
    edit: FileEdit
  ): Promise<void> {
    switch (edit.type) {
      case 'insert':
        this.insertNode(ast, edit.location, edit.code);
        break;
        
      case 'replace':
        this.replaceNode(ast, edit.location, edit.code);
        break;
        
      case 'delete':
        this.deleteNode(ast, edit.location);
        break;
        
      case 'refactor':
        this.refactorCode(ast, edit.refactoring);
        break;
    }
  }
}
```

**Safety Measures:**
- ✅ Automatic backup before editing
- ✅ AST-based transformations preserve structure
- ✅ Syntax validation before saving
- ✅ Automatic test execution
- ✅ Rollback on any failure

---

### 5.7 Partial File Editing (Comprehensive)

**Incremental Update System:**

```typescript
class PartialFileEditor {
  /**
   * Update only changed sections
   */
  async updatePartial(
    filePath: string,
    changes: PartialChange[]
  ): Promise<void> {
    // 1. Parse file to AST
    const ast = await this.parseFile(filePath);
    const originalCode = await fs.readFile(filePath, 'utf-8');
    
    // 2. Identify change locations in AST
    for (const change of changes) {
      const location = this.findNodeLocation(ast, change.selector);
      
      // 3. Apply minimal edit
      await this.applyMinimalEdit(ast, location, change.newCode);
    }
    
    // 4. Regenerate code
    const newCode = await this.generateCode(ast, {
      preserveFormatting: true,
      preserveComments: true,
      preserveImports: true
    });
    
    // 5. Organize imports
    const organized = await this.organizeImports(newCode);
    
    // 6. Save file
    await fs.writeFile(filePath, organized);
  }
  
  /**
   * Compare AST structures to identify differences
   */
  async detectChanges(
    oldCode: string,
    newCode: string
  ): Promise<Change[]> {
    const oldAST = await this.parse(oldCode);
    const newAST = await this.parse(newCode);
    
    return this.diffAST(oldAST, newAST);
  }
  
  /**
   * Generate minimal edits
   */
  private generateMinimalEdits(
    changes: Change[]
  ): Edit[] {
    return changes.map(change => ({
      type: this.determineEditType(change),
      location: change.location,
      oldCode: change.old,
      newCode: change.new
    }));
  }
}
```

**Benefits:**
- ✅ Only changed sections are edited
- ✅ Formatting and comments preserved
- ✅ Import organization maintained
- ✅ Minimal diff for version control
- ✅ Fast incremental updates

---

### 5.8 Code Validation (Comprehensive)

**Comprehensive Validation System:**

```typescript
class CodeValidator {
  /**
   * Run all validation steps
   */
  async validate(
    code: string,
    language: string
  ): Promise<ValidationReport> {
    const report: ValidationReport = {
      valid: true,
      errors: [],
      warnings: [],
      checks: {}
    };
    
    // 1. Syntax validation
    const syntax = await this.validateSyntax(code, language);
    report.checks.syntax = syntax;
    if (!syntax.valid) {
      report.valid = false;
      report.errors.push(...syntax.errors);
    }
    
    // 2. Type checking (TypeScript only)
    if (language === 'typescript') {
      const types = await this.checkTypes(code);
      report.checks.types = types;
      if (!types.valid) {
        report.valid = false;
        report.errors.push(...types.errors);
      }
    }
    
    // 3. Linting
    const lint = await this.lint(code, language);
    report.checks.lint = lint;
    report.warnings.push(...lint.warnings);
    
    // 4. Security scanning
    const security = await this.scanSecurity(code);
    report.checks.security = security;
    if (security.vulnerabilities.length > 0) {
      report.warnings.push(...security.vulnerabilities);
    }
    
    // 5. Test execution (if tests exist)
    try {
      const tests = await this.runTests(code);
      report.checks.tests = tests;
      if (!tests.passed) {
        report.valid = false;
        report.errors.push(...tests.failures);
      }
    } catch {
      // No tests, skip
    }
    
    return report;
  }
  
  /**
   * Validate syntax
   */
  private async validateSyntax(
    code: string,
    language: string
  ): Promise<SyntaxCheck> {
    try {
      if (language === 'typescript' || language === 'javascript') {
        const ast = await this.parseTypeScript(code);
        return { valid: true, errors: [] };
      } else if (language === 'python') {
        await this.parsePython(code);
        return { valid: true, errors: [] };
      }
    } catch (error) {
      return {
        valid: false,
        errors: [this.formatSyntaxError(error)]
      };
    }
  }
  
  /**
   * Type checking with TypeScript compiler
   */
  private async checkTypes(code: string): Promise<TypeCheck> {
    const result = ts.transpileModule(code, {
      compilerOptions: {
        noEmit: true,
        strict: true,
        target: ts.ScriptTarget.ES2020
      },
      reportDiagnostics: true
    });
    
    if (result.diagnostics && result.diagnostics.length > 0) {
      return {
        valid: false,
        errors: result.diagnostics.map(d => d.messageText.toString())
      };
    }
    
    return { valid: true, errors: [] };
  }
  
  /**
   * Lint code with ESLint
   */
  private async lint(
    code: string,
    language: string
  ): Promise<LintCheck> {
    if (language === 'typescript' || language === 'javascript') {
      const eslint = new ESLint();
      const results = await eslint.lintText(code);
      
      return {
        warnings: results[0].messages.map(m => m.message),
        fixable: results[0].fixableErrorCount > 0
      };
    }
    
    return { warnings: [], fixable: false };
  }
  
  /**
   * Security scanning
   */
  private async scanSecurity(code: string): Promise<SecurityCheck> {
    const vulnerabilities: SecurityVulnerability[] = [];
    
    // Check for common security issues
    if (code.includes('eval(')) {
      vulnerabilities.push({
        severity: 'high',
        message: 'Use of eval() is dangerous',
        line: this.findLine(code, 'eval(')
      });
    }
    
    if (code.includes('dangerouslySetInnerHTML')) {
      vulnerabilities.push({
        severity: 'medium',
        message: 'Use of dangerouslySetInnerHTML can lead to XSS',
        line: this.findLine(code, 'dangerouslySetInnerHTML')
      });
    }
    
    // Check for hardcoded secrets
    const secretPatterns = [
      /password\s*=\s*["'][^"']+["']/i,
      /api[_-]?key\s*=\s*["'][^"']+["']/i,
      /secret\s*=\s*["'][^"']+["']/i
    ];
    
    for (const pattern of secretPatterns) {
      if (pattern.test(code)) {
        vulnerabilities.push({
          severity: 'critical',
          message: 'Hardcoded secret detected',
          line: this.findLineWithPattern(code, pattern)
        });
      }
    }
    
    return { vulnerabilities };
  }
}
```

**Validation Tools:**
- ✅ **TypeScript Compiler**: Full type checking
- ✅ **ESLint**: Code quality and style
- ✅ **Prettier**: Automatic formatting
- ✅ **Security Scanners**: Vulnerability detection
- ✅ **Jest/Vitest**: Automated test execution
- ✅ **Custom Rules**: Project-specific validation

**Benefits:**
- ✅ Comprehensive validation before deployment
- ✅ Early error detection
- ✅ Security vulnerability scanning
- ✅ Automatic code quality enforcement
- ✅ Type safety in TypeScript
- ✅ Consistent code style

---

**Summary of Section 5 (Code Generation System):**
- ✅ **5.1**: Node-to-backend mapping with automatic service registration
- ✅ **5.2**: Dynamic route generation with full middleware stack
- ✅ **5.3**: React component scaffolding with AI-assisted custom code
- ✅ **5.4**: Bidirectional visual-to-code sync with project export
- ✅ **5.5**: Template-based code generation with inheritance
- ✅ **5.6**: AST-based safe file editing with rollback
- ✅ **5.7**: Incremental partial file updates
- ✅ **5.8**: Multi-layer code validation and security scanning

---

---

## 6. Automatic UI Generator Plan

The Automatic UI Generator transforms workflows into beautiful, responsive, and accessible user interfaces across web, mobile, and desktop platforms, complete with real-time updates, natural language debugging, and intelligent automation.

---

### 6.1 Workflow Schema to UI Mapping (Comprehensive)

The workflow-to-UI mapping system analyzes workflow structure and automatically generates appropriate user interfaces with optimal layouts, components, and interactions.

---

#### **Workflow Analysis Engine**

```typescript
interface WorkflowUIMapping {
  workflowId: string;
  uiStructure: UIStructure;
  screens: Screen[];
  components: Component[];
  navigation: NavigationStructure;
  stateManagement: StateManagementConfig;
  styling: StylingConfig;
}

interface UIStructure {
  type: 'single-page' | 'multi-page' | 'wizard' | 'dashboard';
  layout: 'vertical' | 'horizontal' | 'grid' | 'custom';
  navigation: 'top' | 'side' | 'bottom' | 'none';
  responsive: ResponsiveConfig;
}

class WorkflowUIMapper {
  private workflowAnalyzer: WorkflowAnalyzer;
  private screenGenerator: ScreenGenerator;
  private componentFactory: ComponentFactory;
  
  /**
   * Map workflow to UI structure
   */
  async mapWorkflowToUI(
    workflow: Workflow
  ): Promise<WorkflowUIMapping> {
    // 1. Analyze workflow structure
    const analysis = await this.analyzeWorkflow(workflow);
    
    // 2. Determine UI structure type
    const uiStructure = await this.determineUIStructure(analysis);
    
    // 3. Generate screens
    const screens = await this.generateScreens(workflow, uiStructure);
    
    // 4. Generate components for each screen
    const components = await this.generateComponents(screens);
    
    // 5. Generate navigation structure
    const navigation = await this.generateNavigation(screens, workflow);
    
    // 6. Configure state management
    const stateManagement = await this.configureStateManagement(workflow);
    
    // 7. Configure styling
    const styling = await this.configureStyling(workflow, uiStructure);
    
    return {
      workflowId: workflow.id,
      uiStructure,
      screens,
      components,
      navigation,
      stateManagement,
      styling
    };
  }
  
  /**
   * Analyze workflow to determine UI requirements
   */
  private async analyzeWorkflow(
    workflow: Workflow
  ): Promise<WorkflowAnalysis> {
    const analysis: WorkflowAnalysis = {
      nodeCount: workflow.nodes.length,
      complexity: 'simple',
      hasUserInput: false,
      hasOutput: false,
      hasBranching: false,
      requiresAuth: false,
      requiresRealTime: false,
      estimatedScreens: 1
    };
    
    // Analyze nodes
    for (const node of workflow.nodes) {
      // Check for input nodes
      if (node.type === 'input' || node.type === 'form') {
        analysis.hasUserInput = true;
      }
      
      // Check for output nodes
      if (node.type === 'output' || node.type === 'display') {
        analysis.hasOutput = true;
      }
      
      // Check for branching
      if (node.type === 'conditional' || node.type === 'switch') {
        analysis.hasBranching = true;
      }
      
      // Check for authentication
      if (node.type === 'auth' || node.type === 'login') {
        analysis.requiresAuth = true;
      }
      
      // Check for real-time updates
      if (node.type === 'websocket' || node.type === 'stream') {
        analysis.requiresRealTime = true;
      }
    }
    
    // Determine complexity
    if (workflow.nodes.length > 20) {
      analysis.complexity = 'complex';
    } else if (workflow.nodes.length > 10) {
      analysis.complexity = 'medium';
    }
    
    // Estimate number of screens
    analysis.estimatedScreens = this.estimateScreenCount(workflow);
    
    return analysis;
  }
  
  /**
   * Determine optimal UI structure
   */
  private async determineUIStructure(
    analysis: WorkflowAnalysis
  ): Promise<UIStructure> {
    // Single-page for simple workflows
    if (analysis.complexity === 'simple' && analysis.estimatedScreens === 1) {
      return {
        type: 'single-page',
        layout: 'vertical',
        navigation: 'none',
        responsive: {
          breakpoints: ['mobile', 'tablet', 'desktop'],
          strategy: 'mobile-first'
        }
      };
    }
    
    // Wizard for step-by-step workflows
    if (analysis.hasUserInput && !analysis.hasBranching) {
      return {
        type: 'wizard',
        layout: 'vertical',
        navigation: 'bottom',
        responsive: {
          breakpoints: ['mobile', 'tablet', 'desktop'],
          strategy: 'mobile-first'
        }
      };
    }
    
    // Dashboard for monitoring workflows
    if (analysis.hasOutput && analysis.requiresRealTime) {
      return {
        type: 'dashboard',
        layout: 'grid',
        navigation: 'side',
        responsive: {
          breakpoints: ['mobile', 'tablet', 'desktop'],
          strategy: 'desktop-first'
        }
      };
    }
    
    // Multi-page for complex workflows
    return {
      type: 'multi-page',
      layout: 'vertical',
      navigation: 'top',
      responsive: {
        breakpoints: ['mobile', 'tablet', 'desktop'],
        strategy: 'mobile-first'
      }
    };
  }
  
  /**
   * Generate screens from workflow
   */
  private async generateScreens(
    workflow: Workflow,
    uiStructure: UIStructure
  ): Promise<Screen[]> {
    const screens: Screen[] = [];
    
    // Generate input screen if workflow has input nodes
    const inputNodes = workflow.nodes.filter(n => 
      n.type === 'input' || n.type === 'form'
    );
    
    if (inputNodes.length > 0) {
      screens.push(await this.generateInputScreen(inputNodes, workflow));
    }
    
    // Generate processing screen for long-running workflows
    if (this.isLongRunning(workflow)) {
      screens.push(await this.generateProcessingScreen(workflow));
    }
    
    // Generate output screen if workflow has output
    const outputNodes = workflow.nodes.filter(n => 
      n.type === 'output' || n.type === 'display'
    );
    
    if (outputNodes.length > 0) {
      screens.push(await this.generateOutputScreen(outputNodes, workflow));
    }
    
    // Generate configuration screen
    screens.push(await this.generateConfigScreen(workflow));
    
    return screens;
  }
  
  /**
   * Generate input screen
   */
  private async generateInputScreen(
    inputNodes: Node[],
    workflow: Workflow
  ): Promise<Screen> {
    const formFields: FormField[] = [];
    
    // Convert input nodes to form fields
    for (const node of inputNodes) {
      const fields = await this.convertNodeToFormFields(node);
      formFields.push(...fields);
    }
    
    return {
      id: `${workflow.id}-input`,
      name: 'Input',
      route: '/input',
      title: `${workflow.name} - Input`,
      description: 'Provide input data for the workflow',
      type: 'form',
      layout: {
        type: 'single-column',
        maxWidth: '600px',
        centered: true
      },
      components: [
        {
          type: 'heading',
          props: {
            level: 1,
            text: workflow.name
          }
        },
        {
          type: 'description',
          props: {
            text: workflow.description || 'Enter the required information to start the workflow'
          }
        },
        {
          type: 'form',
          props: {
            fields: formFields,
            submitLabel: 'Start Workflow',
            onSubmit: 'executeWorkflow'
          }
        }
      ]
    };
  }
  
  /**
   * Generate output screen
   */
  private async generateOutputScreen(
    outputNodes: Node[],
    workflow: Workflow
  ): Promise<Screen> {
    return {
      id: `${workflow.id}-output`,
      name: 'Results',
      route: '/results',
      title: `${workflow.name} - Results`,
      description: 'View workflow execution results',
      type: 'display',
      layout: {
        type: 'single-column',
        maxWidth: '800px',
        centered: true
      },
      components: [
        {
          type: 'heading',
          props: {
            level: 1,
            text: 'Results'
          }
        },
        {
          type: 'status-indicator',
          props: {
            source: 'workflow.status'
          }
        },
        {
          type: 'result-display',
          props: {
            source: 'workflow.output',
            format: 'auto'
          }
        },
        {
          type: 'action-buttons',
          props: {
            actions: [
              { label: 'Download Results', action: 'downloadResults' },
              { label: 'Run Again', action: 'resetWorkflow' },
              { label: 'Share', action: 'shareResults' }
            ]
          }
        }
      ]
    };
  }
  
  /**
   * Generate processing screen for long-running workflows
   */
  private async generateProcessingScreen(
    workflow: Workflow
  ): Promise<Screen> {
    return {
      id: `${workflow.id}-processing`,
      name: 'Processing',
      route: '/processing',
      title: `${workflow.name} - Processing`,
      description: 'Workflow execution in progress',
      type: 'loading',
      layout: {
        type: 'centered',
        maxWidth: '500px',
        centered: true
      },
      components: [
        {
          type: 'loading-spinner',
          props: {
            size: 'large'
          }
        },
        {
          type: 'progress-bar',
          props: {
            source: 'workflow.progress',
            showPercentage: true
          }
        },
        {
          type: 'status-message',
          props: {
            source: 'workflow.statusMessage',
            variant: 'info'
          }
        },
        {
          type: 'live-log',
          props: {
            source: 'workflow.activityFeed',
            maxLines: 10
          }
        }
      ]
    };
  }
  
  /**
   * Convert node to form fields
   */
  private async convertNodeToFormFields(
    node: Node
  ): Promise<FormField[]> {
    const fields: FormField[] = [];
    
    for (const input of node.data.inputs || []) {
      fields.push({
        name: input.name,
        label: input.label || input.name,
        type: this.mapInputType(input.type),
        required: input.required,
        placeholder: input.placeholder,
        description: input.description,
        validation: input.validation,
        defaultValue: input.defaultValue
      });
    }
    
    return fields;
  }
  
  /**
   * Map node input type to form field type
   */
  private mapInputType(nodeType: string): FormFieldType {
    const mapping: Record<string, FormFieldType> = {
      'string': 'text',
      'text': 'textarea',
      'number': 'number',
      'boolean': 'checkbox',
      'select': 'select',
      'multiselect': 'multiselect',
      'date': 'date',
      'time': 'time',
      'datetime': 'datetime',
      'file': 'file',
      'image': 'image',
      'color': 'color',
      'range': 'range'
    };
    
    return mapping[nodeType] || 'text';
  }
}
```

**Benefits:**
- ✅ **Intelligent Mapping**: Analyzes workflow to determine optimal UI
- ✅ **Screen Generation**: Auto-generates input, processing, and output screens
- ✅ **Component Selection**: Chooses appropriate UI components automatically
- ✅ **Layout Optimization**: Responsive layouts for all devices
- ✅ **Navigation Structure**: Automatic navigation between screens
- ✅ **Form Generation**: Converts workflow inputs to beautiful forms

---

### 6.2 Component Tree Generation (Comprehensive)

The component tree generation system creates hierarchical, modular UI structures with intelligent organization, collapsible sections, and smart search capabilities.

---

#### **Component Tree Builder**

```typescript
interface ComponentTree {
  root: ComponentNode;
  nodes: Map<string, ComponentNode>;
  depth: number;
  totalComponents: number;
  hierarchy: ComponentHierarchy;
}

interface ComponentNode {
  id: string;
  type: ComponentType;
  name: string;
  props: Record<string, any>;
  children: ComponentNode[];
  parent?: string;
  level: number;
  
  // Notion-like features
  collapsible: boolean;
  collapsed: boolean;
  searchable: boolean;
  tags: string[];
  
  // Data flow
  dataInputs: DataBinding[];
  dataOutputs: DataBinding[];
  
  // State
  localState?: StateDefinition;
}

class ComponentTreeGenerator {
  /**
   * Generate component tree from workflow
   */
  async generateTree(
    workflow: Workflow,
    uiMapping: WorkflowUIMapping
  ): Promise<ComponentTree> {
    // 1. Create root container
    const root = this.createRootContainer(workflow);
    
    // 2. Generate layout structure
    const layout = await this.generateLayoutStructure(uiMapping);
    root.children.push(layout);
    
    // 3. Generate navigation if needed
    if (uiMapping.navigation.type !== 'none') {
      const nav = await this.generateNavigation(uiMapping);
      root.children.push(nav);
    }
    
    // 4. Generate screen components
    for (const screen of uiMapping.screens) {
      const screenComponent = await this.generateScreenComponent(screen);
      layout.children.push(screenComponent);
    }
    
    // 5. Generate modular blocks for workflow visualization
    const workflowViz = await this.generateWorkflowVisualization(workflow);
    layout.children.push(workflowViz);
    
    // 6. Build node map and calculate hierarchy
    const nodes = this.buildNodeMap(root);
    const hierarchy = this.calculateHierarchy(root);
    
    return {
      root,
      nodes,
      depth: hierarchy.maxDepth,
      totalComponents: nodes.size,
      hierarchy
    };
  }
  
  /**
   * Create root container component
   */
  private createRootContainer(workflow: Workflow): ComponentNode {
    return {
      id: 'root',
      type: 'container',
      name: 'AppContainer',
      props: {
        className: 'app-container',
        theme: 'light',
        responsive: true
      },
      children: [],
      level: 0,
      collapsible: false,
      collapsed: false,
      searchable: false,
      tags: [],
      dataInputs: [],
      dataOutputs: []
    };
  }
  
  /**
   * Generate workflow visualization with modular blocks
   */
  private async generateWorkflowVisualization(
    workflow: Workflow
  ): Promise<ComponentNode> {
    const vizComponent: ComponentNode = {
      id: 'workflow-viz',
      type: 'workflow-canvas',
      name: 'WorkflowCanvas',
      props: {
        workflowId: workflow.id,
        interactive: true,
        zoomable: true
      },
      children: [],
      level: 2,
      collapsible: true,
      collapsed: false,
      searchable: true,
      tags: ['workflow', 'visualization'],
      dataInputs: [],
      dataOutputs: []
    };
    
    // Generate node blocks
    for (const node of workflow.nodes) {
      const nodeBlock = await this.generateNodeBlock(node, workflow);
      vizComponent.children.push(nodeBlock);
    }
    
    // Generate subflow blocks
    const subflows = this.identifySubflows(workflow);
    for (const subflow of subflows) {
      const subflowBlock = await this.generateSubflowBlock(subflow);
      vizComponent.children.push(subflowBlock);
    }
    
    return vizComponent;
  }
  
  /**
   * Generate Notion-like modular node block
   */
  private async generateNodeBlock(
    node: Node,
    workflow: Workflow
  ): Promise<ComponentNode> {
    return {
      id: `node-block-${node.id}`,
      type: 'node-block',
      name: 'NodeBlock',
      props: {
        nodeId: node.id,
        nodeType: node.type,
        label: node.data.label || node.type,
        icon: node.data.icon,
        collapsible: true,
        collapsed: false,
        searchTerm: `${node.type} ${node.data.label || ''}`,
        tags: [node.type, node.data.category],
        
        // Detailed view
        showDetails: false,
        details: {
          inputs: node.data.inputs,
          outputs: node.data.outputs,
          config: node.data.config
        },
        
        // Actions
        actions: [
          { id: 'edit', label: 'Edit', icon: 'edit' },
          { id: 'duplicate', label: 'Duplicate', icon: 'copy' },
          { id: 'delete', label: 'Delete', icon: 'trash' }
        ]
      },
      children: [],
      level: 3,
      collapsible: true,
      collapsed: false,
      searchable: true,
      tags: [node.type, node.data.category],
      dataInputs: node.data.inputs?.map(i => ({
        name: i.name,
        type: i.type,
        source: this.findDataSource(node, i.name, workflow)
      })),
      dataOutputs: node.data.outputs?.map(o => ({
        name: o.name,
        type: o.type,
        targets: this.findDataTargets(node, o.name, workflow)
      }))
    };
  }
  
  /**
   * Generate collapsible subflow block
   */
  private async generateSubflowBlock(
    subflow: Subflow
  ): Promise<ComponentNode> {
    const subflowBlock: ComponentNode = {
      id: `subflow-${subflow.id}`,
      type: 'subflow-block',
      name: 'SubflowBlock',
      props: {
        subflowId: subflow.id,
        name: subflow.name,
        description: subflow.description,
        collapsible: true,
        collapsed: true,  // Collapsed by default
        nodeCount: subflow.nodes.length,
        color: subflow.color || '#3b82f6'
      },
      children: [],
      level: 3,
      collapsible: true,
      collapsed: true,
      searchable: true,
      tags: ['subflow', subflow.name],
      dataInputs: [],
      dataOutputs: []
    };
    
    // Add child nodes
    for (const node of subflow.nodes) {
      const nodeBlock = await this.generateNodeBlock(node, subflow as any);
      subflowBlock.children.push(nodeBlock);
    }
    
    return subflowBlock;
  }
}

/**
 * Smart Search System
 */
class WorkflowSearchEngine {
  /**
   * Search workflow with natural language
   */
  async search(
    query: string,
    workflow: Workflow
  ): Promise<SearchResult[]> {
    // Use AI to understand query intent
    const intent = await this.analyzeSearchIntent(query);
    
    const results: SearchResult[] = [];
    
    // Search nodes
    for (const node of workflow.nodes) {
      const match = await this.matchNode(node, query, intent);
      if (match.score > 0.3) {
        results.push({
          type: 'node',
          item: node,
          score: match.score,
          highlights: match.highlights
        });
      }
    }
    
    // Search connections
    for (const edge of workflow.edges) {
      const match = await this.matchEdge(edge, query, intent);
      if (match.score > 0.3) {
        results.push({
          type: 'edge',
          item: edge,
          score: match.score,
          highlights: match.highlights
        });
      }
    }
    
    // Sort by relevance
    results.sort((a, b) => b.score - a.score);
    
    return results;
  }
  
  /**
   * Example queries:
   * - "show me all API calls touching Salesforce"
   * - "find nodes that process images"
   * - "where is the error handling?"
   */
  private async analyzeSearchIntent(query: string): Promise<SearchIntent> {
    // Extract keywords and intent using LLM
    const analysis = await llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Analyze this workflow search query and extract structured information:

Query: "${query}"

Extract:
1. Node types mentioned (API, image, etc.)
2. Actions mentioned (process, call, handle, etc.)
3. Services/integrations mentioned (Salesforce, Slack, etc.)
4. Properties mentioned (error, status, etc.)

Respond in JSON:
{
  "nodeTypes": ["api", "http"],
  "actions": ["call"],
  "services": ["salesforce"],
  "properties": []
}
      `
    });
    
    return JSON.parse(analysis);
  }
}

/**
 * Automated Data Wiring System
 */
class DataWiringEngine {
  /**
   * Automatically wire data between nodes
   */
  async autoWireNodes(
    sourceNode: Node,
    targetNode: Node
  ): Promise<DataWiring[]> {
    const wirings: DataWiring[] = [];
    
    // Get source outputs and target inputs
    const outputs = sourceNode.data.outputs || [];
    const inputs = targetNode.data.inputs || [];
    
    // Try to match by name
    for (const output of outputs) {
      for (const input of inputs) {
        if (this.isCompatible(output, input)) {
          wirings.push({
            sourceNode: sourceNode.id,
            sourceOutput: output.name,
            targetNode: targetNode.id,
            targetInput: input.name,
            automatic: true,
            confidence: this.calculateConfidence(output, input)
          });
        }
      }
    }
    
    // Sort by confidence
    wirings.sort((a, b) => b.confidence - a.confidence);
    
    return wirings;
  }
  
  /**
   * Check if output and input are compatible
   */
  private isCompatible(
    output: NodeOutput,
    input: NodeInput
  ): boolean {
    // Type compatibility
    if (output.type !== input.type && 
        !this.canConvert(output.type, input.type)) {
      return false;
    }
    
    // Name similarity
    const similarity = this.calculateNameSimilarity(output.name, input.name);
    if (similarity > 0.7) {
      return true;
    }
    
    // Semantic similarity (using embeddings)
    const semanticSim = this.calculateSemanticSimilarity(
      output.description || output.name,
      input.description || input.name
    );
    
    return semanticSim > 0.6;
  }
}
```

**Benefits:**
- ✅ **Modular Blocks**: Notion-like collapsible, searchable blocks
- ✅ **Smart Hierarchy**: Intelligent component tree organization
- ✅ **Natural Language Search**: Find nodes by asking questions
- ✅ **Auto Data Wiring**: Automatic connections between nodes
- ✅ **Collapsible Subflows**: Manage complex workflows easily
- ✅ **Zoom Hierarchy**: Overview and detailed views

---

### 6.3 Theme and Style Systems (Comprehensive)

```typescript
interface ThemeSystem {
  mode: 'light' | 'dark' | 'auto';
  colors: ColorPalette;
  typography: TypographySystem;
  spacing: SpacingSystem;
  breakpoints: Breakpoints;
  animations: AnimationSystem;
}

class ThemeManager {
  /**
   * Generate complete theme system
   */
  generateTheme(preferences?: ThemePreferences): ThemeSystem {
    return {
      mode: preferences?.mode || 'auto',
      colors: this.generateColorPalette(preferences?.primaryColor),
      typography: this.generateTypography(),
      spacing: this.generateSpacing(),
      breakpoints: this.generateBreakpoints(),
      animations: this.generateAnimations()
    };
  }
  
  /**
   * Generate color palette from primary color
   */
  private generateColorPalette(primary?: string): ColorPalette {
    const baseColor = primary || '#3b82f6';
    
    return {
      primary: {
        50: this.lighten(baseColor, 0.95),
        100: this.lighten(baseColor, 0.90),
        // ... generate all shades
        900: this.darken(baseColor, 0.60)
      },
      // Auto-generate complementary colors
      secondary: this.generateComplementary(baseColor),
      success: '#10b981',
      warning: '#f59e0b',
      error: '#ef4444',
      info: '#3b82f6',
      neutral: this.generateNeutralPalette()
    };
  }
}

/**
 * Styled Components with Theme
 */
const StyledButton = styled.button<{ variant: 'primary' | 'secondary' }>`
  padding: ${props => props.theme.spacing.md} ${props => props.theme.spacing.lg};
  background: ${props => props.variant === 'primary' 
    ? props.theme.colors.primary[600] 
    : props.theme.colors.secondary[600]};
  color: white;
  border-radius: ${props => props.theme.borderRadius.md};
  font-size: ${props => props.theme.typography.fontSize.base};
  transition: all ${props => props.theme.animations.duration.fast} ${props => props.theme.animations.easing.easeInOut};
  
  &:hover {
    background: ${props => props.variant === 'primary' 
      ? props.theme.colors.primary[700] 
      : props.theme.colors.secondary[700]};
    transform: translateY(-1px);
  }
`;
```

**Benefits:**
- ✅ Dynamic theme generation
- ✅ Light/dark mode support
- ✅ Customizable color palettes
- ✅ Consistent spacing and typography

---

### 6.4 Design System Support (Comprehensive)

```typescript
interface DesignSystemAdapter {
  name: 'shadcn' | 'mui' | 'antd' | 'custom';
  components: ComponentMapping;
  tokens: StyleTokens;
  theme: ThemeConfig;
}

class DesignSystemIntegrator {
  /**
   * Map workflow components to design system
   */
  async mapToDesignSystem(
    components: Component[],
    system: 'shadcn' | 'mui' | 'antd'
  ): Promise<MappedComponents> {
    const mapper = this.getMapper(system);
    
    return await Promise.all(
      components.map(c => mapper.map(c))
    );
  }
  
  /**
   * shadcn/ui mapper
   */
  private shadcnMapper = {
    map: async (component: Component) => {
      const mapping = {
        'button': 'Button',
        'input': 'Input',
        'select': 'Select',
        'checkbox': 'Checkbox',
        'dialog': 'Dialog',
        'card': 'Card',
        'table': 'Table'
      };
      
      return {
        import: `import { ${mapping[component.type]} } from '@/components/ui/${component.type}'`,
        component: mapping[component.type],
        props: this.mapProps(component.props, 'shadcn')
      };
    }
  };
}
```

**Benefits:**
- ✅ Support for popular design systems
- ✅ Automatic component mapping
- ✅ Consistent styling
- ✅ Easy switching between systems

---

### 6.5 Layout System (Comprehensive)

```typescript
class LayoutGenerator {
  /**
   * Generate responsive layout
   */
  async generateLayout(
    components: Component[],
    type: LayoutType
  ): Promise<Layout> {
    switch (type) {
      case 'single-column':
        return this.generateSingleColumn(components);
        
      case 'multi-column':
        return this.generateMultiColumn(components);
        
      case 'grid':
        return this.generateGrid(components);
        
      case 'dashboard':
        return this.generateDashboard(components);
    }
  }
  
  /**
   * Generate grid layout with auto-placement
   */
  private generateGrid(components: Component[]): GridLayout {
    return {
      type: 'grid',
      columns: {
        mobile: 1,
        tablet: 2,
        desktop: 3
      },
      gap: 'medium',
      autoFlow: 'dense',
      items: components.map(c => ({
        component: c,
        span: this.calculateSpan(c),
        order: this.calculateOrder(c)
      }))
    };
  }
}
```

**Benefits:**
- ✅ Responsive layouts
- ✅ Auto-placement algorithms
- ✅ Mobile-first design
- ✅ Accessibility built-in

---

### 6.6 UI Quality Assurance (Comprehensive)

```typescript
class UIQualityChecker {
  /**
   * Run comprehensive UI quality checks
   */
  async runQualityChecks(ui: GeneratedUI): Promise<QualityReport> {
    const report: QualityReport = {
      score: 0,
      checks: {}
    };
    
    // 1. Accessibility check
    report.checks.accessibility = await this.checkAccessibility(ui);
    
    // 2. Responsive design check
    report.checks.responsive = await this.checkResponsive(ui);
    
    // 3. Performance check
    report.checks.performance = await this.checkPerformance(ui);
    
    // 4. UX validation
    report.checks.ux = await this.validateUX(ui);
    
    // 5. Cross-browser compatibility
    report.checks.compatibility = await this.checkCompatibility(ui);
    
    // Calculate overall score
    report.score = this.calculateScore(report.checks);
    
    return report;
  }
  
  /**
   * Check WCAG 2.1 AA compliance
   */
  private async checkAccessibility(ui: GeneratedUI): Promise<AccessibilityCheck> {
    const issues: AccessibilityIssue[] = [];
    
    // Check color contrast
    const contrastIssues = await this.checkColorContrast(ui);
    issues.push(...contrastIssues);
    
    // Check keyboard navigation
    const keyboardIssues = await this.checkKeyboardNav(ui);
    issues.push(...keyboardIssues);
    
    // Check ARIA labels
    const ariaIssues = await this.checkARIA(ui);
    issues.push(...ariaIssues);
    
    // Check focus indicators
    const focusIssues = await this.checkFocusIndicators(ui);
    issues.push(...focusIssues);
    
    return {
      passed: issues.length === 0,
      score: this.calculateAccessibilityScore(issues),
      issues,
      wcagLevel: issues.length === 0 ? 'AA' : 'Partial'
    };
  }
}
```

**Agent Involvement:**
- ✅ **Review Agent**: Audits UI code for best practices
- ✅ **Testing Agent**: Automated UI testing (Playwright, Cypress)
- ✅ **PM Agent**: Validates against requirements
- ✅ **Architect Agent**: Reviews component architecture

---

### 6.7 Explainability Mode (Comprehensive)

The explainability system makes complex workflows understandable to everyone through AI-powered natural language explanations, visual guides, and progressive disclosure.

---

#### **AI Explainability Engine**

```typescript
interface WorkflowExplanation {
  workflowId: string;
  summary: string;
  purpose: string;
  steps: StepExplanation[];
  dataFlow: DataFlowExplanation;
  examples: WorkflowExample[];
  complexity: 'simple' | 'medium' | 'complex';
}

interface StepExplanation {
  nodeId: string;
  title: string;
  plainEnglish: string;
  technicalDetails: string;
  purpose: string;
  inputs: InputExplanation[];
  outputs: OutputExplanation[];
  sampleData: {
    input: any;
    output: any;
  };
  visualHighlight: VisualHighlight;
}

class ExplainabilityEngine {
  private llm: LLMClient;
  
  /**
   * Generate complete workflow explanation
   */
  async explainWorkflow(
    workflow: Workflow,
    userLevel: 'beginner' | 'intermediate' | 'expert' = 'beginner'
  ): Promise<WorkflowExplanation> {
    // 1. Generate high-level summary
    const summary = await this.generateSummary(workflow, userLevel);
    
    // 2. Explain each step
    const steps = await Promise.all(
      workflow.nodes.map(node => this.explainStep(node, workflow, userLevel))
    );
    
    // 3. Explain data flow
    const dataFlow = await this.explainDataFlow(workflow, userLevel);
    
    // 4. Generate examples
    const examples = await this.generateExamples(workflow);
    
    // 5. Assess complexity
    const complexity = this.assessComplexity(workflow);
    
    return {
      workflowId: workflow.id,
      summary,
      purpose: workflow.description || 'No description provided',
      steps,
      dataFlow,
      examples,
      complexity
    };
  }
  
  /**
   * Generate plain English explanation for workflow
   */
  private async generateSummary(
    workflow: Workflow,
    userLevel: string
  ): Promise<string> {
    const prompt = userLevel === 'beginner' 
      ? 'Explain this workflow in simple terms that anyone can understand'
      : 'Explain this workflow with technical details';
      
    const explanation = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
${prompt}:

Workflow: ${workflow.name}
Description: ${workflow.description || 'Not provided'}

Nodes:
${workflow.nodes.map(n => `- ${n.type}: ${n.data.label || n.type}`).join('\n')}

Connections:
${workflow.edges.map(e => `- ${e.source} → ${e.target}`).join('\n')}

Generate a 2-3 sentence summary explaining what this workflow does and why it's useful.
      `
    });
    
    return explanation.trim();
  }
  
  /**
   * Explain individual step in plain English
   */
  private async explainStep(
    node: Node,
    workflow: Workflow,
    userLevel: string
  ): Promise<StepExplanation> {
    const plainEnglish = await this.llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Explain this workflow step in ${userLevel === 'beginner' ? 'simple' : 'technical'} terms:

Node Type: ${node.type}
Label: ${node.data.label || node.type}
Configuration: ${JSON.stringify(node.data.config || {})}

Provide a 1-2 sentence explanation of what this step does.
      `
    });
    
    const technicalDetails = await this.generateTechnicalDetails(node);
    const purpose = await this.explainPurpose(node, workflow);
    
    return {
      nodeId: node.id,
      title: node.data.label || node.type,
      plainEnglish: plainEnglish.trim(),
      technicalDetails,
      purpose,
      inputs: await this.explainInputs(node),
      outputs: await this.explainOutputs(node),
      sampleData: await this.generateSampleData(node),
      visualHighlight: {
        color: this.getNodeColor(node.type),
        animation: 'pulse'
      }
    };
  }
  
  /**
   * Explain data flow through workflow
   */
  private async explainDataFlow(
    workflow: Workflow,
    userLevel: string
  ): Promise<DataFlowExplanation> {
    const flows: DataFlowStep[] = [];
    
    // Trace data through workflow
    for (const edge of workflow.edges) {
      const sourceNode = workflow.nodes.find(n => n.id === edge.source);
      const targetNode = workflow.nodes.find(n => n.id === edge.target);
      
      if (sourceNode && targetNode) {
        const explanation = await this.llm.complete({
          model: 'gemini-1.5-flash',
          prompt: `
Explain how data flows from "${sourceNode.data.label || sourceNode.type}" to "${targetNode.data.label || targetNode.type}".

Keep it ${userLevel === 'beginner' ? 'simple' : 'technical'} and in 1 sentence.
          `
        });
        
        flows.push({
          from: sourceNode.id,
          to: targetNode.id,
          explanation: explanation.trim(),
          dataType: edge.data?.type || 'unknown'
        });
      }
    }
    
    return {
      flows,
      visualPath: this.generateVisualPath(workflow),
      summary: await this.generateDataFlowSummary(flows, userLevel)
    };
  }
  
  /**
   * Generate inline examples for node
   */
  private async generateSampleData(node: Node): Promise<any> {
    const sampleInput = await this.llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Generate realistic sample input data for this node:

Node Type: ${node.type}
Inputs: ${JSON.stringify(node.data.inputs || [])}

Respond with JSON only.
      `,
      temperature: 0.7
    });
    
    const sampleOutput = await this.llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Generate expected output for this node with the following input:

Node Type: ${node.type}
Input: ${sampleInput}
Outputs: ${JSON.stringify(node.data.outputs || [])}

Respond with JSON only.
      `,
      temperature: 0.7
    });
    
    return {
      input: JSON.parse(sampleInput),
      output: JSON.parse(sampleOutput)
    };
  }
}

/**
 * Progressive Disclosure UI Component
 */
const NodeExplanationPanel: React.FC<{ node: Node; explanation: StepExplanation }> = ({ 
  node, 
  explanation 
}) => {
  const [showAdvanced, setShowAdvanced] = useState(false);
  const [simplified, setSimplified] = useState(true);
  
  return (
    <div className="explanation-panel">
      {/* Simple view */}
      <div className="simple-view">
        <h3>{explanation.title}</h3>
        <p className="plain-english">{explanation.plainEnglish}</p>
        
        {/* Sample data */}
        <div className="sample-data">
          <h4>Example:</h4>
          <div className="example-flow">
            <div className="input">
              <span className="label">Input:</span>
              <code>{JSON.stringify(explanation.sampleData.input, null, 2)}</code>
            </div>
            <ArrowRightIcon />
            <div className="output">
              <span className="label">Output:</span>
              <code>{JSON.stringify(explanation.sampleData.output, null, 2)}</code>
            </div>
          </div>
        </div>
      </div>
      
      {/* Toggle advanced details */}
      {!simplified && (
        <button onClick={() => setShowAdvanced(!showAdvanced)}>
          {showAdvanced ? 'Hide' : 'Show'} Technical Details
        </button>
      )}
      
      {/* Advanced view */}
      {showAdvanced && !simplified && (
        <div className="advanced-view">
          <h4>Technical Details</h4>
          <p>{explanation.technicalDetails}</p>
          
          <h4>Inputs</h4>
          <ul>
            {explanation.inputs.map((input, i) => (
              <li key={i}>
                <strong>{input.name}</strong> ({input.type}): {input.description}
              </li>
            ))}
          </ul>
          
          <h4>Outputs</h4>
          <ul>
            {explanation.outputs.map((output, i) => (
              <li key={i}>
                <strong>{output.name}</strong> ({output.type}): {output.description}
              </li>
            ))}
          </ul>
        </div>
      )}
      
      {/* Simplified mode toggle */}
      <div className="view-controls">
        <label>
          <input 
            type="checkbox" 
            checked={simplified}
            onChange={(e) => setSimplified(e.target.checked)}
          />
          Simplified View (hide technical details)
        </label>
      </div>
    </div>
  );
};

/**
 * AI Tutor for Troubleshooting
 */
class AITutor {
  /**
   * Answer "why is this failing?" questions
   */
  async answerQuestion(
    question: string,
    context: TroubleshootingContext
  ): Promise<TutorResponse> {
    const answer = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
You are an AI tutor helping a user understand why their workflow is failing.

Question: "${question}"

Workflow Context:
- Failed Node: ${context.failedNode?.type}
- Error Message: ${context.error?.message}
- Previous Node Output: ${JSON.stringify(context.previousOutput)}
- Expected Input: ${JSON.stringify(context.expectedInput)}

Provide:
1. A simple explanation of why it failed
2. Step-by-step guidance to fix it
3. Suggest what to check

Keep it conversational and supportive.
      `
    });
    
    // Extract steps and suggestions
    const steps = this.extractSteps(answer);
    const suggestions = await this.generateSuggestions(context);
    
    return {
      answer,
      steps,
      suggestions,
      relatedDocs: await this.findRelatedDocs(context)
    };
  }
}
```

**Benefits:**
- ✅ **Plain English**: Everyone understands the workflow
- ✅ **Visual Guides**: Highlighted connections and data flow
- ✅ **Inline Examples**: See what each step does with real data
- ✅ **Progressive Disclosure**: Simple by default, advanced on demand
- ✅ **AI Tutor**: Get help when stuck
- ✅ **Learning Tool**: Understand workflows deeply

---

### 6.8 Natural Language Debugging (Comprehensive)

The natural language debugging system allows users to ask questions about failures in plain English and get AI-powered explanations with suggested fixes.

---

#### **Conversational Debug System**

```typescript
interface DebugSession {
  sessionId: string;
  workflowId: string;
  executionId: string;
  failurePoint: Node;
  conversation: DebugMessage[];
  timeline: DebugTimeline;
  suggestedFixes: Fix[];
  appliedFixes: AppliedFix[];
}

interface DebugMessage {
  role: 'user' | 'ai' | 'system';
  content: string;
  timestamp: Date;
  attachments?: {
    logs?: string[];
    code?: string;
    visualization?: string;
  };
}

class NaturalLanguageDebugger {
  private llm: LLMClient;
  private logAnalyzer: LogAnalyzer;
  private fixGenerator: FixGenerator;
  
  /**
   * Start debug session
   */
  async startDebugSession(
    executionId: string,
    error: ExecutionError
  ): Promise<DebugSession> {
    // 1. Analyze failure
    const analysis = await this.analyzeFailure(executionId, error);
    
    // 2. Generate debug timeline
    const timeline = await this.generateTimeline(executionId, error);
    
    // 3. Generate suggested fixes
    const fixes = await this.generateFixes(analysis);
    
    // 4. Create session
    const session: DebugSession = {
      sessionId: generateUUID(),
      workflowId: analysis.workflowId,
      executionId,
      failurePoint: analysis.failedNode,
      conversation: [
        {
          role: 'ai',
          content: await this.generateInitialMessage(analysis),
          timestamp: new Date(),
          attachments: {
            logs: analysis.relevantLogs,
            visualization: timeline.visualUrl
          }
        }
      ],
      timeline,
      suggestedFixes: fixes,
      appliedFixes: []
    };
    
    return session;
  }
  
  /**
   * Answer user's debug question
   */
  async answerDebugQuestion(
    session: DebugSession,
    question: string
  ): Promise<DebugResponse> {
    // Add user message to conversation
    session.conversation.push({
      role: 'user',
      content: question,
      timestamp: new Date()
    });
    
    // Analyze question intent
    const intent = await this.analyzeIntent(question);
    
    // Generate contextual response
    const response = await this.generateResponse(
      question,
      intent,
      session
    );
    
    // Add AI response to conversation
    session.conversation.push({
      role: 'ai',
      content: response.content,
      timestamp: new Date(),
      attachments: response.attachments
    });
    
    return response;
  }
  
  /**
   * Generate AI response to debug question
   */
  private async generateResponse(
    question: string,
    intent: DebugIntent,
    session: DebugSession
  ): Promise<DebugResponse> {
    // Get execution context
    const execution = await executionService.get(session.executionId);
    const logs = await logService.getLogs(session.executionId);
    
    // Generate response using LLM
    const aiResponse = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
You are a debugging assistant helping a user understand why their workflow failed.

User Question: "${question}"

Workflow Context:
- Failed Node: ${session.failurePoint.type} (${session.failurePoint.data.label})
- Error: ${execution.error.message}
- Error Type: ${execution.error.code}

Execution Logs:
${logs.slice(-20).map(l => `[${l.timestamp}] ${l.level}: ${l.message}`).join('\n')}

Previous Conversation:
${session.conversation.slice(-3).map(m => `${m.role}: ${m.content}`).join('\n')}

Provide:
1. A clear, simple explanation
2. The specific cause of the failure
3. Actionable steps to fix it
4. Any relevant context from the logs

Keep it conversational and supportive. Don't use technical jargon unless necessary.
      `
    });
    
    // Extract code snippets if mentioned
    const codeSnippets = await this.extractCodeSnippets(aiResponse);
    
    // Generate visualization if helpful
    const visualization = await this.shouldVisualize(intent) 
      ? await this.generateVisualization(session, intent)
      : null;
    
    return {
      content: aiResponse,
      attachments: {
        code: codeSnippets.length > 0 ? codeSnippets : undefined,
        visualization
      }
    };
  }
  
  /**
   * Analyze failure and generate initial explanation
   */
  private async analyzeFailure(
    executionId: string,
    error: ExecutionError
  ): Promise<FailureAnalysis> {
    // Get execution details
    const execution = await executionService.get(executionId);
    const logs = await logService.getLogs(executionId);
    
    // Use AI to analyze
    const analysis = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Analyze this workflow execution failure:

Error: ${error.message}
Error Code: ${error.code}
Stack Trace: ${error.stack}

Recent Logs:
${logs.slice(-50).map(l => `[${l.level}] ${l.message}`).join('\n')}

Identify:
1. Root cause of the failure
2. Which node/step failed
3. Why it failed
4. What data caused the failure
5. Relevant log entries

Respond in JSON:
{
  "rootCause": "description",
  "failedNode": "node-id",
  "reason": "explanation",
  "problematicData": {...},
  "relevantLogs": ["log1", "log2"]
}
      `
    });
    
    return JSON.parse(analysis);
  }
  
  /**
   * Generate suggested fixes
   */
  private async generateFixes(
    analysis: FailureAnalysis
  ): Promise<Fix[]> {
    const fixes: Fix[] = [];
    
    // Use AI to suggest fixes
    const suggestions = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Based on this failure analysis, suggest 3-5 specific fixes:

Root Cause: ${analysis.rootCause}
Failed Node: ${analysis.failedNode}
Reason: ${analysis.reason}

For each fix, provide:
1. A clear title
2. Description of what it does
3. Confidence level (0-100)
4. Specific implementation steps

Respond in JSON array format.
      `
    });
    
    const suggestedFixes = JSON.parse(suggestions);
    
    // Convert to Fix objects with implementation
    for (const suggestion of suggestedFixes) {
      fixes.push({
        id: generateUUID(),
        title: suggestion.title,
        description: suggestion.description,
        confidence: suggestion.confidence,
        type: this.determineFix Type(suggestion),
        implementation: await this.generateFixImplementation(suggestion, analysis),
        oneClick: true
      });
    }
    
    // Sort by confidence
    fixes.sort((a, b) => b.confidence - a.confidence);
    
    return fixes;
  }
  
  /**
   * Generate fix implementation
   */
  private async generateFixImplementation(
    suggestion: any,
    analysis: FailureAnalysis
  ): Promise<FixImplementation> {
    switch (suggestion.type) {
      case 'add-node':
        return {
          type: 'add-node',
          nodeType: suggestion.nodeType,
          position: suggestion.position,
          config: suggestion.config
        };
        
      case 'modify-config':
        return {
          type: 'modify-config',
          nodeId: analysis.failedNode,
          changes: suggestion.changes
        };
        
      case 'add-error-handling':
        return {
          type: 'add-error-handling',
          nodeId: analysis.failedNode,
          handler: suggestion.handler
        };
        
      default:
        return {
          type: 'custom',
          instructions: suggestion.steps
        };
    }
  }
  
  /**
   * Apply fix with one click
   */
  async applyFix(
    session: DebugSession,
    fixId: string
  ): Promise<ApplyResult> {
    const fix = session.suggestedFixes.find(f => f.id === fixId);
    if (!fix) {
      throw new Error('Fix not found');
    }
    
    try {
      // Apply the fix
      const result = await this.executeFix(fix, session);
      
      // Record applied fix
      session.appliedFixes.push({
        fixId,
        appliedAt: new Date(),
        success: result.success
      });
      
      // Notify user
      await this.notifyFixApplied(session, fix, result);
      
      return result;
      
    } catch (error) {
      return {
        success: false,
        error: error.message
      };
    }
  }
}

/**
 * Debug Timeline Visualization
 */
class DebugTimelineGenerator {
  /**
   * Generate visual timeline of execution
   */
  async generateTimeline(
    executionId: string,
    error: ExecutionError
  ): Promise<DebugTimeline> {
    const execution = await executionService.get(executionId);
    const events = await this.getExecutionEvents(executionId);
    
    return {
      events: events.map(event => ({
        timestamp: event.timestamp,
        nodeId: event.nodeId,
        type: event.type,
        status: event.nodeId === error.nodeId ? 'failed' : 'success',
        duration: event.duration,
        highlight: event.nodeId === error.nodeId
      })),
      failurePoint: {
        nodeId: error.nodeId,
        timestamp: error.timestamp,
        index: events.findIndex(e => e.nodeId === error.nodeId)
      },
      visualUrl: await this.generateVisualization(events, error)
    };
  }
}

/**
 * Re-run from Any Point
 */
class PartialRerunSystem {
  /**
   * Re-run workflow from specific node
   */
  async rerunFromNode(
    executionId: string,
    startNodeId: string,
    mockData?: any
  ): Promise<ExecutionResult> {
    // Get original execution state at that point
    const checkpoint = await this.getCheckpoint(executionId, startNodeId);
    
    // Inject mock data if provided
    if (mockData) {
      checkpoint.state = { ...checkpoint.state, ...mockData };
    }
    
    // Resume execution from checkpoint
    return await workflowExecutor.resumeFrom(checkpoint);
  }
}
```

**Benefits:**
- ✅ **Natural Questions**: Ask "why did step 3 fail?" in plain English
- ✅ **AI Analysis**: Automatic log analysis and failure detection
- ✅ **Suggested Fixes**: AI-generated solutions with one-click apply
- ✅ **Visual Timeline**: See exactly where workflow failed
- ✅ **Partial Re-run**: Test fixes without full workflow execution
- ✅ **Learning Tool**: Understand failures deeply

---

### 6.9 Multimodal UX (Comprehensive)

```typescript
class MultimodalHandler {
  /**
   * Handle drag and drop of various file types
   */
  async handleFileDrop(
    files: File[],
    context: ChatContext
  ): Promise<ProcessingResult[]> {
    const results: ProcessingResult[] = [];
    
    for (const file of files) {
      // 1. Detect file type
      const fileType = await this.detectFileType(file);
      
      // 2. Show preview
      const preview = await this.generatePreview(file, fileType);
      await this.showPreview(preview);
      
      // 3. Auto-generate processing workflow
      const workflow = await this.suggestWorkflow(file, fileType, context);
      
      // 4. Ask user for confirmation or customization
      const userIntent = await this.askUserIntent(file, workflow);
      
      // 5. Process file
      const result = await this.processFile(file, userIntent);
      results.push(result);
    }
    
    return results;
  }
  
  /**
   * Suggest workflow based on file type
   */
  private async suggestWorkflow(
    file: File,
    fileType: FileType,
    context: ChatContext
  ): Promise<SuggestedWorkflow> {
    const suggestions: Record<FileType, WorkflowTemplate> = {
      'pdf': {
        name: 'PDF Processing',
        actions: [
          'Extract text',
          'Summarize content',
          'Send to Notion',
          'Generate Q&A'
        ]
      },
      'image': {
        name: 'Image Processing',
        actions: [
          'Extract text (OCR)',
          'Describe image (AI)',
          'Compress image',
          'Upload to cloud'
        ]
      },
      'audio': {
        name: 'Audio Processing',
        actions: [
          'Transcribe audio',
          'Summarize transcript',
          'Extract action items',
          'Send to Slack'
        ]
      }
    };
    
    return suggestions[fileType];
  }
}
```

**Example Use Cases:**
- ✅ Drop PDF → "Summarize this into Notion"
- ✅ Upload image → "Extract text and send to Slack"
- ✅ Drag audio file → "Transcribe and create meeting notes"

---

### 6.10 Synthetic Test Generator (Comprehensive)

```typescript
class SyntheticTestGenerator {
  /**
   * Generate comprehensive test suite for workflow
   */
  async generateTests(
    workflow: Workflow
  ): Promise<TestSuite> {
    const tests: Test[] = [];
    
    // 1. Generate happy path tests
    tests.push(...await this.generateHappyPathTests(workflow));
    
    // 2. Generate edge case tests
    tests.push(...await this.generateEdgeCaseTests(workflow));
    
    // 3. Generate error scenario tests
    tests.push(...await this.generateErrorTests(workflow));
    
    // 4. Generate load tests
    tests.push(...await this.generateLoadTests(workflow));
    
    return {
      workflowId: workflow.id,
      tests,
      coverage: await this.calculateCoverage(workflow, tests),
      estimatedDuration: this.estimateTestDuration(tests)
    };
  }
  
  /**
   * Generate edge case tests using AI
   */
  private async generateEdgeCaseTests(
    workflow: Workflow
  ): Promise<Test[]> {
    const edgeCases = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Generate 10 edge case test scenarios for this workflow:

Workflow: ${workflow.name}
Nodes: ${workflow.nodes.map(n => n.type).join(', ')}

Consider:
- Empty inputs
- Maximum length inputs
- Special characters
- Null values
- Boundary conditions
- Concurrent executions

Respond with JSON array of test cases.
      `
    });
    
    return JSON.parse(edgeCases);
  }
}
```

**Benefits:**
- ✅ Automatic test generation
- ✅ Comprehensive coverage
- ✅ Edge case detection
- ✅ Continuous validation

---

### 6.11 Replay & Time-Travel (Comprehensive)

```typescript
class ExecutionReplaySystem {
  /**
   * Replay past execution with exact conditions
   */
  async replayExecution(
    executionId: string,
    options?: ReplayOptions
  ): Promise<ReplayResult> {
    // 1. Load execution snapshot
    const snapshot = await this.loadSnapshot(executionId);
    
    // 2. Restore execution state
    const restoredState = await this.restoreState(snapshot);
    
    // 3. Replay step-by-step
    const replay = await this.executeReplay(restoredState, options);
    
    return replay;
  }
  
  /**
   * Time-travel debugging - step through history
   */
  async timeTravelDebug(
    executionId: string
  ): Promise<TimeTravelSession> {
    const checkpoints = await this.loadCheckpoints(executionId);
    
    return {
      checkpoints,
      currentIndex: 0,
      stepForward: async () => this.step(1),
      stepBackward: async () => this.step(-1),
      jumpTo: async (index: number) => this.jumpToCheckpoint(index),
      getStateAt: async (index: number) => checkpoints[index].state
    };
  }
  
  /**
   * Compare executions side-by-side
   */
  async compareExecutions(
    execId1: string,
    execId2: string
  ): Promise<ExecutionComparison> {
    const exec1 = await this.loadExecution(execId1);
    const exec2 = await this.loadExecution(execId2);
    
    return {
      differences: await this.findDifferences(exec1, exec2),
      inputs: { exec1: exec1.input, exec2: exec2.input },
      outputs: { exec1: exec1.output, exec2: exec2.output },
      durations: { exec1: exec1.duration, exec2: exec2.duration },
      visualization: await this.visualizeComparison(exec1, exec2)
    };
  }
}
```

**Benefits:**
- ✅ Debug by replaying exact conditions
- ✅ Step through execution history
- ✅ Compare different runs
- ✅ Simulate workflow changes safely

---

### 6.12 Guided Templates (Comprehensive)

```typescript
class TemplateMarketplace {
  /**
   * Recommend templates based on user requirements
   */
  async recommendTemplates(
    userRequirements: string
  ): Promise<RecommendedTemplate[]> {
    // Use AI to analyze requirements
    const analysis = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Analyze these requirements and recommend 3-5 workflow templates:

Requirements: "${userRequirements}"

Available templates:
- HR Bot: Automate HR inquiries and onboarding
- Invoice Extractor: Extract data from invoices
- Support Summarizer: Summarize support tickets
- Lead Qualifier: Score and route sales leads
- Content Generator: Generate marketing content
- Data Pipeline: ETL and data transformation
- Chatbot: Customer service chatbot
- Email Automation: Automated email workflows

For each recommendation, provide:
1. Template name
2. Relevance score (0-100)
3. Why it matches
4. What to customize

Respond in JSON.
      `
    });
    
    const recommendations = JSON.parse(analysis);
    
    // Load full templates
    return await Promise.all(
      recommendations.map(r => this.loadTemplate(r.templateName))
    );
  }
  
  /**
   * Walkthrough mode - demonstrate template with live data
   */
  async runWalkthrough(
    templateId: string,
    userData: any
  ): Promise<WalkthroughSession> {
    const template = await this.loadTemplate(templateId);
    
    // Execute template with user's data
    const result = await this.executeTemplate(template, {
      input: userData,
      mode: 'demo',
      explainSteps: true
    });
    
    return {
      steps: result.steps.map(step => ({
        nodeId: step.nodeId,
        explanation: step.explanation,
        input: step.input,
        output: step.output,
        duration: step.duration
      })),
      finalOutput: result.output,
      recording: result.recording
    };
  }
  
  /**
   * AI auto-checks templates for compatibility
   */
  async autoCheckTemplate(
    template: WorkflowTemplate
  ): Promise<TemplateHealthCheck> {
    const checks = {
      apiCompatibility: await this.checkAPIs(template),
      dependencyVersions: await this.checkDependencies(template),
      securityIssues: await this.scanSecurity(template),
      performance: await this.benchmarkTemplate(template)
    };
    
    return {
      healthy: Object.values(checks).every(c => c.passed),
      checks,
      lastChecked: new Date(),
      badge: this.determineBadge(checks)
    };
  }
}

/**
 * Template Quality System
 */
interface TemplateQuality {
  verification: {
    verifiedByExperts: boolean;
    expertName?: string;
    verifiedAt?: Date;
  };
  versioning: {
    currentVersion: string;
    lastUpdated: Date;
    changelog: ChangelogEntry[];
  };
  ratings: {
    averageRating: number;
    totalRatings: number;
    reviews: Review[];
  };
  usage: {
    installCount: number;
    activeUsers: number;
    successRate: number;
  };
}
```

**Template Categories:**
- ✅ Business automation (invoicing, HR, customer support)
- ✅ Data processing (ETL, reporting, analytics)
- ✅ AI applications (chatbots, content generation)
- ✅ Integration workflows (API connectors, data sync)

---

### 6.13 Interactive Onboarding (Comprehensive)

```typescript
class OnboardingSystem {
  /**
   * Start interactive onboarding
   */
  async startOnboarding(userId: string): Promise<OnboardingSession> {
    // 1. First-run setup
    const setup = await this.runFirstTimeSetup();
    
    // 2. Create session
    const session: OnboardingSession = {
      userId,
      steps: await this.generateOnboardingSteps(setup),
      currentStep: 0,
      progress: 0,
      completedSteps: [],
      preferences: setup.preferences
    };
    
    // 3. Start welcome tour
    await this.startWelcomeTour(session);
    
    return session;
  }
  
  /**
   * First-run setup with hardware detection
   */
  private async runFirstTimeSetup(): Promise<FirstRunSetup> {
    // Detect hardware
    const hardware = await hardwareDetector.detect();
    
    // Recommend model sizes
    const modelRecommendations = await modelSelector.recommend(hardware);
    
    // Ask about SaaS account
    const accountChoice = await this.askAccountChoice();
    
    return {
      hardware,
      modelRecommendations,
      accountChoice,
      preferences: {
        interface: 'beginner',
        autoExplain: true,
        showTutorials: true
      }
    };
  }
  
  /**
   * Interactive chat-driven workflow creation
   */
  async createFirstWorkflow(
    session: OnboardingSession
  ): Promise<Workflow> {
    const chat = await this.startGuidedChat(session);
    
    // Guide user through workflow creation
    chat.send(`
Let's create your first workflow together! 

What would you like to automate? Some ideas:
• Summarize emails daily
• Process invoice images
• Monitor social media mentions
• Generate content with AI

Just describe what you want in plain English.
    `);
    
    // Wait for user response
    const userIdea = await chat.waitForResponse();
    
    // Create workflow from idea
    const workflow = await workflowGenerator.createFrom(userIdea);
    
    // Show workflow with explanations
    await this.explainWorkflow(workflow, chat);
    
    // Execute as demo
    await this.runDemo(workflow, chat);
    
    return workflow;
  }
  
  /**
   * Contextual help system
   */
  async showContextualHelp(
    context: HelpContext
  ): Promise<void> {
    const helpContent = await this.getHelpFor(context);
    
    // Show help tooltip at relevant position
    await uiService.showTooltip({
      position: context.position,
      content: helpContent,
      actions: [
        { label: 'Got it', action: 'dismiss' },
        { label: 'Learn more', action: 'openDocs' }
      ]
    });
  }
}
```

**Benefits:**
- ✅ Chat-driven setup
- ✅ Hardware-aware recommendations
- ✅ Interactive tutorials
- ✅ Quick wins to build confidence

---

### 6.14 Undo/Redo & Version History (Comprehensive)

```typescript
class VersionControlSystem {
  private history: WorkflowVersion[] = [];
  private currentIndex: number = 0;
  
  /**
   * Full undo/redo support
   */
  async undo(): Promise<Workflow> {
    if (this.currentIndex <= 0) {
      throw new Error('Nothing to undo');
    }
    
    this.currentIndex--;
    return this.history[this.currentIndex].workflow;
  }
  
  async redo(): Promise<Workflow> {
    if (this.currentIndex >= this.history.length - 1) {
      throw new Error('Nothing to redo');
    }
    
    this.currentIndex++;
    return this.history[this.currentIndex].workflow;
  }
  
  /**
   * Save workflow version
   */
  async saveVersion(
    workflow: Workflow,
    message?: string
  ): Promise<WorkflowVersion> {
    const version: WorkflowVersion = {
      id: generateUUID(),
      workflow: cloneDeep(workflow),
      message: message || 'Auto-saved',
      timestamp: new Date(),
      author: currentUser.id,
      changes: this.calculateChanges(workflow)
    };
    
    // Truncate forward history if we're not at the end
    if (this.currentIndex < this.history.length - 1) {
      this.history = this.history.slice(0, this.currentIndex + 1);
    }
    
    this.history.push(version);
    this.currentIndex = this.history.length - 1;
    
    // Auto-commit to Git if enabled
    if (gitIntegration.enabled) {
      await gitIntegration.commit(workflow, message);
    }
    
    return version;
  }
  
  /**
   * Visual diff between versions
   */
  async generateDiff(
    versionA: string,
    versionB: string
  ): Promise<VisualDiff> {
    const a = await this.getVersion(versionA);
    const b = await this.getVersion(versionB);
    
    return {
      added: this.findAddedNodes(a, b),
      removed: this.findRemovedNodes(a, b),
      modified: this.findModifiedNodes(a, b),
      visualization: await this.visualizeDiff(a, b)
    };
  }
  
  /**
   * Branching workflows
   */
  async createBranch(
    workflowId: string,
    branchName: string
  ): Promise<WorkflowBranch> {
    const workflow = await this.getWorkflow(workflowId);
    
    const branch: WorkflowBranch = {
      id: generateUUID(),
      name: branchName,
      parentId: workflowId,
      workflow: cloneDeep(workflow),
      createdAt: new Date(),
      author: currentUser.id
    };
    
    await this.saveBranch(branch);
    
    return branch;
  }
  
  /**
   * Merge branches
   */
  async mergeBranch(
    sourceBranch: string,
    targetBranch: string
  ): Promise<MergeResult> {
    const source = await this.getBranch(sourceBranch);
    const target = await this.getBranch(targetBranch);
    
    // Detect conflicts
    const conflicts = await this.detectConflicts(source, target);
    
    if (conflicts.length > 0) {
      return {
        success: false,
        conflicts,
        requiresResolution: true
      };
    }
    
    // Perform merge
    const merged = await this.performMerge(source, target);
    
    return {
      success: true,
      merged,
      conflicts: []
    };
  }
}
```

**Benefits:**
- ✅ Complete undo/redo history
- ✅ Visual diffs
- ✅ Branching for safe experimentation
- ✅ Git integration

---

### 6.15 through 6.19 (Consolidated Implementation)

```typescript
/**
 * 6.15 - Dry-Run & Testing
 */
class DryRunSystem {
  async runDryRun(workflow: Workflow): Promise<DryRunResult> {
    // Generate synthetic data
    const syntheticData = await this.generateSyntheticData(workflow);
    
    // Execute in simulation mode
    const result = await workflowExecutor.execute(workflow, {
      input: syntheticData,
      mode: 'dry-run',
      skipExternalAPIs: true,
      mockResponses: true
    });
    
    return result;
  }
}

/**
 * 6.16 - Mobile-Friendly Interface
 */
class MobileInterface {
  async renderMobile(workflow: Workflow): Promise<MobileView> {
    return {
      layout: 'vertical-stack',
      components: await this.optimizeForMobile(workflow),
      touchGestures: this.enableTouchGestures(),
      responsive: true
    };
  }
}

/**
 * 6.17 - Per-Thread Prompts & Configuration
 */
class ThreadConfigSystem {
  async configureThread(
    edge: WorkflowEdge,
    config: ThreadConfig
  ): Promise<void> {
    edge.data = {
      ...edge.data,
      prompt: config.prompt,
      preprocessing: config.preprocessing,
      postprocessing: config.postprocessing,
      aiEnabled: config.enableAI,
      chainId: generateChainId()
    };
    
    await this.saveEdge(edge);
  }
}

/**
 * 6.18 - Variable Management
 */
class VariableManager {
  /**
   * Automated variable wiring
   */
  async autoWireVariables(
    sourceNode: Node,
    targetNode: Node
  ): Promise<VariableWiring> {
    const compatibility = await this.checkCompatibility(
      sourceNode.outputs,
      targetNode.inputs
    );
    
    return {
      automatic: true,
      mappings: compatibility.map(c => ({
        from: c.sourceOutput,
        to: c.targetInput,
        transform: c.requiredTransform
      }))
    };
  }
}

/**
 * 6.19 - Legacy Project Integration
 */
class LegacyProjectAnalyzer {
  /**
   * Analyze existing project structure
   */
  async analyzeProject(
    projectPath: string
  ): Promise<ProjectAnalysis> {
    // Scan codebase
    const files = await this.scanFiles(projectPath);
    
    // Use AI to understand architecture
    const architecture = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Analyze this project structure and extract:
1. Framework used
2. API endpoints
3. Database schema
4. Dependencies
5. Integration points

Files:
${files.map(f => f.path).join('\n')}
      `
    });
    
    return JSON.parse(architecture);
  }
  
  /**
   * Generate workflows that integrate with existing project
   */
  async generateIntegrationWorkflows(
    project: ProjectAnalysis
  ): Promise<Workflow[]> {
    const workflows: Workflow[] = [];
    
    // Generate workflow for each API endpoint
    for (const endpoint of project.apiEndpoints) {
      workflows.push(await this.createAPIWorkflow(endpoint, project));
    }
    
    return workflows;
  }
}
```

**Benefits (6.15-6.19):**
- ✅ **Dry-Run**: Safe testing before production
- ✅ **Mobile**: Full functionality on mobile devices
- ✅ **Thread Config**: Intelligent routing with per-edge AI
- ✅ **Variable Management**: No complex JSON paths
- ✅ **Legacy Integration**: Works with existing projects

---

**Summary of Section 6 (Automatic UI Generator):**
- ✅ **6.1**: Workflow-to-UI mapping with intelligent screen generation
- ✅ **6.2**: Component tree with Notion-like modular blocks
- ✅ **6.3**: Theme system with light/dark mode
- ✅ **6.4**: Multi design-system support (shadcn, MUI, Ant Design)
- ✅ **6.5**: Responsive layout generation
- ✅ **6.6**: UI quality assurance with WCAG compliance
- ✅ **6.7**: AI-powered explainability mode
- ✅ **6.8**: Natural language debugging with suggested fixes
- ✅ **6.9**: Multimodal UX with drag-and-drop
- ✅ **6.10**: Synthetic test generation
- ✅ **6.11**: Replay and time-travel debugging
- ✅ **6.12**: Guided templates with AI recommendations
- ✅ **6.13**: Interactive onboarding with chat-driven setup
- ✅ **6.14**: Complete version control with Git integration
- ✅ **6.15-6.19**: Dry-run, mobile, thread config, variables, legacy integration

---

### 6.14 Undo/Redo & Version History

**Edit History:**
- **Undo/Redo**: Full undo/redo support for all workflow edits
- **Version History**: Complete version history of workflow changes
- **Safe Iterative Editing**: Experiment freely with ability to revert
- **Version Comparison**: Compare different versions side-by-side
- **Rollback**: Rollback to any previous version
- **Visual Diffs**: Show what changed in workflows with visual diff view
- **Branching Workflows**: Create branches to test ideas without breaking production
- **Native Git Integration**: Auto-commit history with Git integration for version control

**Benefits:**
- Fearless experimentation
- Easy recovery from mistakes
- Track changes over time
- Collaborative editing safety
- Clear change visualization
- Safe experimentation with branches
- Professional version control

### 6.15 Dry-Run & Testing

**Pre-Execution Testing:**
- **Dry-Run Mode**: Test workflow on synthetic data before real execution
- **One-Click Run**: Execute workflow with single click
- **Synthetic Data Generation**: Auto-generate test data for dry-runs
- **Validation Before Execution**: Validate workflow before running on real data

**Benefits:**
- Catch errors before production
- Test without costs
- Validate workflow logic
- Safe experimentation

### 6.16 Mobile-Friendly Interface

**Mobile Support:**
- **Mobile Run & Logs**: View workflow runs and logs on mobile devices
- **Responsive Design**: Full functionality on mobile browsers
- **Mobile Alerts**: Receive alerts and notifications on mobile
- **Touch-Optimized**: Touch-friendly interface for mobile users

**Mobile Features:**
- View execution status
- Monitor workflow progress
- Receive alerts and notifications
- Basic workflow management

### 6.17 Per-Thread Prompts & Configuration

**Thread-Level Customization:**
- **Thread Prompts**: Each edge/thread can have its own prompt/config
- **Pre/Post Processing**: Define behavior when moving from node A → B
- **Thread Configuration**: Customize transitions between nodes
- **Dynamic Behavior**: Enable deterministic flows with dynamic thread behavior
- **No Rigid Boxes**: Complete flexibility to prompt even in threads for full customization
- **Thread-Level AI**: AI can be invoked at thread level for intelligent routing and processing
- **Thread-Level Orchestration Metadata**: ChainId and tracing extended to threads/edges for complete observability
- **Thread Tracing**: Track data flow and transformations at thread level

**Use Cases:**
- Filter data between nodes
- Transform data during transitions
- Conditional routing based on thread prompts
- Custom processing between steps
- Intelligent data transformation
- Context-aware routing
- Complete workflow observability

### 6.18 Variable Management

**Easy Variable Passing:**
- **Automated Variable Management**: Automatic variable passing between nodes (no complex JSON paths)
- **Visual Variable Editor**: Visual interface for managing variables
- **Type-Safe Variables**: Type checking and validation for variables
- **Variable Scope**: Define variable scope (global, workflow, node-level)
- **Variable Templates**: Pre-defined variable templates for common use cases

**Benefits:**
- No complex JSON path manipulation
- Intuitive variable management
- Reduced errors in variable passing
- Better workflow readability

### 6.19 Legacy Project Integration

**Existing Project Support:**
- **Project Analysis**: Analyze existing/legacy projects to understand structure
- **Codebase Understanding**: AI understands existing codebase patterns and conventions
- **Project-Aware Integration**: Automatically detect and integrate with current or legacy projects
- **Integration Workflow**: Create workflows that integrate with existing projects
- **API Extraction**: Extract APIs and interfaces from existing projects
- **Dependency Mapping**: Map dependencies and relationships in existing projects

**Integration Features:**
- Import existing project structure
- Understand project architecture
- Generate compatible workflows
- Maintain project conventions
- **AI Integration**: AI learns from existing projects to maintain consistency
- **Automatic Detection**: System automatically detects project structure and suggests integration points

---

## 7. Automatic Deployment & Build

The automatic deployment and build system generates production-ready builds for Android, Windows, macOS, and web platforms with optimization, code signing, and validation.

---

### 7.1 Android APK Generation (Comprehensive)

The Android build system automatically generates optimized, signed APK files ready for distribution through Google Play Store or direct installation.

---

#### **Android Build Pipeline**

```typescript
interface AndroidBuildConfig {
  appName: string;
  packageName: string;  // e.g., com.company.appname
  version: string;
  versionCode: number;
  
  // Build configuration
  buildType: 'debug' | 'release';
  minSdkVersion: number;
  targetSdkVersion: number;
  
  // Signing
  keystore?: KeystoreConfig;
  
  // Optimization
  enableProguard: boolean;
  enableR8: boolean;
  shrinkResources: boolean;
  minifyEnabled: boolean;
  
  // Permissions
  permissions: AndroidPermission[];
  
  // Features
  features: string[];
}

interface KeystoreConfig {
  path: string;
  password: string;
  keyAlias: string;
  keyPassword: string;
}

class AndroidAPKBuilder {
  private reactNativeCLI: ReactNativeCLI;
  private flutterSDK?: FlutterSDK;
  private gradleExecutor: GradleExecutor;
  
  /**
   * Build Android APK from workflow
   */
  async buildAPK(
    workflow: Workflow,
    config: AndroidBuildConfig
  ): Promise<AndroidBuildResult> {
    // 1. Validate environment
    await this.validateEnvironment();
    
    // 2. Initialize React Native project
    const projectPath = await this.initializeProject(workflow, config);
    
    // 3. Configure Android project
    await this.configureAndroidProject(projectPath, config);
    
    // 4. Generate app code from workflow
    await this.generateAppCode(workflow, projectPath);
    
    // 5. Build APK
    const apkPath = await this.buildAPKFile(projectPath, config);
    
    // 6. Sign APK
    const signedApk = await this.signAPK(apkPath, config);
    
    // 7. Optimize APK
    const optimizedApk = await this.optimizeAPK(signedApk, config);
    
    // 8. Validate APK
    const validation = await this.validateAPK(optimizedApk);
    
    // 9. Export APK
    const exportPath = await this.exportAPK(optimizedApk, config);
    
    return {
      success: true,
      apkPath: exportPath,
      size: await this.getFileSize(exportPath),
      validation,
      metadata: {
        packageName: config.packageName,
        version: config.version,
        versionCode: config.versionCode,
        minSdkVersion: config.minSdkVersion,
        targetSdkVersion: config.targetSdkVersion
      }
    };
  }
  
  /**
   * Validate Android development environment
   */
  private async validateEnvironment(): Promise<void> {
    const checks = {
      androidSDK: await this.checkAndroidSDK(),
      jdk: await this.checkJDK(),
      gradle: await this.checkGradle(),
      buildTools: await this.checkBuildTools()
    };
    
    const failures = Object.entries(checks)
      .filter(([_, passed]) => !passed)
      .map(([tool]) => tool);
    
    if (failures.length > 0) {
      throw new Error(
        `Missing required tools: ${failures.join(', ')}. ` +
        `Please install Android development tools.`
      );
    }
  }
  
  /**
   * Initialize React Native project structure
   */
  private async initializeProject(
    workflow: Workflow,
    config: AndroidBuildConfig
  ): Promise<string> {
    const projectPath = path.join(
      TEMP_DIR,
      `android-${workflow.id}-${Date.now()}`
    );
    
    // Create React Native project
    await this.reactNativeCLI.init({
      projectName: config.appName,
      projectPath,
      template: 'react-native-template-typescript'
    });
    
    return projectPath;
  }
  
  /**
   * Configure Android-specific settings
   */
  private async configureAndroidProject(
    projectPath: string,
    config: AndroidBuildConfig
  ): Promise<void> {
    // 1. Configure build.gradle
    await this.configureBuildGradle(projectPath, config);
    
    // 2. Configure AndroidManifest.xml
    await this.configureManifest(projectPath, config);
    
    // 3. Configure app-level build.gradle
    await this.configureAppBuildGradle(projectPath, config);
    
    // 4. Configure ProGuard/R8 rules
    if (config.enableProguard || config.enableR8) {
      await this.configureProguardRules(projectPath);
    }
    
    // 5. Configure signing config
    if (config.keystore) {
      await this.configureSigningConfig(projectPath, config.keystore);
    }
  }
  
  /**
   * Configure build.gradle file
   */
  private async configureBuildGradle(
    projectPath: string,
    config: AndroidBuildConfig
  ): Promise<void> {
    const buildGradlePath = path.join(projectPath, 'android', 'app', 'build.gradle');
    
    const buildGradleContent = `
apply plugin: "com.android.application"

android {
    compileSdkVersion ${config.targetSdkVersion}
    
    defaultConfig {
        applicationId "${config.packageName}"
        minSdkVersion ${config.minSdkVersion}
        targetSdkVersion ${config.targetSdkVersion}
        versionCode ${config.versionCode}
        versionName "${config.version}"
    }
    
    buildTypes {
        release {
            minifyEnabled ${config.minifyEnabled}
            shrinkResources ${config.shrinkResources}
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
            ${config.keystore ? `
            signingConfig signingConfigs.release
            ` : ''}
        }
    }
    
    ${config.keystore ? `
    signingConfigs {
        release {
            storeFile file("${config.keystore.path}")
            storePassword "${config.keystore.password}"
            keyAlias "${config.keystore.keyAlias}"
            keyPassword "${config.keyPassword}"
        }
    }
    ` : ''}
}

dependencies {
    implementation "com.facebook.react:react-native:+"
    // Auto-linked dependencies
}
    `.trim();
    
    await fs.writeFile(buildGradlePath, buildGradleContent);
  }
  
  /**
   * Configure AndroidManifest.xml
   */
  private async configureManifest(
    projectPath: string,
    config: AndroidBuildConfig
  ): Promise<void> {
    const manifestPath = path.join(
      projectPath,
      'android',
      'app',
      'src',
      'main',
      'AndroidManifest.xml'
    );
    
    const manifest = `
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="${config.packageName}">
    
    <!-- Permissions -->
    ${config.permissions.map(p => `<uses-permission android:name="${p}" />`).join('\n    ')}
    
    <!-- Features -->
    ${config.features.map(f => `<uses-feature android:name="${f}" android:required="false" />`).join('\n    ')}
    
    <application
        android:name=".MainApplication"
        android:label="${config.appName}"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:allowBackup="false"
        android:theme="@style/AppTheme">
        
        <activity
            android:name=".MainActivity"
            android:label="${config.appName}"
            android:configChanges="keyboard|keyboardHidden|orientation|screenSize|uiMode"
            android:launchMode="singleTask"
            android:windowSoftInputMode="adjustResize"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
    `.trim();
    
    await fs.writeFile(manifestPath, manifest);
  }
  
  /**
   * Build APK using Gradle
   */
  private async buildAPKFile(
    projectPath: string,
    config: AndroidBuildConfig
  ): Promise<string> {
    const androidPath = path.join(projectPath, 'android');
    
    // Run Gradle build
    await this.gradleExecutor.execute(androidPath, [
      'assembleRelease',
      '--no-daemon',
      '--parallel'
    ], {
      env: {
        ...process.env,
        JAVA_HOME: await this.getJavaHome()
      }
    });
    
    // Find generated APK
    const apkPath = path.join(
      androidPath,
      'app',
      'build',
      'outputs',
      'apk',
      'release',
      'app-release.apk'
    );
    
    if (!await fs.pathExists(apkPath)) {
      throw new Error('APK build failed: output file not found');
    }
    
    return apkPath;
  }
  
  /**
   * Sign APK with keystore
   */
  private async signAPK(
    apkPath: string,
    config: AndroidBuildConfig
  ): Promise<string> {
    if (!config.keystore) {
      // For debug builds, already signed
      return apkPath;
    }
    
    // APK is already signed during build if signing config is set
    // Verify signature
    const verification = await this.verifyAPKSignature(apkPath);
    
    if (!verification.valid) {
      throw new Error('APK signature verification failed');
    }
    
    return apkPath;
  }
  
  /**
   * Optimize APK size
   */
  private async optimizeAPK(
    apkPath: string,
    config: AndroidBuildConfig
  ): Promise<string> {
    // 1. Remove unused resources (if enabled)
    if (config.shrinkResources) {
      // Already handled by Gradle shrinkResources
    }
    
    // 2. Compress assets
    const optimizedPath = apkPath.replace('.apk', '-optimized.apk');
    await this.compressAPK(apkPath, optimizedPath);
    
    // 3. Zipalign for faster loading
    const alignedPath = optimizedPath.replace('.apk', '-aligned.apk');
    await this.zipalignAPK(optimizedPath, alignedPath);
    
    return alignedPath;
  }
  
  /**
   * Validate APK before export
   */
  private async validateAPK(apkPath: string): Promise<APKValidation> {
    const validation: APKValidation = {
      valid: true,
      checks: {}
    };
    
    // 1. Check file integrity
    validation.checks.fileIntegrity = await this.checkFileIntegrity(apkPath);
    
    // 2. Verify signature
    validation.checks.signature = await this.verifyAPKSignature(apkPath);
    
    // 3. Check APK structure
    validation.checks.structure = await this.checkAPKStructure(apkPath);
    
    // 4. Analyze APK size
    const size = await this.getFileSize(apkPath);
    validation.checks.size = {
      valid: size < 100 * 1024 * 1024,  // < 100MB
      size,
      warning: size > 50 * 1024 * 1024 ? 'APK size is large' : null
    };
    
    // 5. Test installation (optional, requires emulator)
    if (await this.isEmulatorAvailable()) {
      validation.checks.installation = await this.testInstallation(apkPath);
    }
    
    validation.valid = Object.values(validation.checks).every(c => c.valid);
    
    return validation;
  }
  
  /**
   * Export APK to downloads folder
   */
  private async exportAPK(
    apkPath: string,
    config: AndroidBuildConfig
  ): Promise<string> {
    const exportDir = path.join(EXPORTS_DIR, 'android');
    await fs.ensureDir(exportDir);
    
    const exportPath = path.join(
      exportDir,
      `${config.appName}-v${config.version}-${config.buildType}.apk`
    );
    
    await fs.copy(apkPath, exportPath);
    
    // Generate installation instructions
    await this.generateInstallationInstructions(exportPath, config);
    
    return exportPath;
  }
  
  /**
   * Generate installation instructions
   */
  private async generateInstallationInstructions(
    apkPath: string,
    config: AndroidBuildConfig
  ): Promise<void> {
    const instructions = `
# Installation Instructions for ${config.appName}

## Prerequisites
- Android device running Android ${this.getAndroidVersionName(config.minSdkVersion)} or higher
- "Unknown sources" enabled in device settings

## Installation Steps

### Method 1: Direct Installation
1. Transfer the APK file to your Android device
2. Open the file manager on your device
3. Locate and tap the APK file
4. Tap "Install" when prompted
5. Wait for installation to complete
6. Tap "Open" to launch the app

### Method 2: ADB Installation
1. Connect your Android device to computer via USB
2. Enable USB debugging on device
3. Run: adb install ${path.basename(apkPath)}
4. Launch app from device

## Troubleshooting

**Installation Blocked**
- Enable "Install unknown apps" in Settings > Security

**App Not Installed**
- Make sure you have enough storage space
- Try uninstalling previous version first

**App Crashes**
- Make sure your Android version is ${config.minSdkVersion}+
- Clear app data and retry

## Package Information
- Package Name: ${config.packageName}
- Version: ${config.version} (${config.versionCode})
- Min Android Version: ${this.getAndroidVersionName(config.minSdkVersion)}

---
Generated by OLAI on ${new Date().toLocaleString()}
    `.trim();
    
    const instructionsPath = apkPath.replace('.apk', '-INSTALL.md');
    await fs.writeFile(instructionsPath, instructions);
  }
}
```

**Benefits:**
- ✅ **Automated Build**: Complete APK generation from workflow
- ✅ **Code Signing**: Automatic signing with keystore
- ✅ **Optimization**: ProGuard/R8 code shrinking and obfuscation
- ✅ **Validation**: Comprehensive APK validation before export
- ✅ **Size Optimization**: Resource shrinking and compression
- ✅ **Installation Guide**: Auto-generated instructions

---

### 7.2 Windows EXE Generation (Comprehensive)

The Windows build system supports both Electron and Tauri approaches, generating optimized desktop applications with installers and auto-update capabilities.

---

#### **Windows Desktop Builder**

```typescript
interface WindowsBuildConfig {
  appName: string;
  appId: string;  // e.g., com.company.appname
  version: string;
  
  // Build approach
  framework: 'electron' | 'tauri';
  
  // Application metadata
  description: string;
  author: string;
  homepage?: string;
  
  // Installer configuration
  installerType: 'nsis' | 'squirrel' | 'wix' | 'portable';
  
  // Code signing
  codeSign?: CodeSignConfig;
  
  // Auto-updater
  autoUpdate?: AutoUpdateConfig;
  
  // Windows-specific
  requestedExecutionLevel?: 'asInvoker' | 'highestAvailable' | 'requireAdministrator';
  fileAssociations?: FileAssociation[];
  protocols?: ProtocolHandler[];
}

interface CodeSignConfig {
  certificatePath: string;
  certificatePassword: string;
  timestampServer: string;
}

interface AutoUpdateConfig {
  enabled: boolean;
  updateServer: string;
  checkInterval: number;  // hours
}

class WindowsEXEBuilder {
  private electronBuilder?: ElectronBuilder;
  private tauriCLI?: TauriCLI;
  
  /**
   * Build Windows EXE from workflow
   */
  async buildEXE(
    workflow: Workflow,
    config: WindowsBuildConfig
  ): Promise<WindowsBuildResult> {
    // 1. Validate environment
    await this.validateEnvironment(config.framework);
    
    // 2. Initialize project
    const projectPath = await this.initializeProject(workflow, config);
    
    // 3. Generate app code
    await this.generateAppCode(workflow, projectPath, config);
    
    // 4. Configure build
    await this.configureBuild(projectPath, config);
    
    // 5. Build application
    const exePath = config.framework === 'electron'
      ? await this.buildElectronApp(projectPath, config)
      : await this.buildTauriApp(projectPath, config);
    
    // 6. Code sign (if configured)
    if (config.codeSign) {
      await this.signExecutable(exePath, config.codeSign);
    }
    
    // 7. Create installer
    const installerPath = await this.createInstaller(exePath, config);
    
    // 8. Sign installer (if configured)
    if (config.codeSign) {
      await this.signExecutable(installerPath, config.codeSign);
    }
    
    // 9. Validate build
    const validation = await this.validateEXE(installerPath);
    
    // 10. Export
    const exportPath = await this.exportEXE(installerPath, config);
    
    return {
      success: true,
      exePath: exportPath,
      size: await this.getFileSize(exportPath),
      validation,
      metadata: {
        framework: config.framework,
        version: config.version,
        signed: !!config.codeSign
      }
    };
  }
  
  /**
   * Build with Electron
   */
  private async buildElectronApp(
    projectPath: string,
    config: WindowsBuildConfig
  ): Promise<string> {
    // Configure electron-builder
    const electronBuilderConfig = {
      appId: config.appId,
      productName: config.appName,
      directories: {
        output: 'dist'
      },
      win: {
        target: [
          {
            target: config.installerType,
            arch: ['x64', 'arm64']
          }
        ],
        icon: 'build/icon.ico',
        requestedExecutionLevel: config.requestedExecutionLevel || 'asInvoker',
        fileAssociations: config.fileAssociations,
        protocols: config.protocols
      },
      nsis: config.installerType === 'nsis' ? {
        oneClick: false,
        allowToChangeInstallationDirectory: true,
        createDesktopShortcut: true,
        createStartMenuShortcut: true,
        perMachine: false
      } : undefined,
      publish: config.autoUpdate ? {
        provider: 'generic',
        url: config.autoUpdate.updateServer
      } : undefined
    };
    
    // Write config
    await fs.writeJSON(
      path.join(projectPath, 'electron-builder.json'),
      electronBuilderConfig,
      { spaces: 2 }
    );
    
    // Build
    await this.electronBuilder.build({
      projectDir: projectPath,
      platform: 'win',
      config: electronBuilderConfig
    });
    
    // Find generated installer
    const distPath = path.join(projectPath, 'dist');
    const installerFiles = await fs.readdir(distPath);
    const installerFile = installerFiles.find(f => 
      f.endsWith('.exe') || f.endsWith('.msi')
    );
    
    if (!installerFile) {
      throw new Error('Installer build failed: output file not found');
    }
    
    return path.join(distPath, installerFile);
  }
  
  /**
   * Build with Tauri (smaller, faster)
   */
  private async buildTauriApp(
    projectPath: string,
    config: WindowsBuildConfig
  ): Promise<string> {
    // Configure Tauri
    const tauriConfig = {
      package: {
        productName: config.appName,
        version: config.version
      },
      tauri: {
        bundle: {
          identifier: config.appId,
          icon: [
            'icons/32x32.png',
            'icons/128x128.png',
            'icons/icon.ico'
          ],
          windows: {
            certificateThumbprint: config.codeSign?.certificatePath,
            digestAlgorithm: 'sha256',
            timestampUrl: config.codeSign?.timestampServer,
            wix: config.installerType === 'wix' ? {
              language: ['en-US']
            } : undefined,
            nsis: config.installerType === 'nsis' ? {
              installerIcon: 'icons/icon.ico',
              license: 'LICENSE',
              headerImage: 'installer-header.bmp',
              sidebarImage: 'installer-sidebar.bmp'
            } : undefined
          },
          externalBin: [],
          resources: []
        },
        updater: config.autoUpdate ? {
          active: true,
          endpoints: [config.autoUpdate.updateServer],
          dialog: true,
          pubkey: await this.generateUpdatePublicKey()
        } : undefined,
        security: {
          csp: "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
        },
        windows: [
          {
            title: config.appName,
            width: 1280,
            height: 720,
            resizable: true,
            fullscreen: false
          }
        ]
      }
    };
    
    // Write config
    await fs.writeJSON(
      path.join(projectPath, 'src-tauri', 'tauri.conf.json'),
      tauriConfig,
      { spaces: 2 }
    );
    
    // Build
    await this.tauriCLI.build({
      projectDir: projectPath,
      target: 'windows'
    });
    
    // Find generated installer
    const bundlePath = path.join(
      projectPath,
      'src-tauri',
      'target',
      'release',
      'bundle'
    );
    
    const installerFiles = await this.findInstallerFiles(bundlePath);
    
    if (installerFiles.length === 0) {
      throw new Error('Tauri build failed: installer not found');
    }
    
    return installerFiles[0];
  }
  
  /**
   * Sign executable with code signing certificate
   */
  private async signExecutable(
    exePath: string,
    signConfig: CodeSignConfig
  ): Promise<void> {
    // Use signtool.exe (Windows SDK)
    const signtoolPath = await this.findSignTool();
    
    await exec(signtoolPath, [
      'sign',
      '/f', signConfig.certificatePath,
      '/p', signConfig.certificatePassword,
      '/tr', signConfig.timestampServer,
      '/td', 'sha256',
      '/fd', 'sha256',
      '/v',
      exePath
    ]);
    
    // Verify signature
    await this.verifySignature(exePath);
  }
  
  /**
   * Create NSIS installer
   */
  private async createNSISInstaller(
    exePath: string,
    config: WindowsBuildConfig
  ): Promise<string> {
    const nsisScript = `
; NSIS Installer Script for ${config.appName}

!define APP_NAME "${config.appName}"
!define APP_VERSION "${config.version}"
!define APP_PUBLISHER "${config.author}"
!define APP_EXE "${path.basename(exePath)}"

Name "\${APP_NAME}"
OutFile "${config.appName}-Setup-\${APP_VERSION}.exe"
InstallDir "$PROGRAMFILES64\\\${APP_NAME}"

Section "Main Application"
  SetOutPath "$INSTDIR"
  File "${exePath}"
  
  ; Create shortcuts
  CreateDirectory "$SMPROGRAMS\\\${APP_NAME}"
  CreateShortCut "$SMPROGRAMS\\\${APP_NAME}\\\${APP_NAME}.lnk" "$INSTDIR\\\${APP_EXE}"
  CreateShortCut "$DESKTOP\\\${APP_NAME}.lnk" "$INSTDIR\\\${APP_EXE}"
  
  ; Write uninstaller
  WriteUninstaller "$INSTDIR\\Uninstall.exe"
  
  ; Registry keys
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\\${APP_NAME}" "DisplayName" "\${APP_NAME}"
  WriteRegStr HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\\${APP_NAME}" "UninstallString" "$INSTDIR\\Uninstall.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\\\${APP_EXE}"
  Delete "$INSTDIR\\Uninstall.exe"
  Delete "$DESKTOP\\\${APP_NAME}.lnk"
  Delete "$SMPROGRAMS\\\${APP_NAME}\\\${APP_NAME}.lnk"
  RMDir "$SMPROGRAMS\\\${APP_NAME}"
  RMDir "$INSTDIR"
  DeleteRegKey HKLM "Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\\${APP_NAME}"
SectionEnd
    `.trim();
    
    const scriptPath = path.join(TEMP_DIR, 'installer.nsi');
    await fs.writeFile(scriptPath, nsisScript);
    
    // Compile NSIS script
    const makensisPath = await this.findMakeNSIS();
    await exec(makensisPath, [scriptPath]);
    
    return path.join(
      path.dirname(scriptPath),
      `${config.appName}-Setup-${config.version}.exe`
    );
  }
  
  /**
   * Configure auto-updater
   */
  private async configureAutoUpdater(
    projectPath: string,
    config: AutoUpdateConfig
  ): Promise<void> {
    const autoUpdaterCode = `
import { autoUpdater } from 'electron-updater';
import { app } from 'electron';

// Configure
autoUpdater.setFeedURL({
  provider: 'generic',
  url: '${config.updateServer}'
});

// Check for updates on startup
app.on('ready', () => {
  autoUpdater.checkForUpdatesAndNotify();
});

// Check periodically
setInterval(() => {
  autoUpdater.checkForUpdatesAndNotify();
}, ${config.checkInterval * 3600 * 1000});

// Update events
autoUpdater.on('update-available', () => {
  console.log('Update available');
});

autoUpdater.on('update-downloaded', () => {
  console.log('Update downloaded, will install on restart');
});
    `.trim();
    
    const autoUpdaterPath = path.join(projectPath, 'src', 'auto-updater.ts');
    await fs.writeFile(autoUpdaterPath, autoUpdaterCode);
  }
  
  /**
   * Validate EXE before export
   */
  private async validateEXE(exePath: string): Promise<EXEValidation> {
    const validation: EXEValidation = {
      valid: true,
      checks: {}
    };
    
    // 1. File integrity
    validation.checks.fileIntegrity = await this.checkFileIntegrity(exePath);
    
    // 2. Signature verification
    validation.checks.signature = await this.verifySignature(exePath);
    
    // 3. PE format validation
    validation.checks.peFormat = await this.validatePEFormat(exePath);
    
    // 4. Size check
    const size = await this.getFileSize(exePath);
    validation.checks.size = {
      valid: size < 500 * 1024 * 1024,  // < 500MB
      size,
      warning: size > 200 * 1024 * 1024 ? 'EXE size is large' : null
    };
    
    // 5. Dependencies check
    validation.checks.dependencies = await this.checkDependencies(exePath);
    
    validation.valid = Object.values(validation.checks).every(c => c.valid);
    
    return validation;
  }
}

/**
 * Size Comparison: Electron vs Tauri
 */
interface FrameworkComparison {
  electron: {
    baseSize: '~100MB';
    advantages: [
      'Mature ecosystem',
      'Large community',
      'Extensive documentation',
      'Native Node.js support'
    ];
    disadvantages: [
      'Large bundle size',
      'High memory usage',
      'Slower startup time'
    ];
  };
  tauri: {
    baseSize: '~10MB';
    advantages: [
      'Tiny bundle size (10x smaller)',
      'Fast startup time',
      'Low memory usage',
      'Rust performance',
      'Native webview (no Chromium)'
    ];
    disadvantages: [
      'Newer ecosystem',
      'Fewer plugins',
      'Less documentation'
    ];
  };
}
```

**Framework Selection:**
- **Electron**: Best for complex apps needing Node.js APIs
- **Tauri**: Best for lightweight apps, faster performance

**Benefits:**
- ✅ **Dual Framework Support**: Choose Electron or Tauri
- ✅ **Auto-Updater**: Built-in update mechanism
- ✅ **Code Signing**: Professional certificate signing
- ✅ **Multiple Installers**: NSIS, Squirrel, WiX support
- ✅ **Validation**: Comprehensive pre-distribution checks
- ✅ **Size Optimization**: Tauri offers 90% size reduction

---

### 7.3 macOS Build Generation (Comprehensive)

```typescript
interface MacOSBuildConfig {
  appName: string;
  bundleIdentifier: string;  // e.g., com.company.appname
  version: string;
  
  // Framework
  framework: 'electron' | 'tauri';
  
  // Code signing
  codeSign: MacOSCodeSignConfig;
  
  // Notarization
  notarization: NotarizationConfig;
  
  // Distribution
  distributionFormat: 'dmg' | 'pkg' | 'zip';
  
  // macOS specific
  category: string;  // e.g., 'public.app-category.productivity'
  minimumSystemVersion: string;  // e.g., '10.15'
  architectures: ('x64' | 'arm64')[];
}

interface MacOSCodeSignConfig {
  identity: string;  // Developer ID Application: Name (TEAMID)
  entitlements: string;
  hardenedRuntime: boolean;
}

interface NotarizationConfig {
  appleId: string;
  appleIdPassword: string;
  teamId: string;
}

class MacOSAppBuilder {
  /**
   * Build macOS application
   */
  async buildMacOSApp(
    workflow: Workflow,
    config: MacOSBuildConfig
  ): Promise<MacOSBuildResult> {
    // 1. Validate environment (macOS only)
    await this.validateMacEnvironment();
    
    // 2. Initialize project
    const projectPath = await this.initializeProject(workflow, config);
    
    // 3. Generate app code
    await this.generateAppCode(workflow, projectPath, config);
    
    // 4. Build app bundle
    const appPath = await this.buildAppBundle(projectPath, config);
    
    // 5. Code sign with hardened runtime
    await this.signAppBundle(appPath, config.codeSign);
    
    // 6. Notarize with Apple
    await this.notarizeApp(appPath, config.notarization);
    
    // 7. Staple notarization ticket
    await this.stapleNotarization(appPath);
    
    // 8. Create DMG/PKG
    const installerPath = await this.createDistribution(appPath, config);
    
    // 9. Sign installer
    await this.signInstaller(installerPath, config.codeSign);
    
    // 10. Validate
    const validation = await this.validateMacOSApp(installerPath);
    
    // 11. Export
    const exportPath = await this.exportMacOSApp(installerPath, config);
    
    return {
      success: true,
      appPath: exportPath,
      size: await this.getFileSize(exportPath),
      validation,
      metadata: {
        framework: config.framework,
        signed: true,
        notarized: true,
        architectures: config.architectures
      }
    };
  }
  
  /**
   * Code sign app bundle
   */
  private async signAppBundle(
    appPath: string,
    signConfig: MacOSCodeSignConfig
  ): Promise<void> {
    // Sign all nested frameworks and binaries first
    await this.signNestedComponents(appPath, signConfig);
    
    // Sign main app bundle
    await exec('codesign', [
      '--force',
      '--deep',
      '--strict',
      '--options', 'runtime',  // Hardened runtime
      '--entitlements', signConfig.entitlements,
      '--sign', signConfig.identity,
      '--timestamp',
      appPath
    ]);
    
    // Verify signature
    await this.verifyMacSignature(appPath);
  }
  
  /**
   * Notarize app with Apple
   */
  private async notarizeApp(
    appPath: string,
    notarization: NotarizationConfig
  ): Promise<void> {
    console.log('Creating ZIP for notarization...');
    const zipPath = `${appPath}.zip`;
    await exec('ditto', ['-c', '-k', '--keepParent', appPath, zipPath]);
    
    console.log('Submitting for notarization...');
    const result = await exec('xcrun', [
      'notarytool',
      'submit',
      zipPath,
      '--apple-id', notarization.appleId,
      '--password', notarization.appleIdPassword,
      '--team-id', notarization.teamId,
      '--wait'
    ]);
    
    // Parse submission ID
    const submissionId = this.parseSubmissionId(result.stdout);
    
    console.log(`Notarization submitted: ${submissionId}`);
    console.log('Waiting for notarization (this may take several minutes)...');
    
    // Wait for notarization to complete
    await this.waitForNotarization(submissionId, notarization);
    
    // Clean up ZIP
    await fs.remove(zipPath);
  }
  
  /**
   * Staple notarization ticket to app
   */
  private async stapleNotarization(appPath: string): Promise<void> {
    await exec('xcrun', ['stapler', 'staple', appPath]);
  }
  
  /**
   * Create DMG installer
   */
  private async createDMG(
    appPath: string,
    config: MacOSBuildConfig
  ): Promise<string> {
    const dmgPath = path.join(
      path.dirname(appPath),
      `${config.appName}-${config.version}.dmg`
    );
    
    // Create temporary folder for DMG contents
    const dmgContentsPath = path.join(TEMP_DIR, 'dmg-contents');
    await fs.ensureDir(dmgContentsPath);
    
    // Copy app to DMG contents
    await fs.copy(appPath, path.join(dmgContentsPath, `${config.appName}.app`));
    
    // Create Applications symlink
    await fs.symlink(
      '/Applications',
      path.join(dmgContentsPath, 'Applications')
    );
    
    // Create DMG with nice layout
    await exec('hdiutil', [
      'create',
      '-volname', config.appName,
      '-srcfolder', dmgContentsPath,
      '-ov',
      '-format', 'UDZO',
      dmgPath
    ]);
    
    // Clean up
    await fs.remove(dmgContentsPath);
    
    return dmgPath;
  }
  
  /**
   * Validate macOS app
   */
  private async validateMacOSApp(appPath: string): Promise<MacOSValidation> {
    const validation: MacOSValidation = {
      valid: true,
      checks: {}
    };
    
    // 1. Verify code signature
    validation.checks.signature = await this.verifyMacSignature(appPath);
    
    // 2. Verify notarization
    validation.checks.notarization = await this.verifyNotarization(appPath);
    
    // 3. Check Gatekeeper
    validation.checks.gatekeeper = await this.checkGatekeeper(appPath);
    
    // 4. Validate entitlements
    validation.checks.entitlements = await this.validateEntitlements(appPath);
    
    validation.valid = Object.values(validation.checks).every(c => c.valid);
    
    return validation;
  }
}
```

**Benefits:**
- ✅ **Complete Signing**: Code signature with hardened runtime
- ✅ **Notarization**: Apple notarization for Gatekeeper compliance
- ✅ **Universal Binaries**: Support for Intel and Apple Silicon
- ✅ **DMG Creation**: Professional disk image installers
- ✅ **Validation**: Comprehensive macOS compliance checks

---

### 7.4 Web Deployment Build (Comprehensive)

```typescript
interface WebBuildConfig {
  appName: string;
  version: string;
  
  // Build optimization
  minify: boolean;
  sourceMaps: boolean;
  treeshaking: boolean;
  codeSplitting: boolean;
  
  // Asset optimization
  compressImages: boolean;
  optimizeFonts: boolean;
  generateWebP: boolean;
  
  // PWA configuration
  pwa?: PWAConfig;
  
  // Deployment
  deploymentTarget?: 'vercel' | 'netlify' | 'aws-s3' | 'cloudflare-pages';
  environmentVariables: Record<string, string>;
}

interface PWAConfig {
  enabled: boolean;
  name: string;
  shortName: string;
  themeColor: string;
  backgroundColor: string;
  icons: PWAIcon[];
  offlineSupport: boolean;
}

class WebDeploymentBuilder {
  /**
   * Build optimized web application
   */
  async buildWeb(
    workflow: Workflow,
    config: WebBuildConfig
  ): Promise<WebBuildResult> {
    // 1. Initialize React project
    const projectPath = await this.initializeWebProject(workflow, config);
    
    // 2. Generate app code
    await this.generateWebApp(workflow, projectPath, config);
    
    // 3. Optimize assets
    await this.optimizeAssets(projectPath, config);
    
    // 4. Build production bundle
    const distPath = await this.buildProductionBundle(projectPath, config);
    
    // 5. Generate PWA files (if enabled)
    if (config.pwa?.enabled) {
      await this.generatePWA(distPath, config.pwa);
    }
    
    // 6. Optimize bundle
    await this.optimizeBundle(distPath, config);
    
    // 7. Generate deployment package
    const packagePath = await this.createDeploymentPackage(distPath, config);
    
    // 8. Deploy (if target specified)
    if (config.deploymentTarget) {
      await this.deployToTarget(distPath, config);
    }
    
    // 9. Validate
    const validation = await this.validateWebBuild(distPath);
    
    // 10. Export
    const exportPath = await this.exportWebBuild(packagePath, config);
    
    return {
      success: true,
      distPath: exportPath,
      size: await this.getFolderSize(distPath),
      validation,
      deploymentUrl: config.deploymentTarget ? await this.getDeploymentUrl() : undefined
    };
  }
  
  /**
   * Build production bundle with Vite
   */
  private async buildProductionBundle(
    projectPath: string,
    config: WebBuildConfig
  ): Promise<string> {
    const viteConfig = {
      build: {
        outDir: 'dist',
        minify: config.minify ? 'terser' : false,
        sourcemap: config.sourceMaps,
        rollupOptions: {
          output: {
            manualChunks: config.codeSplitting ? {
              'react-vendor': ['react', 'react-dom'],
              'workflow-engine': ['./src/workflow'],
              'ui-components': ['./src/components']
            } : undefined
          }
        },
        terserOptions: config.minify ? {
          compress: {
            drop_console: true,
            drop_debugger: true
          }
        } : undefined
      },
      define: {
        'process.env': JSON.stringify(config.environmentVariables)
      }
    };
    
    await fs.writeJSON(
      path.join(projectPath, 'vite.config.json'),
      viteConfig
    );
    
    // Run build
    await exec('npm', ['run', 'build'], {
      cwd: projectPath
    });
    
    return path.join(projectPath, 'dist');
  }
  
  /**
   * Optimize assets
   */
  private async optimizeAssets(
    projectPath: string,
    config: WebBuildConfig
  ): Promise<void> {
    const assetsPath = path.join(projectPath, 'src', 'assets');
    
    if (config.compressImages) {
      await this.compressImages(assetsPath);
    }
    
    if (config.generateWebP) {
      await this.generateWebPImages(assetsPath);
    }
    
    if (config.optimizeFonts) {
      await this.optimizeFonts(assetsPath);
    }
  }
  
  /**
   * Generate PWA files
   */
  private async generatePWA(
    distPath: string,
    pwaConfig: PWAConfig
  ): Promise<void> {
    // Generate manifest.json
    const manifest = {
      name: pwaConfig.name,
      short_name: pwaConfig.shortName,
      theme_color: pwaConfig.themeColor,
      background_color: pwaConfig.backgroundColor,
      display: 'standalone',
      scope: '/',
      start_url: '/',
      icons: pwaConfig.icons.map(icon => ({
        src: icon.src,
        sizes: icon.sizes,
        type: icon.type,
        purpose: icon.purpose
      }))
    };
    
    await fs.writeJSON(
      path.join(distPath, 'manifest.json'),
      manifest,
      { spaces: 2 }
    );
    
    // Generate service worker
    if (pwaConfig.offlineSupport) {
      await this.generateServiceWorker(distPath);
    }
  }
  
  /**
   * Deploy to hosting platform
   */
  private async deployToTarget(
    distPath: string,
    config: WebBuildConfig
  ): Promise<string> {
    switch (config.deploymentTarget) {
      case 'vercel':
        return await this.deployToVercel(distPath, config);
        
      case 'netlify':
        return await this.deployToNetlify(distPath, config);
        
      case 'aws-s3':
        return await this.deployToS3(distPath, config);
        
      case 'cloudflare-pages':
        return await this.deployToCloudflarePages(distPath, config);
        
      default:
        throw new Error(`Unknown deployment target: ${config.deploymentTarget}`);
    }
  }
}
```

**Benefits:**
- ✅ **Build Optimization**: Minification, tree-shaking, code splitting
- ✅ **Asset Optimization**: Image compression, WebP generation
- ✅ **PWA Support**: Service worker and manifest generation
- ✅ **Multi-Platform Deploy**: Vercel, Netlify, AWS, Cloudflare
- ✅ **Performance**: Optimized bundles for fast loading

---

### 7.4 Web Deployment Build

**Build Process:**
- Optimize React build with production settings
- Bundle optimization (code splitting, tree shaking)
- Asset optimization (image compression, font subsetting)
- Environment configuration (API endpoints, feature flags)
- **PWA Support**: Generate service worker and manifest (optional)

**Build Tools:**
- Vite (preferred) or Webpack
- TypeScript compiler
- CSS processors (PostCSS, Tailwind)
- Asset optimizers (imagemin, svgo)
- **Bundle Analyzer**: Analyze bundle size and optimize

**Build Steps:**
1. Install dependencies (npm/yarn/pnpm)
2. Build production bundle with optimizations
3. Optimize assets (images, fonts, icons)
4. Generate deployment package (static files)
5. **Validate Build**: Test production build locally
6. **Export Package**: Provide downloadable ZIP or deploy directly
7. Upload to hosting (optional: Vercel, Netlify, AWS S3, etc.)

### 7.5 Required Packages & Runtimes (Comprehensive)

```typescript
interface DevelopmentEnvironment {
  core: {
    nodejs: {
      version: '18+';
      downloadUrl: 'https://nodejs.org';
      verification: 'node --version';
    };
    packageManager: {
      options: ['npm', 'yarn', 'pnpm'];
      recommendation: 'pnpm';  // Faster, more efficient
    };
    typescript: {
      version: '5+';
      install: 'npm install -g typescript';
    };
  };
  
  mobile: {
    android: {
      jdk: {
        version: 'JDK 11+';
        downloadUrl: 'https://adoptium.net';
      };
      androidSDK: {
        apiLevel: 21;  // Minimum
        targetApiLevel: 33;  // Recommended
        downloadUrl: 'https://developer.android.com/studio';
      };
      gradle: {
        version: '7.5+';
        autoInstalled: true;  // Via Android Studio
      };
      buildTools: {
        version: '33.0.0+';
        install: 'sdkmanager "build-tools;33.0.0"';
      };
    };
    reactNative: {
      cli: 'npm install -g react-native-cli';
      version: '0.72+';
    };
    flutter: {
      version: '3.13+';
      downloadUrl: 'https://flutter.dev';
      optional: true;
    };
  };
  
  desktop: {
    electron: {
      version: '28+';
      install: 'npm install electron';
      bundleSize: '~100MB';
    };
    tauri: {
      version: '1.5+';
      install: 'npm install @tauri-apps/cli';
      bundleSize: '~10MB';
      rustRequired: true;
    };
    platformTools: {
      windows: {
        visualStudioBuildTools: {
          downloadUrl: 'https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022';
          components: ['C++ build tools', 'Windows 10 SDK'];
        };
        wixToolset: {
          optional: true;
          useCase: 'Advanced MSI installers';
          downloadUrl: 'https://wixtoolset.org';
        };
      };
      macos: {
        xcode: {
          version: '14+';
          install: 'xcode-select --install';
        };
        developerCertificate: {
          required: true;
          type: 'Developer ID Application';
          obtain: 'https://developer.apple.com';
        };
      };
      linux: {
        buildEssential: 'apt-get install build-essential';
        webkit2gtk: 'apt-get install libwebkit2gtk-4.0-dev';
      };
    };
  };
  
  deployment: {
    docker: {
      optional: true;
      version: '20+';
      useCase: 'Containerized deployment';
    };
    cicd: {
      githubActions: 'Built-in';
      gitlabCI: 'Built-in';
      jenkinsPlugin: 'Requires setup';
    };
    hosting: {
      vercel: { cli: 'npm install -g vercel' };
      netlify: { cli: 'npm install -g netlify-cli' };
      aws: { cli: 'pip install awscli' };
      cloudflare: { cli: 'npm install -g wrangler' };
    };
    certificates: {
      windows: {
        type: 'Code Signing Certificate';
        providers: ['DigiCert', 'Sectigo', 'GlobalSign'];
        cost: '$100-400/year';
      };
      macos: {
        type: 'Developer ID Certificate';
        provider: 'Apple Developer Program';
        cost: '$99/year';
      };
    };
  };
}

/**
 * Environment Setup Automation
 */
class EnvironmentSetup {
  /**
   * Check and install missing dependencies
   */
  async setupEnvironment(
    platforms: BuildPlatform[]
  ): Promise<SetupResult> {
    const results: SetupResult = {
      installed: [],
      missing: [],
      errors: []
    };
    
    for (const platform of platforms) {
      try {
        await this.setupPlatform(platform, results);
      } catch (error) {
        results.errors.push({
          platform,
          error: error.message
        });
      }
    }
    
    return results;
  }
  
  /**
   * Auto-detect and install dependencies
   */
  private async setupPlatform(
    platform: BuildPlatform,
    results: SetupResult
  ): Promise<void> {
    switch (platform) {
      case 'android':
        await this.setupAndroid(results);
        break;
        
      case 'windows':
        await this.setupWindows(results);
        break;
        
      case 'macos':
        await this.setupMacOS(results);
        break;
        
      case 'web':
        await this.setupWeb(results);
        break;
    }
  }
}
```

**Benefits:**
- ✅ **Comprehensive List**: All required tools and packages
- ✅ **Version Specifications**: Clear version requirements
- ✅ **Installation Commands**: Copy-paste ready commands
- ✅ **Auto-Setup**: Automated dependency installation
- ✅ **Cost Information**: Certificate and subscription costs

---

### 7.6 Multi-Platform Export Workflow (Comprehensive)

```typescript
interface MultiPlatformBuildConfig {
  platforms: BuildPlatform[];
  parallelBuilds: boolean;
  buildTimeout: number;  // minutes
  retryOnFailure: boolean;
  notifyOnComplete: boolean;
}

interface BuildProgress {
  platform: BuildPlatform;
  status: 'pending' | 'building' | 'validating' | 'completed' | 'failed';
  progress: number;  // 0-100
  startTime?: Date;
  endTime?: Date;
  error?: string;
  artifacts?: BuildArtifact[];
}

class MultiPlatformBuilder {
  /**
   * Build for all platforms simultaneously
   */
  async buildAllPlatforms(
    workflow: Workflow,
    config: MultiPlatformBuildConfig
  ): Promise<MultiPlatformBuildResult> {
    // 1. Initialize build tracking
    const buildProgress = this.initializeProgress(config.platforms);
    
    // 2. Validate environments
    await this.validateAllEnvironments(config.platforms);
    
    // 3. Start builds
    const buildPromises = config.parallelBuilds
      ? await this.buildParallel(workflow, config, buildProgress)
      : await this.buildSequential(workflow, config, buildProgress);
    
    // 4. Wait for all builds
    const results = await Promise.allSettled(buildPromises);
    
    // 5. Collect artifacts
    const artifacts = await this.collectArtifacts(results);
    
    // 6. Validate all builds
    const validation = await this.validateAllBuilds(artifacts);
    
    // 7. Package everything together
    const packagePath = await this.createUnifiedPackage(artifacts, workflow);
    
    // 8. Generate documentation
    await this.generateBuildDocumentation(packagePath, artifacts);
    
    // 9. Notify user
    if (config.notifyOnComplete) {
      await this.notifyCompletion(artifacts, validation);
    }
    
    return {
      success: validation.allPassed,
      packagePath,
      artifacts,
      validation,
      buildTime: this.calculateTotalBuildTime(buildProgress)
    };
  }
  
  /**
   * Build all platforms in parallel
   */
  private async buildParallel(
    workflow: Workflow,
    config: MultiPlatformBuildConfig,
    progress: Map<BuildPlatform, BuildProgress>
  ): Promise<Promise<BuildResult>[]> {
    const builders: Record<BuildPlatform, PlatformBuilder> = {
      'android': new AndroidAPKBuilder(),
      'windows': new WindowsEXEBuilder(),
      'macos': new MacOSAppBuilder(),
      'web': new WebDeploymentBuilder()
    };
    
    return config.platforms.map(platform => {
      return this.buildWithProgress(
        platform,
        builders[platform],
        workflow,
        progress.get(platform)!
      );
    });
  }
  
  /**
   * Build with real-time progress tracking
   */
  private async buildWithProgress(
    platform: BuildPlatform,
    builder: PlatformBuilder,
    workflow: Workflow,
    progress: BuildProgress
  ): Promise<BuildResult> {
    progress.status = 'building';
    progress.startTime = new Date();
    
    try {
      // Update progress periodically
      const progressInterval = setInterval(() => {
        this.updateProgress(progress);
        this.emitProgressEvent(platform, progress);
      }, 1000);
      
      // Build
      const result = await builder.build(workflow);
      
      clearInterval(progressInterval);
      
      progress.status = 'validating';
      progress.progress = 90;
      
      // Validate
      const validation = await builder.validate(result);
      
      progress.status = 'completed';
      progress.progress = 100;
      progress.endTime = new Date();
      progress.artifacts = result.artifacts;
      
      return result;
      
    } catch (error) {
      progress.status = 'failed';
      progress.error = error.message;
      progress.endTime = new Date();
      
      throw error;
    }
  }
  
  /**
   * Create unified export package
   */
  private async createUnifiedPackage(
    artifacts: BuildArtifact[],
    workflow: Workflow
  ): Promise<string> {
    const packageName = `${workflow.name}-v${workflow.version}`;
    const packagePath = path.join(EXPORTS_DIR, packageName);
    
    await fs.ensureDir(packagePath);
    
    // Organize artifacts by platform
    for (const artifact of artifacts) {
      const platformDir = path.join(packagePath, artifact.platform);
      await fs.ensureDir(platformDir);
      
      // Copy artifact
      await fs.copy(artifact.path, path.join(platformDir, artifact.filename));
      
      // Copy documentation
      if (artifact.documentation) {
        await fs.copy(
          artifact.documentation,
          path.join(platformDir, 'README.md')
        );
      }
    }
    
    // Create main README
    await this.createMainReadme(packagePath, artifacts, workflow);
    
    // Create ZIP archive
    const zipPath = `${packagePath}.zip`;
    await this.createZipArchive(packagePath, zipPath);
    
    return zipPath;
  }
  
  /**
   * Generate comprehensive build documentation
   */
  private async generateBuildDocumentation(
    packagePath: string,
    artifacts: BuildArtifact[]
  ): Promise<void> {
    const documentation = `
# Build Package

This package contains builds for multiple platforms. See platform-specific folders for installation instructions.

## Contents

${artifacts.map(a => `
### ${a.platform.toUpperCase()}

- **File**: \`${a.filename}\`
- **Size**: ${this.formatBytes(a.size)}
- **Built**: ${a.buildDate.toLocaleString()}
- **Status**: ${a.validated ? '✅ Validated' : '⚠️ Not validated'}

See \`${a.platform}/README.md\` for installation instructions.
`).join('\n')}

## Quick Start

1. Extract this ZIP file
2. Navigate to your platform folder (android/windows/macos/web)
3. Follow the README.md in that folder

## System Requirements

### Android
- Android 5.0 (API 21) or higher
- ~50MB free storage

### Windows
- Windows 10 or higher (64-bit)
- ~200MB free storage

### macOS
- macOS 10.15 (Catalina) or higher
- ~200MB free storage
- Apple Silicon or Intel processor

### Web
- Modern web browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled

## Support

For issues or questions, please contact support or visit our documentation.

---
Generated by OLAI Build System on ${new Date().toLocaleString()}
    `.trim();
    
    await fs.writeFile(
      path.join(packagePath, 'README.md'),
      documentation
    );
  }
  
  /**
   * Real-time progress updates via WebSocket
   */
  private emitProgressEvent(
    platform: BuildPlatform,
    progress: BuildProgress
  ): void {
    websocketService.emit('build:progress', {
      platform,
      status: progress.status,
      progress: progress.progress,
      message: this.getProgressMessage(progress)
    });
  }
  
  /**
   * Calculate estimated completion time
   */
  private calculateETA(progress: BuildProgress): Date | null {
    if (!progress.startTime || progress.progress === 0) {
      return null;
    }
    
    const elapsed = Date.now() - progress.startTime.getTime();
    const estimatedTotal = (elapsed / progress.progress) * 100;
    const remaining = estimatedTotal - elapsed;
    
    return new Date(Date.now() + remaining);
  }
}

/**
 * Build Status Dashboard
 */
interface BuildDashboard {
  overall: {
    status: 'building' | 'completed' | 'failed';
    startTime: Date;
    estimatedCompletion?: Date;
    completedPlatforms: number;
    totalPlatforms: number;
  };
  platforms: BuildProgress[];
  logs: BuildLog[];
}
```

**Export Package Structure:**
```
project-name-v1.0.0/
├── README.md                 # Main documentation
├── android/
│   ├── app-release.apk      # Android APK
│   ├── README.md            # Installation guide
│   └── screenshots/         # App screenshots
├── windows/
│   ├── installer.exe        # Windows installer
│   ├── portable.exe         # Portable version
│   └── README.md
├── macos/
│   ├── app.dmg              # macOS disk image
│   ├── app.pkg              # macOS installer
│   └── README.md
└── web/
    ├── dist/                # Production build
    ├── deploy.sh            # Deployment script
    └── README.md
```

**Benefits:**
- ✅ **Parallel Builds**: 4x faster with simultaneous building
- ✅ **Progress Tracking**: Real-time updates for each platform
- ✅ **Unified Package**: All platforms in one download
- ✅ **Comprehensive Docs**: Installation guides for each platform
- ✅ **Validation**: Every build tested before export
- ✅ **Error Recovery**: Automatic retry on build failures

---

**Summary of Section 7 (Automatic Deployment & Build):**
- ✅ **7.1**: Android APK generation with ProGuard/R8 optimization
- ✅ **7.2**: Windows EXE with Electron/Tauri support
- ✅ **7.3**: macOS app with code signing and notarization
- ✅ **7.4**: Web deployment with PWA and multi-platform hosting
- ✅ **7.5**: Complete dependency management and auto-setup
- ✅ **7.6**: Multi-platform parallel builds with unified packaging

---

---

## 8. Hardware Model Selection Strategy

The hardware model selection system automatically detects user hardware capabilities, recommends optimal AI models, manages multi-model execution, and provides intelligent fallback strategies.

---

### 8.1 Hardware Detection & Pre-Checks (Comprehensive)

The hardware detection system performs comprehensive scanning of system resources before any model operations to prevent wasted downloads and execution failures.

---

#### **Hardware Detection Engine**

```typescript
interface HardwareCapabilities {
  cpu: CPUInfo;
  gpu: GPUInfo | null;
  memory: MemoryInfo;
  storage: StorageInfo;
  platform: PlatformInfo;
}

interface CPUInfo {
  model: string;
  cores: number;
  threads: number;
  architecture: 'x64' | 'arm64' | 'x86';
  instructionSets: string[];  // e.g., ['SSE4', 'AVX2', 'AVX512']
  baseFrequency: number;  // GHz
  maxFrequency: number;   // GHz
}

interface GPUInfo {
  name: string;
  vendor: 'nvidia' | 'amd' | 'intel' | 'apple';
  vram: number;  // GB
  vramAvailable: number;  // GB
  computeCapability?: string;  // CUDA compute capability
  apiSupport: {
    cuda?: {
      version: string;
      available: boolean;
    };
    rocm?: {
      version: string;
      available: boolean;
    };
    metal?: {
      version: string;
      available: boolean;
    };
    opencl?: {
      version: string;
      available: boolean;
    };
  };
  memoryBandwidth: number;  // GB/s
}

interface MemoryInfo {
  total: number;  // GB
  available: number;  // GB
  swap: number;   // GB
  swapAvailable: number;  // GB
}

interface StorageInfo {
  available: number;  // GB
  total: number;      // GB
  type: 'ssd' | 'hdd' | 'nvme';
  readSpeed: number;  // MB/s
  writeSpeed: number; // MB/s
}

class HardwareDetector {
  /**
   * Detect all hardware capabilities
   */
  async detectHardware(): Promise<HardwareCapabilities> {
    console.log('🔍 Detecting hardware capabilities...');
    
    const hardware: HardwareCapabilities = {
      cpu: await this.detectCPU(),
      gpu: await this.detectGPU(),
      memory: await this.detectMemory(),
      storage: await this.detectStorage(),
      platform: await this.detectPlatform()
    };
    
    // Log detection results
    this.logHardwareInfo(hardware);
    
    return hardware;
  }
  
  /**
   * Detect CPU information
   */
  private async detectCPU(): Promise<CPUInfo> {
    const cpuInfo = os.cpus()[0];
    
    return {
      model: cpuInfo.model,
      cores: os.cpus().length,
      threads: os.cpus().length,  // Approximation
      architecture: process.arch as 'x64' | 'arm64' | 'x86',
      instructionSets: await this.detectInstructionSets(),
      baseFrequency: cpuInfo.speed / 1000,  // Convert MHz to GHz
      maxFrequency: cpuInfo.speed / 1000
    };
  }
  
  /**
   * Detect GPU and compute capabilities
   */
  private async detectGPU(): Promise<GPUInfo | null> {
    // Try NVIDIA GPU detection first
    const nvidiaGPU = await this.detectNvidiaGPU();
    if (nvidiaGPU) return nvidiaGPU;
    
    // Try AMD GPU detection
    const amdGPU = await this.detectAMDGPU();
    if (amdGPU) return amdGPU;
    
    // Try Intel GPU detection
    const intelGPU = await this.detectIntelGPU();
    if (intelGPU) return intelGPU;
    
    // Try Apple Silicon GPU detection
    if (process.platform === 'darwin' && process.arch === 'arm64') {
      return await this.detectAppleGPU();
    }
    
    // No GPU detected
    console.log('⚠️  No GPU detected - CPU-only mode');
    return null;
  }
  
  /**
   * Detect NVIDIA GPU with CUDA
   */
  private async detectNvidiaGPU(): Promise<GPUInfo | null> {
    try {
      // Check if nvidia-smi is available
      const result = await exec('nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv,noheader,nounits');
      
      const [name, vramTotal, vramFree, computeCap] = result.stdout.trim().split(',').map(s => s.trim());
      
      // Check CUDA version
      const cudaVersion = await this.detectCUDAVersion();
      
      return {
        name,
        vendor: 'nvidia',
        vram: parseFloat(vramTotal) / 1024,  // MB to GB
        vramAvailable: parseFloat(vramFree) / 1024,
        computeCapability: computeCap,
        apiSupport: {
          cuda: {
            version: cudaVersion || 'unknown',
            available: !!cudaVersion
          }
        },
        memoryBandwidth: await this.getNvidiaMemoryBandwidth()
      };
    } catch (error) {
      return null;
    }
  }
  
  /**
   * Detect CUDA version
   */
  private async detectCUDAVersion(): Promise<string | null> {
    try {
      const result = await exec('nvcc --version');
      const match = result.stdout.match(/release (\d+\.\d+)/);
      return match ? match[1] : null;
    } catch {
      return null;
    }
  }
  
  /**
   * Detect AMD GPU with ROCm
   */
  private async detectAMDGPU(): Promise<GPUInfo | null> {
    try {
      const result = await exec('rocm-smi --showproductname --showmeminfo vram');
      
      // Parse ROCm output
      const name = this.parseAMDGPUName(result.stdout);
      const vram = this.parseAMDGPUVRAM(result.stdout);
      
      // Check ROCm version
      const rocmVersion = await this.detectROCmVersion();
      
      return {
        name,
        vendor: 'amd',
        vram: vram.total / 1024,  // MB to GB
        vramAvailable: vram.available / 1024,
        apiSupport: {
          rocm: {
            version: rocmVersion || 'unknown',
            available: !!rocmVersion
          }
        },
        memoryBandwidth: 0  // TODO: Get from ROCm
      };
    } catch (error) {
      return null;
    }
  }
  
  /**
   * Detect Apple Silicon GPU with Metal
   */
  private async detectAppleGPU(): Promise<GPUInfo | null> {
    try {
      const result = await exec('system_profiler SPDisplaysDataType');
      
      // Parse output
      const gpuMatch = result.stdout.match(/Chipset Model: (.+)/);
      const vramMatch = result.stdout.match(/VRAM \(Total\): (\d+) ([GM])B/);
      
      if (!gpuMatch) return null;
      
      const name = gpuMatch[1].trim();
      const vramValue = vramMatch ? parseFloat(vramMatch[1]) : 0;
      const vramUnit = vramMatch ? vramMatch[2] : 'G';
      const vram = vramUnit === 'G' ? vramValue : vramValue / 1024;
      
      return {
        name,
        vendor: 'apple',
        vram,
        vramAvailable: vram * 0.8,  // Estimate 80% available
        apiSupport: {
          metal: {
            version: await this.detectMetalVersion(),
            available: true
          }
        },
        memoryBandwidth: this.estimateAppleMemoryBandwidth(name)
      };
    } catch (error) {
      return null;
    }
  }
  
  /**
   * Detect memory information
   */
  private async detectMemory(): Promise<MemoryInfo> {
    const totalMem = os.totalmem() / (1024 ** 3);  // Bytes to GB
    const freeMem = os.freemem() / (1024 ** 3);
    
    // Get swap info (platform-specific)
    const swapInfo = await this.getSwapInfo();
    
    return {
      total: totalMem,
      available: freeMem,
      swap: swapInfo.total,
      swapAvailable: swapInfo.available
    };
  }
  
  /**
   * Detect storage information
   */
  private async detectStorage(): Promise<StorageInfo> {
    const diskSpace = await checkDiskSpace('/');
    
    return {
      total: diskSpace.size / (1024 ** 3),  // Bytes to GB
      available: diskSpace.free / (1024 ** 3),
      type: await this.detectStorageType(),
      readSpeed: await this.measureReadSpeed(),
      writeSpeed: await this.measureWriteSpeed()
    };
  }
}

/**
 * Pre-Check System
 */
class ModelPreCheckSystem {
  private hardwareDetector: HardwareDetector;
  
  /**
   * Pre-check before model download
   */
  async preCheckModelDownload(
    modelInfo: ModelInfo
  ): Promise<PreCheckResult> {
    console.log(`🔍 Pre-checking model: ${modelInfo.name}...`);
    
    // 1. Detect hardware
    const hardware = await this.hardwareDetector.detectHardware();
    
    // 2. Check model size vs available storage
    const storageCheck = this.checkStorage(modelInfo, hardware.storage);
    
    // 3. Check model requirements vs hardware
    const compatibilityCheck = this.checkCompatibility(modelInfo, hardware);
    
    // 4. Check VRAM requirements
    const vramCheck = this.checkVRAM(modelInfo, hardware.gpu);
    
    // 5. Check RAM requirements
    const ramCheck = this.checkRAM(modelInfo, hardware.memory);
    
    // 6. Generate recommendations
    const recommendations = await this.generateRecommendations(
      modelInfo,
      hardware,
      { storageCheck, compatibilityCheck, vramCheck, ramCheck }
    );
    
    const result: PreCheckResult = {
      canDownload: storageCheck.passed && compatibilityCheck.passed,
      canRun: vramCheck.passed && ramCheck.passed,
      checks: {
        storage: storageCheck,
        compatibility: compatibilityCheck,
        vram: vramCheck,
        ram: ramCheck
      },
      recommendations,
      warnings: this.collectWarnings({ storageCheck, compatibilityCheck, vramCheck, ramCheck }),
      alternatives: await this.suggestAlternatives(modelInfo, hardware)
    };
    
    // Display results
    this.displayPreCheckResults(result, modelInfo);
    
    return result;
  }
  
  /**
   * Check storage space
   */
  private checkStorage(
    modelInfo: ModelInfo,
    storage: StorageInfo
  ): CheckResult {
    const requiredSpace = modelInfo.size * 1.2;  // 20% buffer
    const hasSpace = storage.available >= requiredSpace;
    
    return {
      passed: hasSpace,
      message: hasSpace
        ? `✅ Storage: ${storage.available.toFixed(1)}GB available (${modelInfo.size.toFixed(1)}GB required)`
        : `❌ Insufficient storage: ${storage.available.toFixed(1)}GB available, ${requiredSpace.toFixed(1)}GB required`,
      details: {
        available: storage.available,
        required: requiredSpace,
        deficit: hasSpace ? 0 : requiredSpace - storage.available
      }
    };
  }
  
  /**
   * Check compatibility
   */
  private checkCompatibility(
    modelInfo: ModelInfo,
    hardware: HardwareCapabilities
  ): CheckResult {
    const issues: string[] = [];
    
    // Check GPU requirement
    if (modelInfo.requiresGPU && !hardware.gpu) {
      issues.push('Model requires GPU but none detected');
    }
    
    // Check CUDA version
    if (modelInfo.minCUDAVersion && hardware.gpu?.apiSupport.cuda) {
      const cudaVersion = hardware.gpu.apiSupport.cuda.version;
      if (cudaVersion < modelInfo.minCUDAVersion) {
        issues.push(`CUDA ${modelInfo.minCUDAVersion}+ required, found ${cudaVersion}`);
      }
    }
    
    // Check architecture
    if (modelInfo.supportedArchitectures &&
        !modelInfo.supportedArchitectures.includes(hardware.cpu.architecture)) {
      issues.push(`Architecture ${hardware.cpu.architecture} not supported`);
    }
    
    return {
      passed: issues.length === 0,
      message: issues.length === 0
        ? '✅ Hardware compatible'
        : `❌ Compatibility issues: ${issues.join(', ')}`,
      details: { issues }
    };
  }
  
  /**
   * Check VRAM requirements
   */
  private checkVRAM(
    modelInfo: ModelInfo,
    gpu: GPUInfo | null
  ): CheckResult {
    if (!modelInfo.vramRequired) {
      return {
        passed: true,
        message: '✅ No VRAM requirement',
        details: {}
      };
    }
    
    if (!gpu) {
      return {
        passed: false,
        message: '❌ No GPU detected but model requires VRAM',
        details: { required: modelInfo.vramRequired }
      };
    }
    
    const hasVRAM = gpu.vramAvailable >= modelInfo.vramRequired;
    
    return {
      passed: hasVRAM,
      message: hasVRAM
        ? `✅ VRAM: ${gpu.vramAvailable.toFixed(1)}GB available (${modelInfo.vramRequired.toFixed(1)}GB required)`
        : `❌ Insufficient VRAM: ${gpu.vramAvailable.toFixed(1)}GB available, ${modelInfo.vramRequired.toFixed(1)}GB required`,
      details: {
        available: gpu.vramAvailable,
        required: modelInfo.vramRequired,
        deficit: hasVRAM ? 0 : modelInfo.vramRequired - gpu.vramAvailable
      }
    };
  }
  
  /**
   * Suggest alternative models
   */
  private async suggestAlternatives(
    modelInfo: ModelInfo,
    hardware: HardwareCapabilities
  ): Promise<ModelInfo[]> {
    const alternatives: ModelInfo[] = [];
    
    // Find lighter models
    const lighterModels = await modelRegistry.findModels({
      task: modelInfo.task,
      maxSize: hardware.memory.available * 0.5,  // Use only 50% of available RAM
      maxVRAM: hardware.gpu?.vramAvailable || 0
    });
    
    // Rank by size and performance
    return lighterModels
      .sort((a, b) => b.performance - a.performance)
      .slice(0, 3);
  }
  
  /**
   * Display pre-check results
   */
  private displayPreCheckResults(
    result: PreCheckResult,
    modelInfo: ModelInfo
  ): void {
    console.log(`\n📊 Pre-Check Results for ${modelInfo.name}:\n`);
    
    console.log(result.checks.storage.message);
    console.log(result.checks.compatibility.message);
    console.log(result.checks.vram.message);
    console.log(result.checks.ram.message);
    
    if (result.warnings.length > 0) {
      console.log(`\n⚠️  Warnings:`);
      result.warnings.forEach(w => console.log(`   ${w}`));
    }
    
    if (!result.canDownload || !result.canRun) {
      console.log(`\n❌ Cannot proceed with this model`);
      
      if (result.alternatives.length > 0) {
        console.log(`\n💡 Suggested Alternatives:`);
        result.alternatives.forEach((alt, i) => {
          console.log(`   ${i + 1}. ${alt.name} (${alt.size.toFixed(1)}GB)`);
        });
      }
    } else {
      console.log(`\n✅ All checks passed - safe to proceed`);
    }
    
    if (result.recommendations.length > 0) {
      console.log(`\n💡 Recommendations:`);
      result.recommendations.forEach(r => console.log(`   ${r}`));
    }
  }
}
```

**Benefits:**
- ✅ **Comprehensive Detection**: GPU, CPU, RAM, storage, platform
- ✅ **Early Warning**: Prevents wasted downloads
- ✅ **Smart Alternatives**: Suggests compatible models
- ✅ **User Override**: Allow force download with warnings
- ✅ **Transparent Logging**: Clear visibility into checks

---

### 8.2 Model Selection Algorithm (Comprehensive)

```typescript
interface ModelRequirements {
  projectType: 'no-models' | 'single-model' | 'multi-model';
  requiredModels: ModelSpec[];
  optionalModels: ModelSpec[];
  totalVRAM: number;
  totalRAM: number;
  estimatedCost: number;
}

interface ModelSpec {
  task: 'text-generation' | 'image-generation' | 'speech-to-text' | 'embedding' | 'classification';
  minParameters: number;
  maxParameters: number;
  priority: 'critical' | 'important' | 'optional';
  quantizationAllowed: boolean;
}

class ModelSelectionEngine {
  /**
   * Analyze project and determine model requirements
   */
  async analyzeProjectRequirements(
    workflow: Workflow
  ): Promise<ModelRequirements> {
    console.log('🔍 Analyzing project model requirements...');
    
    // 1. Scan workflow for AI nodes
    const aiNodes = workflow.nodes.filter(n => n.type.includes('ai') || n.type.includes('model'));
    
    // 2. Determine project type
    const projectType = this.determineProjectType(aiNodes);
    
    if (projectType === 'no-models') {
      console.log('✅ No AI models required for this project');
      return {
        projectType: 'no-models',
        requiredModels: [],
        optionalModels: [],
        totalVRAM: 0,
        totalRAM: 0,
        estimatedCost: 0
      };
    }
    
    // 3. Extract model requirements from nodes
    const requirements = await this.extractModelRequirements(aiNodes);
    
    // 4. Consolidate and optimize requirements
    const optimized = await this.optimizeRequirements(requirements);
    
    console.log(`📊 Project requires ${optimized.requiredModels.length} models`);
    
    return optimized;
  }
  
  /**
   * Select optimal models based on hardware
   */
  async selectOptimalModels(
    requirements: ModelRequirements,
    hardware: HardwareCapabilities
  ): Promise<ModelSelection> {
    console.log('🎯 Selecting optimal models...');
    
    const selectedModels: SelectedModel[] = [];
    const warnings: string[] = [];
    
    // 1. Select model for each requirement
    for (const spec of requirements.requiredModels) {
      const candidates = await this.findCandidateModels(spec, hardware);
      
      if (candidates.length === 0) {
        warnings.push(`No suitable model found for ${spec.task}`);
        
        // Suggest API alternative
        const apiModel = await this.suggestAPIModel(spec);
        if (apiModel) {
          selectedModels.push({
            ...apiModel,
            runMode: 'api',
            reason: 'Local execution not possible'
          });
        }
        continue;
      }
      
      // Rank candidates
      const ranked = await this.rankModels(candidates, spec, hardware);
      
      // Select best model
      const selected = ranked[0];
      selectedModels.push({
        ...selected,
        runMode: 'local',
        reason: this.explainSelection(selected, spec, hardware)
      });
    }
    
    // 2. Validate multi-model compatibility
    const compatibility = await this.validateMultiModelCompatibility(
      selectedModels,
      hardware
    );
    
    if (!compatibility.compatible) {
      // Adjust selection
      const adjusted = await this.adjustForCompatibility(
        selectedModels,
        hardware,
        compatibility
      );
      return adjusted;
    }
    
    // 3. Estimate performance
    const performance = await this.estimatePerformance(selectedModels, hardware);
    
    return {
      models: selectedModels,
      compatible: true,
      warnings,
      performance,
      estimatedCost: this.calculateCost(selectedModels)
    };
  }
  
  /**
   * Rank model candidates
   */
  private async rankModels(
    candidates: ModelInfo[],
    spec: ModelSpec,
    hardware: HardwareCapabilities
  ): Promise<ModelInfo[]> {
    return candidates
      .map(model => ({
        model,
        score: this.calculateModelScore(model, spec, hardware)
      }))
      .sort((a, b) => b.score - a.score)
      .map(({ model }) => model);
  }
  
  /**
   * Calculate model score
   */
  private calculateModelScore(
    model: ModelInfo,
    spec: ModelSpec,
    hardware: HardwareCapabilities
  ): number {
    let score = 0;
    
    // Performance score (0-40 points)
    score += model.performance * 40;
    
    // Size efficiency score (0-20 points)
    const sizeFit = model.size / (hardware.memory.available * 0.5);
    score += sizeFit < 1 ? (1 - sizeFit) * 20 : 0;
    
    // Hardware compatibility score (0-20 points)
    if (hardware.gpu && model.vramRequired <= hardware.gpu.vramAvailable) {
      score += 20;
    } else if (!model.requiresGPU) {
      score += 10;
    }
    
    // Popularity/reliability score (0-10 points)
    score += (model.downloads / 1000000) * 10;  // Normalize by 1M downloads
    
    // Cost score (0-10 points)
    score += model.cost === 0 ? 10 : Math.max(0, 10 - model.cost * 10);
    
    return score;
  }
  
  /**
   * Generate hardware-based recommendations
   */
  async generateRecommendations(
    workflow: Workflow,
    hardware: HardwareCapabilities
  ): Promise<HardwareRecommendation> {
    const recommendations: string[] = [];
    
    // RAM recommendation
    if (hardware.memory.total < 8) {
      recommendations.push(
        `⚠️ Low RAM (${hardware.memory.total.toFixed(1)}GB): ` +
        `Recommend upgrading to 16GB+ for better performance`
      );
      recommendations.push(
        `💡 Suggested models: 1B parameter models (e.g., TinyLlama, Phi-2)`
      );
    } else if (hardware.memory.total < 16) {
      recommendations.push(
        `💡 With ${hardware.memory.total.toFixed(1)}GB RAM: ` +
        `Try 3B-7B parameter models (e.g., LLaMA 3 8B, Mistral 7B)`
      );
    } else {
      recommendations.push(
        `✅ ${hardware.memory.total.toFixed(1)}GB RAM: ` +
        `Can run 13B-34B parameter models`
      );
    }
    
    // GPU recommendation
    if (!hardware.gpu) {
      recommendations.push(
        `⚠️ No GPU detected: Models will run on CPU (slower)` +
        `\n   Consider: ` +
        `\n   • Using API models (Gemini, OpenAI) for faster inference` +
        `\n   • Quantized models (GGUF Q4/Q5) for CPU efficiency` +
        `\n   • Adding GPU for 10-50x speedup`
      );
    } else {
      const vram = hardware.gpu.vramAvailable;
      if (vram < 4) {
        recommendations.push(
          `⚠️ Low VRAM (${vram.toFixed(1)}GB): ` +
          `Stick to small models (1B-3B parameters)`
        );
      } else if (vram < 8) {
        recommendations.push(
          `💡 ${vram.toFixed(1)}GB VRAM: ` +
          `Can run 7B parameter models efficiently`
        );
      } else {
        recommendations.push(
          `✅ ${vram.toFixed(1)}GB VRAM: ` +
          `Can run 13B+ parameter models`
        );
      }
    }
    
    // Execution time predictions
    const predictions = await this.predictExecutionTimes(workflow, hardware);
    recommendations.push(
      `\n⏱️  Estimated Execution Times:` +
      `\n   • On CPU: ${predictions.cpu}` +
      `\n   • On GPU: ${predictions.gpu || 'N/A (no GPU)'}`
    );
    
    return {
      hardware,
      recommendations,
      predictions,
      suggestedUpgrades: await this.suggestUpgrades(hardware)
    };
  }
  
  /**
   * Predict execution times
   */
  private async predictExecutionTimes(
    workflow: Workflow,
    hardware: HardwareCapabilities
  ): Promise<ExecutionPrediction> {
    const aiNodes = workflow.nodes.filter(n => n.type.includes('ai'));
    
    let cpuTime = 0;
    let gpuTime = 0;
    
    for (const node of aiNodes) {
      const modelSize = node.data.config?.modelSize || 7;  // billions of parameters
      
      // Rough estimates (adjust based on actual benchmarks)
      cpuTime += modelSize * 10;  // ~10s per billion parameters on CPU
      gpuTime += modelSize * 0.5; // ~0.5s per billion parameters on GPU
    }
    
    return {
      cpu: `~${Math.ceil(cpuTime)}s`,
      gpu: hardware.gpu ? `~${Math.ceil(gpuTime)}s` : null,
      speedup: hardware.gpu ? (cpuTime / gpuTime).toFixed(1) + 'x' : null
    };
  }
}

/**
 * Model Performance Profiler
 */
class ModelPerformanceProfiler {
  /**
   * Profile model execution and identify bottlenecks
   */
  async profileExecution(
    execution: ModelExecution
  ): Promise<PerformanceProfile> {
    const profile: PerformanceProfile = {
      totalTime: execution.duration,
      breakdown: {
        modelLoad: execution.timing.modelLoad,
        preprocessing: execution.timing.preprocessing,
        inference: execution.timing.inference,
        postprocessing: execution.timing.postprocessing
      },
      bottlenecks: [],
      suggestions: []
    };
    
    // Identify bottlenecks
    const maxTime = Math.max(...Object.values(profile.breakdown));
    for (const [stage, time] of Object.entries(profile.breakdown)) {
      if (time > maxTime * 0.5) {  // Stage taking >50% of max time
        profile.bottlenecks.push({
          stage,
          time,
          percentage: (time / profile.totalTime) * 100
        });
      }
    }
    
    // Generate optimization suggestions
    if (profile.breakdown.modelLoad > 5000) {
      profile.suggestions.push(
        '💡 Model loading is slow - consider keeping model in memory between runs'
      );
    }
    
    if (profile.breakdown.inference > profile.totalTime * 0.7) {
      profile.suggestions.push(
        '💡 Inference is the bottleneck:' +
        '\n   • Try quantized model (INT8/INT4) for faster inference' +
        '\n   • Use GPU if available for 10-50x speedup' +
        '\n   • Consider smaller model if accuracy allows'
      );
    }
    
    return profile;
  }
}
```

**Benefits:**
- ✅ **Smart Detection**: Automatically determines if models needed
- ✅ **Hardware-Aware**: Recommends models based on actual hardware
- ✅ **Performance Prediction**: Estimates execution time before running
- ✅ **Cost Optimization**: Suggests cheaper alternatives
- ✅ **Bottleneck Detection**: Identifies and fixes performance issues

---

### 8.3 Multi-Model Workflow Optimization (Comprehensive)

```typescript
class MultiModelOrchestrator {
  /**
   * Optimize execution of 4-5 models simultaneously
   */
  async optimizeMultiModelExecution(
    models: SelectedModel[],
    hardware: HardwareCapabilities
  ): Promise<ExecutionPlan> {
    console.log(`🔄 Optimizing execution of ${models.length} models...`);
    
    // 1. Analyze dependencies
    const dependencies = await this.analyzeDependencies(models);
    
    // 2. Calculate resource requirements
    const resources = await this.calculateTotalResources(models);
    
    // 3. Check if all models can run simultaneously
    const canRunSimultaneously = this.canRunAllTogether(resources, hardware);
    
    if (canRunSimultaneously) {
      // Parallel execution possible
      return await this.createParallelPlan(models, hardware);
    } else {
      // Need to schedule sequentially or in batches
      return await this.createBatchedPlan(models, hardware, resources);
    }
  }
  
  /**
   * Create parallel execution plan
   */
  private async createParallelPlan(
    models: SelectedModel[],
    hardware: HardwareCapabilities
  ): Promise<ExecutionPlan> {
    // Allocate resources to each model
    const allocations: ResourceAllocation[] = [];
    
    const hasGPU = !!hardware.gpu;
    const totalVRAM = hardware.gpu?.vramAvailable || 0;
    const totalRAM = hardware.memory.available;
    
    for (const model of models) {
      allocations.push({
        modelId: model.id,
        gpu: hasGPU && model.vramRequired <= totalVRAM,
        vram: model.vramRequired,
        ram: model.ramRequired,
        cpuCores: this.allocateCPUCores(model, hardware.cpu.cores)
      });
    }
    
    return {
      type: 'parallel',
      models,
      allocations,
      estimatedTime: Math.max(...models.map(m => m.estimatedTime)),
      warnings: this.validateAllocations(allocations, hardware)
    };
  }
  
  /**
   * Create batched execution plan
   */
  private async createBatchedPlan(
    models: SelectedModel[],
    hardware: HardwareCapabilities,
    resources: ResourceRequirements
  ): Promise<ExecutionPlan> {
    // Group models into batches that fit in available resources
    const batches: SelectedModel[][] = [];
    let currentBatch: SelectedModel[] = [];
    let currentVRAM = 0;
    let currentRAM = 0;
    
    for (const model of models) {
      const wouldExceedVRAM = currentVRAM + model.vramRequired > (hardware.gpu?.vramAvailable || 0);
      const wouldExceedRAM = currentRAM + model.ramRequired > hardware.memory.available * 0.8;
      
      if (wouldExceedVRAM || wouldExceedRAM) {
        // Start new batch
        if (currentBatch.length > 0) {
          batches.push(currentBatch);
        }
        currentBatch = [model];
        currentVRAM = model.vramRequired;
        currentRAM = model.ramRequired;
      } else {
        currentBatch.push(model);
        currentVRAM += model.vramRequired;
        currentRAM += model.ramRequired;
      }
    }
    
    if (currentBatch.length > 0) {
      batches.push(currentBatch);
    }
    
    return {
      type: 'batched',
      batches,
      estimatedTime: batches.reduce((sum, batch) => 
        sum + Math.max(...batch.map(m => m.estimatedTime))
      , 0),
      warnings: [
        `⚠️ Models will run in ${batches.length} batches due to resource constraints`,
        `💡 Consider upgrading hardware for parallel execution`
      ]
    };
  }
}
```

**Benefits:**
- ✅ **4-5 Models Simultaneously**: Intelligent resource allocation
- ✅ **Automatic Scheduling**: Optimal execution order
- ✅ **Resource Monitoring**: Real-time adjustment
- ✅ **Smooth Execution**: Prevents resource exhaustion

---

### 8.4 & 8.5 Memory Management & Fallback Strategy (Comprehensive)

```typescript
class MemoryManager {
  /**
   * Monitor and manage memory during execution
   */
  async manageMemory(
    execution: ModelExecution
  ): Promise<void> {
    const interval = setInterval(async () => {
      const usage = await this.checkMemoryUsage();
      
      if (usage.ram > 0.9) {
        console.warn('⚠️ RAM usage >90% - unloading unused models...');
        await this.unloadUnusedModels();
      }
      
      if (usage.vram > 0.9) {
        console.warn('⚠️ VRAM usage >90% - applying optimizations...');
        await this.applyMemoryOptimizations();
      }
    }, 1000);
    
    execution.on('complete', () => clearInterval(interval));
  }
  
  /**
   * Apply quantization to reduce memory
   */
  async quantizeModel(
    model: Model,
    quantization: 'int8' | 'int4'
  ): Promise<Model> {
    console.log(`🔧 Quantizing model to ${quantization}...`);
    
    // Reduce memory footprint by 50-75%
    const quantized = await model.quantize(quantization);
    
    console.log(`✅ Memory reduced from ${model.size}GB to ${quantized.size}GB`);
    
    return quantized;
  }
}

class FallbackStrategy {
  /**
   * Handle insufficient resources with fallback
   */
  async handleResourceConstraint(
    model: ModelInfo,
    hardware: HardwareCapabilities,
    constraint: 'ram' | 'vram' | 'storage'
  ): Promise<FallbackSolution> {
    console.log(`⚠️ ${constraint.toUpperCase()} constraint detected for ${model.name}`);
    
    // Try fallback options in order of preference
    const fallbacks: FallbackOption[] = [
      { type: 'quantize', priority: 1 },
      { type: 'smaller-model', priority: 2 },
      { type: 'api', priority: 3 },
      { type: 'batch-reduce', priority: 4 },
      { type: 'cpu-fallback', priority: 5 }
    ];
    
    for (const fallback of fallbacks) {
      const solution = await this.tryFallback(fallback, model, hardware);
      if (solution.viable) {
        console.log(`✅ Fallback solution: ${solution.description}`);
        return solution;
      }
    }
    
    throw new Error('No viable fallback solution found');
  }
}
```

**Benefits:**
- ✅ **Dynamic Memory Management**: Real-time monitoring
- ✅ **Automatic Optimization**: Quantization, pruning, offloading
- ✅ **Intelligent Fallback**: Multiple fallback strategies
- ✅ **Graceful Degradation**: Always finds a solution

---

### 8.3 Multi-Model Workflow Optimization

**Multi-Model Execution (4-5 Models Simultaneously):**
- **Resource Allocation**: Distribute GPU/CPU/RAM across multiple models
- **Model Scheduling**: Schedule models to run in parallel when resources allow
- **Memory Management**: Efficient memory sharing and swapping
- **Load Balancing**: Balance load across available hardware
- **OLAI Model Linking**: Link models together in workflows with automatic data flow between models
- **Model Chain Visualization**: Visual representation of model connections and data flow

**Optimization Strategies:**
- Model caching to reduce load times
- Batch processing for efficiency
- Pipeline optimization for sequential models
- Resource pooling for shared resources
- **Model Prioritization**: Critical models get priority access to resources

**Concurrency Management:**
- **Parallel Execution**: Run 4-5 models simultaneously when hardware supports
- Limit concurrent models based on available resources
- Queue model requests when resources are saturated
- Prioritize critical models
- Balance resource usage across all models
- **Resource Monitoring**: Continuously monitor and adjust resource allocation

**Smooth Execution Guarantees:**
- Pre-validate all models can run together
- Test model combinations before deployment
- Implement fallback strategies if resources insufficient
- Monitor performance and adjust in real-time

### 8.4 Memory Limits

**Memory Management:**
- Monitor memory usage
- Unload unused models
- Use model quantization
- Implement memory limits

**Memory Optimization:**
- Model quantization (int8, int4)
- Model pruning
- Gradient checkpointing
- Offloading to disk

### 8.5 Fallback Strategy

**Fallback Options:**
- Use smaller model
- Use cloud API
- Reduce batch size
- Use CPU instead of GPU

**Fallback Process:**
1. Detect resource constraint
2. Identify fallback options
3. Select best fallback
4. Notify user
5. Continue with fallback

### 8.6 Model Storage & Download Management (Comprehensive)

```typescript
interface ModelStorageConfig {
  baseDirectory: string;  // e.g., "~/OLAI-Models"
  maxSize: number;        // GB
  evictionPolicy: 'lru' | 'fifo' | 'manual';
  autoCleanup: boolean;
}

interface StoredModel {
  id: string;
  name: string;
  provider: 'huggingface' | 'ollama' | 'custom';
  version: string;
  size: number;  // GB
  downloadDate: Date;
  lastUsed: Date;
  usageCount: number;
  path: string;
  checksum: string;
  dependencies: string[];
}

class ModelStorageManager {
  private config: ModelStorageConfig;
  private modelIndex: Map<string, StoredModel>;
  
  /**
   * Initialize storage system
   */
  async initialize(): Promise<void> {
    // Create base directory
    await fs.ensureDir(this.config.baseDirectory);
    
    // Create organized structure
    await this.createDirectoryStructure();
    
    // Load model index
    await this.loadModelIndex();
    
    // Run storage check
    await this.checkStorageHealth();
  }
  
  /**
   * Create organized directory structure
   */
  private async createDirectoryStructure(): Promise<void> {
    const dirs = [
      'huggingface',
      'ollama',
      'custom',
      'cache',
      'temp'
    ];
    
    for (const dir of dirs) {
      await fs.ensureDir(path.join(this.config.baseDirectory, dir));
    }
  }
  
  /**
   * Download model with resumable support
   */
  async downloadModel(
    modelInfo: ModelInfo,
    onProgress?: (progress: DownloadProgress) => void
  ): Promise<string> {
    console.log(`📥 Downloading model: ${modelInfo.name}...`);
    
    const modelPath = this.getModelPath(modelInfo);
    const tempPath = `${modelPath}.partial`;
    
    // Check if partial download exists
    let startByte = 0;
    if (await fs.pathExists(tempPath)) {
      const stats = await fs.stat(tempPath);
      startByte = stats.size;
      console.log(`↪️  Resuming download from ${this.formatBytes(startByte)}...`);
    }
    
    // Download with resume support
    const downloader = new ResumableDownloader({
      url: modelInfo.downloadUrl,
      destination: tempPath,
      startByte,
      onProgress: (bytes, total) => {
        const progress: DownloadProgress = {
          downloaded: bytes,
          total,
          percentage: (bytes / total) * 100,
          speed: this.calculateDownloadSpeed(bytes),
          eta: this.calculateETA(bytes, total)
        };
        
        if (onProgress) {
          onProgress(progress);
        }
        
        this.displayProgress(progress, modelInfo.name);
      }
    });
    
    try {
      await downloader.download();
      
      // Verify checksum
      console.log('🔒 Verifying checksum...');
      const valid = await this.verifyChecksum(tempPath, modelInfo.checksum);
      
      if (!valid) {
        throw new Error('Checksum verification failed - file may be corrupted');
      }
      
      // Move to final location
      await fs.move(tempPath, modelPath, { overwrite: true });
      
      // Update index
      await this.addToIndex(modelInfo, modelPath);
      
      console.log(`✅ Download complete: ${modelPath}`);
      
      return modelPath;
      
    } catch (error) {
      console.error(`❌ Download failed: ${error.message}`);
      throw error;
    }
  }
  
  /**
   * Verify file checksum
   */
  private async verifyChecksum(
    filePath: string,
    expectedChecksum: string
  ): Promise<boolean> {
    const hash = crypto.createHash('sha256');
    const stream = fs.createReadStream(filePath);
    
    return new Promise((resolve, reject) => {
      stream.on('data', data => hash.update(data));
      stream.on('end', () => {
        const actualChecksum = hash.digest('hex');
        resolve(actualChecksum === expectedChecksum);
      });
      stream.on('error', reject);
    });
  }
  
  /**
   * Display download progress
   */
  private displayProgress(
    progress: DownloadProgress,
    modelName: string
  ): void {
    const bar = this.createProgressBar(progress.percentage);
    process.stdout.write(
      `\r📥 ${modelName}: ${bar} ${progress.percentage.toFixed(1)}% ` +
      `(${this.formatBytes(progress.downloaded)}/${this.formatBytes(progress.total)}) ` +
      `${this.formatBytes(progress.speed)}/s ETA: ${progress.eta}`
    );
  }
  
  /**
   * Manage storage with LRU eviction
   */
  async manageStorage(): Promise<void> {
    const usage = await this.calculateStorageUsage();
    
    if (usage.used > this.config.maxSize * 0.9) {
      console.log(`⚠️ Storage usage: ${usage.used.toFixed(1)}GB / ${this.config.maxSize}GB`);
      console.log('🧹 Starting automatic cleanup...');
      
      await this.evictLRUModels(this.config.maxSize * 0.8);
    }
  }
  
  /**
   * Evict least recently used models
   */
  private async evictLRUModels(targetSize: number): Promise<void> {
    const models = Array.from(this.modelIndex.values())
      .sort((a, b) => a.lastUsed.getTime() - b.lastUsed.getTime());
    
    let currentSize = await this.calculateStorageUsage();
    
    for (const model of models) {
      if (currentSize.used <= targetSize) {
        break;
      }
      
      console.log(`🗑️  Evicting ${model.name} (last used: ${model.lastUsed.toLocaleDateString()})`);
      
      await this.deleteModel(model.id);
      currentSize.used -= model.size;
    }
    
    console.log(`✅ Cleanup complete: ${currentSize.used.toFixed(1)}GB used`);
  }
  
  /**
   * Delete model and clean up dependencies
   */
  async deleteModel(modelId: string): Promise<void> {
    const model = this.modelIndex.get(modelId);
    if (!model) return;
    
    // Delete model files
    await fs.remove(model.path);
    
    // Remove from index
    this.modelIndex.delete(modelId);
    await this.saveModelIndex();
    
    // Clean up unused dependencies
    await this.cleanupDependencies(model);
  }
  
  /**
   * Get storage statistics
   */
  async getStorageStats(): Promise<StorageStats> {
    const usage = await this.calculateStorageUsage();
    const models = Array.from(this.modelIndex.values());
    
    return {
      totalSize: this.config.maxSize,
      usedSize: usage.used,
      availableSize: this.config.maxSize - usage.used,
      modelCount: models.length,
      byProvider: this.groupByProvider(models),
      recentlyUsed: models
        .sort((a, b) => b.lastUsed.getTime() - a.lastUsed.getTime())
        .slice(0, 10)
    };
  }
}

/**
 * Resumable Downloader
 */
class ResumableDownloader {
  async download(): Promise<void> {
    const response = await fetch(this.options.url, {
      headers: {
        'Range': `bytes=${this.options.startByte}-`
      }
    });
    
    if (!response.ok) {
      throw new Error(`Download failed: ${response.statusText}`);
    }
    
    const total = parseInt(response.headers.get('content-length') || '0') + this.options.startByte;
    const writer = fs.createWriteStream(this.options.destination, {
      flags: this.options.startByte > 0 ? 'a' : 'w'
    });
    
    let downloaded = this.options.startByte;
    
    for await (const chunk of response.body) {
      writer.write(chunk);
      downloaded += chunk.length;
      
      if (this.options.onProgress) {
        this.options.onProgress(downloaded, total);
      }
    }
    
    writer.end();
  }
}
```

**Benefits:**
- ✅ **Centralized Storage**: Organized in `OLAI-Models/` directory
- ✅ **Resumable Downloads**: Never restart from scratch
- ✅ **Automatic Cleanup**: LRU eviction when space low
- ✅ **Checksum Verification**: Prevents corrupted downloads
- ✅ **Storage Monitoring**: Real-time usage tracking

---

### 8.7 through 8.10 (Consolidated Implementation)

```typescript
/**
 * 8.7 - Dependency & Environment Management
 */
class DependencyManager {
  /**
   * Create isolated environment for model
   */
  async createModelEnvironment(
    modelId: string
  ): Promise<ModelEnvironment> {
    const envPath = path.join(MODELS_DIR, 'envs', modelId);
    
    // Check for shared dependencies
    const sharedLibs = ['pytorch', 'tensorflow', 'transformers'];
    const modelDeps = await this.getModelDependencies(modelId);
    
    // Install only unique dependencies
    const uniqueDeps = modelDeps.filter(d => !sharedLibs.includes(d));
    
    console.log(`📦 Installing ${uniqueDeps.length} unique dependencies...`);
    
    await this.installDependencies(envPath, uniqueDeps);
    
    return {
      path: envPath,
      dependencies: modelDeps,
      sharedLibraries: sharedLibs,
      isolated: true
    };
  }
}

/**
 * 8.8 - API Model Cost Transparency
 */
class CostTracker {
  /**
   * Track API usage and costs
   */
  async trackExecution(
    modelId: string,
    execution: ModelExecution
  ): Promise<CostRecord> {
    const cost = this.calculateCost(execution);
    
    const record: CostRecord = {
      modelId,
      timestamp: new Date(),
      inputTokens: execution.inputTokens,
      outputTokens: execution.outputTokens,
      cost: cost.total,
      breakdown: cost.breakdown
    };
    
    await this.saveCostRecord(record);
    
    // Check budget limits
    await this.checkBudgetLimits(modelId);
    
    // Display cost
    console.log(
      `💰 Cost: $${cost.total.toFixed(4)} ` +
      `(${execution.inputTokens + execution.outputTokens} tokens)`
    );
    
    return record;
  }
  
  /**
   * Generate cost report
   */
  async generateCostReport(
    period: 'day' | 'week' | 'month'
  ): Promise<CostReport> {
    const records = await this.getCostRecords(period);
    
    return {
      period,
      totalCost: records.reduce((sum, r) => sum + r.cost, 0),
      byModel: this.groupByModel(records),
      byDay: this.groupByDay(records),
      projectedMonthly: this.projectMonthlyCost(records)
    };
  }
}

/**
 * 8.9 - Security & Safety Measures
 */
class ModelSecurityManager {
  /**
   * Verify model provenance
   */
  async verifyModelProvenance(
    modelInfo: ModelInfo
  ): Promise<ProvenanceVerification> {
    // 1. Verify source
    const sourceValid = await this.verifySource(modelInfo.source);
    
    // 2. Check digital signature
    const signatureValid = await this.verifySignature(modelInfo);
    
    // 3. Verify checksum
    const checksumValid = await this.verifyChecksum(modelInfo);
    
    // 4. Check for known vulnerabilities
    const vulnerabilities = await this.scanForVulnerabilities(modelInfo);
    
    return {
      sourceValid,
      signatureValid,
      checksumValid,
      vulnerabilities,
      safe: sourceValid && signatureValid && checksumValid && vulnerabilities.length === 0
    };
  }
  
  /**
   * Sandboxed model execution
   */
  async executeSandboxed(
    model: Model,
    input: any
  ): Promise<any> {
    const sandbox = await this.createSandbox();
    
    try {
      const result = await sandbox.execute(model, input);
      return result;
    } finally {
      await sandbox.cleanup();
    }
  }
}

/**
 * 8.10 - Standardized Input/Output Handling
 */
class IOStandardizer {
  /**
   * Standardize model output
   */
  standardizeOutput(
    output: any,
    type: IOType
  ): StandardizedOutput {
    return {
      type,
      data: this.formatData(output, type),
      metadata: {
        timestamp: new Date(),
        format: this.detectFormat(output),
        size: this.calculateSize(output)
      }
    };
  }
  
  /**
   * Chain models with automatic type conversion
   */
  async chainModels(
    models: Model[],
    initialInput: any
  ): Promise<StandardizedOutput> {
    let currentOutput = initialInput;
    
    for (const model of models) {
      // Convert output to model's expected input format
      const convertedInput = await this.convertForModel(currentOutput, model);
      
      // Execute model
      currentOutput = await model.run(convertedInput);
      
      // Standardize output
      currentOutput = this.standardizeOutput(currentOutput, model.outputType);
    }
    
    return currentOutput;
  }
}
```

**Benefits (8.7-8.10):**
- ✅ **Isolated Environments**: No dependency conflicts
- ✅ **Cost Transparency**: Real-time cost tracking and budgets
- ✅ **Provenance Verification**: Ensure model authenticity
- ✅ **Sandboxed Execution**: Safe model running
- ✅ **Seamless Chaining**: Universal I/O format

---

**Summary of Section 8 (Hardware Model Selection):**
- ✅ **8.1**: Comprehensive hardware detection with GPU/CPU/RAM/storage
- ✅ **8.2**: Intelligent model selection with hardware-based recommendations
- ✅ **8.3**: Multi-model optimization for 4-5 simultaneous models
- ✅ **8.4**: Dynamic memory management with quantization
- ✅ **8.5**: Intelligent fallback strategies
- ✅ **8.6**: Resumable downloads and LRU eviction
- ✅ **8.7**: Isolated environments with shared common libraries
- ✅ **8.8**: Complete API cost tracking and budgets
- ✅ **8.9**: Model provenance verification and sandboxing
- ✅ **8.10**: Standardized I/O for seamless model chaining

---

### 8.7 Dependency & Environment Management

**Isolated Model Environments:**
- **Per-Model Isolation**: Each Hugging Face model runs in isolated lightweight environment
- **Virtual Environment Approach**: Use virtual environments or containerized approach
- **No Dependency Conflicts**: Models cannot break each other's dependencies

**Efficient Dependency Management:**
- **Shared Common Libraries**: Install common libraries (PyTorch, TensorFlow, transformers) once and reuse
- **Unique Dependencies Only**: Only model-specific dependencies stored per model
- **Dependency Caching**: Cache installed dependencies to avoid reinstallation
- **Version Compatibility Matrix**: Track compatible dependency versions

**Environment Benefits:**
- No dependency hell or conflicts
- Efficient storage (no duplication of common libraries)
- Isolated execution prevents model interference
- Faster setup for new models (reuse common dependencies)

**Transparent Dependency Logs:**
- **Download Tracking**: Log all dependency downloads with source and version
- **Install Tracking**: Track installation steps and dependencies
- **Runtime Tracking**: Monitor dependency usage during execution
- **Storage Tracking**: Track where dependencies are stored
- **Complete Transparency**: Full visibility into all dependency operations

### 8.8 API Model Cost Transparency

**Cost Tracking & Transparency:**
- **Secure API Key Storage**: API keys stored encrypted locally (Gemini, OpenAI, Claude, DeepSeek)
- **Cost Estimation**: Show cost/log estimate before execution (tokens used, approximate $)
- **Usage History**: Maintain usage history showing total spend per model/provider
- **Real-Time Cost Display**: Display costs during execution
- **Budget Alerts**: Warn when approaching budget limits
- **Single-Line Cost Display**: Show run cost in a single line beside each task/node
- **Cost Per Node**: Individual cost tracking for each node in workflow
- **Cost Visualization**: Visual cost breakdown and trends

**Cost Management:**
- **Per-Request Cost Breakdown**: Show cost per request with token counts
- **Monthly/Project Summaries**: Aggregate cost reports by time period or project
- **Cost Comparison**: Compare costs across different models/providers
- **Spending Limits**: Set and enforce spending limits

**Transparency Benefits:**
- No surprise bills
- Clear cost expectations upfront
- Informed model selection based on cost
- Budget control and monitoring

### 8.9 Security & Safety Measures

**API Key Security:**
- **Encrypted Storage**: API keys encrypted at rest using secure encryption
- **Access Control**: Keys only accessible to authorized processes
- **Key Rotation Support**: Support for key rotation and updates

**Model Security:**
- **Checksum Verification**: Verify Hugging Face model downloads via checksum to prevent tampering
- **Tamper Detection**: Detect any modifications to downloaded models
- **Model Provenance**: Verify model origin, version, and authenticity (provenance verification)
- **Source Validation**: Validate model source and authenticity
- **Sandboxed Execution**: Sandbox model execution to prevent arbitrary code execution
- **Repository Security**: Block or sandbox arbitrary code from model repositories

**Security Benefits:**
- Safe to use without compromising system
- Protection against malicious models
- Secure credential management
- Verified model integrity

### 8.10 Standardized Input/Output Handling

**Universal Input/Output Support:**
- **Any Input Type**: Accept text, image, audio, video, or file inputs
- **Any Output Type**: Support text, image, audio, video, or appended file outputs
- **Multimodal Data Support**: Full support for text, images, audio, video, and files across all nodes
- **Standardized JSON Format**: All outputs standardized into consistent JSON format:
  ```json
  {
    "type": "text|image|audio|video|file",
    "data": "...",
    "metadata": {...}
  }
  ```

**Model Chaining Support:**
- **Seamless Chaining**: Output of one model → input of another without format conversion
- **Type Validation**: Automatic type checking and conversion when needed
- **Error Prevention**: Prevent mismatch errors through standardized formats

**Benefits:**
- No format mismatch errors
- Smooth model chaining
- Consistent data handling
- Universal compatibility

---

## 9. Architecture for Auto-Updating Core Templates

The auto-updating template system manages versioned templates for all OLAI components, ensuring user projects stay compatible with new features while maintaining backward compatibility.

---

### 9.1 Template Storage (Comprehensive)

The template storage system uses a distributed architecture with version control, registry services, and CDN distribution for reliable template management.

---

#### **Template Storage Architecture**

```typescript
interface TemplateMetadata {
  id: string;
  name: string;
  category: TemplateCategory;
  version: string;
  description: string;
  author: string;
  license: string;
  
  // Versioning
  semver: {
    major: number;
    minor: number;
    patch: number;
  };
  
  // Dependencies
  dependencies: {
    [packageName: string]: string;  // version constraint
  };
  peerDependencies?: {
    [packageName: string]: string;
  };
  
  // Compatibility
  minOLAIVersion: string;
  compatibleWith: string[];  // Other template versions
  breakingChanges?: string[];
  
  // Files
  files: {
    code: string[];
    tests: string[];
    docs: string[];
    examples: string[];
  };
  
  // Metadata
  tags: string[];
  homepage?: string;
  repository?: string;
  bugs?: string;
  
  // Statistics
  downloads: number;
  stars: number;
  lastUpdated: Date;
  createdAt: Date;
}

type TemplateCategory = 
  | 'backend'
  | 'frontend'
  | 'mobile'
  | 'desktop'
  | 'hardware'
  | 'model-runner'
  | 'integration'
  | 'utility';

interface TemplatePackage {
  metadata: TemplateMetadata;
  files: Map<string, string>;  // path -> content
  checksum: string;
  signature?: string;
}

class TemplateStorageSystem {
  private registry: TemplateRegistry;
  private cdn: CDNClient;
  private cache: TemplateCache;
  private git: GitClient;
  
  /**
   * Initialize template storage
   */
  async initialize(): Promise<void> {
    // 1. Connect to template registry
    await this.registry.connect();
    
    // 2. Initialize local cache
    await this.cache.initialize();
    
    // 3. Sync with CDN
    await this.syncWithCDN();
    
    // 4. Index local templates
    await this.indexLocalTemplates();
  }
  
  /**
   * Store template in version-controlled repository
   */
  async storeTemplate(
    template: TemplatePackage
  ): Promise<void> {
    const repoPath = this.getTemplateRepoPath(template.metadata);
    
    // 1. Clone or update repository
    await this.git.ensureRepo(repoPath);
    
    // 2. Create version branch
    const branchName = `v${template.metadata.version}`;
    await this.git.createBranch(branchName);
    
    // 3. Write template files
    for (const [path, content] of template.files) {
      await fs.writeFile(
        `${repoPath}/${path}`,
        content
      );
    }
    
    // 4. Write metadata
    await fs.writeJSON(
      `${repoPath}/template.json`,
      template.metadata,
      { spaces: 2 }
    );
    
    // 5. Commit and tag
    await this.git.commit(`Release v${template.metadata.version}`);
    await this.git.tag(`v${template.metadata.version}`);
    
    // 6. Push to remote
    await this.git.push({ includeTags: true });
    
    // 7. Register in template registry
    await this.registry.register(template.metadata);
    
    // 8. Upload to CDN
    await this.uploadToCDN(template);
    
    console.log(`✅ Template ${template.metadata.name}@${template.metadata.version} stored`);
  }
  
  /**
   * Upload template to CDN
   */
  private async uploadToCDN(
    template: TemplatePackage
  ): Promise<void> {
    // Create tarball
    const tarball = await this.createTarball(template);
    
    // Generate CDN path
    const cdnPath = this.getCDNPath(template.metadata);
    
    // Upload with cache headers
    await this.cdn.upload(tarball, cdnPath, {
      contentType: 'application/gzip',
      cacheControl: 'public, max-age=31536000',  // 1 year
      metadata: {
        version: template.metadata.version,
        checksum: template.checksum
      }
    });
    
    // Update latest pointer for major.minor version
    const latestPath = this.getLatestPath(template.metadata);
    await this.cdn.updatePointer(latestPath, cdnPath);
  }
  
  /**
   * Download template from storage
   */
  async downloadTemplate(
    templateId: string,
    version?: string
  ): Promise<TemplatePackage> {
    console.log(`📥 Downloading template ${templateId}@${version || 'latest'}...`);
    
    // 1. Check local cache first
    const cached = await this.cache.get(templateId, version);
    if (cached) {
      console.log('✅ Found in cache');
      return cached;
    }
    
    // 2. Fetch from CDN (fast)
    try {
      const template = await this.downloadFromCDN(templateId, version);
      await this.cache.set(templateId, version, template);
      return template;
    } catch (error) {
      console.warn('⚠️  CDN download failed, trying Git...');
    }
    
    // 3. Fallback to Git repository
    const template = await this.downloadFromGit(templateId, version);
    await this.cache.set(templateId, version, template);
    
    return template;
  }
  
  /**
   * Download from CDN
   */
  private async downloadFromCDN(
    templateId: string,
    version?: string
  ): Promise<TemplatePackage> {
    const metadata = await this.registry.getMetadata(templateId, version);
    const cdnPath = this.getCDNPath(metadata);
    
    // Download tarball
    const tarball = await this.cdn.download(cdnPath);
    
    // Verify checksum
    const checksum = await this.calculateChecksum(tarball);
    if (checksum !== metadata.checksum) {
      throw new Error('Checksum mismatch - template may be corrupted');
    }
    
    // Extract tarball
    const files = await this.extractTarball(tarball);
    
    return {
      metadata,
      files,
      checksum: metadata.checksum
    };
  }
  
  /**
   * List available templates
   */
  async listTemplates(
    category?: TemplateCategory
  ): Promise<TemplateMetadata[]> {
    const templates = await this.registry.list({ category });
    
    // Sort by popularity
    return templates.sort((a, b) => b.downloads - a.downloads);
  }
  
  /**
   * Search templates
   */
  async searchTemplates(
    query: string
  ): Promise<TemplateMetadata[]> {
    return await this.registry.search(query);
  }
}

/**
 * Template Cache for Fast Access
 */
class TemplateCache {
  private cacheDir: string;
  private index: Map<string, CachedTemplate>;
  
  async get(
    templateId: string,
    version?: string
  ): Promise<TemplatePackage | null> {
    const key = this.getCacheKey(templateId, version);
    const cached = this.index.get(key);
    
    if (!cached) return null;
    
    // Check if cache is stale
    if (this.isStale(cached)) {
      await this.evict(key);
      return null;
    }
    
    // Load from disk
    return await this.loadFromDisk(cached.path);
  }
  
  async set(
    templateId: string,
    version: string | undefined,
    template: TemplatePackage
  ): Promise<void> {
    const key = this.getCacheKey(templateId, version);
    const cachePath = path.join(this.cacheDir, key);
    
    // Save to disk
    await this.saveToDisk(cachePath, template);
    
    // Update index
    this.index.set(key, {
      path: cachePath,
      metadata: template.metadata,
      cachedAt: new Date(),
      size: await this.calculateSize(cachePath)
    });
    
    // Persist index
    await this.saveIndex();
  }
}

/**
 * Template Registry Service
 */
class TemplateRegistry {
  private apiUrl: string;
  private client: HTTPClient;
  
  /**
   * Register new template version
   */
  async register(metadata: TemplateMetadata): Promise<void> {
    await this.client.post(`${this.apiUrl}/templates`, metadata);
  }
  
  /**
   * Get template metadata
   */
  async getMetadata(
    templateId: string,
    version?: string
  ): Promise<TemplateMetadata> {
    const url = version
      ? `${this.apiUrl}/templates/${templateId}/${version}`
      : `${this.apiUrl}/templates/${templateId}/latest`;
    
    return await this.client.get(url);
  }
  
  /**
   * List templates
   */
  async list(filters?: {
    category?: TemplateCategory;
    tags?: string[];
  }): Promise<TemplateMetadata[]> {
    const params = new URLSearchParams();
    if (filters?.category) params.set('category', filters.category);
    if (filters?.tags) params.set('tags', filters.tags.join(','));
    
    return await this.client.get(`${this.apiUrl}/templates?${params}`);
  }
  
  /**
   * Search templates
   */
  async search(query: string): Promise<TemplateMetadata[]> {
    return await this.client.get(
      `${this.apiUrl}/templates/search?q=${encodeURIComponent(query)}`
    );
  }
}
```

**Benefits:**
- ✅ **Version Control**: Git-based template versioning
- ✅ **CDN Distribution**: Fast global template delivery
- ✅ **Local Cache**: Instant access to frequently used templates
- ✅ **Registry Service**: Centralized template discovery
- ✅ **Checksums**: Verified template integrity

---

### 9.2 Update Mechanism (Comprehensive)

```typescript
interface UpdateCheck {
  templateId: string;
  currentVersion: string;
  latestVersion: string;
  updateAvailable: boolean;
  updateType: 'major' | 'minor' | 'patch';
  releaseNotes: string;
  breakingChanges: string[];
  requiresApproval: boolean;
}

class TemplateUpdateManager {
  private storage: TemplateStorageSystem;
  private notifier: UpdateNotifier;
  
  /**
   * Check for template updates
   */
  async checkForUpdates(
    installedTemplates: InstalledTemplate[]
  ): Promise<UpdateCheck[]> {
    console.log('🔍 Checking for template updates...');
    
    const updates: UpdateCheck[] = [];
    
    for (const installed of installedTemplates) {
      const latest = await this.storage.registry.getMetadata(
        installed.id,
        'latest'
      );
      
      if (semver.gt(latest.version, installed.version)) {
        const updateType = this.determineUpdateType(
          installed.version,
          latest.version
        );
        
        updates.push({
          templateId: installed.id,
          currentVersion: installed.version,
          latestVersion: latest.version,
          updateAvailable: true,
          updateType,
          releaseNotes: await this.getReleaseNotes(installed.id, latest.version),
          breakingChanges: latest.breakingChanges || [],
          requiresApproval: updateType === 'major'
        });
      }
    }
    
    if (updates.length > 0) {
      console.log(`✨ ${updates.length} template update(s) available`);
      await this.notifier.notify(updates);
    } else {
      console.log('✅ All templates are up to date');
    }
    
    return updates;
  }
  
  /**
   * Apply template update
   */
  async applyUpdate(
    update: UpdateCheck,
    projectPath: string
  ): Promise<UpdateResult> {
    console.log(`🔄 Updating ${update.templateId} from ${update.currentVersion} to ${update.latestVersion}...`);
    
    try {
      // 1. Create backup
      const backupPath = await this.createBackup(projectPath);
      console.log(`💾 Backup created: ${backupPath}`);
      
      // 2. Download new template
      const newTemplate = await this.storage.downloadTemplate(
        update.templateId,
        update.latestVersion
      );
      
      // 3. Validate template
      await this.validateTemplate(newTemplate);
      
      // 4. Test template (if tests available)
      if (newTemplate.metadata.files.tests.length > 0) {
        await this.runTemplateTests(newTemplate);
      }
      
      // 5. Generate migration plan
      const migration = await this.generateMigrationPlan(
        update.currentVersion,
        update.latestVersion,
        projectPath
      );
      
      // 6. Execute migration
      await this.executeMigration(migration, projectPath);
      
      // 7. Validate project still works
      const validation = await this.validateProject(projectPath);
      
      if (!validation.passed) {
        console.error('❌ Project validation failed after update');
        await this.rollback(projectPath, backupPath);
        throw new Error('Update validation failed - rolled back');
      }
      
      // 8. Clean up backup (optional)
      if (validation.passed) {
        await this.cleanupBackup(backupPath);
      }
      
      console.log(`✅ Update complete: ${update.templateId}@${update.latestVersion}`);
      
      return {
        success: true,
        previousVersion: update.currentVersion,
        newVersion: update.latestVersion,
        migration,
        validation
      };
      
    } catch (error) {
      console.error(`❌ Update failed: ${error.message}`);
      return {
        success: false,
        error: error.message
      };
    }
  }
  
  /**
   * Automated update system with policies
   */
  async runAutomatedUpdates(
    policy: UpdatePolicy
  ): Promise<void> {
    const installed = await this.getInstalledTemplates();
    const updates = await this.checkForUpdates(installed);
    
    for (const update of updates) {
      // Apply policy
      const shouldUpdate = this.shouldAutoUpdate(update, policy);
      
      if (shouldUpdate) {
        console.log(`🤖 Auto-updating ${update.templateId}...`);
        await this.applyUpdate(update, policy.projectPath);
      } else {
        console.log(`⏸️  Update ${update.templateId} requires manual approval`);
        await this.notifier.notifyManualApprovalRequired(update);
      }
    }
  }
  
  /**
   * Determine if update should be applied automatically
   */
  private shouldAutoUpdate(
    update: UpdateCheck,
    policy: UpdatePolicy
  ): boolean {
    switch (update.updateType) {
      case 'patch':
        return policy.autoPatch;
        
      case 'minor':
        return policy.autoMinor;
        
      case 'major':
        return policy.autoMajor && update.breakingChanges.length === 0;
        
      default:
        return false;
    }
  }
  
  /**
   * Scheduled update checks
   */
  async startScheduledChecks(
    interval: number = 24 * 60 * 60 * 1000  // 24 hours
  ): Promise<void> {
    console.log(`🕐 Starting scheduled update checks (every ${interval / 3600000}h)`);
    
    setInterval(async () => {
      const installed = await this.getInstalledTemplates();
      await this.checkForUpdates(installed);
    }, interval);
  }
  
  /**
   * Webhook-based update notifications
   */
  async setupWebhook(webhookUrl: string): Promise<void> {
    await this.storage.registry.registerWebhook({
      url: webhookUrl,
      events: ['template.published', 'template.deprecated'],
      secret: await this.generateWebhookSecret()
    });
  }
}

/**
 * Update Notifier
 */
class UpdateNotifier {
  /**
   * Notify user of available updates
   */
  async notify(updates: UpdateCheck[]): Promise<void> {
    const notification = {
      title: 'Template Updates Available',
      body: `${updates.length} template update(s) are available`,
      actions: [
        { label: 'View Updates', action: 'viewUpdates' },
        { label: 'Update All', action: 'updateAll' },
        { label: 'Dismiss', action: 'dismiss' }
      ]
    };
    
    await notificationService.send(notification);
    
    // Also log to console
    console.log('\n📦 Template Updates Available:');
    for (const update of updates) {
      console.log(
        `   • ${update.templateId}: ${update.currentVersion} → ${update.latestVersion} ` +
        `(${update.updateType})`
      );
    }
  }
}
```

**Benefits:**
- ✅ **Automatic Detection**: Multiple update detection methods
- ✅ **Smart Policies**: Auto-update patches, manual approve majors
- ✅ **Safe Updates**: Backup, validate, rollback on failure
- ✅ **Scheduled Checks**: Automatic periodic update checks
- ✅ **Webhooks**: Real-time update notifications

---

### 9.3 Compatibility Management (Comprehensive)

```typescript
interface CompatibilityMatrix {
  templateId: string;
  version: string;
  compatible: {
    olaiVersion: string;
    nodeVersion: string;
    dependencies: Record<string, string>;
    otherTemplates: Record<string, string>;
  };
  breakingChanges: BreakingChange[];
  deprecations: Deprecation[];
}

interface BreakingChange {
  version: string;
  description: string;
  migration: string;
  affectedAPIs: string[];
  automated: boolean;  // Can be auto-migrated?
}

class CompatibilityManager {
  /**
   * Check version compatibility
   */
  async checkCompatibility(
    templateVersion: string,
    projectVersion: string
  ): Promise<CompatibilityCheck> {
    const matrix = await this.getCompatibilityMatrix(templateVersion);
    
    return {
      compatible: this.isCompatible(matrix, projectVersion),
      issues: await this.findCompatibilityIssues(matrix, projectVersion),
      migrations: await this.findRequiredMigrations(templateVersion, projectVersion),
      recommendations: await this.generateRecommendations(matrix, projectVersion)
    };
  }
  
  /**
   * Detect breaking changes between versions
   */
  async detectBreakingChanges(
    oldVersion: string,
    newVersion: string
  ): Promise<BreakingChange[]> {
    const changes: BreakingChange[] = [];
    
    // Get all versions between old and new
    const versions = await this.getVersionsBetween(oldVersion, newVersion);
    
    for (const version of versions) {
      const metadata = await templateRegistry.getMetadata(version);
      
      if (metadata.breakingChanges) {
        changes.push(...metadata.breakingChanges.map(bc => ({
          version,
          description: bc.description,
          migration: bc.migration,
          affectedAPIs: bc.affectedAPIs,
          automated: bc.automated
        })));
      }
    }
    
    return changes;
  }
  
  /**
   * Generate migration scripts
   */
  async generateMigrationScript(
    fromVersion: string,
    toVersion: string,
    projectPath: string
  ): Promise<MigrationScript> {
    console.log(`🔧 Generating migration script: ${fromVersion} → ${toVersion}`);
    
    // 1. Analyze project
    const analysis = await this.analyzeProject(projectPath);
    
    // 2. Identify breaking changes
    const breakingChanges = await this.detectBreakingChanges(fromVersion, toVersion);
    
    // 3. Generate migration steps
    const steps: MigrationStep[] = [];
    
    for (const change of breakingChanges) {
      if (change.automated) {
        // Generate automated migration
        const step = await this.generateAutomatedMigration(change, analysis);
        steps.push(step);
      } else {
        // Manual migration required
        steps.push({
          type: 'manual',
          description: change.description,
          instructions: change.migration,
          affectedFiles: this.findAffectedFiles(change, analysis)
        });
      }
    }
    
    // 4. Add dependency updates
    const depUpdates = await this.generateDependencyUpdates(fromVersion, toVersion);
    steps.push(...depUpdates);
    
    return {
      fromVersion,
      toVersion,
      steps,
      estimatedDuration: this.estimateMigrationTime(steps),
      reversible: this.isMigrationReversible(steps)
    };
  }
  
  /**
   * Build compatibility matrix
   */
  async buildCompatibilityMatrix(
    templateId: string,
    version: string
  ): Promise<CompatibilityMatrix> {
    const metadata = await templateRegistry.getMetadata(templateId, version);
    
    return {
      templateId,
      version,
      compatible: {
        olaiVersion: metadata.minOLAIVersion,
        nodeVersion: await this.getRequiredNodeVersion(metadata),
        dependencies: metadata.dependencies,
        otherTemplates: await this.getCompatibleTemplates(metadata)
      },
      breakingChanges: metadata.breakingChanges || [],
      deprecations: await this.getDeprecations(metadata)
    };
  }
  
  /**
   * Semantic versioning rules
   */
  private getUpdateStrategy(updateType: 'major' | 'minor' | 'patch'): UpdateStrategy {
    const strategies: Record<string, UpdateStrategy> = {
      'major': {
        autoUpdate: false,
        requiresApproval: true,
        requiresBackup: true,
        requiresValidation: true,
        notification: 'critical',
        description: 'Major version with breaking changes - manual approval required'
      },
      'minor': {
        autoUpdate: true,
        requiresApproval: false,
        requiresBackup: true,
        requiresValidation: true,
        notification: 'info',
        description: 'Minor version with new features - safe to auto-update'
      },
      'patch': {
        autoUpdate: true,
        requiresApproval: false,
        requiresBackup: false,
        requiresValidation: false,
        notification: 'silent',
        description: 'Patch version with bug fixes - auto-applied'
      }
    };
    
    return strategies[updateType];
  }
}
```

**Benefits:**
- ✅ **Semantic Versioning**: Clear update policies
- ✅ **Breaking Change Detection**: Automatic identification
- ✅ **Migration Scripts**: Automated when possible
- ✅ **Compatibility Matrix**: Clear dependency tracking

---

### 9.4 User Project Compatibility (Comprehensive)

```typescript
class ProjectMigrationSystem {
  /**
   * Check project compatibility with new template
   */
  async checkProjectCompatibility(
    projectPath: string,
    newTemplateVersion: string
  ): Promise<ProjectCompatibility> {
    console.log('🔍 Checking project compatibility...');
    
    // 1. Get current template version
    const currentVersion = await this.getProjectTemplateVersion(projectPath);
    
    // 2. Analyze project structure
    const projectAnalysis = await this.analyzeProjectStructure(projectPath);
    
    // 3. Check compatibility
    const compatibility = await compatibilityManager.checkCompatibility(
      newTemplateVersion,
      currentVersion
    );
    
    // 4. Identify required changes
    const requiredChanges = await this.identifyRequiredChanges(
      projectAnalysis,
      compatibility
    );
    
    return {
      currentVersion,
      targetVersion: newTemplateVersion,
      compatible: compatibility.compatible,
      issues: compatibility.issues,
      requiredChanges,
      migrationComplexity: this.assessMigrationComplexity(requiredChanges),
      estimatedTime: this.estimateMigrationTime(requiredChanges)
    };
  }
  
  /**
   * Execute project migration
   */
  async migrateProject(
    projectPath: string,
    targetVersion: string
  ): Promise<MigrationResult> {
    console.log(`🚀 Starting project migration to ${targetVersion}...`);
    
    try {
      // 1. Backup project
      const backupPath = await this.createProjectBackup(projectPath);
      console.log(`💾 Backup created: ${backupPath}`);
      
      // 2. Analyze current state
      const currentVersion = await this.getProjectTemplateVersion(projectPath);
      const analysis = await this.analyzeProjectStructure(projectPath);
      
      // 3. Generate migration plan
      const migration = await compatibilityManager.generateMigrationScript(
        currentVersion,
        targetVersion,
        projectPath
      );
      
      console.log(`📋 Migration plan: ${migration.steps.length} steps`);
      
      // 4. Execute migration steps
      const results: StepResult[] = [];
      
      for (let i = 0; i < migration.steps.length; i++) {
        const step = migration.steps[i];
        console.log(`\n[${i + 1}/${migration.steps.length}] ${step.description}`);
        
        try {
          const result = await this.executeMigrationStep(step, projectPath);
          results.push({ step, success: true, result });
          console.log(`   ✅ Success`);
        } catch (error) {
          results.push({ step, success: false, error: error.message });
          console.error(`   ❌ Failed: ${error.message}`);
          throw error;  // Stop on first failure
        }
      }
      
      // 5. Update project template version
      await this.updateProjectTemplateVersion(projectPath, targetVersion);
      
      // 6. Validate migrated project
      console.log('\n🔍 Validating migrated project...');
      const validation = await this.validateMigratedProject(projectPath);
      
      if (!validation.passed) {
        throw new Error('Project validation failed after migration');
      }
      
      console.log('✅ Migration complete and validated');
      
      // 7. Clean up backup (optional)
      await this.promptBackupCleanup(backupPath);
      
      return {
        success: true,
        fromVersion: currentVersion,
        toVersion: targetVersion,
        steps: results,
        validation,
        backupPath
      };
      
    } catch (error) {
      console.error(`\n❌ Migration failed: ${error.message}`);
      console.log('🔄 Rolling back changes...');
      
      await this.rollbackMigration(projectPath, backupPath);
      
      return {
        success: false,
        error: error.message,
        backupPath
      };
    }
  }
  
  /**
   * Execute individual migration step
   */
  private async executeMigrationStep(
    step: MigrationStep,
    projectPath: string
  ): Promise<any> {
    switch (step.type) {
      case 'file-rename':
        return await this.renameFile(step.from, step.to, projectPath);
        
      case 'file-modify':
        return await this.modifyFile(step.file, step.changes, projectPath);
        
      case 'dependency-update':
        return await this.updateDependency(step.package, step.version, projectPath);
        
      case 'code-transform':
        return await this.transformCode(step.transformation, projectPath);
        
      case 'config-update':
        return await this.updateConfig(step.config, step.values, projectPath);
        
      case 'manual':
        return await this.promptManualStep(step);
        
      default:
        throw new Error(`Unknown migration step type: ${step.type}`);
    }
  }
  
  /**
   * Validate migrated project
   */
  private async validateMigratedProject(
    projectPath: string
  ): Promise<ValidationResult> {
    const checks: ValidationCheck[] = [];
    
    // 1. Check file structure
    checks.push(await this.validateFileStructure(projectPath));
    
    // 2. Check dependencies
    checks.push(await this.validateDependencies(projectPath));
    
    // 3. Check configuration files
    checks.push(await this.validateConfigurations(projectPath));
    
    // 4. Run tests (if available)
    if (await this.hasTests(projectPath)) {
      checks.push(await this.runTests(projectPath));
    }
    
    // 5. Try building project
    checks.push(await this.tryBuild(projectPath));
    
    const passed = checks.every(c => c.passed);
    
    return {
      passed,
      checks,
      errors: checks.filter(c => !c.passed).map(c => c.error),
      warnings: checks.flatMap(c => c.warnings || [])
    };
  }
  
  /**
   * Rollback migration
   */
  private async rollbackMigration(
    projectPath: string,
    backupPath: string
  ): Promise<void> {
    console.log('🔄 Restoring from backup...');
    
    // Remove current project
    await fs.remove(projectPath);
    
    // Restore backup
    await fs.copy(backupPath, projectPath);
    
    console.log('✅ Project restored to previous state');
  }
}
```

**Benefits:**
- ✅ **Automated Migration**: Execute migrations automatically
- ✅ **Backup & Rollback**: Safe migration with fallback
- ✅ **Validation**: Comprehensive post-migration checks
- ✅ **Manual Steps**: Handle non-automatable changes
- ✅ **Progress Tracking**: Clear migration progress

---

### 9.5 Template Categories (Comprehensive)

```typescript
/**
 * Template Category Definitions
 */
const TEMPLATE_CATEGORIES = {
  backend: {
    name: 'Backend Templates',
    description: 'Server-side application templates',
    subcategories: [
      {
        id: 'fastify',
        name: 'Fastify',
        description: 'Fast and low overhead web framework',
        features: ['TypeScript', 'JSON Schema validation', 'Logging', 'Authentication']
      },
      {
        id: 'express',
        name: 'Express',
        description: 'Minimalist web framework',
        features: ['Middleware', 'Routing', 'Static files', 'Sessions']
      },
      {
        id: 'nestjs',
        name: 'NestJS',
        description: 'Progressive Node.js framework',
        features: ['TypeScript', 'Dependency injection', 'Microservices', 'GraphQL']
      }
    ]
  },
  
  frontend: {
    name: 'Frontend Templates',
    description: 'Client-side application templates',
    subcategories: [
      {
        id: 'react',
        name: 'React',
        description: 'React with TypeScript and Tailwind',
        features: ['TypeScript', 'Tailwind CSS', 'React Router', 'State management']
      },
      {
        id: 'vue',
        name: 'Vue',
        description: 'Vue 3 with Composition API',
        features: ['TypeScript', 'Composition API', 'Vue Router', 'Pinia']
      },
      {
        id: 'svelte',
        name: 'Svelte',
        description: 'Svelte with SvelteKit',
        features: ['TypeScript', 'SvelteKit', 'Server-side rendering', 'Stores']
      }
    ]
  },
  
  mobile: {
    name: 'Mobile Templates',
    description: 'Mobile application templates',
    subcategories: [
      {
        id: 'react-native',
        name: 'React Native',
        description: 'Cross-platform mobile with React Native',
        features: ['TypeScript', 'Navigation', 'Native modules', 'Async storage']
      },
      {
        id: 'flutter',
        name: 'Flutter',
        description: 'Cross-platform mobile with Flutter',
        features: ['Dart', 'Material Design', 'Cupertino', 'State management']
      }
    ]
  },
  
  desktop: {
    name: 'Desktop Templates',
    description: 'Desktop application templates',
    subcategories: [
      {
        id: 'electron',
        name: 'Electron',
        description: 'Cross-platform desktop with Electron',
        features: ['TypeScript', 'IPC', 'Native menus', 'Auto-updater']
      },
      {
        id: 'tauri',
        name: 'Tauri',
        description: 'Lightweight desktop with Tauri',
        features: ['Rust', 'Small bundle', 'Native APIs', 'Security']
      }
    ]
  },
  
  hardware: {
    name: 'Hardware Integration Templates',
    description: 'Templates for hardware device integration',
    subcategories: [
      {
        id: 'camera',
        name: 'Camera Integration',
        description: 'Camera access and image processing',
        features: ['Camera API', 'Image capture', 'Video recording', 'Filters']
      },
      {
        id: 'sensors',
        name: 'Sensor Integration',
        description: 'Device sensor access',
        features: ['Accelerometer', 'Gyroscope', 'GPS', 'Ambient light']
      },
      {
        id: 'bluetooth',
        name: 'Bluetooth Integration',
        description: 'Bluetooth device communication',
        features: ['BLE', 'Device discovery', 'Data transfer', 'Pairing']
      }
    ]
  },
  
  modelRunner: {
    name: 'Model Runner Templates',
    description: 'AI model execution templates',
    subcategories: [
      {
        id: 'huggingface',
        name: 'Hugging Face',
        description: 'Hugging Face model integration',
        features: ['Transformers', 'Pipeline API', 'Model caching', 'Quantization']
      },
      {
        id: 'ollama',
        name: 'Ollama',
        description: 'Local LLM with Ollama',
        features: ['Local models', 'Streaming', 'Context management', 'Multiple models']
      },
      {
        id: 'tensorflowjs',
        name: 'TensorFlow.js',
        description: 'ML in browser/Node.js',
        features: ['Browser support', 'GPU acceleration', 'Model conversion', 'Training']
      }
    ]
  }
} as const;

/**
 * Template Package Manager
 */
class TemplatePackageManager {
  /**
   * Get templates by category
   */
  async getTemplatesByCategory(
    category: TemplateCategory
  ): Promise<TemplateMetadata[]> {
    return await templateRegistry.list({ category });
  }
  
  /**
   * Get template recommendations
   */
  async getRecommendations(
    projectType: string,
    requirements: string[]
  ): Promise<TemplateRecommendation[]> {
    // Use AI to recommend templates
    const recommendations = await llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Recommend OLAI templates for this project:

Project Type: ${projectType}
Requirements: ${requirements.join(', ')}

Available categories:
${Object.entries(TEMPLATE_CATEGORIES).map(([id, cat]) => 
  `- ${cat.name}: ${cat.description}`
).join('\n')}

Recommend 3-5 templates and explain why.
      `
    });
    
    return this.parseRecommendations(recommendations);
  }
  
  /**
   * Install template
   */
  async installTemplate(
    templateId: string,
    projectPath: string,
    options?: InstallOptions
  ): Promise<InstallResult> {
    console.log(`📦 Installing template: ${templateId}...`);
    
    // 1. Download template
    const template = await templateStorage.downloadTemplate(templateId);
    
    // 2. Extract to project
    await this.extractTemplate(template, projectPath, options);
    
    // 3. Install dependencies
    await this.installDependencies(projectPath);
    
    // 4. Run post-install scripts
    if (template.metadata.postInstall) {
      await this.runPostInstallScripts(template.metadata.postInstall, projectPath);
    }
    
    // 5. Update project metadata
    await this.updateProjectMetadata(projectPath, template.metadata);
    
    console.log(`✅ Template installed: ${templateId}@${template.metadata.version}`);
    
    return {
      success: true,
      templateId,
      version: template.metadata.version,
      installedFiles: Array.from(template.files.keys())
    };
  }
}
```

**Benefits:**
- ✅ **Comprehensive Categories**: All template types covered
- ✅ **AI Recommendations**: Smart template suggestions
- ✅ **Easy Installation**: One-command template setup
- ✅ **Post-Install Scripts**: Automated configuration
- ✅ **Subcategories**: Organized template discovery

---

**Summary of Section 9 (Auto-Updating Core Templates):**
- ✅ **9.1**: Version-controlled storage with CDN and local cache
- ✅ **9.2**: Automatic update detection with smart policies
- ✅ **9.3**: Semantic versioning and migration scripts
- ✅ **9.4**: Safe project migration with backup and rollback
- ✅ **9.5**: Comprehensive template categories and AI recommendations

---

## 10. Future Expansion Plan

This section outlines OLAI's roadmap for advanced features, enterprise capabilities, and cutting-edge AI integrations planned for future releases.

---

### 10.1 Agent Memory Improvements (Comprehensive)

Advanced memory systems enable agents to learn from past interactions, maintain project context, and provide increasingly intelligent assistance over time.

---

```typescript
interface AgentMemory {
  projectId: string;
  memoryGraph: MemoryGraph;
  vectorStore: VectorStore;
  conversationHistory: ConversationEntry[];
  learnedPatterns: LearnedPattern[];
  projectKnowledge: ProjectKnowledge;
}

interface MemoryGraph {
  nodes: MemoryNode[];
  edges: MemoryEdge[];
  clusters: MemoryCluster[];
}

interface MemoryNode {
  id: string;
  type: 'concept' | 'decision' | 'pattern' | 'preference' | 'error' | 'solution';
  content: string;
  embedding: number[];
  importance: number;
  accessCount: number;
  lastAccessed: Date;
  relatedNodes: string[];
}

class AgentMemorySystem {
  /**
   * Store interaction in memory graph
   */
  async storeInteraction(
    interaction: AgentInteraction
  ): Promise<void> {
    // 1. Extract key concepts
    const concepts = await this.extractConcepts(interaction);
    
    // 2. Generate embeddings
    const embeddings = await this.generateEmbeddings(concepts);
    
    // 3. Store in vector database
    await this.vectorStore.upsert(embeddings);
    
    // 4. Build memory graph connections
    await this.buildGraphConnections(concepts);
    
    // 5. Identify patterns
    const patterns = await this.identifyPatterns(interaction);
    await this.storePatterns(patterns);
    
    // 6. Update project knowledge
    await this.updateProjectKnowledge(interaction);
  }
  
  /**
   * Retrieve relevant context for query
   */
  async retrieveContext(
    query: string,
    projectId: string,
    limit: number = 10
  ): Promise<MemoryContext> {
    // 1. Generate query embedding
    const queryEmbedding = await this.embedModel.embed(query);
    
    // 2. Semantic search in vector store
    const similarMemories = await this.vectorStore.search(
      queryEmbedding,
      { limit, projectId }
    );
    
    // 3. Graph-based expansion
    const expandedContext = await this.expandWithGraph(similarMemories);
    
    // 4. Rank by relevance and recency
    const ranked = this.rankMemories(expandedContext, query);
    
    // 5. Compress if needed
    if (ranked.length > limit) {
      return await this.compressContext(ranked, limit);
    }
    
    return {
      memories: ranked,
      patterns: await this.getRelatedPatterns(ranked),
      suggestions: await this.generateSuggestions(ranked, query)
    };
  }
  
  /**
   * Graphical memory visualization
   */
  async visualizeMemory(
    projectId: string
  ): Promise<MemoryVisualization> {
    const memory = await this.getProjectMemory(projectId);
    
    // Generate force-directed graph layout
    const layout = await this.generateGraphLayout(memory.memoryGraph);
    
    return {
      nodes: memory.memoryGraph.nodes.map(node => ({
        id: node.id,
        label: this.summarizeNode(node),
        type: node.type,
        size: Math.log(node.accessCount + 1) * 10,
        color: this.getNodeColor(node.type),
        position: layout.positions[node.id]
      })),
      edges: memory.memoryGraph.edges.map(edge => ({
        from: edge.source,
        to: edge.target,
        strength: edge.weight,
        type: edge.type
      })),
      clusters: memory.memoryGraph.clusters.map(cluster => ({
        id: cluster.id,
        label: cluster.theme,
        members: cluster.nodeIds,
        color: this.getClusterColor(cluster.id)
      }))
    };
  }
  
  /**
   * Project-specific training
   */
  async trainProjectMemory(
    projectId: string
  ): Promise<TrainingResult> {
    const memory = await this.getProjectMemory(projectId);
    
    // 1. Collect training data from interactions
    const trainingData = await this.collectTrainingData(memory);
    
    // 2. Identify frequent patterns
    const patterns = await this.analyzePatterns(trainingData);
    
    // 3. Build project-specific knowledge base
    const knowledgeBase = await this.buildKnowledgeBase(patterns);
    
    // 4. Fine-tune retrieval for this project
    await this.optimizeRetrieval(projectId, knowledgeBase);
    
    return {
      patternsLearned: patterns.length,
      knowledgeItems: knowledgeBase.items.length,
      retrievalImprovement: await this.measureImprovement(projectId)
    };
  }
  
  /**
   * Memory compression
   */
  async compressMemory(
    memories: MemoryNode[],
    targetSize: number
  ): Promise<MemoryNode[]> {
    // Use LLM to summarize and compress
    const compressed = await this.llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
Compress these memories into ${targetSize} most important items:

${memories.map(m => `- ${m.content}`).join('\n')}

Preserve key information and relationships.
      `
    });
    
    return this.parseCompressedMemories(compressed);
  }
}

/**
 * Project Memory Isolation
 */
class ProjectMemoryManager {
  /**
   * Create isolated memory space for project
   */
  async createProjectMemory(
    projectId: string
  ): Promise<ProjectMemory> {
    return {
      projectId,
      namespace: `project:${projectId}`,
      vectorStore: await this.createIsolatedVectorStore(projectId),
      graph: new MemoryGraph(),
      accessControl: {
        read: [projectId],
        write: [projectId]
      },
      createdAt: new Date()
    };
  }
  
  /**
   * Prevent cross-project memory leakage
   */
  private async enforceIsolation(
    query: VectorQuery
  ): Promise<VectorQuery> {
    return {
      ...query,
      filter: {
        ...query.filter,
        projectId: query.projectId
      }
    };
  }
}
```

**Benefits:**
- ✅ **Long-Term Memory**: Persistent context across sessions
- ✅ **Graph Structure**: Complex relationship modeling
- ✅ **Visual Representation**: Interactive memory visualization
- ✅ **Project-Specific Learning**: Tailored to each project
- ✅ **Contextual Retrieval**: Relevant context for every query
- ✅ **Memory Compression**: Efficient storage and retrieval

---

### 10.2 Offline-First Agent Execution (Comprehensive)

```typescript
class OfflineAgentSystem {
  /**
   * Execute workflow offline
   */
  async executeOffline(
    workflow: Workflow
  ): Promise<ExecutionResult> {
    // 1. Check connectivity
    const isOnline = await this.checkConnectivity();
    
    if (!isOnline) {
      console.log('📴 Offline mode - using local resources');
    }
    
    // 2. Replace online dependencies with local alternatives
    const localizedWorkflow = await this.localizeWorkflow(workflow);
    
    // 3. Queue for offline execution
    await this.offlineQueue.enqueue({
      workflow: localizedWorkflow,
      timestamp: new Date(),
      syncRequired: !isOnline
    });
    
    // 4. Execute with local resources
    const result = await this.executeWithLocalResources(localizedWorkflow);
    
    // 5. Store for later sync
    if (!isOnline) {
      await this.storePendingSync(result);
    }
    
    return result;
  }
  
  /**
   * Sync when back online
   */
  async syncWhenOnline(): Promise<void> {
    // Monitor connectivity
    this.connectivityMonitor.on('online', async () => {
      console.log('🌐 Back online - syncing...');
      
      const pending = await this.getPendingSync();
      
      for (const item of pending) {
        try {
          await this.syncItem(item);
          await this.markSynced(item.id);
        } catch (error) {
          // Handle conflict
          await this.resolveConflict(item, error);
        }
      }
    });
  }
  
  /**
   * Local connector system
   */
  private localConnectors = {
    'file-system': new FileSystemConnector(),
    'sqlite': new SQLiteConnector(),
    'local-api': new LocalAPIConnector()
  };
  
  /**
   * Graceful degradation
   */
  async degradeToLocal(
    node: WorkflowNode
  ): Promise<WorkflowNode> {
    const alternatives = {
      'gemini-api': 'ollama-llama3',
      's3-storage': 'local-storage',
      'cloud-db': 'sqlite'
    };
    
    if (alternatives[node.type]) {
      return {
        ...node,
        type: alternatives[node.type],
        data: {
          ...node.data,
          fallback: true
        }
      };
    }
    
    return node;
  }
}
```

**Benefits:**
- ✅ **Full Offline Operation**: Complete workflows without internet
- ✅ **Local Model Execution**: Hugging Face, Ollama models
- ✅ **Automatic Sync**: Seamless sync when online
- ✅ **Enterprise Security**: Perfect for air-gapped environments
- ✅ **Graceful Degradation**: Smart fallback to local resources

---

### 10.3 Multi-Platform Build Pipeline (Comprehensive)

```typescript
class ExtendedBuildPipeline {
  /**
   * Build for iOS
   */
  async buildiOS(workflow: Workflow): Promise<iOSBuildResult> {
    // Xcode project generation
    // Fastlane integration
    // TestFlight upload
    return await this.executeIOSBuild(workflow);
  }
  
  /**
   * Build for Linux
   */
  async buildLinux(workflow: Workflow): Promise<LinuxBuildResult> {
    // AppImage, Snap, or Flatpak
    return await this.executeLinuxBuild(workflow);
  }
  
  /**
   * Build WebAssembly
   */
  async buildWasm(workflow: Workflow): Promise<WasmBuildResult> {
    // Rust/C++ to WASM compilation
    return await this.executeWasmBuild(workflow);
  }
  
  /**
   * Build Progressive Web App
   */
  async buildPWA(workflow: Workflow): Promise<PWABuildResult> {
    // Service worker generation
    // Manifest configuration
    // Offline support
    return await this.executePWABuild(workflow);
  }
}
```

---

### 10.4 Plugins System (Comprehensive)

```typescript
interface PluginManifest {
  id: string;
  name: string;
  version: string;
  type: 'node' | 'agent' | 'template' | 'integration';
  author: string;
  license: string;
  
  // Entry points
  main: string;
  exports: Record<string, string>;
  
  // Dependencies
  dependencies: Record<string, string>;
  olaiVersion: string;
  
  // Permissions
  permissions: Permission[];
  
  // Lifecycle hooks
  hooks: {
    onInstall?: string;
    onActivate?: string;
    onDeactivate?: string;
    onUninstall?: string;
  };
}

class PluginSystem {
  /**
   * Load and register plugin
   */
  async loadPlugin(pluginPath: string): Promise<Plugin> {
    // 1. Load manifest
    const manifest = await this.loadManifest(pluginPath);
    
    // 2. Validate plugin
    await this.validatePlugin(manifest);
    
    // 3. Check permissions
    await this.checkPermissions(manifest.permissions);
    
    // 4. Create isolated sandbox
    const sandbox = await this.createSandbox(manifest);
    
    // 5. Load plugin code
    const plugin = await sandbox.load(manifest.main);
    
    // 6. Register in registry
    await this.pluginRegistry.register(manifest.id, plugin);
    
    // 7. Run activation hook
    if (manifest.hooks.onActivate) {
      await plugin[manifest.hooks.onActivate]();
    }
    
    return plugin;
  }
  
  /**
   * Plugin isolation sandbox
   */
  private async createSandbox(
    manifest: PluginManifest
  ): Promise<PluginSandbox> {
    return {
      // Limited API access
      api: this.createLimitedAPI(manifest.permissions),
      
      // Resource limits
      limits: {
        memory: '100MB',
        cpu: '50%',
        storage: '10MB'
      },
      
      // Isolated execution
      vm: new VM({
        sandbox: {
          olai: this.createOLAIAPI(manifest.permissions),
          console: this.createSafeConsole()
        }
      })
    };
  }
}
```

---

### 10.5 Marketplace (Comprehensive)

```typescript
class OLAIMarketplace {
  /**
   * Publish item to marketplace
   */
  async publish(
    item: MarketplaceItem
  ): Promise<PublishResult> {
    // 1. Validate item
    const validation = await this.validateItem(item);
    if (!validation.passed) {
      throw new Error(`Validation failed: ${validation.errors.join(', ')}`);
    }
    
    // 2. Security scan
    const securityScan = await this.scanForSecurity(item);
    if (securityScan.issues.length > 0) {
      throw new Error(`Security issues found: ${securityScan.issues.join(', ')}`);
    }
    
    // 3. Generate listing
    const listing = await this.generateListing(item);
    
    // 4. Set pricing
    if (item.paid) {
      listing.pricing = await this.setupPricing(item.price);
    }
    
    // 5. Publish
    await this.marketplaceDB.insert(listing);
    
    // 6. Notify followers
    await this.notifyFollowers(item.author);
    
    return {
      success: true,
      listingId: listing.id,
      url: `${MARKETPLACE_URL}/items/${listing.id}`
    };
  }
  
  /**
   * Revenue sharing
   */
  async processPayment(
    purchase: Purchase
  ): Promise<void> {
    const item = await this.getItem(purchase.itemId);
    
    // Split: 70% creator, 30% platform
    const creatorShare = purchase.amount * 0.70;
    const platformShare = purchase.amount * 0.30;
    
    await this.transferFunds(item.author, creatorShare);
    await this.recordRevenue(platformShare);
  }
  
  /**
   * AI-powered discovery
   */
  async recommend(
    userId: string,
    context?: string
  ): Promise<MarketplaceItem[]> {
    // 1. Get user history
    const history = await this.getUserHistory(userId);
    
    // 2. Generate recommendations using AI
    const recommendations = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Recommend marketplace items for this user:

User History:
${history.map(h => `- ${h.itemName}: ${h.rating}/5`).join('\n')}

Current Context: ${context || 'General browsing'}

Consider:
- User preferences
- Popular items
- Complementary items
- New releases

Recommend 10 items with reasoning.
      `
    });
    
    return this.parseRecommendations(recommendations);
  }
}
```

---

### 10.6 Agent Fine-Tuning (Comprehensive)

```typescript
class OnDemandTrainingSystem {
  /**
   * Auto-train model for project
   */
  async trainForProject(
    projectRequirements: string,
    projectData: any[]
  ): Promise<TrainingResult> {
    console.log('🤖 Starting on-demand model training...');
    
    // 1. Discover optimal datasets
    const datasets = await this.discoverDatasets(projectRequirements);
    console.log(`📊 Found ${datasets.length} suitable datasets`);
    
    // 2. Prepare training data
    const trainingData = await this.prepareTrainingData(
      datasets,
      projectData
    );
    
    // 3. Select base model
    const baseModel = await this.selectBaseModel(projectRequirements);
    
    // 4. Fine-tune model
    const fineTunedModel = await this.fineTune({
      baseModel,
      trainingData,
      epochs: 3,
      learningRate: 0.0001,
      validationSplit: 0.2
    });
    
    // 5. Validate improvements
    const validation = await this.validateModel(fineTunedModel);
    
    // 6. Deploy if improved
    if (validation.improved) {
      await this.deployModel(fineTunedModel);
      console.log('✅ Model deployed');
    }
    
    return {
      success: validation.improved,
      metrics: validation.metrics,
      modelId: fineTunedModel.id
    };
  }
  
  /**
   * Dataset discovery using AI
   */
  private async discoverDatasets(
    requirements: string
  ): Promise<Dataset[]> {
    const discovery = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Find optimal training datasets for this project:

Requirements: ${requirements}

Search Hugging Face, Kaggle, and other sources.
Recommend 5 best datasets with reasoning.
      `
    });
    
    return this.parseDatasetRecommendations(discovery);
  }
}
```

---

### 10.7 Vector Memory & RAG (Comprehensive)

```typescript
class RAGPipeline {
  /**
   * Setup RAG pipeline
   */
  async setupRAG(
    documents: Document[]
  ): Promise<RAGSystem> {
    // 1. Chunk documents
    const chunks = await this.chunkDocuments(documents);
    
    // 2. Generate embeddings
    const embeddings = await this.generateEmbeddings(chunks);
    
    // 3. Store in vector DB
    await this.vectorDB.upsert(embeddings);
    
    // 4. Setup retriever
    const retriever = new HybridRetriever({
      vectorDB: this.vectorDB,
      reranker: new CrossEncoderReranker()
    });
    
    return {
      retriever,
      query: async (question: string) => {
        const retrieved = await retriever.retrieve(question, 10);
        const reranked = await retriever.rerank(retrieved, question);
        return reranked.slice(0, 5);
      }
    };
  }
  
  /**
   * Intelligent chunking
   */
  private async chunkDocuments(
    documents: Document[]
  ): Promise<Chunk[]> {
    const chunks: Chunk[] = [];
    
    for (const doc of documents) {
      // Semantic chunking (not just size-based)
      const semanticChunks = await this.semanticChunk(doc.content);
      
      for (const chunk of semanticChunks) {
        chunks.push({
          id: generateUUID(),
          content: chunk.text,
          metadata: {
            source: doc.id,
            page: chunk.page,
            section: chunk.section
          },
          embedding: await this.embedModel.embed(chunk.text)
        });
      }
    }
    
    return chunks;
  }
}
```

**Benefits (10.2-10.7):**
- ✅ **Offline-First**: Full functionality without internet
- ✅ **Extended Platforms**: iOS, Linux, WASM, PWA
- ✅ **Plugin System**: Extensible architecture
- ✅ **Marketplace**: Revenue sharing for creators
- ✅ **On-Demand Training**: Auto-train models
- ✅ **RAG Pipelines**: Built-in vector search

---

### 10.3 Multi-Platform Build Pipeline

**Platform Support:**
- iOS (React Native, Flutter)
- Linux (Electron, Tauri)
- WebAssembly
- Progressive Web Apps

**Pipeline Features:**
- Parallel builds
- Build caching
- Automated testing
- Distribution automation

### 10.4 Plugins System

**Plugin Architecture:**
- Plugin API
- Plugin registry
- Plugin lifecycle
- Plugin isolation

**Plugin Types:**
- Custom nodes
- Custom agents
- Custom templates
- Custom integrations

### 10.5 Marketplace

**Marketplace Features:**
- Node marketplace
- Template marketplace
- Agent marketplace
- Integration marketplace
- **Workflow Marketplace**: Share or sell ready-made workflows (e.g., "Resume screener bot" available in one click)
- **One-Click Installation**: Install workflows/agents with single click
- **Version Management**: Track and update shared workflows

**Marketplace Infrastructure:**
- User authentication
- Payment processing
- Rating and reviews
- Version management
- **Revenue Sharing**: Creators can monetize their workflows and agents
- **Discovery System**: AI-powered search and recommendations
- **Certified Connectors**: Curated and verified integrations with quality badges
- **Vetted Connectors**: Thoroughly reviewed and tested connectors for reliability
- **Marketplace Monetization**: Workflow packs, model packs, and revenue share for creators

### 10.6 Agent Fine-Tuning

**Fine-Tuning Strategy:**
- Task-specific fine-tuning
- User preference learning
- Domain adaptation
- Performance optimization
- **Automatic Model Training (On-Demand)**: Automatically find best dataset for required project and train models
- **Dataset Discovery**: AI identifies and recommends optimal training datasets
- **Training Pipeline**: Automated training pipeline with validation and testing
- **Model Optimization**: Continuous model improvement based on project requirements

**Fine-Tuning Process:**
- Collect training data
- **Dataset Selection**: AI selects best datasets for project requirements
- Fine-tune models
- Validate improvements
- Deploy updated models
- **On-Demand Training**: Train models when needed for specific projects

### 10.7 Vector Memory for Agents

**Vector Memory System:**
- Embedding generation
- Vector storage
- Similarity search
- Context retrieval

**Implementation:**
- Vector database (Pinecone, Weaviate, Qdrant)
- Embedding models
- Search algorithms
- Memory management

### 10.8 through 10.15 (Consolidated Comprehensive Implementation)

```typescript
/**
 * 10.8 - AI Connector Builder
 */
class AIConnectorBuilder {
  /**
   * Generate connector from natural language description
   */
  async buildConnector(description: string): Promise<Connector> {
    console.log('🤖 Building connector from description...');
    
    // Use AI to generate connector code
    const code = await this.llm.complete({
      model: 'claude-3.5-sonnet',
      prompt: `
Generate a complete Node.js connector for this API:

Description: ${description}

Include:
- Authentication handling
- Rate limiting
- Error handling
- Type definitions
- Tests

Respond with complete, runnable code.
      `
    });
    
    // Parse and validate generated code
    const connector = await this.parseConnector(code);
    
    // Auto-test connector
    const testResults = await this.testConnector(connector);
    
    if (!testResults.passed) {
      // Iterate with AI to fix issues
      return await this.fixConnector(connector, testResults.errors);
    }
    
    return connector;
  }
  
  /**
   * GitHub repository integration
   */
  async integrateGitHubRepo(repoUrl: string): Promise<RepoIntegration> {
    // 1. Clone repository
    const repo = await this.cloneRepo(repoUrl);
    
    // 2. Analyze structure
    const analysis = await this.analyzeRepo(repo);
    
    // 3. Extract functions/APIs
    const exports = await this.extractExports(repo, analysis);
    
    // 4. Generate OLAI nodes
    const nodes = await this.generateNodes(exports);
    
    // 5. Install dependencies
    await this.installRepoDependencies(repo);
    
    return {
      repo: repoUrl,
      nodes,
      analysis,
      ready: true
    };
  }
}

/**
 * 10.9 & 10.10 - Auto-Optimize Workflows
 */
class WorkflowOptimizer {
  /**
   * Continuously monitor and optimize
   */
  async monitorAndOptimize(workflowId: string): Promise<void> {
    setInterval(async () => {
      const metrics = await this.collectMetrics(workflowId);
      
      // Check for optimization opportunities
      const opportunities = await this.findOptimizations(metrics);
      
      if (opportunities.length > 0) {
        await this.notifyUserOfOptimizations(opportunities);
      }
    }, 60 * 60 * 1000);  // Every hour
  }
  
  /**
   * AI-powered optimization suggestions
   */
  private async findOptimizations(
    metrics: WorkflowMetrics
  ): Promise<Optimization[]> {
    const suggestions = await this.llm.complete({
      model: 'gemini-1.5-pro',
      prompt: `
Analyze this workflow and suggest optimizations:

Metrics:
- Cost: $${metrics.cost}/month
- Execution Time: ${metrics.avgExecutionTime}s
- API Calls: ${metrics.apiCalls}/day
- Local Model Capable: ${metrics.canRunLocally}

Suggest:
1. Cost reductions
2. Performance improvements
3. Resource optimizations

Be specific and quantify savings.
      `
    });
    
    return this.parseOptimizations(suggestions);
  }
}

/**
 * 10.11 - Self-Improving Agents
 */
class SelfImprovingAgent {
  /**
   * Learn from usage patterns
   */
  async learnFromUsage(userId: string): Promise<LearningResult> {
    const usage = await this.getUserUsage(userId);
    
    // Detect patterns
    const patterns = await this.detectPatterns(usage);
    
    // Generate proactive suggestions
    for (const pattern of patterns) {
      if (pattern.frequency > 5 && !pattern.automated) {
        await this.suggestAutomation(pattern);
      }
    }
    
    return {
      patternsDetected: patterns.length,
      suggestionsGenerated: patterns.filter(p => !p.automated).length
    };
  }
  
  /**
   * Proactive suggestion example
   */
  private async suggestAutomation(pattern: UsagePattern): Promise<void> {
    const suggestion = await this.llm.complete({
      model: 'gemini-1.5-flash',
      prompt: `
User repeatedly does: ${pattern.description}

Suggest an automation to save time. Be specific and actionable.
      `
    });
    
    await notificationService.send({
      title: 'Automation Suggestion',
      body: suggestion,
      actions: [
        { label: 'Auto-create', action: 'create-automation' },
        { label: 'Dismiss', action: 'dismiss' }
      ]
    });
  }
}

/**
 * 10.12 - Real-Time Collaboration
 */
class RealtimeCollaboration {
  private wss: WebSocketServer;
  private sessions: Map<string, CollabSession>;
  
  /**
   * Handle user connection
   */
  async handleConnection(userId: string, workflowId: string): Promise<void> {
    const session = this.getOrCreateSession(workflowId);
    
    // Add user to session
    session.users.add(userId);
    
    // Broadcast presence
    this.broadcast(workflowId, {
      type: 'user-joined',
      userId,
      cursor: null
    });
    
    // Setup event handlers
    this.setupHandlers(userId, workflowId);
  }
  
  /**
   * Handle real-time edits
   */
  private setupHandlers(userId: string, workflowId: string): void {
    // Cursor movement
    this.on(`cursor:${userId}`, (position) => {
      this.broadcast(workflowId, {
        type: 'cursor-move',
        userId,
        position
      }, [userId]);  // Exclude sender
    });
    
    // Node edit
    this.on(`edit:${userId}`, async (edit) => {
      // Apply operational transformation for conflict resolution
      const transformed = await this.transformEdit(edit, workflowId);
      
      // Apply to workflow
      await this.applyEdit(workflowId, transformed);
      
      // Broadcast to other users
      this.broadcast(workflowId, {
        type: 'edit',
        userId,
        edit: transformed
      }, [userId]);
    });
    
    // Comments
    this.on(`comment:${userId}`, (comment) => {
      this.broadcast(workflowId, {
        type: 'comment',
        userId,
        comment
      });
    });
  }
  
  /**
   * Operational transformation for conflict resolution
   */
  private async transformEdit(
    edit: Edit,
    workflowId: string
  ): Promise<Edit> {
    const currentState = await this.getWorkflowState(workflowId);
    
    // Transform edit based on current state
    return OT.transform(edit, currentState);
  }
}

/**
 * 10.13 - SaaS & Productization
 */
class SaaSPlatform {
  /**
   * White-label configuration
   */
  async configureWhiteLabel(config: WhiteLabelConfig): Promise<void> {
    // Apply branding
    await this.applyBranding({
      logo: config.logo,
      colors: config.colors,
      fonts: config.fonts,
      favicon: config.favicon
    });
    
    // Setup custom domain
    await this.setupCustomDomain(config.domain);
    
    // Configure email templates
    await this.customizeEmailTemplates(config.branding);
  }
  
  /**
   * Multi-tenant isolation
   */
  private async ensureTenantIsolation(
    tenantId: string,
    operation: () => Promise<any>
  ): Promise<any> {
    // Set tenant context
    const context = { tenantId };
    
    // Execute in isolated context
    return await this.isolatedExecutor.run(context, operation);
  }
  
  /**
   * Instant API generation
   */
  async exposeAsAPI(workflowId: string): Promise<APIEndpoint> {
    const workflow = await this.getWorkflow(workflowId);
    
    // Generate OpenAPI spec
    const spec = await this.generateOpenAPISpec(workflow);
    
    // Create endpoint
    const endpoint = await this.createEndpoint({
      path: `/api/workflows/${workflowId}/execute`,
      method: 'POST',
      handler: async (req, res) => {
        const result = await workflowExecutor.execute(workflow, req.body);
        res.json(result);
      },
      rateLimit: {
        windowMs: 60000,
        max: 100
      }
    });
    
    // Generate documentation
    const docs = await this.generateAPIDocs(spec);
    
    return {
      url: endpoint.url,
      spec,
      docs
    };
  }
}

/**
 * 10.14 - Developer SDK & CLI
 */
class DeveloperSDK {
  /**
   * SDK usage example (JavaScript)
   */
  static exampleUsage = `
// Initialize OLAI SDK
import { OLAI } from '@olai/sdk';

const olai = new OLAI({
  apiKey: process.env.OLAI_API_KEY
});

// Create workflow
const workflow = await olai.workflows.create({
  name: 'Email Processor',
  nodes: [
    {
      type: 'email-trigger',
      config: { folder: 'inbox' }
    },
    {
      type: 'llm-summarize',
      config: { model: 'gemini-1.5-flash' }
    },
    {
      type: 'slack-send',
      config: { channel: '#summaries' }
    }
  ]
});

// Execute workflow
const result = await workflow.execute({
  input: { emailId: '12345' }
});

// Model.run API
const summary = await olai.model.run({
  model: 'gemini-1.5-flash',
  input: 'Summarize this email...',
  output: 'text',
  config: { maxTokens: 150 }
});
  `;
  
  /**
   * CLI commands
   */
  static cliCommands = {
    'olai start': 'Start local OLAI server',
    'olai create <name>': 'Create new workflow',
    'olai run <workflow>': 'Execute workflow',
    'olai deploy <workflow>': 'Deploy workflow to cloud',
    'olai logs <workflow>': 'View workflow logs',
    'olai models list': 'List available models',
    'olai models pull <model>': 'Download model locally'
  };
}

/**
 * 10.15 - Self-Hosted Runtime
 */
class SelfHostedRuntime {
  /**
   * First-run setup
   */
  async runFirstTimeSetup(): Promise<SetupResult> {
    console.log('🚀 Welcome to OLAI Self-Hosted Runtime!\n');
    
    // 1. Hardware checks
    console.log('🔍 Detecting hardware...');
    const hardware = await hardwareDetector.detect();
    this.displayHardwareInfo(hardware);
    
    // 2. Model recommendations
    console.log('\n💡 Model Recommendations:');
    const recommendations = await this.recommendModels(hardware);
    this.displayRecommendations(recommendations);
    
    // 3. Optional SaaS linking
    console.log('\n🌐 SaaS Integration (Optional):');
    const linkSaaS = await this.promptYesNo(
      'Link to OLAI Cloud for marketplace access?'
    );
    
    if (linkSaaS) {
      await this.linkSaaSAccount();
    }
    
    // 4. Start server
    console.log('\n✅ Setup complete! Starting server...');
    await this.startServer();
    
    return {
      hardware,
      saasLinked: linkSaaS,
      serverUrl: 'http://localhost:3000'
    };
  }
  
  /**
   * Start local server
   */
  private async startServer(): Promise<void> {
    const app = fastify();
    
    // Serve web UI
    app.register(fastifyStatic, {
      root: path.join(__dirname, 'ui'),
      prefix: '/'
    });
    
    // API routes
    app.register(apiRoutes, { prefix: '/api' });
    
    // Start server
    await app.listen({ port: 3000 });
    
    console.log('🎉 OLAI running at http://localhost:3000');
    
    // Auto-open browser or VS Code
    if (process.env.VSCODE_INTEGRATION) {
      await this.openVSCode();
    } else {
      await open('http://localhost:3000');
    }
  }
}
```

**Benefits (10.8-10.15):**
- ✅ **AI Connector Builder**: Natural language → working integrations
- ✅ **Auto-Optimize**: Continuous cost & performance optimization
- ✅ **Self-Improving**: Learns patterns, proactive suggestions
- ✅ **Real-Time Collab**: Figma-like co-editing with live cursors
- ✅ **SaaS Platform**: White-label, multi-tenant, instant APIs
- ✅ **Developer SDK**: Full SDK in JS/Python with Model.run API
- ✅ **Self-Hosted**: Complete runtime with offline capabilities
- ✅ **VS Code Integration**: First-class editor experience

---

**Summary of Section 10 (Future Expansion Plan):**
- ✅ **10.1**: Agent memory with graph visualization and project-specific learning
- ✅ **10.2**: Offline-first execution with local models and graceful degradation
- ✅ **10.3**: Extended platforms (iOS, Linux, WASM, PWA)
- ✅ **10.4**: Plugin system with sandboxed execution
- ✅ **10.5**: Marketplace with AI discovery and revenue sharing
- ✅ **10.6**: On-demand model training with dataset discovery
- ✅ **10.7**: Vector memory and RAG pipelines
- ✅ **10.8**: AI connector builder for any API
- ✅ **10.9-10.10**: Auto-optimization of workflows
- ✅ **10.11**: Self-improving agents with usage learning
- ✅ **10.12**: Real-time collaboration like Figma
- ✅ **10.13**: Full SaaS platform with white-labeling
- ✅ **10.14**: Developer SDK & CLI with VS Code integration
- ✅ **10.15**: Self-hosted runtime with enterprise distribution

---

**Benefits:**
- Data privacy and security
- Offline operation
- No cloud dependency
- Enterprise compliance
- Developer-friendly local development

### 10.16 Monetization Strategy

**Pricing Tiers:**
- **Freemium**: Local runs free with limits (limited runs, basic features)
- **Pro (Monthly)**: Unlocks RAG, multi-agent, priority model access, increased run quotas
- **Enterprise Licensing**: On-prem + SLA, professional services, advanced features
- **API Pass-Through Margin**: Optional transparent markup on API calls (requires explicit opt-in)

**Billing Models:**
- **Local Execution**: Free (compute on user hardware); premium local features may require Pro
- **API Provider Direct**: User provides own API keys → user billed by provider; OLAI shows estimates and tracks usage but does not bill
- **API Relay via OLAI (Optional)**: Route calls through OLAI SaaS for convenience → OLAI bills user per-call at transparent markup (must show pre-run estimate and require explicit consent)
- **Marketplace Purchases**: One-off or subscription for premium workflows
- **Enterprise**: Flat license + on-prem options; revenue share for certified partners

**Cost Transparency:**
- **Always Show Estimates**: Cost estimate shown before any chargeable API calls
- **Require Opt-In**: Explicit consent required before any charges
- **Usage Tracking**: Track all usage and costs (even when using own API keys)
- **Budget Alerts**: Warn when approaching budget limits

**Revenue Streams:**
- **Subscription Revenue**: Monthly/annual subscriptions
- **Marketplace Revenue Share**: Revenue share from premium workflows and model packs
- **Enterprise Licensing**: One-time or annual enterprise licenses
- **Professional Services**: Custom implementation and support services

**Pricing Factors:**
- Number of workflow runs
- Model usage (local vs API)
- Storage and compute resources
- Advanced features (RAG, multi-agent, etc.)
- Support level (community vs enterprise)

### 10.17 Production Architecture

**High-Level Architecture:**
- **API Gateway & Web UI (SaaS)**: Chat UI, editor, marketplace, billing
- **Orchestrator/Workflow Engine**: Schedules runs, enforces policies, stores metadata
- **Model Runner Service Pool**: Stateless workers that dispatch to API adapters or local agents
- **Worker Pool Architecture**: Stateless worker pool with queue-based job distribution
- **Dependency Manager & Model Cache**: Per-model envs, shared layer for common libs
- **Vector DB & Storage**: Embeddings, persistence, and search
- **Cost Estimator and Billing Engine**: Usage tracking and projections
- **SDKs, CLI & Local Agent**: For developers and on-prem customers
- **Security Layer**: Secrets vault, RBAC, audit logs, sandboxing
- **Telemetry & Observability**: Traces, execution logs, SLOs, replay capability, ChainId tracking

**Recommended Technology Stack:**
- **Frontend**: React + Tailwind (web), VS Code Webview + extension for editor integration
- **Backend (SaaS)**: Node.js/TypeScript or Python (FastAPI) for API; Kubernetes for orchestration
- **Queue**: Redis + Bull / RabbitMQ for job queue (built-in, no external Redis required unless desired)
- **Model Runner**: Workers in containers (K8s pods) with GPU scheduling via device plugin
- **Execution Engine**: Rust/Go-based engine for lightweight, high-performance execution
- **Local Agent**: Docker image and native installers (npm, pip, binary)
- **Vector DB**: Open-source FAISS/Weaviate locally; optional hosted vector store
- **Secrets**: Vault or KMS + encrypted store
- **Telemetry**: Prometheus, Grafana, Sentry, ELK/Opensearch
- **Packaging**: pip wheel, npm package, native installer, Docker image

**Scaling Architecture:**
- **Serverless Workers**: Spin up only when needed for cost efficiency
- **Lightweight Server**: Serverless or lightweight server architecture for scalability
- **Worker Pools**: Stateless worker pools with queue-based job distribution
- **GPU Scheduling**: GPU scheduling via Kubernetes device plugin for model execution
- **Built-in Horizontal Scaling**: No Redis setup required (built-in queue & cache)
- **Queue Architecture**: Kafka/Redis for reliable job ingestion and retries (optional external)
- **Worker Autoscaling**: Kubernetes Horizontal Pod Autoscaler with job concurrency limits
- **Smart Scaling Slider**: Configure "Handle up to 1000 requests/min" with automatic scaling
- **Sharded Vector DB**: Scale vector search with sharding (Pinecone-like or self-hosted FAISS)
- **CDN**: Static assets + edge caching for embeddings
- **Edge Caching**: Edge caching for embeddings and frequently accessed data
- **Multi-Region Deployment**: Low latency with failover capabilities
- **Instrumentation**: Prometheus/Grafana, Sentry for monitoring and alerting
- **SLOs**: Capacity planning for token/requests throughput

**One-Click Deployment:**
- **Serverless Backends**: One-click deploy to Vercel, Fly.io, AWS Lambda
- **No Infrastructure Setup**: Built-in queue & cache, no external dependencies required
- **Auto-Configuration**: Automatic configuration for deployment target

**Security & Privacy:**
- **TLS Everywhere**: All communications encrypted in transit
- **Encryption at Rest**: KMS for secrets and sensitive data
- **Encrypted API Keys**: Per-user encrypted storage; enterprise HSM option
- **HSM/Secrets Manager**: Enterprise-grade Hardware Security Module support for key storage
- **Free Tier Security**: Free tier includes encrypted credentials + RBAC basics
- **Privacy-First**: Local mode ensures no data leaves machine
- **Tenant Isolation**: Complete isolation across storage and runtime
- **Fine-Grained Permissions**: Per-workflow, per-user permission controls
- **Sandboxed Execution**: User-submitted code/nodes run in sandbox
- **No Arbitrary Remote Code**: Default deny for remote code execution
- **Block Untrusted Code**: Block arbitrary/untrusted code execution by default
- **Enterprise Opt-In**: Enterprise users can opt-in for explicit code execution with proper controls
- **Model Verification**: Package checksums and source validation
- **Data Retention Policies**: Configurable retention with easy deletion for compliance
- **Audit Logs**: Complete audit trail for compliance and security
- **Policy-as-Code**: Define security and governance policies as code
- **Enterprise Compliance**: FedRAMP/GDPR compliance support
- **SSO Support**: SAML/OAuth single sign-on for enterprise
- **Advanced RBAC**: Role-based access control with policy enforcement

**Reliability Features:**
- **Multi-Region Failover**: Automatic failover between regions
- **Job Retries**: Automatic retry with exponential backoff
- **Health Checks**: Continuous health monitoring and auto-recovery
- **Backup & Recovery**: Regular backups with point-in-time recovery
- **Disaster Recovery**: Documented DR procedures and testing

---

## Appendix A: Node Implementation Status

### Implemented Nodes (50+)
[List all implemented nodes with brief descriptions - see section 1.2]

### Pending Nodes (40+)
[List all pending nodes from utilityNodesImplementation.json - see section 1.3]

---

## Appendix B: Technology Stack

**Backend:**
- Fastify (Node.js framework)
- TypeScript
- PostgreSQL, MongoDB
- JWT authentication

**Frontend:**
- React
- TypeScript
- ReactFlow
- Tailwind CSS

**AI Models:**
- Gemini API
- Ollama (local)
- Hugging Face

**Build Tools:**
- Vite/Webpack
- TypeScript Compiler
- ESLint, Prettier

---

## Appendix C: Key Decisions & Rationale

**Modular Assembly Approach:**
- Enables rapid development
- Maintains consistency
- Simplifies maintenance
- Supports extensibility

**Node-Based Architecture:**
- Visual workflow design
- Reusable components
- Easy testing
- Clear dependencies

**Multi-Agent System:**
- Specialized agents for specialized tasks
- Parallel execution
- Better quality
- Scalable architecture

---

---

## 11. Complete End-to-End Workflow

This section demonstrates OLAI's complete orchestration from initial user prompt to production-ready application delivery across all platforms.

---

### 11.1 User Journey: From Prompt to Production (Comprehensive)

```typescript
/**
 * Complete End-to-End Workflow Orchestrator
 */
class WorkflowOrchestrator {
  private pmAgent: PMAgent;
  private architectAgent: ArchitectAgent;
  private codingAgent: CodingAgent;
  private researchAgent: ResearchAgent;
  private testingAgent: TestingAgent;
  private builderAgent: BuilderAgent;
  private reviewAgent: ReviewAgent;
  private releaseAgent: ReleaseAgent;
  
  /**
   * Main orchestration method - handles entire workflow
   */
  async executeFullWorkflow(
    userPrompt: string,
    deadline?: Date
  ): Promise<ProjectDelivery> {
    console.log('🚀 Starting OLAI Project Workflow...\n');
    
    // Step 1: Initial Prompt Analysis
    const analysis = await this.analyzePrompt(userPrompt, deadline);
    
    // Step 2: Requirements Gathering
    const requirements = await this.gatherRequirements(analysis);
    
    // Step 3: Model Selection (if AI-powered)
    let modelSelection: ModelSelection | null = null;
    if (requirements.requiresAI) {
      modelSelection = await this.selectModels(requirements);
    }
    
    // Step 4: Architecture Design
    const architecture = await this.designArchitecture(requirements, modelSelection);
    
    // Step 5: Development Phase
    const codebase = await this.developApplication(architecture, requirements);
    
    // Step 6: Testing Phase
    const testResults = await this.testApplication(codebase);
    
    // Step 7: Review Phase
    const reviewResults = await this.reviewCode(codebase);
    
    // Step 8: Continuous Improvement
    const optimized = await this.optimizeUntilDeadline(
      codebase,
      deadline || this.calculateDeadline(requirements)
    );
    
    // Step 9: Build Phase
    const builds = await this.buildAllPlatforms(optimized);
    
    // Step 10: Release Phase
    const release = await this.prepareRelease(builds, requirements);
    
    // Step 11: Delivery
    const delivery = await this.deliverProject(release);
    
    console.log('✅ Project Complete!\n');
    return delivery;
  }
  
  /**
   * Step 1: Analyze Initial Prompt
   */
  private async analyzePrompt(
    prompt: string,
    deadline?: Date
  ): Promise<PromptAnalysis> {
    console.log('📋 Step 1: Analyzing prompt...');
    
    const analysis = await this.pmAgent.analyze({
      prompt,
      deadline,
      timestamp: new Date()
    });
    
    console.log(`   Project Type: ${analysis.projectType}`);
    console.log(`   Complexity: ${analysis.complexity}`);
    console.log(`   Requires AI: ${analysis.requiresAI ? 'Yes' : 'No'}`);
    if (deadline) {
      console.log(`   Deadline: ${deadline.toLocaleString()}`);
    }
    console.log('');
    
    return analysis;
  }
  
  /**
   * Step 2: Three-Document Requirements-First Flow
   *
   * CRITICAL WORKFLOW: Before any implementation begins, the PM Agent creates three comprehensive documents
   * that serve as the single source of truth for the entire project lifecycle.
   */
  private async gatherRequirements(
    analysis: PromptAnalysis
  ): Promise<ProjectRequirements> {
    console.log('📋 Step 2: Three-Document Requirements-First Flow...\n');

    // ===== THREE-DOCUMENT CREATION PROCESS =====

    // Document 1: Single Page Idea Summary
    console.log('   📄 Creating Document 1: Single Page Idea Summary...');
    const ideaSummary = await this.createIdeaSummary(analysis);
    console.log('   ✅ Idea Summary created\n');

    // Document 2: Detailed Technical Documentation
    console.log('   📚 Creating Document 2: Detailed Technical Documentation...');
    const technicalDocs = await this.createTechnicalDocumentation(analysis, ideaSummary);
    console.log('   ✅ Technical Documentation created\n');

    // Document 3: Project Map (Nodular Tree View)
    console.log('   🗺️  Creating Document 3: Project Map (Nodular Tree)...');
    const projectMap = await this.createProjectMap(analysis, technicalDocs);
    console.log('   ✅ Project Map created\n');

    // ===== USER REVIEW & APPROVAL =====
    console.log('   👀 Presenting documents for user review...\n');

    const userFeedback = await this.presentDocumentsForReview(
      ideaSummary,
      technicalDocs,
      projectMap
    );

    if (!userFeedback.approved) {
      console.log('   🔄 User requested changes, iterating...');
      return await this.iterateOnDocuments(
        userFeedback.changes,
        ideaSummary,
        technicalDocs,
        projectMap
      );
    }

    console.log('   ✅ All documents approved by user\n');

    // ===== REQUIREMENTS EXTRACTION =====
    // Extract final requirements from approved documents
    const requirements = await this.extractRequirementsFromDocuments(
      ideaSummary,
      technicalDocs,
      projectMap
    );

    console.log('   🎯 Requirements extracted from approved documents\n');
    return requirements;
  }

  /**
   * Creates Document 1: Single Page Idea Summary
   */
  private async createIdeaSummary(analysis: PromptAnalysis): Promise<IdeaSummary> {
    return await this.pmAgent.generateIdeaSummary({
      userPrompt: analysis.userPrompt,
      projectType: analysis.projectType,
      initialAnalysis: analysis,
      format: 'single-page'
    });
  }

  /**
   * Creates Document 2: Detailed Technical Documentation
   */
  private async createTechnicalDocumentation(
    analysis: PromptAnalysis,
    ideaSummary: IdeaSummary
  ): Promise<TechnicalDocumentation> {
    return await this.pmAgent.generateTechnicalDocumentation({
      ideaSummary,
      analysis,
      includeDetails: {
        aiModels: true,
        algorithms: true,
        modules: true,
        workflows: true,
        services: true,
        apis: true,
        dataFlows: true,
        integrations: true
      }
    });
  }

  /**
   * Creates Document 3: Project Map (Nodular Tree View)
   */
  private async createProjectMap(
    analysis: PromptAnalysis,
    technicalDocs: TechnicalDocumentation
  ): Promise<ProjectMap> {
    return await this.pmAgent.generateProjectMap({
      technicalDocumentation: technicalDocs,
      analysis,
      structure: 'nodular-tree',
      includeDependencies: true,
      includeRelationships: true
    });
  }

  /**
   * Presents all three documents for user review
   */
  private async presentDocumentsForReview(
    ideaSummary: IdeaSummary,
    technicalDocs: TechnicalDocumentation,
    projectMap: ProjectMap
  ): Promise<UserReview> {
    console.log('   📋 Document 1: Idea Summary');
    console.log('   📚 Document 2: Technical Documentation');
    console.log('   🗺️  Document 3: Project Map');

    // In real implementation, show these in the UI for user review
    return await this.getUserApproval();
  }

  /**
   * Extracts final requirements from approved documents
   */
  private async extractRequirementsFromDocuments(
    ideaSummary: IdeaSummary,
    technicalDocs: TechnicalDocumentation,
    projectMap: ProjectMap
  ): Promise<ProjectRequirements> {
    return {
      projectType: ideaSummary.projectType,
      features: technicalDocs.features,
      constraints: technicalDocs.constraints,
      technicalRequirements: technicalDocs.technicalStack,
      aiModels: technicalDocs.aiModels,
      architecture: technicalDocs.architecture,
      projectMap: projectMap,
      documents: {
        ideaSummary,
        technicalDocs,
        projectMap
      }
    };
  }
  
  /**
   * Step 3: Model Selection (AI-powered projects)
   */
  private async selectModels(
    requirements: ProjectRequirements
  ): Promise<ModelSelection> {
    console.log('🤖 Step 3: Selecting AI models...\n');
    
    // Detect hardware capabilities
    const hardware = await this.researchAgent.detectHardware();
    console.log(`   GPU: ${hardware.gpu || 'None'}`);
    console.log(`   RAM: ${hardware.ram}GB`);
    console.log(`   VRAM: ${hardware.vram || 0}GB\n`);
    
    // Identify required models
    const requiredModels = await this.researchAgent.identifyModels(requirements);
    console.log(`   Required models: ${requiredModels.length}`);
    
    // Check compatibility
    const compatible = await this.researchAgent.checkCompatibility(
      requiredModels,
      hardware
    );
    
    // Ensure multi-model execution is smooth
    if (requiredModels.length >= 4) {
      console.log(`   Testing multi-model execution (${requiredModels.length} models)...`);
      const canRunSimultaneously = await this.researchAgent.testMultiModelExecution(
        compatible,
        hardware
      );
      
      if (!canRunSimultaneously) {
        console.log('   ⚠️  Suggesting optimized alternatives...');
        const alternatives = await this.researchAgent.suggestAlternatives(
          requiredModels,
          hardware
        );
        console.log(`   ✅ Found ${alternatives.length} compatible alternatives\n`);
        return { models: alternatives, hardware };
      }
    }
    
    console.log('   ✅ All models compatible\n');
    return { models: compatible, hardware };
  }
  
  /**
   * Step 4: Architecture Design
   */
  private async designArchitecture(
    requirements: ProjectRequirements,
    modelSelection: ModelSelection | null
  ): Promise<Architecture> {
    console.log('🏗️  Step 4: Designing architecture...\n');
    
    const architecture = await this.architectAgent.design({
      requirements,
      models: modelSelection?.models || [],
      patterns: ['microservices', 'event-driven', 'modular']
    });
    
    console.log(`   Folder Structure: ${architecture.folders.length} directories`);
    console.log(`   API Endpoints: ${architecture.endpoints.length} routes`);
    console.log(`   Database: ${architecture.database.type}`);
    console.log(`   Frontend: ${architecture.frontend.framework}`);
    console.log('');
    
    // PM reviews architecture
    const approved = await this.pmAgent.reviewArchitecture(architecture);
    
    if (!approved.approved) {
      console.log('   🔄 Revising architecture...');
      return await this.designArchitecture(requirements, modelSelection);
    }
    
    console.log('   ✅ Architecture approved\n');
    return architecture;
  }
  
  /**
   * Step 5: Development Phase with Parallel Execution
   */
  private async developApplication(
    architecture: Architecture,
    requirements: ProjectRequirements
  ): Promise<Codebase> {
    console.log('💻 Step 5: Development phase...\n');
    
    // Break into tasks
    const tasks = await this.pmAgent.breakIntoTasks(architecture, requirements);
    console.log(`   Total tasks: ${tasks.length}`);
    
    // Prioritize tasks
    const prioritized = await this.pmAgent.prioritizeTasks(tasks);
    
    const codebase: Codebase = {
      files: new Map(),
      structure: architecture.folders,
      dependencies: []
    };
    
    // Execute tasks with progress tracking
    let completed = 0;
    for (const task of prioritized) {
      completed++;
      console.log(`   [${completed}/${tasks.length}] ${task.description}`);
      
      // Code generation
      const code = await this.codingAgent.generateCode(task);
      
      // Add to codebase
      codebase.files.set(task.targetFile, code);
      
      // Progress update
      await this.pmAgent.updateProgress(completed / tasks.length);
    }
    
    console.log('\n   ✅ Development complete\n');
    return codebase;
  }
  
  /**
   * Step 6: Testing Phase
   */
  private async testApplication(
    codebase: Codebase
  ): Promise<TestResults> {
    console.log('🧪 Step 6: Testing phase...\n');
    
    // Generate tests
    const tests = await this.testingAgent.generateTests(codebase);
    console.log(`   Generated ${tests.length} tests`);
    
    // Run tests
    const results = await this.testingAgent.runTests(tests);
    
    console.log(`   Passed: ${results.passed}/${results.total}`);
    console.log(`   Failed: ${results.failed}/${results.total}`);
    
    // Fix failures
    if (results.failed > 0) {
      console.log('\n   🔧 Fixing issues...');
      
      for (const failure of results.failures) {
        const fix = await this.codingAgent.fixIssue(failure, codebase);
        codebase.files.set(fix.file, fix.code);
      }
      
      // Re-run tests
      console.log('   🔄 Re-running tests...');
      return await this.testApplication(codebase);
    }
    
    console.log('   ✅ All tests passed\n');
    return results;
  }
  
  /**
   * Step 7: Code Review
   */
  private async reviewCode(
    codebase: Codebase
  ): Promise<ReviewResults> {
    console.log('👁️  Step 7: Code review...\n');
    
    const review = await this.reviewAgent.audit(codebase);
    
    console.log(`   Issues found: ${review.issues.length}`);
    console.log(`   Suggestions: ${review.suggestions.length}`);
    
    // Implement improvements
    if (review.suggestions.length > 0) {
      console.log('\n   ✨ Implementing improvements...');
      
      for (const suggestion of review.suggestions) {
        const improved = await this.codingAgent.implement(suggestion, codebase);
        codebase.files.set(improved.file, improved.code);
      }
    }
    
    console.log('   ✅ Code review complete\n');
    return review;
  }
  
  /**
   * Step 8: Continuous Improvement Until Deadline
   */
  private async optimizeUntilDeadline(
    codebase: Codebase,
    deadline: Date
  ): Promise<Codebase> {
    console.log('⚡ Step 8: Continuous improvement...\n');
    
    const startTime = Date.now();
    const timeAvailable = deadline.getTime() - startTime;
    
    console.log(`   Time until deadline: ${Math.round(timeAvailable / 60000)} minutes`);
    
    let iteration = 1;
    while (Date.now() < deadline.getTime() - 600000) {  // Stop 10 min before deadline
      console.log(`\n   Iteration ${iteration}:`);
      
      // Identify optimization opportunities
      const opportunities = await this.pmAgent.findOptimizations(codebase);
      
      if (opportunities.length === 0) {
        console.log('   No more optimizations found');
        break;
      }
      
      // Implement highest priority optimization
      const top = opportunities[0];
      console.log(`   - ${top.description}`);
      
      const optimized = await this.codingAgent.optimize(top, codebase);
      codebase.files.set(optimized.file, optimized.code);
      
      iteration++;
    }
    
    console.log('\n   ✅ Optimization complete\n');
    return codebase;
  }
  
  /**
   * Step 9: Build All Platforms in Parallel
   */
  private async buildAllPlatforms(
    codebase: Codebase
  ): Promise<PlatformBuilds> {
    console.log('🏭 Step 9: Building all platforms...\n');
    
    const platforms = ['web', 'android', 'windows', 'macos'];
    const builds: PlatformBuilds = {};
    
    // Parallel builds
    const buildPromises = platforms.map(async (platform) => {
      console.log(`   Building ${platform}...`);
      
      const build = await this.builderAgent.build({
        platform,
        codebase,
        config: this.getBuildConfig(platform)
      });
      
      console.log(`   ✅ ${platform} build complete`);
      return { platform, build };
    });
    
    const results = await Promise.all(buildPromises);
    
    for (const { platform, build } of results) {
      builds[platform] = build;
    }
    
    console.log('\n   ✅ All platforms built\n');
    return builds;
  }
  
  /**
   * Step 10: Prepare Release Package
   */
  private async prepareRelease(
    builds: PlatformBuilds,
    requirements: ProjectRequirements
  ): Promise<Release> {
    console.log('📦 Step 10: Preparing release...\n');
    
    const release = await this.releaseAgent.package({
      builds,
      requirements,
      version: '1.0.0'
    });
    
    console.log(`   Release package: ${release.packagePath}`);
    console.log(`   Size: ${release.totalSize} MB`);
    console.log(`   Platforms: ${Object.keys(builds).join(', ')}`);
    console.log('');
    
    // Validate all builds
    const validation = await this.releaseAgent.validate(release);
    
    if (!validation.passed) {
      throw new Error('Release validation failed');
    }
    
    console.log('   ✅ Release ready\n');
    return release;
  }
  
  /**
   * Step 11: Deliver Project to User
   */
  private async deliverProject(
    release: Release
  ): Promise<ProjectDelivery> {
    console.log('🎁 Step 11: Delivering project...\n');
    
    const delivery: ProjectDelivery = {
      releasePackage: release.packagePath,
      builds: release.builds,
      documentation: await this.generateDocumentation(release),
      installationGuide: await this.generateInstallationGuide(release),
      deliveredAt: new Date()
    };
    
    console.log(`   📄 Documentation: ${delivery.documentation}`);
    console.log(`   📖 Installation guide: ${delivery.installationGuide}`);
    console.log(`   📦 Package: ${delivery.releasePackage}`);
    console.log('');
    
    return delivery;
  }
  
  // Helper methods
  private async getUserInput(question: Question): Promise<string> {
    // In real system, this would wait for actual user input
    return question.defaultAnswer || 'User response';
  }
  
  private needsMoreInfo(requirements: Partial<ProjectRequirements>): boolean {
    // Check if requirements are complete enough
    return Object.values(requirements).some(v => v === undefined);
  }
  
  private calculateDeadline(requirements: ProjectRequirements): Date {
    // Default deadline based on complexity
    const hours = requirements.complexity === 'high' ? 48 : 24;
    return new Date(Date.now() + hours * 60 * 60 * 1000);
  }
  
  private getBuildConfig(platform: string): BuildConfig {
    return {
      platform,
      optimization: 'production',
      minify: true,
      sourceMaps: false
    };
  }
  
  private async generateDocumentation(release: Release): Promise<string> {
    return `${release.packagePath}/README.md`;
  }
  
  private async generateInstallationGuide(release: Release): Promise<string> {
    return `${release.packagePath}/INSTALL.md`;
  }
}
```

**Benefits:**
- ✅ **Complete Orchestration**: Entire workflow from prompt to delivery
- ✅ **Parallel Execution**: Multiple agents work simultaneously
- ✅ **Progress Tracking**: Real-time updates at every step
- ✅ **Error Recovery**: Automatic retries and fixes
- ✅ **Deadline Management**: Optimizes until time runs out
- ✅ **Multi-Platform**: All platforms built in parallel

---

### 11.2 Example: Portfolio Website Workflow (Comprehensive)

```typescript
/**
 * Real-World Example: Portfolio Website
 * Demonstrates UI-only project without AI models
 */
class PortfolioWorkflowExample {
  async execute(): Promise<ProjectDelivery> {
    // User prompt
    const prompt = "Build me a portfolio website by 6:00 PM";
    const deadline = new Date();
    deadline.setHours(18, 0, 0, 0);  // 6:00 PM today
    
    console.log('👤 User Prompt: "Build me a portfolio website by 6:00 PM"\n');
    console.log(`⏰ Deadline: ${deadline.toLocaleTimeString()}\n`);
    
    // ========================================
    // STEP 1: PM Agent Analysis
    // ========================================
    console.log('🤖 PM Agent Analysis:\n');
    
    const analysis = {
      projectType: 'portfolio-website',
      requiresAI: false,
      complexity: 'medium',
      estimatedTime: '4 hours',
      features: ['responsive-design', 'projects-showcase', 'contact-form', 'social-links']
    };
    
    console.log(`   Project Type: ${analysis.projectType}`);
    console.log(`   Requires AI: ${analysis.requiresAI} ✅`);
    console.log(`   Complexity: ${analysis.complexity}`);
    console.log(`   Approach: Pure UI/Backend (no models needed)\n`);
    
    // ========================================
    // STEP 2: Dynamic Questions
    // ========================================
    console.log('❓ PM Agent Questions:\n');
    
    const questions = [
      { q: "What's your name and profession?", a: "John Smith, Full-Stack Developer" },
      { q: "What social media links should be included?", a: "GitHub, LinkedIn, Twitter" },
      { q: "What projects should be showcased?", a: "3 recent projects: TaskManager, EcommerceApp, WeatherDashboard" },
      { q: "Preferred color scheme?", a: "Dark mode with blue accents" },
      { q: "Any specific features?", a: "Blog section and contact form" }
    ];
    
    const userInfo: any = {};
    for (const { q, a } of questions) {
      console.log(`   Q: ${q}`);
      console.log(`   A: ${a}\n`);
      
      // Parse answers into structured data
      if (q.includes('name')) {
        const [name, profession] = a.split(', ');
        userInfo.name = name;
        userInfo.profession = profession;
      } else if (q.includes('social')) {
        userInfo.social = a.split(', ');
      } else if (q.includes('projects')) {
        userInfo.projects = ['TaskManager', 'EcommerceApp', 'WeatherDashboard'];
      } else if (q.includes('color')) {
        userInfo.theme = 'dark';
        userInfo.accentColor = 'blue';
      } else if (q.includes('features')) {
        userInfo.features = ['blog', 'contact-form'];
      }
    }
    
    // ========================================
    // STEP 3: Architecture Design
    // ========================================
    console.log('🏗️  Architecture Agent Design:\n');
    
    const architecture = {
      frontend: {
        framework: 'React 18 + TypeScript',
        styling: 'Tailwind CSS',
        routing: 'React Router',
        components: [
          'Hero', 'About', 'Projects', 'Blog', 'Contact', 'Footer'
        ]
      },
      backend: {
        framework: 'Fastify + TypeScript',
        endpoints: [
          'POST /api/contact',
          'GET /api/blog',
          'POST /api/blog (admin only)'
        ]
      },
      database: {
        type: 'PostgreSQL',
        tables: ['blog_posts', 'contact_messages']
      }
    };
    
    console.log(`   Frontend: ${architecture.frontend.framework}`);
    console.log(`   Styling: ${architecture.frontend.styling}`);
    console.log(`   Backend: ${architecture.backend.framework}`);
    console.log(`   Database: ${architecture.database.type}`);
    console.log(`   Components: ${architecture.frontend.components.length}\n`);
    
    // ========================================
    // STEP 4: Development
    // ========================================
    console.log('💻 Coding Agent - Development:\n');
    
    const files = [
      'src/components/Hero.tsx',
      'src/components/About.tsx',
      'src/components/Projects.tsx',
      'src/components/Blog.tsx',
      'src/components/Contact.tsx',
      'src/pages/Home.tsx',
      'backend/routes/contact.ts',
      'backend/routes/blog.ts',
      'backend/db/schema.sql'
    ];
    
    for (let i = 0; i < files.length; i++) {
      console.log(`   [${i + 1}/${files.length}] Generating ${files[i]}`);
      await this.delay(100);  // Simulate work
    }
    console.log('');
    
    // Example generated component
    const heroComponent = `
import React from 'react';

export const Hero: React.FC = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-900">
      <div className="text-center">
        <h1 className="text-6xl font-bold text-white mb-4">
          ${userInfo.name}
        </h1>
        <p className="text-2xl text-blue-400 mb-8">
          ${userInfo.profession}
        </p>
        <div className="flex gap-4 justify-center">
          ${userInfo.social.map((s: string) => `
            <a href="https://${s.toLowerCase()}.com" className="text-gray-400 hover:text-blue-400">
              ${s}
            </a>
          `).join('')}
        </div>
      </div>
    </div>
  );
};
    `;
    
    console.log('   📄 Generated Hero Component (preview):');
    console.log(heroComponent.trim() + '\n');
    
    // ========================================
    // STEP 5: Testing
    // ========================================
    console.log('🧪 Testing Agent:\n');
    console.log('   Generated 15 unit tests');
    console.log('   Generated 8 integration tests');
    console.log('   Running tests...');
    await this.delay(500);
    console.log('   ✅ All 23 tests passed\n');
    
    // ========================================
    // STEP 6: Review & Optimization
    // ========================================
    console.log('👁️  Review Agent:\n');
    console.log('   ✅ Code quality: Excellent');
    console.log('   ✅ Accessibility: WCAG 2.1 AA compliant');
    console.log('   ✅ Performance: Lighthouse score 98/100');
    console.log('   ✅ SEO: All meta tags present\n');
    
    // ========================================
    // STEP 7: Continuous Improvement
    // ========================================
    console.log('⚡ Continuous Improvement:\n');
    
    const improvements = [
      'Added lazy loading for images',
      'Implemented service worker for offline support',
      'Optimized bundle size (reduced by 30%)',
      'Added smooth scroll animations',
      'Implemented dark mode toggle'
    ];
    
    for (const improvement of improvements) {
      console.log(`   ✨ ${improvement}`);
      await this.delay(100);
    }
    console.log('');
    
    // ========================================
    // STEP 8: Multi-Platform Build
    // ========================================
    console.log('🏭 Builder Agent - Platform Builds:\n');
    
    const buildResults = await Promise.all([
      this.buildPlatform('Web (Vite)', '2.3 MB'),
      this.buildPlatform('Android APK', '8.5 MB'),
      this.buildPlatform('Windows EXE', '65 MB'),
      this.buildPlatform('macOS App', '58 MB')
    ]);
    
    console.log('');
    
    // ========================================
    // STEP 9: Delivery
    // ========================================
    console.log('🎁 Release Agent - Delivery:\n');
    console.log('   📦 Package: portfolio-john-smith-v1.0.0.zip');
    console.log('   📄 README.md generated');
    console.log('   📖 INSTALL.md generated');
    console.log('   🌐 Preview URL: https://john-smith-portfolio.olai.app');
    console.log(`   ⏰ Delivered at: ${new Date().toLocaleTimeString()}`);
    console.log(`   ✅ Delivered ${Math.floor((deadline.getTime() - Date.now()) / 60000)} minutes before deadline!\n`);
    
    return {
      releasePackage: 'portfolio-john-smith-v1.0.0.zip',
      builds: buildResults,
      previewUrl: 'https://john-smith-portfolio.olai.app',
      deliveredAt: new Date()
    };
  }
  
  private async buildPlatform(name: string, size: string): Promise<any> {
    console.log(`   Building ${name}...`);
    await this.delay(300);
    console.log(`   ✅ ${name} complete (${size})`);
    return { platform: name, size, path: `./${name.toLowerCase().replace(/\s+/g, '-')}` };
  }
  
  private delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

---

### 11.3 Example: AI Patient Monitoring System (Comprehensive)

```typescript
/**
 * Real-World Example: AI Patient Monitoring System
 * Demonstrates multi-model AI integration
 */
class PatientMonitoringWorkflowExample {
  async execute(): Promise<ProjectDelivery> {
    // User prompt
    const prompt = "Create an AI-powered patient monitoring system";
    
    console.log('🏥 User Prompt: "Create an AI-powered patient monitoring system"\n');
    
    // ========================================
    // STEP 1: PM Agent Analysis
    // ========================================
    console.log('🤖 PM Agent Analysis:\n');
    
    const analysis = {
      projectType: 'healthcare-ai-system',
      requiresAI: true,
      complexity: 'high',
      estimatedModels: 5,
      features: ['real-time-monitoring', 'alert-system', 'pose-detection', 'vital-signs']
    };
    
    console.log(`   Project Type: ${analysis.projectType}`);
    console.log(`   Requires AI: ${analysis.requiresAI} 🤖`);
    console.log(`   Complexity: ${analysis.complexity}`);
    console.log(`   Estimated Models: ${analysis.estimatedModels}\n`);
    
    // ========================================
    // STEP 2: Requirements Gathering
    // ========================================
    console.log('❓ PM Agent Questions:\n');
    
    const questions = [
      { q: "What type of monitoring?", a: "Vital signs (heart rate, O2) + behavior monitoring" },
      { q: "What data sources?", a: "Camera feed + wearable sensors" },
      { q: "Alert thresholds?", a: "HR > 120 or < 50, O2 < 90%, fall detection" },
      { q: "User interface?", a: "Real-time dashboard with historical charts" }
    ];
    
    const requirements: any = {};
    for (const { q, a } of questions) {
      console.log(`   Q: ${q}`);
      console.log(`   A: ${a}\n`);
    }
    
    requirements.monitoring = ['vitals', 'behavior'];
    requirements.sources = ['camera', 'wearables'];
    requirements.alerts = ['heart-rate', 'oxygen', 'falls'];
    
    // ========================================
    // STEP 3: Hardware Detection
    // ========================================
    console.log('🔍 Research Agent - Hardware Detection:\n');
    
    const hardware = {
      gpu: 'NVIDIA RTX 3060',
      vram: '12 GB',
      ram: '32 GB',
      cpu: 'AMD Ryzen 7 5800X',
      cuda: '11.8'
    };
    
    console.log(`   GPU: ${hardware.gpu}`);
    console.log(`   VRAM: ${hardware.vram}`);
    console.log(`   RAM: ${hardware.ram}`);
    console.log(`   CUDA: ${hardware.cuda}`);
    console.log('   ✅ Hardware suitable for multi-model execution\n');
    
    // ========================================
    // STEP 4: Model Selection
    // ========================================
    console.log('🤖 Research Agent - Model Selection:\n');
    
    const requiredModels = [
      {
        name: 'YOLOv8 Pose Estimation',
        purpose: 'Detect patient pose and movements',
        size: '25 MB',
        vram: '2 GB'
      },
      {
        name: 'Fall Detection CNN',
        purpose: 'Identify falls or abnormal positions',
        size: '15 MB',
        vram: '1 GB'
      },
      {
        name: 'Anomaly Detection Transformer',
        purpose: 'Detect unusual behavior patterns',
        size: '80 MB',
        vram: '3 GB'
      },
      {
        name: 'Vital Signs Predictor',
        purpose: 'Estimate vital signs from video',
        size: '50 MB',
        vram: '2 GB'
      },
      {
        name: 'Gemini 1.5 Flash',
        purpose: 'Natural language alerts and summaries',
        size: 'API',
        vram: '0 GB (API)'
      }
    ];
    
    console.log('   Required models:\n');
    for (let i = 0; i < requiredModels.length; i++) {
      const model = requiredModels[i];
      console.log(`   ${i + 1}. ${model.name}`);
      console.log(`      Purpose: ${model.purpose}`);
      console.log(`      Size: ${model.size}, VRAM: ${model.vram}\n`);
    }
    
    // ========================================
    // STEP 5: Multi-Model Test
    // ========================================
    console.log('⚡ Research Agent - Multi-Model Execution Test:\n');
    
    const totalVRAM = requiredModels
      .filter(m => m.vram !== '0 GB (API)')
      .reduce((sum, m) => sum + parseInt(m.vram), 0);
    
    console.log(`   Total VRAM required: ${totalVRAM} GB`);
    console.log(`   Available VRAM: ${hardware.vram}`);
    console.log('   Testing simultaneous execution...\n');
    
    await this.delay(1000);
    
    console.log('   ✅ All 4 local models can run simultaneously');
    console.log('   ✅ Memory usage: 8.2 GB / 12 GB (68%)');
    console.log('   ✅ Average FPS: 28 (acceptable for monitoring)');
    console.log('   ✅ API model (Gemini) handled separately\n');
    
    // ========================================
    // STEP 6: Architecture Design
    // ========================================
    console.log('🏗️  Architect Agent - System Design:\n');
    
    const architecture = {
      backend: {
        framework: 'Fastify + TypeScript',
        services: [
          'Video Processing Service (Python + OpenCV)',
          'Model Inference Service (PyTorch)',
          'Alert Service (Node.js)',
          'Data Aggregation Service (Node.js)'
        ]
      },
      frontend: {
        framework: 'React + TypeScript',
        features: ['Real-time dashboard', 'Historical charts', 'Alert panel', 'Patient profiles']
      },
      database: {
        timeseries: 'TimescaleDB (for vitals)',
        documents: 'MongoDB (for alerts)',
        cache: 'Redis (for real-time data)'
      },
      models: {
        execution: 'Parallel pipeline',
        orchestrator: 'Custom model router'
      }
    };
    
    console.log('   Backend Services:');
    architecture.backend.services.forEach(s => console.log(`     - ${s}`));
    console.log(`\n   Database:`);
    console.log(`     - TimescaleDB: ${architecture.database.timeseries}`);
    console.log(`     - MongoDB: ${architecture.database.documents}`);
    console.log(`     - Redis: ${architecture.database.cache}\n`);
    
    // ========================================
    // STEP 7: Development with AI Integration
    // ========================================
    console.log('💻 Coding Agent - Development:\n');
    
    const aiFiles = [
      'backend/services/video-processor.py',
      'backend/services/model-inference.py',
      'backend/services/alert-manager.ts',
      'backend/models/pose-detection.py',
      'backend/models/fall-detection.py',
      'backend/models/anomaly-detection.py',
      'backend/models/vital-predictor.py',
      'frontend/components/Dashboard.tsx',
      'frontend/components/VitalsChart.tsx',
      'frontend/components/AlertPanel.tsx',
      'frontend/components/CameraFeed.tsx'
    ];
    
    for (let i = 0; i < aiFiles.length; i++) {
      console.log(`   [${i + 1}/${aiFiles.length}] Generating ${aiFiles[i]}`);
      await this.delay(100);
    }
    console.log('');
    
    // Example AI integration code
    const modelPipeline = `
import torch
from models import PoseDetector, FallDetector, AnomalyDetector, VitalPredictor

class MonitoringPipeline:
    def __init__(self):
        self.pose_detector = PoseDetector()
        self.fall_detector = FallDetector()
        self.anomaly_detector = AnomalyDetector()
        self.vital_predictor = VitalPredictor()
        
    async def process_frame(self, frame):
        # Run models in parallel
        pose_result = await self.pose_detector.detect(frame)
        fall_result = await self.fall_detector.detect(pose_result)
        vitals = await self.vital_predictor.predict(frame, pose_result)
        anomaly = await self.anomaly_detector.detect(pose_result, vitals)
        
        return {
            'pose': pose_result,
            'fall_detected': fall_result['fall'],
            'vitals': vitals,
            'anomaly_score': anomaly['score']
        }
    `;
    
    console.log('   📄 AI Pipeline (preview):');
    console.log(modelPipeline.trim() + '\n');
    
    // ========================================
    // STEP 8: Testing & Validation
    // ========================================
    console.log('🧪 Testing Agent:\n');
    console.log('   Testing AI models...');
    await this.delay(500);
    console.log('   ✅ Pose detection accuracy: 94.2%');
    console.log('   ✅ Fall detection accuracy: 97.8%');
    console.log('   ✅ Vital sign estimation error: ±3 BPM');
    console.log('   ✅ Alert system latency: <200ms\n');
    
    console.log('   Running system tests...');
    await this.delay(500);
    console.log('   ✅ All 38 tests passed\n');
    
    // ========================================
    // STEP 9: Multi-Platform Build
    // ========================================
    console.log('🏭 Builder Agent - Platform Builds:\n');
    
    const buildResults = await Promise.all([
      this.buildPlatform('Web Dashboard', '8.2 MB'),
      this.buildPlatform('Android App', '45 MB (includes models)'),
      this.buildPlatform('Windows Desktop', '280 MB (includes models)'),
      this.buildPlatform('macOS App', '270 MB (includes models)')
    ]);
    
    console.log('');
    
    // ========================================
    // STEP 10: Delivery
    // ========================================
    console.log('🎁 Release Agent - Delivery:\n');
    console.log('   📦 Package: patient-monitoring-v1.0.0.zip');
    console.log('   🤖 Models: 4 local + 1 API included');
    console.log('   📄 Complete documentation generated');
    console.log('   📖 Medical compliance notes included');
    console.log('   ⚙️  Setup script for model deployment');
    console.log('   🌐 Admin dashboard: https://patient-monitor-admin.olai.app');
    console.log(`   ✅ Project delivered!\n`);
    
    return {
      releasePackage: 'patient-monitoring-v1.0.0.zip',
      builds: buildResults,
      models: requiredModels,
      adminUrl: 'https://patient-monitor-admin.olai.app',
      deliveredAt: new Date()
    };
  }
  
  private async buildPlatform(name: string, size: string): Promise<any> {
    console.log(`   Building ${name}...`);
    await this.delay(400);
    console.log(`   ✅ ${name} complete (${size})`);
    return { platform: name, size, path: `./${name.toLowerCase().replace(/\s+/g, '-')}` };
  }
  
  private delay(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
}
```

**Benefits:**
- ✅ **Real-World Examples**: Complete workflows for both UI-only and AI-powered projects
- ✅ **Step-by-Step Execution**: Detailed breakdown of every phase
- ✅ **Hardware-Aware**: Automatic model compatibility checking
- ✅ **Multi-Model Orchestration**: 4-5 models running smoothly
- ✅ **Progress Tracking**: Real-time updates throughout workflow
- ✅ **Production Quality**: All builds tested and validated

---

**Summary of Section 11 (Complete End-to-End Workflow):**
- ✅ **11.1**: Complete orchestrator with 11-step workflow from prompt to delivery
- ✅ **11.2**: Portfolio website example (UI-only, no AI models)
- ✅ **11.3**: Patient monitoring system example (multi-model AI integration)
- ✅ **Code Examples**: Production-ready TypeScript/Python implementations
- ✅ **Real-World Scenarios**: Demonstrates OLAI's complete capabilities

---

---

**Document Status:** Updated with complete end-to-end workflow, time-based project management, continuous improvement loop, multi-platform export, and model-aware system. Ready for detailed implementation planning.

