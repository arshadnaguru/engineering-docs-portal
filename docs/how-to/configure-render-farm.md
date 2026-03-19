# Configure a Render Farm

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Set up a distributed render farm for batch processing 3D renders across multiple machines.

## Prerequisites

- 2+ render nodes on the same network
- Blender, Maya, or After Effects installed on all nodes
- Shared network storage (NFS or SMB)

## Step 1: Set Up Shared Storage

```bash
# On the file server (Ubuntu)
sudo apt install nfs-kernel-server
sudo mkdir -p /srv/render_share
echo "/srv/render_share *(rw,sync,no_subtree_check)" | sudo tee -a /etc/exports
sudo exportfs -a
sudo systemctl restart nfs-kernel-server

# On each render node
sudo mount server_ip:/srv/render_share /mnt/render_share
```

## Step 2: Install a Render Manager

Options: **Deadline** (industry standard), **Flamenco** (free, for Blender), or custom scripts.

### Using Flamenco (Blender)

```bash
# Download Flamenco Manager
wget https://flamenco.blender.org/downloads/flamenco-manager-linux.tar.gz
tar xzf flamenco-manager-linux.tar.gz
./flamenco-manager -setup
```

## Step 3: Configure Worker Nodes

```yaml
# flamenco-worker.yaml
manager_url: http://192.168.1.100:8080
task_types:
  - blender-render
  - ffmpeg-video-encoding
```

## Step 4: Submit a Render Job

1. Open your Blender project
2. Set output path to the shared storage: `/mnt/render_share/project_name/`
3. Submit via Flamenco add-on or the web interface
4. Monitor progress at `http://manager-ip:8080`

## Monitoring

```bash
# Check node status
curl http://192.168.1.100:8080/api/v3/workers

# Check job progress
curl http://192.168.1.100:8080/api/v3/jobs
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
