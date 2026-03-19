# Getting Started with OpenCV

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Learn the fundamentals of computer vision using OpenCV in Python — image loading, processing, and basic transformations.

## Prerequisites

- Python 3.9+ with a virtual environment
- Basic understanding of NumPy arrays

## Step 1: Install OpenCV

```bash
pip install opencv-python numpy matplotlib
```

## Step 2: Load and Display an Image

```python
import cv2
import matplotlib.pyplot as plt

# Load an image
img = cv2.imread("sample.jpg")

# OpenCV loads images in BGR — convert to RGB for display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

print(f"Image shape: {img.shape}")  # (height, width, channels)
```

## Step 3: Basic Transformations

```python
# Resize
resized = cv2.resize(img, (640, 480))

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# Edge detection
edges = cv2.Canny(gray, 50, 150)
```

## Step 4: Save the Output

```python
cv2.imwrite("output_gray.jpg", gray)
cv2.imwrite("output_edges.jpg", edges)
print("Images saved successfully")
```

## Step 5: Real-Time Video Capture

```python
cap = cv2.VideoCapture(0)  # 0 = default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Live Feed", gray_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: cv2` | Run `pip install opencv-python` |
| Image loads as `None` | Check file path — use absolute paths if unsure |
| Webcam not opening | Try `VideoCapture(1)` or check camera permissions |

---

*Last updated: March 2026 · Author: Arshad Naguru*
