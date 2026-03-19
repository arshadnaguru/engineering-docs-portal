# Set Up a Virtual Production Stage

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Configure an LED wall virtual production stage with Unreal Engine for real-time background rendering.

## Requirements

- LED wall or large display panel
- Unreal Engine 5.x with nDisplay plugin
- Tracking system (OptiTrack or Vicon)
- Camera with genlock capability

## Step 1: Configure nDisplay in Unreal Engine

1. Enable the **nDisplay** plugin in Edit → Plugins
2. Create an nDisplay configuration file defining your LED wall geometry
3. Set the viewport resolution to match your physical LED panel layout

```json
{
  "nDisplay": {
    "cluster": {
      "masterNode": {
        "host": "192.168.1.100",
        "ports": { "sync": 41000, "cluster": 41001 }
      }
    },
    "screens": [
      { "id": "main_wall", "size": { "x": 9.0, "y": 4.0 }, "resolution": { "x": 3840, "y": 2160 } }
    ]
  }
}
```

## Step 2: Calibrate Camera Tracking

1. Mount tracking markers on the physical camera
2. Calibrate the tracking volume in OptiTrack Motive
3. Configure the LiveLink connection between OptiTrack and Unreal Engine

```
# In Unreal: Edit → Project Settings → Live Link
Source: OptiTrack Natnet
Server IP: 192.168.1.50
```

## Step 3: Set Up Frustum Rendering

The frustum is the camera-tracked perspective correction zone on the LED wall:

1. Create an inner frustum actor in the nDisplay config
2. Link it to the tracked camera
3. Adjust the frustum size to match the camera's field of view

## Step 4: Color Calibration

1. Display a white test pattern on the LED wall
2. Use a color meter to measure output
3. Adjust LED panel brightness and color temperature to match your camera's white balance

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Camera tracking latency | Reduce network hops; use a dedicated tracking network |
| Color fringing on LED wall | Adjust inner frustum overscan settings |
| Unreal Engine dropping frames | Reduce scene complexity or increase render cluster nodes |

---

*Last updated: March 2026 · Author: Arshad Naguru*
