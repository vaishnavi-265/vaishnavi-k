# ContextBridge AI

> Portable conversation context across AI assistants.

ContextBridge AI converts long AI conversations into a compact, provider-neutral context package that can be safely reused when continuing work in another LLM application. Instead of copying an entire transcript, it extracts decisions, facts, requirements, tasks and important conversation history into a structured JSON file.

## Why it matters

AI users frequently switch between ChatGPT, Claude, Gemini and other assistants. ContextBridge provides a neutral interoperability layer so users can preserve the useful context of a conversation without depending on one provider.

## Architecture

```text
Chat Export / Transcript
        |
        v
Normalization Layer
        |
        v
Context Extraction + Compression
  | facts | decisions | tasks |
        |
        v
Provider-Neutral Context Package
        |
   +----+----+
   |    |    |
ChatGPT Claude Gemini / Any LLM
```

## Features

- Provider-neutral conversation schema
- Intelligent transcript normalization
- Context compression with configurable token/character budget
- Extraction of facts, decisions, requirements and open tasks
- PII-aware redaction hooks
- JSON export for portability
- FastAPI REST service
- Extensible provider adapter interface
- Dockerized local development
- Unit tests

## Tech Stack

Python 3.11, FastAPI, Pydantic, Uvicorn, Pytest, Docker

## Quick start

```bash
cd contextbridge-ai
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI.

## Example

POST `/v1/context/build`

```json
{
  "source_provider": "gemini",
  "target_provider": "chatgpt",
  "max_chars": 4000,
  "messages": [
    {"role": "user", "content": "We decided to build the backend with FastAPI."},
    {"role": "assistant", "content": "I will use PostgreSQL and Docker for the deployment."},
    {"role": "user", "content": "Remember that authentication must use OAuth2."}
  ]
}
```

The API returns a compact context package containing summary, facts, decisions, requirements, tasks and selected message history.

## Roadmap

- LLM-assisted semantic compression
- Browser extension for user-authorized exports
- MCP server exposing portable memory as tools/resources
- Encrypted `.contextbridge` package format
- Token-aware compression using model-specific tokenizers
- Provider adapters for officially supported export/import formats
- PII detection and selective redaction
- Web UI for drag-and-drop transcript migration

## Security & Privacy

ContextBridge is designed around user-authorized transcripts. It does not scrape private AI conversations or bypass provider permissions. Sensitive context should be reviewed before exporting to another provider.

## Author

Vaishnavi Kandakatla — AI Engineer / Software Engineer
