# Information Architecture Principles

## What Is Information Architecture?

Information architecture (IA) is the practice of organizing and structuring content so that people can find what they need efficiently. In documentation, IA answers a fundamental question: **"Where does this piece of information live?"**

Good IA means a new team member can navigate to the right document without asking anyone. Bad IA means people can't find things even when they exist, leading to duplicated effort and wasted time.

## Core Principles

### 1. Every Document Has One Home

A document should exist in exactly one place. If the same information appears in multiple locations, it will inevitably go out of sync. Instead of duplicating content, link to the single source of truth.

**Instead of this:**
Copying the Docker setup instructions into three different guides.

**Do this:**
Write Docker setup once in `tutorials/docker-fastapi.md` and link to it from other documents that reference Docker.

### 2. Organize by Reader Need, Not by Author Convenience

Content should be structured around what the reader is looking for, not around how the author thinks about it. This is why we use Diátaxis — it categorizes content by the reader's intent (learn, do, look up, or understand).

### 3. Use Consistent Naming

Predictable naming helps people guess where things are:

- File names: `kebab-case-descriptive-name.md`
- Folders: match Diátaxis categories exactly
- Headings: clear, specific, and scannable

A reader should be able to guess the filename from the topic and vice versa.

### 4. Flat Over Deep

Avoid deeply nested folder structures. Two levels of hierarchy (category → document) is usually sufficient. If you find yourself creating sub-sub-folders, the content probably needs to be reorganized, not further nested.

```
# Good: flat and scannable
docs/tutorials/python-ml-setup.md
docs/tutorials/docker-fastapi.md

# Bad: too deep
docs/tutorials/python/machine-learning/environment/setup.md
```

### 5. Navigation Should Be Obvious

A reader should never wonder "where do I go next?" Every document should include:

- **Prerequisites** at the top (what should I read first?)
- **Next Steps** at the bottom (where do I go after this?)
- **Cross-links** to related content throughout

## Applying These Principles

When adding a new document, ask yourself:

1. **What is it?** → Determines the Diátaxis category
2. **Who is it for?** → Determines the assumed knowledge level
3. **What comes before it?** → Determines prerequisites
4. **What comes after it?** → Determines next steps
5. **Does it duplicate anything?** → If yes, link instead of copying

## Signs of Bad Information Architecture

- People ask questions that are already answered in the docs
- The same information exists in multiple places with conflicting details
- New team members say they "can't find anything"
- Documents have vague titles like "Notes" or "Misc"
- There is a catch-all folder (often called "Other" or "General")

If you notice any of these, it is time for a documentation audit and restructure.

---

*Last updated: March 2026 · Author: Arshad Naguru*
