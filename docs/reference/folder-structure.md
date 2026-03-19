# Project Folder Structure

This reference describes the standard directory layout for this documentation portal and how content maps to the Diátaxis framework.

## Repository Layout

```
engineering-docs-portal/
├── mkdocs.yml                  # Site configuration and navigation
├── CONTRIBUTING.md             # Contribution guidelines
├── README.md                   # Repository overview
├── scripts/
│   └── format_notes.py         # Raw-to-Markdown conversion script
├── templates/
│   ├── tutorial.md             # Template for tutorials
│   ├── how-to.md               # Template for how-to guides
│   └── reference.md            # Template for reference docs
└── docs/
    ├── index.md                # Portal homepage
    ├── assets/                 # Images, diagrams, static files
    ├── tutorials/              # Learning-oriented content
    │   ├── index.md
    │   ├── python-ml-setup.md
    │   ├── docker-fastapi.md
    │   └── git-for-docs.md
    ├── how-to/                 # Task-oriented content
    │   ├── index.md
    │   ├── docker-deploy-linux.md
    │   ├── format-notes-markdown.md
    │   └── doc-review-workflow.md
    ├── reference/              # Information-oriented content
    │   ├── index.md
    │   ├── markdown-style-guide.md
    │   ├── api-doc-template.md
    │   └── folder-structure.md
    └── explanation/            # Understanding-oriented content
        ├── index.md
        ├── why-diataxis.md
        ├── docs-as-code.md
        └── information-architecture.md
```

## Diátaxis Category Mapping

| Directory | Diátaxis Type | Content Purpose | Reader Need |
|-----------|--------------|-----------------|-------------|
| `tutorials/` | Tutorial | Step-by-step learning experiences | "I want to learn" |
| `how-to/` | How-To Guide | Practical task completion | "I want to do X" |
| `reference/` | Reference | Technical specifications and standards | "I want to look something up" |
| `explanation/` | Explanation | Conceptual context and reasoning | "I want to understand why" |

## Where to Put New Content

Ask yourself what the reader needs:

- **"Follow along and learn"** → `tutorials/`
- **"Get this specific thing done"** → `how-to/`
- **"Look up how X works"** → `reference/`
- **"Understand the reasoning"** → `explanation/`

If you are unsure, see [Why Diátaxis?](../explanation/why-diataxis.md) for a deeper explanation of each category.

---

*Last updated: March 2026 · Author: Arshad Naguru*
