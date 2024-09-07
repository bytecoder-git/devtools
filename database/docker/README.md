# Database Docker Installation Scripts

This repository contains two bash scripts for easily installing SQL Server and PostgreSQL in Docker containers. These scripts provide a convenient way to quickly set up database environments for development or testing purposes.

## Scripts

1. `install_sqlserver.sh`: Installs Microsoft SQL Server in a Docker container.
2. `install_postgres.sh`: Installs PostgreSQL in a Docker container.

## Prerequisites

- Docker installed on your system
- Bash shell

## Usage

### SQL Server Installation

```bash
./install_sqlserver.sh -p <password> [OPTIONS]
```

Options:
- `-p, --password PASSWORD`: Set the SQL Server SA password (required)
- `-d, --data-path PATH`: Set the local data path (default: /path/to/your/data/directory)
- `-n, --name NAME`: Set the container name (default: sql-server-container)
- `-i, --image IMAGE`: Set the SQL Server image (default: mcr.microsoft.com/mssql/server:2022-latest)
- `--port PORT`: Set the SQL Server port (default: 1433)
- `-h, --help`: Display help message

Example:
```bash
./install_sqlserver.sh -p MySecurePassword123! -d /mnt/data/sqlserver -n my-sqlserver --port 14333
```

### PostgreSQL Installation

```bash
./install_postgres.sh -p <password> [OPTIONS]
```

Options:
- `-p, --password PASSWORD`: Set the PostgreSQL password (required)
- `-u, --user USER`: Set the PostgreSQL user (default: postgres)
- `-db, --database DB`: Set the PostgreSQL database name (default: mydatabase)
- `-d, --data-path PATH`: Set the local data path (default: /path/to/your/postgres/data)
- `-n, --name NAME`: Set the container name (default: postgres-container)
- `-i, --image IMAGE`: Set the PostgreSQL image (default: postgres:15)
- `--port PORT`: Set the PostgreSQL port (default: 5432)
- `-h, --help`: Display help message

Example:
```bash
./install_postgres.sh -p MySecurePassword123! -u myuser -db mydb -d /mnt/data/postgres -n my-postgres --port 5433
```

## Features

- Easy installation of SQL Server or PostgreSQL in Docker containers
- Customizable configuration options
- Automatic creation of data directories
- Verification of successful container startup
- Sample data insertion (for PostgreSQL)

## License

MIT License

Copyright (c) 2024 Bill Heyman (bill@bytecoder.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.