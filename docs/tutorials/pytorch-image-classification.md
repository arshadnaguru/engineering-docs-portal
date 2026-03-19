# Image Classification with PyTorch

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Build an image classifier using PyTorch with transfer learning on a custom dataset.

## Prerequisites

- Python 3.9+, PyTorch installed
- GPU recommended for training

## Step 1: Install Dependencies

```bash
pip install torch torchvision matplotlib pillow
```

## Step 2: Load and Prepare Data

```python
import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

train_dataset = datasets.ImageFolder("data/train", transform=transform)
val_dataset = datasets.ImageFolder("data/val", transform=transform)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

print(f"Classes: {train_dataset.classes}")
print(f"Training samples: {len(train_dataset)}")
```

## Step 3: Define the Model

```python
from torchvision import models
import torch.nn as nn

model = models.resnet50(pretrained=True)

# Freeze all layers
for param in model.parameters():
    param.requires_grad = False

# Replace final layer for our number of classes
num_classes = len(train_dataset.classes)
model.fc = nn.Linear(model.fc.in_features, num_classes)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
```

## Step 4: Train

```python
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

for epoch in range(10):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        _, predicted = outputs.max(1)
        total += labels.size(0)
        correct += predicted.eq(labels).sum().item()
    
    accuracy = 100.0 * correct / total
    print(f"Epoch {epoch+1}: Loss={running_loss/len(train_loader):.4f}, Acc={accuracy:.2f}%")
```

## Step 5: Save the Model

```python
torch.save(model.state_dict(), "model_weights.pth")
print("Model saved successfully")
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
