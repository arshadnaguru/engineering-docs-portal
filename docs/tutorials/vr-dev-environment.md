# Setting Up a VR Development Environment

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

This tutorial walks you through configuring a development environment for VR/XR projects, covering headset setup, SDK installation, and your first test scene.

## Prerequisites

- A VR headset (Meta Quest 2/3 or HTC Vive recommended)
- PC with a dedicated GPU (NVIDIA GTX 1060 or higher)
- Unity Hub installed

## Step 1: Install Unity with VR Support

1. Download and install [Unity Hub](https://unity.com/download)
2. Install Unity 2022 LTS or newer
3. During installation, check **Android Build Support** (for Quest) or **Windows Build Support**

```bash
# Verify Unity installation via CLI (optional)
unity -version
```

## Step 2: Install the XR Plugin

Open your Unity project and install the required XR packages:

1. Go to **Window → Package Manager**
2. Search for and install:
   - `XR Interaction Toolkit`
   - `OpenXR Plugin`
   - `XR Plugin Management`

## Step 3: Configure XR Settings

1. Go to **Edit → Project Settings → XR Plug-in Management**
2. Enable **OpenXR** for your target platform
3. Under OpenXR settings, add your headset's interaction profile

## Step 4: Create a Test Scene

```csharp
// Simple XR Origin setup script
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class VRTestSetup : MonoBehaviour
{
    void Start()
    {
        Debug.Log("VR Environment Initialized Successfully");
    }
}
```

## Step 5: Build and Test

1. Connect your headset via USB (or set up wireless debugging)
2. Go to **File → Build Settings → Build and Run**
3. Put on your headset — you should see the test scene

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Headset not detected | Check USB connection and install headset drivers |
| Black screen in headset | Verify OpenXR is enabled in Project Settings |
| Low frame rate | Reduce scene complexity or check GPU drivers |

## Next Steps

- Learn about [motion capture data processing](mocap-data-processing.md)
- Read [What is VR/XR?](../explanation/what-is-vr-xr.md) for conceptual background

---

*Last updated: March 2026 · Author: Arshad Naguru*
