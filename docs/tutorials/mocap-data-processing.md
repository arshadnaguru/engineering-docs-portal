# Introduction to Motion Capture Data Processing

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Learn how to work with motion capture (mocap) data — loading BVH/FBX files, visualizing joint data, and cleaning noisy captures.

## Prerequisites

- Python 3.9+
- Basic understanding of 3D coordinate systems

## Step 1: Install Required Libraries

```bash
pip install numpy pandas matplotlib bvhio
```

## Step 2: Understanding Mocap File Formats

| Format | Description | Common Use |
|--------|-------------|------------|
| BVH | Biovision Hierarchy — text-based, widely supported | Animation, research |
| FBX | Autodesk format — binary, supports meshes + animation | Game dev, VFX |
| C3D | Biomechanics format — stores 3D marker positions | Research, sports science |
| CSV | Raw marker positions exported from capture software | Custom pipelines |

## Step 3: Load and Inspect a BVH File

```python
import numpy as np

def parse_bvh_basic(filepath):
    """Basic BVH parser to extract joint names and frame data."""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    joints = []
    motion_start = 0
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("JOINT") or stripped.startswith("ROOT"):
            joint_name = stripped.split()[-1]
            joints.append(joint_name)
        if stripped == "MOTION":
            motion_start = i
            break
    
    # Parse frame count and frame time
    num_frames = int(lines[motion_start + 1].split(":")[1].strip())
    frame_time = float(lines[motion_start + 2].split(":")[1].strip())
    
    print(f"Joints: {len(joints)}")
    print(f"Frames: {num_frames}")
    print(f"Frame time: {frame_time}s ({1/frame_time:.0f} FPS)")
    
    return joints, num_frames, frame_time

joints, frames, ft = parse_bvh_basic("capture_data.bvh")
```

## Step 4: Clean Noisy Data

```python
from scipy.signal import savgol_filter

def smooth_motion_data(data, window=11, poly_order=3):
    """Apply Savitzky-Golay filter to smooth noisy mocap data."""
    smoothed = np.copy(data)
    for joint_idx in range(data.shape[1]):
        for axis in range(3):  # x, y, z
            smoothed[:, joint_idx, axis] = savgol_filter(
                data[:, joint_idx, axis], window, poly_order
            )
    return smoothed
```

## Step 5: Visualize Joint Trajectories

```python
import matplotlib.pyplot as plt

def plot_joint_trajectory(data, joint_idx, joint_name):
    """Plot the 3D trajectory of a single joint over time."""
    fig, axes = plt.subplots(3, 1, figsize=(12, 8))
    labels = ['X', 'Y', 'Z']
    
    for i, ax in enumerate(axes):
        ax.plot(data[:, joint_idx, i], linewidth=0.8)
        ax.set_ylabel(f"{labels[i]} Position")
        ax.grid(True, alpha=0.3)
    
    axes[0].set_title(f"Joint Trajectory: {joint_name}")
    axes[2].set_xlabel("Frame")
    plt.tight_layout()
    plt.savefig(f"trajectory_{joint_name}.png", dpi=150)
    plt.show()
```

!!! warning
    Always back up raw capture data before applying any cleaning or smoothing operations.

## Next Steps

- Learn about [VR development environments](vr-dev-environment.md)
- Read [What is Motion Capture?](../explanation/what-is-mocap.md)

---

*Last updated: March 2026 · Author: Arshad Naguru*
