# Setting Up MySQL for a Project

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** Tutorial

Set up a MySQL database for your application, create tables, and connect from Python.

## Prerequisites

- MySQL Server 8.0+ installed
- Python 3.9+

## Step 1: Install MySQL

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server

# Start the service
sudo systemctl start mysql
sudo systemctl enable mysql
```

## Step 2: Secure the Installation

```bash
sudo mysql_secure_installation
```

Follow the prompts to set a root password and remove test databases.

## Step 3: Create a Database and User

```sql
-- Log into MySQL
-- sudo mysql -u root -p

CREATE DATABASE project_db;

CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON project_db.* TO 'app_user'@'localhost';
FLUSH PRIVILEGES;
```

## Step 4: Create Tables

```sql
USE project_db;

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    category ENUM('tutorial', 'how-to', 'reference', 'explanation') DEFAULT 'how-to',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE contributors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role ENUM('author', 'reviewer', 'admin') DEFAULT 'author'
);
```

## Step 5: Connect from Python

```bash
pip install mysql-connector-python
```

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="app_user",
    password="secure_password",
    database="project_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM documents")
results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Access denied for user | Verify username, password, and grants |
| Can't connect to MySQL | Check if service is running: `systemctl status mysql` |
| Table doesn't exist | Confirm you're using the correct database: `USE project_db;` |

---

*Last updated: March 2026 · Author: Arshad Naguru*
