# API Documentation Template

Use this template when documenting REST API endpoints. Copy the structure below and fill in the details for each endpoint.

## Template

````markdown
# API Name

> **Base URL:** `https://api.example.com/v1`
> **Authentication:** Bearer Token
> **Version:** 1.0.0

## Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/resource` | List all resources |
| GET    | `/resource/{id}` | Get a specific resource |
| POST   | `/resource` | Create a new resource |
| PUT    | `/resource/{id}` | Update a resource |
| DELETE | `/resource/{id}` | Delete a resource |

---

## GET `/resource`

Retrieve a list of all resources.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `page` | integer | No | Page number (default: 1) |
| `limit` | integer | No | Results per page (default: 20, max: 100) |

**Request:**

```bash
curl -X GET "https://api.example.com/v1/resource?page=1&limit=10" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Response (200 OK):**

```json
{
  "data": [
    {
      "id": "abc123",
      "name": "Example Resource",
      "created_at": "2026-03-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 42
  }
}
```

**Error Responses:**

| Status | Description |
|--------|-------------|
| 401 | Unauthorized — invalid or missing token |
| 500 | Internal server error |
````

## Usage Guidelines

1. **Document every endpoint** your API exposes, even simple ones
2. **Include real examples** — copy-paste-ready `curl` commands
3. **Show both success and error responses** with actual JSON
4. **List all parameters** including optional ones with their defaults
5. **Keep it updated** — outdated API docs are worse than no docs

## Where to Place API Docs

API documentation belongs in the **Reference** section:

```
docs/reference/api-<service-name>.md
```

Examples:

- `docs/reference/api-document-portal.md`
- `docs/reference/api-detection-service.md`

---

*Last updated: March 2026 · Author: Arshad Naguru*
