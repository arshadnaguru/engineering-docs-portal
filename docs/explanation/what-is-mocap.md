# What Is Motion Capture?

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Explanation

## Definition

Motion capture (mocap) is the process of recording the movement of objects or people and translating that movement into digital data. In studio environments, it's used to animate 3D characters, analyze human movement, and drive real-time avatars in VR.

## Types of Motion Capture

### Optical (Marker-Based)

Reflective markers are placed on the performer's body. Infrared cameras track the markers' positions in 3D space at high frame rates (120-240 fps).

**Pros:** High accuracy, industry standard, large capture volumes
**Cons:** Markers can be occluded, setup time, requires calibrated camera array
**Systems:** OptiTrack, Vicon

### Inertial (IMU-Based)

Small sensors (accelerometers, gyroscopes) are worn on the body. They measure rotation and acceleration without cameras.

**Pros:** No occlusion issues, portable, works anywhere
**Cons:** Positional drift over time, lower accuracy than optical
**Systems:** Xsens, Rokoko

### Markerless

Computer vision algorithms track body movement from standard video cameras without any sensors on the performer.

**Pros:** No suit or markers needed, fast setup
**Cons:** Lower accuracy, sensitive to lighting, limited body parts
**Systems:** Move.ai, DeepMotion

## The Data

Motion capture produces time-series data — 3D positions and/or rotations for each tracked point, captured many times per second. This data is stored in formats like BVH, FBX, or C3D (see [Mocap File Formats Reference](../reference/mocap-file-formats.md)).

Raw mocap data almost always needs cleaning — filling gaps where markers were lost, smoothing jitter, and removing noise. This is one of the most time-consuming parts of the pipeline and one of the most important to document well.

## Applications in Our Studio

- **Character animation** for games and film
- **Real-time avatar driving** in VR experiences
- **Performance analysis** for research projects
- **Virtual production** — driving digital characters live on set

---

*Last updated: March 2026 · Author: Arshad Naguru*
