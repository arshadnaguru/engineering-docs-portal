# Manage Python Dependencies with pip

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Keep project dependencies organized, reproducible, and conflict-free.

## Create a Requirements File

```bash
# Generate from current environment
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt
```

## Best Practices for requirements.txt

```txt
# Pin exact versions for production
torch==2.1.0
scikit-learn==1.3.2
pandas==2.1.4
numpy==1.26.2

# Use >= for development/flexibility
matplotlib>=3.7.0
seaborn>=0.12.0
```

!!! warning
    Always pin exact versions in production. Unpinned dependencies can break your project when upstream packages update.

## Use Virtual Environments

```bash
# Create
python -m venv .venv

# Activate (Linux/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Deactivate
deactivate
```

## Check for Outdated Packages

```bash
pip list --outdated
```

## Resolve Conflicts

```bash
# Check what depends on a package
pip show numpy

# Force reinstall
pip install --force-reinstall numpy==1.26.2
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
