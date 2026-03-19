# Back Up and Restore a MySQL Database

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Create reliable backups and restore MySQL databases when needed.

## Create a Backup

```bash
# Single database
mysqldump -u root -p project_db > backup_project_db_$(date +%Y%m%d).sql

# All databases
mysqldump -u root -p --all-databases > backup_all_$(date +%Y%m%d).sql

# Specific tables only
mysqldump -u root -p project_db documents contributors > backup_tables.sql
```

## Restore from Backup

```bash
# Restore to existing database
mysql -u root -p project_db < backup_project_db_20260319.sql

# Restore creating new database
mysql -u root -p -e "CREATE DATABASE project_db_restored;"
mysql -u root -p project_db_restored < backup_project_db_20260319.sql
```

## Automate Daily Backups

Create `/etc/cron.d/mysql-backup`:

```bash
# Run backup at 2 AM daily
0 2 * * * root mysqldump -u root -pYOUR_PASSWORD project_db | gzip > /backups/project_db_$(date +\%Y\%m\%d).sql.gz
```

## Verify Backup Integrity

```bash
# Check if file is valid SQL
head -5 backup_project_db.sql

# Test restore to a temporary database
mysql -u root -p -e "CREATE DATABASE test_restore;"
mysql -u root -p test_restore < backup_project_db.sql
mysql -u root -p -e "SHOW TABLES IN test_restore;"
mysql -u root -p -e "DROP DATABASE test_restore;"
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
