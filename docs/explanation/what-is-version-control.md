# What Is Version Control?

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Explanation

## The Problem

Imagine three team members editing the same setup guide. Without version control, you end up with `setup_guide_v2_final_FINAL_johns_edits.md`. Nobody knows which version is current. Someone's changes get overwritten. A week later, nobody can reconstruct what was changed or why.

## The Solution

Version control (specifically Git) tracks every change to every file over time. Each change is recorded as a **commit** — a snapshot of the project at a point in time, with a message explaining what changed and who changed it.

## Key Concepts

**Repository (repo):** A project folder tracked by Git. Contains all files plus their complete history.

**Commit:** A saved snapshot. Each commit has a unique ID, author, timestamp, and message. Think of it as a "save point" you can always return to.

**Branch:** A parallel line of development. Create a branch to work on a new document without affecting the main version. When it's ready, merge it back.

**Merge:** Combining changes from one branch into another. Git handles most of this automatically — it only asks for help when two people changed the same line.

**Pull Request / Merge Request:** A formal request to merge your branch. Others review your changes before they enter the main branch — this is how quality control works.

## Why It Matters for Documentation

- **Nothing is ever lost.** Accidentally deleted a paragraph last week? Recover it from history.
- **Parallel work.** Multiple people can write different documents at the same time without conflicts.
- **Accountability.** Every change is attributed to a person — you know who wrote what.
- **Review before publish.** Merge requests ensure documentation is reviewed before it goes live.

## Git vs Other Systems

| Feature | Git | Google Docs | Shared Drive |
|---------|-----|-------------|--------------|
| Full history | Yes | Partial | No |
| Offline work | Yes | No | Yes |
| Branching | Yes | No | No |
| Code review | Yes | Comments only | No |
| Scales to large teams | Yes | Limited | No |

---

*Last updated: March 2026 · Author: Arshad Naguru*
