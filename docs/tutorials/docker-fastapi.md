# Containerizing a FastAPI App with Docker

This tutorial walks you through packaging a FastAPI REST application into a Docker container for consistent, reproducible deployment across any environment.

## Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- A working FastAPI application
- Basic terminal/command line knowledge

## Step 1: Prepare Your Application

Ensure your FastAPI project follows this minimal structure:

```
my-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   └── routes/
│       └── __init__.py
├── requirements.txt
└── README.md
```

Your `main.py` should look something like this:

```python
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
```

## Step 2: Create the Dockerfile

Create a `Dockerfile` in your project root:

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

!!! note "Why copy requirements.txt first?"
    Docker caches each layer. By copying and installing dependencies before copying your code, Docker can reuse the cached dependency layer when only your code changes. This speeds up rebuilds significantly.

## Step 3: Create a .dockerignore

Add a `.dockerignore` file to keep the image clean:

```
__pycache__
*.pyc
.git
.gitignore
.env
venv/
.vscode/
*.md
```

## Step 4: Build the Docker Image

```bash
# Build the image with a tag
docker build -t my-fastapi-app:latest .

# Verify the image was created
docker images | grep my-fastapi-app
```

## Step 5: Run the Container

```bash
# Run the container
docker run -d -p 8000:8000 --name my-api my-fastapi-app:latest

# Verify it's running
docker ps
```

Test the API:

```bash
# Health check
curl http://localhost:8000/health

# Expected output:
# {"status": "healthy"}
```

## Step 6: Manage the Container

```bash
# View logs
docker logs my-api

# Stop the container
docker stop my-api

# Remove the container
docker rm my-api
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port already in use | Change the host port: `docker run -p 8001:8000 ...` |
| Container exits immediately | Check logs: `docker logs my-api` |
| Module not found error | Verify `requirements.txt` includes all dependencies |
| Permission denied | Run Docker commands with `sudo` or add user to docker group |

## Next Steps

- Set up [Docker Compose](../how-to/docker-deploy-linux.md) for multi-container deployments
- Document your API endpoints using the [API Documentation Template](../reference/api-doc-template.md)

---

*Last updated: March 2026 · Author: Arshad Naguru*
