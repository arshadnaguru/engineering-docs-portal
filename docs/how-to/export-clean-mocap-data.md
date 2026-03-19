# Export and Clean Motion Capture Data

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Export motion capture data from studio software and clean it for use in production pipelines.

## When to Use This

- You have completed a mocap capture session and need to export usable data
- Raw data contains noise, jitter, or dropped frames that need cleaning

## Export from Capture Software

### OptiTrack Motive

1. Select the take in the **Takes** panel
2. Go to **File → Export Tracking Data**
3. Choose format: **FBX** (for animation) or **CSV** (for analysis)
4. Set coordinate system to **Y-Up, Right-Handed**
5. Click Export

### Vicon Nexus

1. Open the trial in Nexus
2. **Pipeline → Run Export**
3. Select **C3D** or **FBX** format
4. Verify marker labels are correct before exporting

## Clean the Data in Python

```python
import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

# Load CSV export
df = pd.read_csv("mocap_export.csv")

# Check for missing frames
missing = df.isnull().sum()
print(f"Missing values per column:\n{missing[missing > 0]}")

# Interpolate small gaps (< 10 frames)
df = df.interpolate(method='linear', limit=10)

# Smooth noisy joints
for col in df.columns:
    if col.startswith("Joint_"):
        df[col] = savgol_filter(df[col].fillna(method='ffill'), window_length=11, polyorder=3)

# Export cleaned data
df.to_csv("mocap_cleaned.csv", index=False)
print("Cleaned data exported successfully")
```

## Quality Checklist

- [ ] No gaps longer than 10 frames remain
- [ ] Joint positions are physically plausible (no teleporting markers)
- [ ] Frame rate matches project settings (e.g., 120fps for mocap, 30fps for final)
- [ ] Coordinate system matches target software

---

*Last updated: March 2026 · Author: Arshad Naguru*
