# Git Command Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Quick reference for Git commands used in documentation and development workflows.

## Setup

| Command | Description |
|---------|-------------|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "email"` | Set your email |
| `git init` | Initialize a new repository |
| `git clone url` | Clone a remote repository |

## Daily Workflow

| Command | Description |
|---------|-------------|
| `git status` | Check modified/staged files |
| `git add file` | Stage a specific file |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git push origin branch` | Push to remote |
| `git pull origin branch` | Pull latest changes |

## Branching

| Command | Description |
|---------|-------------|
| `git branch` | List local branches |
| `git branch -a` | List all branches (including remote) |
| `git checkout -b branch` | Create and switch to new branch |
| `git checkout branch` | Switch to existing branch |
| `git merge branch` | Merge branch into current |
| `git branch -d branch` | Delete a branch |

## History and Inspection

| Command | Description |
|---------|-------------|
| `git log --oneline` | Compact commit history |
| `git log --oneline --graph` | Visual branch history |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git show commit_hash` | Show a specific commit |
| `git blame file` | See who changed each line |

## Undoing Changes

| Command | Description |
|---------|-------------|
| `git checkout -- file` | Discard unstaged changes |
| `git reset HEAD file` | Unstage a file |
| `git revert commit_hash` | Create a new commit that undoes changes |
| `git stash` | Temporarily save changes |
| `git stash pop` | Restore stashed changes |

## Documentation Commit Convention

```
docs(<category>): <short description>
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
