<div align="center">

# 🌉 ContextBridge AI

### Take your AI conversation with you.

**A provider-neutral context portability layer for moving useful conversational memory across AI assistants.**

`ChatGPT ↔ Claude ↔ Gemini ↔ Any LLM`

<br/>

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Schemas-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Roadmap-6C5CE7?style=for-the-badge)

<br/>

**Conversation → Understand → Compress → Package → Continue**

</div>

---

## ✨ The Idea

You spend an hour solving a problem with one AI assistant. It now understands your requirements, decisions, constraints, unfinished tasks and the direction of your work.

Then you switch to another assistant.

And suddenly you are starting from zero.

**ContextBridge AI is designed to solve that problem.**

Instead of treating a conversation as a giant block of text, ContextBridge turns it into a compact, structured **portable context package** that another AI system can consume.

> The goal is not to copy every message. The goal is to preserve what the next AI actually needs to know.

---

## 🧠 What Makes ContextBridge Different?

A normal export preserves the **transcript**.

ContextBridge preserves the **meaning of the work**.

<table>
<tr>
<td width="33%" align="center"><b>01 — Understand</b><br/><br/>Normalize conversation history into a provider-independent representation.</td>
<td width="33%" align="center"><b>02 — Distill</b><br/><br/>Extract decisions, facts, requirements, tasks and high-value conversational context.</td>
<td width="33%" align="center"><b>03 — Transfer</b><br/><br/>Create a lightweight context package that can travel to another AI environment.</td>
</tr>
</table>

---

## 🌐 The Context Bridge

```text
┌─────────────────┐
│    ChatGPT      │
└────────┬────────┘
         │
┌────────▼────────┐       ┌─────────────────┐
│     Claude      │──────►│                 │
└─────────────────┘       │  CONTEXTBRIDGE  │
                          │                 │
┌─────────────────┐       │   Normalize     │
│     Gemini      │──────►│   Understand    │
└─────────────────┘       │   Compress      │
                          │   Structure      │
┌─────────────────┐       │                 │
│    Any LLM      │──────►│       AI        │
└─────────────────┘       └────────┬────────┘
                                   │
                                   ▼
                         ┌────────────────────┐
                         │ PORTABLE CONTEXT   │
                         │                    │
                         │ ✓ Facts            │
                         │ ✓ Decisions        │
                         │ ✓ Requirements     │
                         │ ✓ Open Tasks       │
                         │ ✓ Key History      │
                         │ ✓ Summary          │
                         └─────────┬──────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
                 ChatGPT        Claude         Gemini
```

ContextBridge itself is **provider-neutral**. Providers are treated as adapters around one common internal context model.

---

## ⚡ Example Experience

Imagine this conversation happened in Gemini:

```text
You: We are building a healthcare RAG application.
AI:  Let's use FastAPI for the backend.
You: We decided on Pinecone. All patient PII must be redacted.
AI:  I'll structure retrieval around hybrid search and re-ranking.
You: Next we need to implement authentication and evaluation.
```

Instead of pasting the entire conversation into another assistant, ContextBridge can produce:

```json
{
  "source_provider": "gemini",
  "target_provider": "chatgpt",
  "summary": "Building a privacy-aware healthcare RAG application.",
  "decisions": [
    "Use FastAPI for the backend",
    "Use Pinecone for vector retrieval",
    "Use hybrid retrieval with re-ranking"
  ],
  "requirements": [
    "Patient PII must be redacted"
  ],
  "open_tasks": [
    "Implement authentication",
    "Add RAG evaluation"
  ]
}
```

The next assistant gets the **working context**, not just raw history.

---

## 🏗️ Architecture

```mermaid
flowchart LR
    A[User-authorized transcript] --> B[Provider Adapter]
    B --> C[Conversation Normalizer]
    C --> D[Context Extraction Engine]
    D --> E[Budget-aware Compression]
    E --> F[Portable Context Schema]
    F --> G[JSON Context Package]
    G --> H[Target AI Assistant]
```

### Processing pipeline

```text
INPUT
  │
  ▼
Provider Transcript
  │
  ▼
Normalization
  │
  ├── role mapping
  ├── message cleanup
  └── provider-independent schema
  │
  ▼
Context Extraction
  │
  ├── facts
  ├── decisions
  ├── requirements
  └── tasks
  │
  ▼
Budget-Aware Compression
  │
  ▼
PortableContext
  │
  ▼
JSON / Future MCP Resource
```

---

## 🔥 Current Capabilities

| Capability | Status | Description |
|---|:---:|---|
| Provider-neutral message schema | ✅ | One internal representation independent of the source assistant |
| Transcript normalization | ✅ | Cleans and standardizes imported conversations |
| Context extraction | ✅ | Separates facts, decisions, requirements and tasks |
| Budget-aware compression | ✅ | Keeps context within a configurable size budget |
| Portable JSON package | ✅ | Machine-readable context for reuse elsewhere |
| FastAPI REST API | ✅ | Programmatic context generation |
| Docker environment | ✅ | Reproducible local execution |
| Automated tests | ✅ | Core API and compression validation |
| Semantic LLM compression | 🚧 | Planned intelligent meaning-aware compression |
| MCP context server | 🚧 | Planned portable memory through MCP resources/tools |
| Web migration UI | 🚧 | Planned drag-and-drop migration interface |
| Encrypted package format | 🚧 | Planned secure `.contextbridge` file |

