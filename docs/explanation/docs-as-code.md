# Docs-as-Code Philosophy

## What Is Docs-as-Code?

Docs-as-Code is the practice of treating documentation with the same rigor as software code. Instead of editing documents in Google Docs or Word and sharing them via email, you write documentation in plain text (Markdown), store it in a version-controlled repository (Git), and use the same review and deployment workflows that software teams use.

## How It Works in Practice

| Traditional Documentation | Docs-as-Code |
|--------------------------|---------------|
| Write in Google Docs or Word | Write in Markdown in a code editor |
| Share via email or shared drive | Store in a Git repository |
| Edits are untracked | Every change has a commit message |
| Review happens in comments | Review happens via merge requests |
| Published by copying files | Published automatically via CI/CD |
| One person "owns" the doc | Anyone can contribute via branches |

## Why Plain Text (Markdown)?

Markdown is the standard because:

- **Portable** — Markdown renders on GitHub, GitLab, MkDocs, Notion, and virtually every documentation platform
- **Diffable** — Git can show exactly what changed line by line, unlike binary formats like `.docx`
- **Lightweight** — No special software needed; any text editor works
- **Future-proof** — Plain text files will be readable decades from now

## Why Version Control (Git)?

Git solves three critical documentation problems:

**Problem 1: "Who changed this?"** — Every edit is tracked with an author, timestamp, and commit message. You can see exactly who wrote or modified any line.

**Problem 2: "What did it say before?"** — Git keeps the entire history. You can revert to any previous version of any document instantly.

**Problem 3: "Two people edited the same doc."** — Branching and merge requests allow multiple people to work on different parts simultaneously without overwriting each other.

## Why Review Workflows?

In a Docs-as-Code workflow, documentation changes go through the same review process as code:

1. Author creates a branch and writes/edits content
2. Author opens a merge request
3. Reviewer checks for accuracy, formatting, and completeness
4. Changes are discussed and refined
5. Approved changes are merged into the main branch
6. Documentation is automatically published

This ensures that no unreviewed content reaches the published documentation. It also distributes knowledge — the reviewer learns about the topic during the review.

## How We Apply It Here

This portal is built entirely on Docs-as-Code principles:

- All content is written in **Markdown**
- Everything lives in a **Git repository**
- Changes go through **merge request reviews**
- The site is built with **MkDocs**, which generates a static site from Markdown files
- Our [formatting script](../how-to/format-notes-markdown.md) automates the conversion of raw notes into our Markdown standard

## When Docs-as-Code Is Not the Right Fit

Docs-as-Code works best for technical documentation maintained by teams comfortable with Git. It may not suit:

- Non-technical teams with no Git experience (though this is learnable)
- Highly visual documents where layout matters more than content structure
- Documents that require real-time collaborative editing (use a shared editor, then migrate to Markdown)

For our use case — engineering documentation in a technical environment — Docs-as-Code is the right approach.

---

*Last updated: March 2026 · Author: Arshad Naguru*
