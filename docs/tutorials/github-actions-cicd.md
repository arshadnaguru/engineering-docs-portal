# Setting Up CI/CD with GitHub Actions

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Automate testing and deployment with GitHub Actions — create workflows that run on every push.

## Prerequisites

- A GitHub repository
- Familiarity with YAML syntax

## Step 1: Create the Workflow File

Create `.github/workflows/ci.yml`:

```yaml
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest
      
      - name: Run tests
        run: pytest tests/ -v
      
      - name: Lint check
        run: |
          pip install flake8
          flake8 src/ --max-line-length=120
```

## Step 2: Add a Documentation Build Job

```yaml
  docs:
    runs-on: ubuntu-latest
    needs: test
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install MkDocs
        run: pip install mkdocs-material
      
      - name: Build documentation
        run: mkdocs build --strict
      
      - name: Deploy to GitHub Pages
        if: github.ref == 'refs/heads/main'
        run: mkdocs gh-deploy --force
```

## Step 3: Monitor Workflow Runs

Go to your repository → **Actions** tab to see workflow runs, logs, and status badges.

## Adding a Status Badge

Add to your `README.md`:

```markdown
![CI](https://github.com/yourusername/yourrepo/actions/workflows/ci.yml/badge.svg)
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