---

## 🛠️ Engineering Stack

<div align="center">

| Layer | Technology |
|---|---|
| **API** | FastAPI + Uvicorn |
| **Language** | Python 3.11 |
| **Data Contracts** | Pydantic |
| **Context Engine** | Custom extraction + compression pipeline |
| **Portable Format** | Structured JSON |
| **Testing** | Pytest + FastAPI TestClient |
| **Packaging** | Docker |
| **Future Agent Interface** | Model Context Protocol (MCP) |

</div>

---

## 🚀 Run ContextBridge

### 1. Clone

```bash
git clone https://github.com/vaishnavi-265/vaishnavi-k.git
cd vaishnavi-k/contextbridge-ai
```

### 2. Create an environment

```bash
python -m venv .venv
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

Open Swagger at:

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 API

### Build a portable context package

```http
POST /v1/context/build
```

```json
{
  "source_provider": "gemini",
  "target_provider": "chatgpt",
  "max_chars": 4000,
  "messages": [
    {
      "role": "user",
      "content": "We decided to use FastAPI for the backend."
    },
    {
      "role": "assistant",
      "content": "The service will use PostgreSQL and Docker."
    },
    {
      "role": "user",
      "content": "Remember that authentication must use OAuth2."
    }
  ]
}
```

### Health check

```http
GET /health
```

---

## 📦 Portable Context Model

The project intentionally separates the **conversation provider** from the **context representation**.

```python
PortableContext(
    source_provider="gemini",
    target_provider="chatgpt",
    summary="...",
    facts=[...],
    decisions=[...],
    requirements=[...],
    tasks=[...],
    selected_history=[...]
)
```

That separation is the foundation for adding new providers without rebuilding the context engine.

---

## 🔐 Privacy by Design

Context portability creates an important privacy boundary: information safe to use with one provider may not be appropriate to send to another.

ContextBridge therefore follows a **user-authorized portability model**.

```text
Private Conversation
        │
        ▼
 User explicitly exports
        │
        ▼
 ContextBridge processing
        │
        ▼
 Review / Redaction Layer
        │
        ▼
 User chooses destination
```

The project does **not** attempt to scrape private conversations, bypass provider permissions or silently transfer account data.

Planned privacy features include PII detection, selective redaction, encrypted context packages and explicit destination review.

---

## 🗺️ Roadmap

### Phase 01 — Portable Context Core `CURRENT`
- [x] Provider-neutral schemas
- [x] FastAPI service
- [x] Structured extraction
- [x] Context budgeting
- [x] JSON portability
- [x] Automated tests

### Phase 02 — Intelligent Context Engine
- [ ] LLM-assisted semantic compression
- [ ] Token-aware context budgeting
- [ ] Importance scoring
- [ ] Duplicate-memory removal
- [ ] Conversation topic segmentation
- [ ] PII detection and redaction

### Phase 03 — Provider Interoperability
- [ ] ChatGPT export adapter
- [ ] Claude export adapter
- [ ] Gemini export adapter
- [ ] Provider capability registry
- [ ] Import-ready target prompts

### Phase 04 — ContextBridge MCP
- [ ] MCP server
- [ ] Context resources
- [ ] Searchable conversation memory
- [ ] Selective memory retrieval
- [ ] Agent-accessible context tools

### Phase 05 — User Experience
- [ ] Web application
- [ ] Drag-and-drop transcript import
- [ ] Context preview and editing
- [ ] Destination selector
- [ ] Encrypted `.contextbridge` packages

---

## 🧪 Engineering Principles

**Provider independence** — the core model should not belong to OpenAI, Anthropic, Google or any single vendor.

**Context over transcript** — preserve decisions and intent before preserving conversational noise.

**User control** — users decide what leaves one AI environment and where it goes.

**Small context, high signal** — portability should reduce unnecessary tokens rather than duplicate entire conversations.

**Extensibility** — providers, compression strategies and output formats should be replaceable components.

---

## 💡 Why I Built This

AI assistants are increasingly becoming places where people accumulate **working memory**: product decisions, research findings, code discussions, requirements and unfinished tasks.

That memory should not become useful only inside one conversation window.

ContextBridge explores a simple question:

> **What would a portable memory layer for the multi-LLM world look like?**

---

## 👩‍💻 Author

<div align="center">

### Vaishnavi Kandakatla

**AI Engineer · Software Engineer**

Building production-oriented systems across **Agentic AI, RAG, MCP, LLM applications, backend engineering and enterprise AI automation.**

[![GitHub](https://img.shields.io/badge/GitHub-vaishnavi--265-181717?style=for-the-badge&logo=github)](https://github.com/vaishnavi-265)
[![Email](https://img.shields.io/badge/Email-Connect-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:vaishuvishnupriya8121@gmail.com)

<br/>

### `Your conversation may end. Your context shouldn't.`

</div>
