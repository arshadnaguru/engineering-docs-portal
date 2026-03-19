# Setting Up a Python ML Environment

This tutorial walks you through creating a clean, reproducible Python environment for machine learning projects. By the end, you will have a fully configured workspace with PyTorch, scikit-learn, and essential data science tools.

## Prerequisites

- Python 3.9+ installed on your system
- `pip` package manager
- Terminal/command line access
- (Optional) NVIDIA GPU with CUDA drivers for GPU acceleration

## Step 1: Create a Virtual Environment

Always isolate your project dependencies using a virtual environment:

```bash
# Create a new virtual environment
python -m venv ml-env

# Activate it
# On Linux/macOS:
source ml-env/bin/activate

# On Windows:
ml-env\Scripts\activate
```

You should see `(ml-env)` in your terminal prompt, confirming the environment is active.

## Step 2: Install Core Dependencies

Create a `requirements.txt` file with the following packages:

```txt
# Core ML frameworks
torch>=2.0.0
tensorflow>=2.13.0
scikit-learn>=1.3.0

# Data processing
pandas>=2.0.0
numpy>=1.24.0

# Visualization
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0

# Utilities
jupyter>=1.0.0
tqdm>=4.65.0
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

## Step 3: Verify the Installation

Run the following script to confirm everything is installed correctly:

```python
import torch
import sklearn
import pandas as pd
import numpy as np
import matplotlib

print(f"PyTorch:      {torch.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
print(f"Pandas:       {pd.__version__}")
print(f"NumPy:        {np.__version__}")
print(f"Matplotlib:   {matplotlib.__version__}")

# Check GPU availability
if torch.cuda.is_available():
    print(f"GPU:          {torch.cuda.get_device_name(0)}")
else:
    print("GPU:          Not available (CPU mode)")
```

Expected output:

```
PyTorch:      2.1.0
scikit-learn: 1.3.2
Pandas:       2.1.4
NumPy:        1.26.2
Matplotlib:   3.8.2
GPU:          NVIDIA GeForce RTX 3060 (or "Not available")
```

## Step 4: Set Up Jupyter Notebook

Launch Jupyter to start experimenting:

```bash
jupyter notebook
```

Create a new notebook and run the verification script from Step 3 to confirm your environment works inside Jupyter as well.

## Step 5: Project Structure

Organize your ML project using this standard layout:

```
my-ml-project/
├── data/
│   ├── raw/              # Original, unprocessed data
│   └── processed/        # Cleaned and transformed data
├── notebooks/            # Jupyter notebooks for exploration
├── src/
│   ├── data/             # Data loading and preprocessing
│   ├── models/           # Model definitions
│   ├── training/         # Training scripts
│   └── evaluation/       # Evaluation and metrics
├── tests/                # Unit tests
├── requirements.txt
├── README.md
└── .gitignore
```

## Next Steps

- Learn how to [containerize your project with Docker](docker-fastapi.md) for reproducible deployment
- Review the [Markdown Style Guide](../reference/markdown-style-guide.md) for documentation standards

---

*Last updated: March 2026 · Author: Arshad Naguru*
