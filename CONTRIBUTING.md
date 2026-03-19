# Contributing to the Engineering Documentation Portal

Thank you for contributing! This guide explains how to submit, review, and maintain documentation in this portal.

## Before You Start

1. Read the [Markdown Style Guide](docs/reference/markdown-style-guide.md) — all contributions must follow these formatting standards
2. Understand [Why Diátaxis?](docs/explanation/why-diataxis.md) — so you place your content in the correct category
3. Review the [Folder Structure](docs/reference/folder-structure.md) — know where your document belongs

## Contribution Workflow

### Step 1: Identify Where Your Content Belongs

| If your content... | Category | Folder |
|---------------------|----------|--------|
| Teaches something step-by-step | Tutorial | `docs/tutorials/` |
| Helps accomplish a specific task | How-To Guide | `docs/how-to/` |
| Describes specifications or standards | Reference | `docs/reference/` |
| Explains concepts or reasoning | Explanation | `docs/explanation/` |

### Step 2: Create a Branch

```bash
git checkout main
git pull origin main
git checkout -b docs/<category>/<short-description>
```

Branch naming examples:
- `docs/tutorial/vr-headset-setup`
- `docs/how-to/export-mocap-data`
- `docs/reference/render-farm-specs`

### Step 3: Write Your Document

Use the appropriate template from the `templates/` folder:

```bash
cp templates/tutorial.md docs/tutorials/my-new-tutorial.md
```

File naming rules:
- Use `kebab-case`: `my-document-name.md`
- Be descriptive but concise
- No spaces, underscores, or capital letters

### Step 4: Use the Formatting Script (Optional)

If you are converting raw notes or drafts:

```bash
python scripts/format_notes.py --input my-raw-notes.txt --output docs/how-to/my-guide.md --category how-to
```

### Step 5: Submit a Merge Request

```bash
git add docs/tutorials/my-new-tutorial.md
git commit -m "docs(tutorial): add VR headset setup walkthrough"
git push origin docs/tutorial/vr-headset-setup
```

Then open a Merge Request on GitHub/GitLab with:
- A clear title describing the content
- The Diátaxis category
- A brief summary of what the document covers

### Step 6: Review Checklist

Your merge request will be reviewed against this checklist:

- [ ] Follows the [Markdown Style Guide](docs/reference/markdown-style-guide.md)
- [ ] Placed in the correct Diátaxis category folder
- [ ] All code blocks specify a language tag
- [ ] No broken internal or external links
- [ ] Includes author attribution and last-updated date in footer
- [ ] Reviewed for technical accuracy
- [ ] File uses `kebab-case` naming

## Commit Message Convention

```
docs(<category>): <short description>
```

Examples:
- `docs(tutorial): add motion capture calibration guide`
- `docs(how-to): update render pipeline export steps`
- `docs(reference): add API endpoint reference for asset manager`
- `docs(fix): correct broken links in tutorials section`

## Documentation Sprints

For large-scale documentation efforts, we run structured sprints:

1. **Gap Analysis** — Identify missing or outdated content
2. **Issue Creation** — Each gap becomes a tracked issue
3. **Assignment** — Tasks distributed across team members
4. **Sprint Period** — Typically 1–2 weeks
5. **Review & Merge** — All submissions go through standard review

## Questions?

If you're unsure where your content belongs or how to structure it, open an issue or ask in the team Slack channel before writing. It's easier to get the structure right upfront than to reorganize later.
