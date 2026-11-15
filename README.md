# DevPilot AI

An early-stage autonomous software engineering assistant.

## Current starter features
- FastAPI backend with a health-check endpoint
- Basic local repository scanner
- Placeholder agent workflow for future LangGraph integration
- Pytest starter test

## Requirements
- Python 3.11 recommended
- Git
- VS Code (recommended)

## Run locally (Windows PowerShell)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
- API health check: http://127.0.0.1:8000/health
- Interactive API docs: http://127.0.0.1:8000/docs

## Run tests

```powershell
pytest
```

## Environment variables
Copy `.env.example` to `.env` and add credentials only when we integrate a hosted LLM.
Never commit `.env` or API keys.

## Safety
This starter does not execute repository code. Later execution features must run in an isolated sandbox,
with timeouts, resource limits, restricted network access and explicit human approval.

## Deployment
The FastAPI backend can be deployed to Render or Railway. Vercel can host a Python API, but for this
long-running agent project it is not the first choice because agent jobs, test execution and sandbox
workloads are better suited to a persistent backend/worker. A frontend can be hosted separately on
Vercel if we later build a Next.js interface.
