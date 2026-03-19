# Format Raw Notes into Structured Markdown

This guide shows you how to use our `format_notes.py` script to convert raw, unstructured notes (from meetings, student logs, or scratch documents) into properly formatted Markdown that follows our portal's style standards.

## When to Use This

- You have raw meeting notes, student logs, or draft documents
- Content needs to be restructured into our Markdown standard before publishing
- You want to batch-process multiple files at once

## Prerequisites

- Python 3.9+
- The `format_notes.py` script from the `scripts/` directory

## Using the Script

### Single File

```bash
python scripts/format_notes.py --input raw_notes.txt --output docs/how-to/formatted-guide.md
```

### Batch Processing

```bash
# Process all .txt files in a directory
python scripts/format_notes.py --input-dir drafts/ --output-dir docs/tutorials/
```

### What the Script Does

The script performs the following transformations:

1. **Adds YAML-style metadata header** (title, author, date, category)
2. **Converts headings** to proper Markdown hierarchy (`#`, `##`, `###`)
3. **Wraps code snippets** in fenced code blocks with language tags
4. **Normalizes lists** into consistent Markdown bullet or numbered format
5. **Adds admonition blocks** for notes, warnings, and tips
6. **Inserts a standard footer** with author and last-updated date
7. **Validates internal links** and flags any broken references

### Example

**Input** (`raw_notes.txt`):

```
docker setup notes
- install docker from website
- run docker build command: docker build -t myapp .
- make sure port 8000 is open
NOTE: dont forget .dockerignore file
updated by arshad march 2026
```

**Output** (`formatted-guide.md`):

```markdown
# Docker Setup Notes

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

## Installation

- Install Docker from the [official website](https://docs.docker.com/get-docker/)

## Build the Image

Run the build command:

\`\`\`bash
docker build -t myapp .
\`\`\`

Ensure port 8000 is open on your host machine.

!!! warning
    Don't forget to create a `.dockerignore` file to exclude unnecessary files from the build context.

---

*Last updated: March 2026 · Author: Arshad Naguru*
```

## Customizing the Template

The script uses templates from the `templates/` directory. You can modify:

- `templates/tutorial.md` — For learning-oriented content
- `templates/how-to.md` — For task-oriented guides
- `templates/reference.md` — For technical reference docs

See the [Markdown Style Guide](../reference/markdown-style-guide.md) for the full formatting specification.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script can't detect headings | Ensure raw notes use some form of hierarchy (indentation, numbering, or caps) |
| Code blocks not detected | Put code on a separate line, prefixed with `$`, `>`, or indented with 4+ spaces |
| Output looks wrong | Run with `--verbose` flag to see each transformation step |

---

*Last updated: March 2026 · Author: Arshad Naguru*
