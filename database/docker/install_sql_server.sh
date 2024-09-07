#!/bin/bash

# Function to display help
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Install SQL Server in a Docker container."
    echo
    echo "Options:"
    echo "  -p, --password PASSWORD    Set the SQL Server SA password (required)"
    echo "  -d, --data-path PATH       Set the local data path (default: /path/to/your/data/directory)"
    echo "  -n, --name NAME            Set the container name (default: sql-server-container)"
    echo "  -i, --image IMAGE          Set the SQL Server image (default: mcr.microsoft.com/mssql/server:2022-latest)"
    echo "  --port PORT                Set the SQL Server port (default: 1433)"
    echo "  -h, --help                 Display this help message"
}

# Default values
SQL_SERVER_PASSWORD=""
LOCAL_DATA_PATH="/path/to/your/data/directory"
CONTAINER_NAME="sql-server-container"
SQL_SERVER_IMAGE="mcr.microsoft.com/mssql/server:2022-latest"
SQL_SERVER_PORT=1433

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p|--password) SQL_SERVER_PASSWORD="$2"; shift ;;
        -d|--data-path) LOCAL_DATA_PATH="$2"; shift ;;
        -n|--name) CONTAINER_NAME="$2"; shift ;;
        -i|--image) SQL_SERVER_IMAGE="$2"; shift ;;
        --port) SQL_SERVER_PORT="$2"; shift ;;
        -h|--help) show_help; exit 0 ;;
        *) echo "Unknown parameter passed: $1"; show_help; exit 1 ;;
    esac
    shift
done

# Check if password is provided
if [ -z "$SQL_SERVER_PASSWORD" ]; then
    echo "Error: SQL Server password is required."
    show_help
    exit 1
fi

# Create the local directory for SQL Server data if it doesn't exist
sudo mkdir -p $LOCAL_DATA_PATH

# Pull the SQL Server Docker image
sudo docker pull $SQL_SERVER_IMAGE

# Run the SQL Server container
sudo docker run -e "ACCEPT_EULA=Y" \
    -e "MSSQL_SA_PASSWORD=$SQL_SERVER_PASSWORD" \
    -p $SQL_SERVER_PORT:1433 \
    -v $LOCAL_DATA_PATH:/var/opt/mssql \
    --name $CONTAINER_NAME \
    -d $SQL_SERVER_IMAGE

# Wait for the container to start
echo "Waiting for SQL Server to start..."
sleep 20

# Check if the container is running
if [ "$(sudo docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "SQL Server is now running in Docker!"
    echo "Connection string: Server=localhost,$SQL_SERVER_PORT;Database=master;User Id=sa;Password=$SQL_SERVER_PASSWORD"
else
    echo "Failed to start SQL Server container. Please check the logs:"
    sudo docker logs $CONTAINER_NAME
fi