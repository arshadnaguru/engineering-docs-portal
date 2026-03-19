# Deploy a Dockerized Application on Linux

This guide covers deploying a containerized application to a Linux server using Docker Compose, including environment configuration, health checks, and log management.

## Prerequisites

- Linux server with SSH access
- Docker and Docker Compose installed on the server
- Application already containerized (see [Containerizing a FastAPI App](../tutorials/docker-fastapi.md))

## Create a Docker Compose File

Create `docker-compose.yml` in your project root:

```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - ENV=production
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  db:
    image: mysql:8.0
    environment:
      - MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
      - MYSQL_DATABASE=${MYSQL_DATABASE}
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped

volumes:
  db_data:
```

## Configure Environment Variables

Create a `.env` file (never commit this to Git):

```bash
DATABASE_URL=mysql://root:password@db:3306/myapp
MYSQL_ROOT_PASSWORD=your_secure_password
MYSQL_DATABASE=myapp
```

## Deploy to the Server

```bash
# SSH into your server
ssh user@your-server-ip

# Clone the repository
git clone https://github.com/yourusername/your-app.git
cd your-app

# Create .env file with production values
nano .env

# Build and start services
docker-compose up -d --build

# Verify services are running
docker-compose ps
```

## Monitor the Deployment

```bash
# View logs for all services
docker-compose logs -f

# View logs for a specific service
docker-compose logs -f api

# Check health status
docker inspect --format='{{.State.Health.Status}}' your-app-api-1
```

## Update the Application

```bash
# Pull latest code
git pull origin main

# Rebuild and restart (zero-downtime)
docker-compose up -d --build

# Verify the update
docker-compose ps
docker-compose logs -f api
```

## Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Container keeps restarting | Application crash | Check logs: `docker-compose logs api` |
| Cannot connect to database | Network or credentials issue | Verify `.env` values and service names |
| Port already in use | Another service on port 8000 | Change port mapping in `docker-compose.yml` |
| Out of disk space | Docker images accumulating | Run `docker system prune -a` |

---

*Last updated: March 2026 · Author: Arshad Naguru*
