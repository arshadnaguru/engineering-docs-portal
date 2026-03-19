# Linux Command Cheat Sheet

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Quick reference for essential Linux commands used in studio and server environments.

## File System

| Command | Description | Example |
|---------|-------------|---------|
| `ls -la` | List all files with details | `ls -la /home/studio/` |
| `cd` | Change directory | `cd /srv/render_share` |
| `pwd` | Print working directory | `pwd` |
| `mkdir -p` | Create nested directories | `mkdir -p project/assets/textures` |
| `cp -r` | Copy recursively | `cp -r source/ dest/` |
| `mv` | Move or rename | `mv old_name.md new_name.md` |
| `rm -rf` | Remove recursively (careful!) | `rm -rf build/` |
| `find` | Search for files | `find . -name "*.md" -type f` |
| `du -sh` | Directory size | `du -sh /srv/render_share/*` |
| `df -h` | Disk space | `df -h` |

## File Permissions

| Command | Description | Example |
|---------|-------------|---------|
| `chmod 755` | Owner: rwx, Group: rx, Other: rx | `chmod 755 script.sh` |
| `chmod 644` | Owner: rw, Group: r, Other: r | `chmod 644 config.yml` |
| `chown` | Change ownership | `chown studio:studio file.txt` |
| `chown -R` | Change ownership recursively | `chown -R studio:studio project/` |

## Process Management

| Command | Description | Example |
|---------|-------------|---------|
| `ps aux` | List all processes | `ps aux \| grep python` |
| `top` / `htop` | Real-time process monitor | `htop` |
| `kill PID` | Stop a process | `kill 12345` |
| `kill -9 PID` | Force stop | `kill -9 12345` |
| `nohup` | Run process after logout | `nohup python train.py &` |
| `screen` | Persistent terminal session | `screen -S training` |

## Networking

| Command | Description | Example |
|---------|-------------|---------|
| `ssh` | Remote login | `ssh user@192.168.1.100` |
| `scp` | Secure copy | `scp file.txt user@server:/path/` |
| `curl` | HTTP request | `curl http://localhost:8000/health` |
| `netstat -tlnp` | Show listening ports | `netstat -tlnp` |
| `ping` | Test connectivity | `ping 192.168.1.100` |

## Compression

| Command | Description | Example |
|---------|-------------|---------|
| `tar czf` | Create .tar.gz | `tar czf archive.tar.gz folder/` |
| `tar xzf` | Extract .tar.gz | `tar xzf archive.tar.gz` |
| `zip -r` | Create .zip | `zip -r archive.zip folder/` |
| `unzip` | Extract .zip | `unzip archive.zip` |

---

*Last updated: March 2026 · Author: Arshad Naguru*
