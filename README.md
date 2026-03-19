# Engineering Documentation Portal

A centralized, version-controlled documentation hub organized using the [Diátaxis framework](https://diataxis.fr/) and built with [Docs-as-Code](docs/explanation/docs-as-code.md) principles.

## Purpose

In fast-moving engineering environments with frequent team turnover, institutional knowledge is constantly at risk. This portal prevents knowledge loss by:

- **Standardizing** all documentation into strict Markdown format
- **Organizing** content using Diátaxis (Tutorials, How-To Guides, Reference, Explanation)
- **Automating** the conversion of raw notes into structured guides via Python scripts
- **Version-controlling** everything through Git-based review workflows

## Structure

```
docs/
├── tutorials/       # Learning-oriented: step-by-step walkthroughs
├── how-to/          # Task-oriented: practical instructions
├── reference/       # Information-oriented: specs, templates, standards
└── explanation/     # Understanding-oriented: concepts and reasoning
```

## Quick Start

### View the Documentation

```bash
# Install MkDocs with Material theme
pip install mkdocs-material

# Serve locally
mkdocs serve

# Open http://127.0.0.1:8000 in your browser
```

### Convert Raw Notes to Structured Markdown

```bash
python scripts/format_notes.py --input raw_notes.txt --output docs/how-to/my-guide.md --category how-to
```

### Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow, branch naming conventions, and review checklist.

## Tech Stack

| Tool | Purpose |
|------|---------|
| [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | Static site generator |
| Markdown | Content format |
| Git / GitLab | Version control & review |
| Python | Automation scripts |
| Diátaxis | Documentation framework |

## Author

**Arshad Naguru** — [an2629@rit.edu](mailto:an2629@rit.edu) · [GitHub](https://github.com/arshadnaguru)

## License

This project is licensed under the MIT License.
