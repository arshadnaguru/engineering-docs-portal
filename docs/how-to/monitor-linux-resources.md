# Monitor System Resources on Linux

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Track CPU, memory, disk, and GPU usage on Linux render nodes and servers.

## Quick Status Check

```bash
# CPU and memory overview
htop

# Disk usage
df -h

# GPU usage (NVIDIA)
nvidia-smi
```

## CPU Monitoring

```bash
# Real-time CPU usage per core
mpstat -P ALL 1

# Top CPU-consuming processes
top -o %CPU -bn1 | head -20

# Load average (1, 5, 15 min)
uptime
```

## Memory Monitoring

```bash
# Detailed memory info
free -h

# Top memory consumers
ps aux --sort=-%mem | head -10
```

## Disk I/O

```bash
# Real-time disk activity
iostat -x 1

# Find large files
du -sh /home/* | sort -rh | head -10
```

## GPU Monitoring (NVIDIA)

```bash
# Continuous monitoring every 2 seconds
watch -n 2 nvidia-smi

# Log GPU usage to file
nvidia-smi --query-gpu=timestamp,gpu_bus_id,utilization.gpu,utilization.memory,memory.used --format=csv -l 5 > gpu_log.csv
```

## Set Up Alerts

```bash
#!/bin/bash
# alert_high_cpu.sh - Alert if CPU exceeds 90%
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d. -f1)
if [ "$CPU_USAGE" -gt 90 ]; then
    echo "HIGH CPU: ${CPU_USAGE}% on $(hostname)" | mail -s "CPU Alert" admin@team.com
fi
```

Add to crontab: `*/5 * * * * /scripts/alert_high_cpu.sh`

---

*Last updated: March 2026 · Author: Arshad Naguru*
