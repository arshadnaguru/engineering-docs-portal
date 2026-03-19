# Getting Started with Unity for VR

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Create your first interactive VR scene in Unity with hand tracking and object interaction.

## Prerequisites

- Unity 2022 LTS with XR packages installed (see [VR Dev Environment Setup](vr-dev-environment.md))
- VR headset connected

## Step 1: Create a New VR Project

1. Open Unity Hub → **New Project**
2. Select **3D (URP)** template
3. Name it and click Create

## Step 2: Set Up the XR Rig

1. Delete the default Main Camera
2. Right-click in Hierarchy → **XR → XR Origin (VR)**
3. This creates a camera rig that tracks your headset and controllers

## Step 3: Add Interactable Objects

```csharp
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class GrabbableObject : MonoBehaviour
{
    private XRGrabInteractable grabInteractable;
    
    void Start()
    {
        grabInteractable = GetComponent<XRGrabInteractable>();
        grabInteractable.selectEntered.AddListener(OnGrab);
        grabInteractable.selectExited.AddListener(OnRelease);
    }
    
    private void OnGrab(SelectEnterEventArgs args)
    {
        Debug.Log($"Grabbed: {gameObject.name}");
    }
    
    private void OnRelease(SelectExitEventArgs args)
    {
        Debug.Log($"Released: {gameObject.name}");
    }
}
```

## Step 4: Add a 3D Environment

1. Right-click in Hierarchy → **3D Object → Plane** (floor)
2. Add cubes and spheres as interactable objects
3. Add **Rigidbody** and **XR Grab Interactable** components to each object

## Step 5: Build and Test

1. **File → Build Settings** → Select your platform
2. Click **Build and Run**
3. Pick up and throw objects in VR

---

*Last updated: March 2026 · Author: Arshad Naguru*
