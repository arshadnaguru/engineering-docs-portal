# Environment Variables Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Standard environment variables used across projects and how to manage them.

## Common Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `mysql://user:pass@localhost:3306/db` |
| `SECRET_KEY` | Application secret for auth/sessions | `a1b2c3d4e5f6...` |
| `ENV` | Environment mode | `development`, `staging`, `production` |
| `PORT` | Application port | `8000` |
| `DEBUG` | Enable debug mode | `true` / `false` |
| `LOG_LEVEL` | Logging verbosity | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

## Setting Environment Variables

### Linux / macOS

```bash
# Temporary (current session)
export DATABASE_URL="mysql://user:pass@localhost/db"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export DATABASE_URL="mysql://user:pass@localhost/db"' >> ~/.bashrc
source ~/.bashrc
```

### Windows

```powershell
# Temporary
$env:DATABASE_URL = "mysql://user:pass@localhost/db"

# Permanent
[System.Environment]::SetEnvironmentVariable("DATABASE_URL", "value", "User")
```

### Using .env Files

Create a `.env` file in your project root:

```bash
DATABASE_URL=mysql://user:pass@localhost/db
SECRET_KEY=your-secret-key-here
ENV=development
DEBUG=true
PORT=8000
```

Load in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv("DATABASE_URL")
```

## Security Rules

- **Never** commit `.env` files to Git — add to `.gitignore`
- **Never** hardcode secrets in source code
- Use different values for development, staging, and production
- Rotate secrets regularly

---

*Last updated: March 2026 · Author: Arshad Naguru*
