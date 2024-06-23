#!/bin/bash

# Run the docker container
# Usage: ./run.sh <directory_path> <option_arguments>

# Check if the docker image already exists
if [ "$(docker images -q demake-finder)" ]; then
    echo "Docker image already exists. Skipping build."
else
    # Build the docker image
    echo "Building the docker image..."
    # Check if the docker image is built successfully
    if ! docker build -t demake-finder .; then
        echo "Failed to build the docker image."
        exit 1
    fi
fi

# Check if the docker container already exists
if [ "$(docker ps -aq -f name=run-df)" ]; then
    # If it exists, restart the container
    echo "Restarting the docker container..."
    if ! docker restart run-df; then
        echo "Failed to restart the docker container."
        exit 1
    fi
else
    # If it does not exist, run the docker container
    echo "Running the docker container..."
    if ! docker run -it --name run-df demake-finder "$1" "$2"; then
        echo "Failed to run the docker container."
        exit 1
    fi
fi
