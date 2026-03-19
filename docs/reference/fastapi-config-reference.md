# FastAPI Configuration Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Reference for FastAPI application configuration, middleware, and deployment settings.

## Application Setup

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Project API",
    description="API for document management",
    version="1.0.0",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc",     # ReDoc
    openapi_url="/openapi.json"
)
```

## CORS Configuration

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Environment Variables

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "mysql://user:pass@localhost/db"
    secret_key: str = "change-me"
    debug: bool = False
    port: int = 8000
    
    class Config:
        env_file = ".env"

settings = Settings()
```

## HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET/PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 422 | Unprocessable Entity | Validation error |
| 500 | Internal Server Error | Server-side failure |

## Uvicorn Run Options

| Flag | Description | Default |
|------|-------------|---------|
| `--host` | Bind address | `127.0.0.1` |
| `--port` | Port number | `8000` |
| `--reload` | Auto-reload on changes | `False` |
| `--workers` | Number of worker processes | `1` |
| `--log-level` | Logging level | `info` |

```bash
# Development
uvicorn main:app --reload --port 8000

# Production
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
