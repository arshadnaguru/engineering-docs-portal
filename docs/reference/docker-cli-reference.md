# Docker CLI Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Essential Docker commands for building, running, and managing containers.

## Images

| Command | Description |
|---------|-------------|
| `docker build -t name:tag .` | Build image from Dockerfile |
| `docker images` | List all images |
| `docker pull image:tag` | Download an image |
| `docker rmi image_id` | Remove an image |
| `docker image prune` | Remove unused images |

## Containers

| Command | Description |
|---------|-------------|
| `docker run -d -p 8000:8000 --name myapp image` | Run container (detached) |
| `docker run -it image /bin/bash` | Run interactive shell |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker stop container` | Stop a container |
| `docker rm container` | Remove a container |
| `docker logs container` | View container logs |
| `docker logs -f container` | Follow logs in real-time |
| `docker exec -it container /bin/bash` | Shell into running container |

## Docker Compose

| Command | Description |
|---------|-------------|
| `docker-compose up -d` | Start all services |
| `docker-compose up -d --build` | Rebuild and start |
| `docker-compose down` | Stop and remove containers |
| `docker-compose logs -f` | Follow all logs |
| `docker-compose ps` | List service status |
| `docker-compose exec service bash` | Shell into a service |

## Volumes and Networks

| Command | Description |
|---------|-------------|
| `docker volume ls` | List volumes |
| `docker volume create name` | Create a volume |
| `docker network ls` | List networks |
| `docker network create name` | Create a network |

## Cleanup

```bash
# Remove everything unused
docker system prune -a

# Check disk usage
docker system df
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
