# Motion Capture File Formats Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Reference for common motion capture file formats, their capabilities, and use cases.

## Format Comparison

| Format | Type | Skeleton | Mesh | Markers | Common Software |
|--------|------|----------|------|---------|-----------------|
| BVH | Text | Yes | No | No | MotionBuilder, Blender |
| FBX | Binary | Yes | Yes | Yes | Maya, Unreal, Unity |
| C3D | Binary | No | No | Yes | Vicon, OptiTrack |
| CSV | Text | Varies | No | Yes | Custom pipelines |
| ASF/AMC | Text | Yes | No | No | Research, CMU database |

## BVH (Biovision Hierarchy)

- **Extension:** `.bvh`
- **Type:** Plain text
- **Structure:** Skeleton hierarchy + motion data
- **Frame data:** Joint rotations (Euler angles) per frame
- **Best for:** Animation retargeting, research, Blender import

## FBX (Filmbox)

- **Extension:** `.fbx`
- **Type:** Binary (also ASCII variant)
- **Structure:** Full scene — skeleton, mesh, materials, animation
- **Frame data:** Joint transforms, blendshapes, camera data
- **Best for:** Game engines (Unity/Unreal), Maya, full production pipelines

## C3D (Coordinate 3D)

- **Extension:** `.c3d`
- **Type:** Binary
- **Structure:** 3D marker positions + analog data (force plates, EMG)
- **Frame data:** Raw XYZ coordinates per marker per frame
- **Best for:** Biomechanics research, sports science, clinical analysis

## CSV (Comma-Separated Values)

- **Extension:** `.csv`
- **Type:** Plain text
- **Structure:** Custom — typically one row per frame, columns for each marker axis
- **Best for:** Custom Python/R analysis pipelines, data science workflows

## Recommended Export Settings

| Target | Format | Frame Rate | Coordinate System |
|--------|--------|------------|-------------------|
| Unreal Engine | FBX | 30 fps | Z-Up, Left-Handed |
| Unity | FBX | 30 fps | Y-Up, Left-Handed |
| Blender | BVH or FBX | 24/30 fps | Z-Up, Right-Handed |
| Python analysis | CSV or C3D | Native (120 fps) | Y-Up, Right-Handed |

---

*Last updated: March 2026 · Author: Arshad Naguru*
