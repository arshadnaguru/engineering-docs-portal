# Troubleshoot Common Docker Errors

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Quick fixes for the most common Docker issues.

## Permission Denied

```bash
# Error: Got permission denied while trying to connect to the Docker daemon
sudo usermod -aG docker $USER
newgrp docker  # Apply without logout
```

## Port Already in Use

```bash
# Error: Bind for 0.0.0.0:8000 failed: port is already allocated
# Find what's using the port
sudo lsof -i :8000

# Kill it or use a different port
docker run -p 8001:8000 myapp
```

## Out of Disk Space

```bash
# Check Docker disk usage
docker system df

# Remove all unused resources
docker system prune -a

# Remove specific items
docker image prune     # Unused images
docker container prune # Stopped containers
docker volume prune    # Unused volumes
```

## Container Exits Immediately

```bash
# Check the exit code and logs
docker logs container_name

# Run interactively to debug
docker run -it myapp /bin/bash

# Common causes:
# - Exit code 1: Application error (check logs)
# - Exit code 137: Out of memory (increase memory limit)
# - Exit code 0: Process completed (use CMD that stays running)
```

## Cannot Connect to Container

```bash
# Verify container is running
docker ps

# Check port mapping
docker port container_name

# Test from inside the container
docker exec -it container_name curl localhost:8000
```

## Build Fails at pip install

```dockerfile
# Fix: Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
