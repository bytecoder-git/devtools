#!/bin/bash

# Function to display help
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Install PostgreSQL in a Docker container."
    echo
    echo "Options:"
    echo "  -p, --password PASSWORD    Set the PostgreSQL password (required)"
    echo "  -u, --user USER            Set the PostgreSQL user (default: postgres)"
    echo "  -db, --database DB         Set the PostgreSQL database name (default: mydatabase)"
    echo "  -d, --data-path PATH       Set the local data path (default: /path/to/your/postgres/data)"
    echo "  -n, --name NAME            Set the container name (default: postgres-container)"
    echo "  -i, --image IMAGE          Set the PostgreSQL image (default: postgres:15)"
    echo "  --port PORT                Set the PostgreSQL port (default: 5432)"
    echo "  -h, --help                 Display this help message"
}

# Default values
POSTGRES_PASSWORD=""
POSTGRES_USER="postgres"
POSTGRES_DB="mydatabase"
LOCAL_DATA_PATH="/path/to/your/postgres/data"
CONTAINER_NAME="postgres-container"
POSTGRES_IMAGE="postgres:15"
POSTGRES_PORT="5432"

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p|--password) POSTGRES_PASSWORD="$2"; shift ;;
        -u|--user) POSTGRES_USER="$2"; shift ;;
        -db|--database) POSTGRES_DB="$2"; shift ;;
        -d|--data-path) LOCAL_DATA_PATH="$2"; shift ;;
        -n|--name) CONTAINER_NAME="$2"; shift ;;
        -i|--image) POSTGRES_IMAGE="$2"; shift ;;
        --port) POSTGRES_PORT="$2"; shift ;;
        -h|--help) show_help; exit 0 ;;
        *) echo "Unknown parameter passed: $1"; show_help; exit 1 ;;
    esac
    shift
done

# Check if password is provided
if [ -z "$POSTGRES_PASSWORD" ]; then
    echo "Error: PostgreSQL password is required."
    show_help
    exit 1
fi

# Create the local directory for PostgreSQL data if it doesn't exist
sudo mkdir -p $LOCAL_DATA_PATH
sudo chown -R 1000:1000 $LOCAL_DATA_PATH

# Pull the PostgreSQL Docker image
sudo docker pull $POSTGRES_IMAGE

# Run the PostgreSQL container
sudo docker run -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
    -e POSTGRES_USER=$POSTGRES_USER \
    -e POSTGRES_DB=$POSTGRES_DB \
    -p $POSTGRES_PORT:5432 \
    -v $LOCAL_DATA_PATH:/var/lib/postgresql/data \
    --name $CONTAINER_NAME \
    -d $POSTGRES_IMAGE

# Wait for the container to start
echo "Waiting for PostgreSQL to start..."
sleep 10

# Check if the container is running
if [ "$(sudo docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "PostgreSQL is now running in Docker!"
    echo "Connection string: postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:$POSTGRES_PORT/$POSTGRES_DB"
    
    # Create a sample table and insert data
    echo "Creating a sample table and inserting data..."
    sudo docker exec -i $CONTAINER_NAME psql -U $POSTGRES_USER -d $POSTGRES_DB << EOF
CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(50));
INSERT INTO test_table (name) VALUES ('Test Data');
SELECT * FROM test_table;
EOF
else
    echo "Failed to start PostgreSQL container. Please check the logs:"
    sudo docker logs $CONTAINER_NAME
fi