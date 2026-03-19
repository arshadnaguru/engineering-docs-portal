# Getting Started with Git for Documentation

This tutorial teaches you Git fundamentals specifically in the context of managing documentation. By the end, you will be able to create a documentation repository, make structured commits, and collaborate through branches and merge requests.

## Prerequisites

- Git installed ([Download Git](https://git-scm.com/downloads))
- A GitHub or GitLab account
- Terminal/command line access

## Step 1: Configure Git

Set up your identity (one-time setup):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify
git config --list
```

## Step 2: Initialize a Documentation Repository

```bash
# Create project folder
mkdir my-docs && cd my-docs

# Initialize Git
git init

# Create initial structure
mkdir -p docs/{tutorials,how-to,reference,explanation}
touch docs/{tutorials,how-to,reference,explanation}/.gitkeep
```

## Step 3: Create Your First Document

Create `docs/reference/setup-guide.md`:

```markdown
# Setup Guide

## Overview
This guide covers the initial setup for our project.

## Requirements
- Python 3.9+
- Docker 20+

## Installation
1. Clone the repository
2. Install dependencies
3. Run the application
```

## Step 4: Stage and Commit

```bash
# Check what's changed
git status

# Stage your new file
git add docs/reference/setup-guide.md

# Commit with a descriptive message
git commit -m "docs(reference): add initial setup guide"
```

!!! tip "Commit Message Convention"
    Use the format `docs(<section>): <short description>` for all documentation commits. This keeps the Git history scannable and organized.

    Examples:

    - `docs(tutorial): add Python ML setup walkthrough`
    - `docs(how-to): update Docker deployment steps`
    - `docs(reference): fix typo in API template`
    - `docs(explanation): add Diátaxis overview`

## Step 5: Create a Branch for New Content

Never commit directly to `main`. Use feature branches:

```bash
# Create and switch to a new branch
git checkout -b docs/add-docker-tutorial

# Write your document, then stage and commit
git add docs/tutorials/docker-setup.md
git commit -m "docs(tutorial): add Docker containerization tutorial"

# Push to remote
git push origin docs/add-docker-tutorial
```

## Step 6: Open a Merge Request

On GitHub/GitLab:

1. Navigate to your repository
2. Click **"New Pull Request"** (GitHub) or **"New Merge Request"** (GitLab)
3. Select your branch (`docs/add-docker-tutorial`) → `main`
4. Add a description of what you documented and why
5. Request a review from a team member

## Step 7: Review and Merge

During review, check for:

- [ ] Follows the [Markdown Style Guide](../reference/markdown-style-guide.md)
- [ ] Placed in the correct Diátaxis category
- [ ] No broken links or images
- [ ] Code blocks are properly formatted and tested

Once approved, merge into `main`.

## Common Git Commands for Documentation

| Command | Purpose |
|---------|---------|
| `git status` | See what files have changed |
| `git diff` | View exact changes line by line |
| `git log --oneline` | View commit history (compact) |
| `git pull origin main` | Get latest changes from remote |
| `git stash` | Temporarily save uncommitted changes |

## Next Steps

- Read the [Markdown Style Guide](../reference/markdown-style-guide.md) for formatting standards
- Learn about our [Documentation Review Workflow](../how-to/doc-review-workflow.md)

---

*Last updated: March 2026 · Author: Arshad Naguru*
