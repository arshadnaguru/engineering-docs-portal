# Python Virtual Environment Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Complete reference for creating and managing Python virtual environments.

## Creating Environments

| Method | Command | Notes |
|--------|---------|-------|
| venv (built-in) | `python -m venv .venv` | Recommended for most projects |
| conda | `conda create -n myenv python=3.11` | For data science, manages non-Python deps |
| virtualenv | `virtualenv .venv` | Legacy, use venv instead |

## Activation / Deactivation

| OS | Activate | Deactivate |
|----|----------|------------|
| Linux/macOS | `source .venv/bin/activate` | `deactivate` |
| Windows (CMD) | `.venv\Scripts\activate.bat` | `deactivate` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` | `deactivate` |
| Windows (Git Bash) | `source .venv/Scripts/activate` | `deactivate` |

## Dependency Management

```bash
# Install packages
pip install package_name

# Save current dependencies
pip freeze > requirements.txt

# Install from file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade package_name

# Uninstall
pip uninstall package_name
```

## .gitignore Entry

Always add your virtual environment to `.gitignore`:

```
.venv/
venv/
env/
```

## Common Issues

| Issue | Solution |
|-------|----------|
| `command not found: python` | Use `python3` instead |
| PowerShell execution policy error | Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Wrong Python version in venv | Specify: `python3.11 -m venv .venv` |

---

*Last updated: March 2026 · Author: Arshad Naguru*
