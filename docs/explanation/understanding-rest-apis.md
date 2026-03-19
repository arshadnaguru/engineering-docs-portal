# Understanding REST APIs

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Explanation

## What Is a REST API?

REST (Representational State Transfer) is an architectural style for building web services. A REST API allows different software systems to communicate over HTTP using standard methods — the same protocol your browser uses to load web pages.

## The Core Idea

Everything is a **resource** — a document, a user, a render job, a mocap recording. Each resource has a URL, and you interact with it using HTTP methods:

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Read/retrieve | `GET /documents/42` — fetch document #42 |
| POST | Create new | `POST /documents` — create a new document |
| PUT | Update existing | `PUT /documents/42` — update document #42 |
| DELETE | Remove | `DELETE /documents/42` — delete document #42 |

## Why REST?

**It uses what already exists.** HTTP is everywhere. Every programming language can make HTTP requests. No special protocols or libraries needed.

**It's stateless.** Each request contains everything the server needs to process it. The server doesn't remember previous requests. This makes APIs scalable — any server in a cluster can handle any request.

**It's uniform.** Once you learn how one REST API works, you understand the pattern for all of them. Resources, URLs, HTTP methods, JSON responses — the conventions are consistent.

## How It Fits in Our Work

REST APIs connect the different parts of our systems:

- The **documentation portal** could expose an API to query guides programmatically
- **Render farm managers** use APIs to submit and monitor jobs
- **Mocap systems** use APIs to stream data to Unreal Engine via LiveLink
- **Automation scripts** call APIs to trigger builds, deployments, or exports

## Request and Response

A typical API interaction:

```
Client → Server:
  GET /api/v1/documents?category=tutorial
  Headers: Authorization: Bearer token123

Server → Client:
  Status: 200 OK
  Body: {
    "data": [
      {"id": 1, "title": "Python ML Setup", "category": "tutorial"},
      {"id": 2, "title": "Docker Basics", "category": "tutorial"}
    ],
    "count": 2
  }
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
