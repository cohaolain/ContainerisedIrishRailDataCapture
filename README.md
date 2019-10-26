# IrishRail Train Data Logger

## Setup

Here's everything you need to run this on your own.

### Prerequisites

-   Configured MySQL/PostgreSQL database
-   Python 3 if running without Docker
-   Can also be run using a Docker image

### Preparing the database

In the case of MySQL, to set up a server simply do the following:

```bash
λ sudo apt install mysql-server
```

followed by

```sql
mysql>  CREATE DATABASE irishrail_logger;
Query OK, 1 row affected (0.00 sec)

mysql>  CREATE USER irishrail_logger
        IDENTIFIED BY 'supersecretpassword';
Query OK, 0 rows affected (0.01 sec)

mysql>  GRANT ALL PRIVILEGES ON irishrail_logger.*
        to 'irishrail_logger'@'localhost';
Query OK, 0 rows affected, 1 warning (0.00 sec)
```

Then populate `.env` in the same format as `.sample_env` with your DB details.

-   If running with Docker, run `docker run --net=host --env-file=.env -d irishrail-logger`.
-   If running without Docker, run `python3 logger.py`.
