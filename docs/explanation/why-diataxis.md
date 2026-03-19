# Why Diátaxis?

## The Problem

Most documentation fails because it tries to do everything at once. A single document might mix a step-by-step tutorial with conceptual background, reference tables, and troubleshooting tips. The reader has to mentally filter through all of it to find what they actually need.

In environments with high turnover — like university labs and studio teams — this problem is amplified. Knowledge leaves when people leave, and what documentation does exist is often a disorganized mix of scattered notes, outdated wikis, and tribal knowledge that lives in someone's head.

## What Is Diátaxis?

Diátaxis is a documentation framework created by Daniele Procida that organizes content based on **what the reader needs at that moment**. It defines four distinct types of documentation, each serving a different purpose:

### The Four Quadrants

|  | **Learning** (practical) | **Information** (theoretical) |
|--|--------------------------|-------------------------------|
| **Acquiring** | **Tutorial** — "Teach me" | **Explanation** — "Help me understand" |
| **Applying** | **How-To Guide** — "Help me do X" | **Reference** — "Give me the facts" |

Each quadrant has fundamentally different characteristics:

**Tutorials** are learning-oriented. They take the reader by the hand through a series of steps, building up from nothing to a working result. The focus is on the learning journey, not efficiency.

**How-To Guides** are task-oriented. The reader already knows the basics and needs to accomplish a specific goal. These are practical, focused, and assume some prior knowledge.

**Reference** documentation is information-oriented. It describes the system accurately and completely — parameters, configurations, specifications. It is consulted, not read start-to-finish.

**Explanation** documentation is understanding-oriented. It provides context, discusses decisions, explores alternatives, and answers "why" questions. It helps the reader build a mental model.

## Why It Works

The framework works because it forces you to answer one question before writing anything: **"What does my reader need right now?"**

A developer who just wants to look up a command doesn't want to read through a tutorial. A new team member trying to learn the system doesn't want a dry reference table. By separating these concerns, each document does one thing well.

## Why We Use It Here

This documentation portal serves teams with regular turnover — student workers, research assistants, and collaborators who rotate through. Diátaxis helps because:

- **New members** start with Tutorials to build foundational skills
- **Active contributors** use How-To Guides for specific tasks
- **Everyone** uses Reference docs to look up standards and specs
- **Decision-makers** read Explanations to understand why things are the way they are

The framework also makes it obvious where a new document should go. If someone writes a guide, they can look at the four categories and immediately know where it belongs.

## Common Mistakes

**Mixing types in one document.** A tutorial that suddenly becomes a reference table halfway through. Keep types separate — link between them instead.

**Putting everything in "How-To."** Not every document is a how-to. If it teaches a concept, it is an explanation. If it lists specifications, it is a reference.

**Skipping Explanation.** Teams often write tutorials and references but never explain _why_ things work the way they do. Explanation docs are what prevent the same questions from being asked repeatedly.

## Further Reading

- [Diátaxis Official Documentation](https://diataxis.fr/)
- [Folder Structure Reference](../reference/folder-structure.md) — How Diátaxis maps to our directory layout

---

*Last updated: March 2026 · Author: Arshad Naguru*
