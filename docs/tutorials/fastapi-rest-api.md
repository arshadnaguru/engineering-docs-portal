# Building a REST API with FastAPI

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

This tutorial covers building a complete REST API from scratch using FastAPI, including endpoints, request validation, and database integration.

## Prerequisites

- Python 3.9+
- Familiarity with HTTP methods (GET, POST, PUT, DELETE)

## Step 1: Install FastAPI

```bash
pip install fastapi uvicorn pydantic
```

## Step 2: Create the Application

Create `main.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Project API", version="1.0.0")

# In-memory data store
documents = {}

class Document(BaseModel):
    title: str
    content: str
    category: Optional[str] = "general"

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/documents")
def list_documents():
    return {"documents": list(documents.values()), "count": len(documents)}

@app.get("/documents/{doc_id}")
def get_document(doc_id: str):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents[doc_id]

@app.post("/documents/{doc_id}")
def create_document(doc_id: str, doc: Document):
    documents[doc_id] = doc.dict()
    return {"message": "Document created", "id": doc_id}

@app.delete("/documents/{doc_id}")
def delete_document(doc_id: str):
    if doc_id not in documents:
        raise HTTPException(status_code=404, detail="Document not found")
    del documents[doc_id]
    return {"message": "Document deleted"}
```

## Step 3: Run the Server

```bash
uvicorn main:app --reload --port 8000
```

## Step 4: Test the Endpoints

```bash
# Create a document
curl -X POST "http://localhost:8000/documents/doc1" \
  -H "Content-Type: application/json" \
  -d '{"title": "Setup Guide", "content": "Step 1...", "category": "tutorial"}'

# List all documents
curl http://localhost:8000/documents

# Get a specific document
curl http://localhost:8000/documents/doc1

# Delete a document
curl -X DELETE http://localhost:8000/documents/doc1
```

## Step 5: View Auto-Generated Docs

FastAPI automatically generates interactive API documentation:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## Next Steps

- [Containerize this API with Docker](docker-fastapi.md)
- [Deploy to Linux](../how-to/docker-deploy-linux.md)
- Use the [API Documentation Template](../reference/api-doc-template.md) to document your endpoints

---

*Last updated: March 2026 · Author: Arshad Naguru*
