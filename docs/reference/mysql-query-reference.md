# MySQL Query Reference

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Reference

Common MySQL queries for data management and reporting.

## Database Management

```sql
SHOW DATABASES;
CREATE DATABASE project_db;
USE project_db;
DROP DATABASE test_db;
```

## Table Operations

```sql
SHOW TABLES;
DESCRIBE table_name;

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    category VARCHAR(50) DEFAULT 'general',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE documents ADD COLUMN author VARCHAR(100);
DROP TABLE documents;
```

## CRUD Operations

```sql
-- Create
INSERT INTO documents (title, content, category) 
VALUES ('Setup Guide', 'Step 1...', 'tutorial');

-- Read
SELECT * FROM documents WHERE category = 'tutorial' ORDER BY created_at DESC;
SELECT title, category, COUNT(*) as count FROM documents GROUP BY category;

-- Update
UPDATE documents SET content = 'Updated content' WHERE id = 1;

-- Delete
DELETE FROM documents WHERE id = 1;
```

## Useful Queries

```sql
-- Search
SELECT * FROM documents WHERE title LIKE '%docker%';

-- Join
SELECT d.title, c.name as contributor
FROM documents d
JOIN contributors c ON d.author_id = c.id;

-- Count by category
SELECT category, COUNT(*) as total FROM documents GROUP BY category;

-- Recent entries
SELECT * FROM documents ORDER BY created_at DESC LIMIT 10;
```

## User Management

```sql
CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON project_db.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'app_user'@'localhost';
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
