# Markdown Style Guide

This style guide defines the formatting standards for all documentation in this portal. Every contributor must follow these rules to maintain consistency.

## Document Structure

Every document must follow this structure:

```markdown
# Document Title

> **Author:** Name · **Last Updated:** Month Year · **Category:** Tutorial|How-To|Reference|Explanation

Brief 1-2 sentence overview of what this document covers.

## Prerequisites (if applicable)

## Main Content Sections

## Next Steps / Related Docs

---

*Last updated: Month Year · Author: Name*
```

## Headings

- **H1 (`#`):** Document title only — one per document
- **H2 (`##`):** Major sections
- **H3 (`###`):** Subsections within a section
- **H4 (`####`):** Avoid if possible; restructure content instead

```markdown
# Document Title          ← Only one per file
## Major Section          ← Primary divisions
### Subsection            ← Details within a section
```

!!! warning "Never skip heading levels"
    Do not jump from `##` to `####`. Always use sequential heading levels.

## Code Blocks

Always specify the language for syntax highlighting:

````markdown
```python
def hello():
    return "Hello, world!"
```

```bash
docker build -t myapp .
```

```sql
SELECT * FROM users WHERE active = 1;
```
````

For inline code, use single backticks: `variable_name`, `docker ps`, `pip install`.

## Lists

**Unordered lists** — use `-` (not `*` or `+`):

```markdown
- First item
- Second item
  - Nested item
```

**Ordered lists** — use sequential numbers:

```markdown
1. First step
2. Second step
3. Third step
```

!!! tip "When to use which"
    Use **ordered lists** for sequential steps (do this, then this). Use **unordered lists** for items where order doesn't matter.

## Tables

Use tables for structured comparisons, command references, or parameter lists:

```markdown
| Column A | Column B | Column C |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
```

Keep tables simple. If a table exceeds 4 columns, consider restructuring as a definition list or separate subsections.

## Admonitions

Use admonition blocks for callouts:

```markdown
!!! note
    General information the reader should be aware of.

!!! tip
    Helpful advice that improves the reader's experience.

!!! warning
    Something that could cause problems if ignored.

!!! danger
    Critical information — ignoring this could cause data loss or system failure.
```

## Links

**Internal links** — use relative paths:

```markdown
See the [Markdown Style Guide](../reference/markdown-style-guide.md)
```

**External links** — use full URLs with descriptive text:

```markdown
See the [Docker documentation](https://docs.docker.com/)
```

Never use "click here" or raw URLs as link text.

## Images

Store images in `docs/assets/` and reference with relative paths:

```markdown
![Architecture diagram](../assets/architecture-overview.png)
```

Always include descriptive alt text for accessibility.

## File Naming

- Use `kebab-case` for all filenames: `my-guide-name.md`
- Keep names short but descriptive
- No spaces, underscores, or capital letters in filenames

## Commit Messages

Follow this convention for all documentation commits:

```
docs(<category>): <short description>
```

Examples:

- `docs(tutorial): add Python ML setup guide`
- `docs(reference): update style guide with admonition rules`
- `docs(fix): correct broken links in how-to section`

---

*Last updated: March 2026 · Author: Arshad Naguru*
