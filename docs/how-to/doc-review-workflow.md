# Set Up a Documentation Review Workflow

This guide explains how to configure a Git-based review workflow for documentation contributions, ensuring quality and consistency before content reaches the main branch.

## Overview

Every documentation change goes through this pipeline:

```
Draft → Branch → Merge Request → Review → Approval → Merge to main
```

This ensures all published documentation meets our [Markdown Style Guide](../reference/markdown-style-guide.md) and is placed in the correct Diátaxis category.

## Step 1: Configure Branch Protection

On GitHub or GitLab, protect the `main` branch:

**GitHub:**

1. Go to **Settings → Branches → Branch protection rules**
2. Add rule for `main`
3. Enable: _Require a pull request before merging_
4. Enable: _Require approvals_ (minimum 1)

**GitLab:**

1. Go to **Settings → Repository → Protected branches**
2. Set `main` to _Allowed to merge: Maintainers_, _Allowed to push: No one_

## Step 2: Define the Branch Naming Convention

All documentation branches follow this pattern:

```
docs/<category>/<short-description>
```

Examples:

- `docs/tutorial/python-ml-setup`
- `docs/how-to/docker-deploy`
- `docs/reference/api-template-update`
- `docs/fix/broken-links-tutorials`

## Step 3: Create a Merge Request Template

Save this as `.github/PULL_REQUEST_TEMPLATE.md` (GitHub) or `.gitlab/merge_request_templates/Documentation.md` (GitLab):

```markdown
## Documentation Change

**Diátaxis Category:** (Tutorial / How-To / Reference / Explanation)

**Summary:**
Brief description of what this document covers.

## Checklist

- [ ] Follows the [Markdown Style Guide](docs/reference/markdown-style-guide.md)
- [ ] Placed in the correct Diátaxis category folder
- [ ] All code blocks specify a language tag
- [ ] No broken internal links
- [ ] Includes author attribution and last-updated date
- [ ] Reviewed for technical accuracy
```

## Step 4: Review Criteria

When reviewing documentation, check for:

| Criterion | What to Look For |
|-----------|-----------------|
| **Accuracy** | Are technical steps correct and tested? |
| **Category** | Is it in the right Diátaxis section? |
| **Formatting** | Does it follow the Markdown Style Guide? |
| **Completeness** | Are there missing steps or grey areas? |
| **Links** | Do all internal and external links work? |
| **Voice** | Is the tone consistent, clear, and professional? |

## Step 5: Documentation Sprint Process

For large-scale documentation efforts:

1. **Identify gaps** — Review existing docs for missing or outdated content
2. **Create issues** — Open a GitLab/GitHub issue for each documentation task
3. **Assign owners** — Distribute tasks across team members
4. **Set a deadline** — Typically a 1-2 week sprint
5. **Review and merge** — All submissions go through the standard review workflow

---

*Last updated: March 2026 · Author: Arshad Naguru*
