#!/bin/bash

# Run the docker container
# Usage: ./run.sh <directory_path> <option_arguments>

# Build the docker image
echo "Building the docker image..."

# Check if the docker image is built successfully
if ! docker build -t demake-finder .; then
    echo "Failed to build the docker image."
    exit 1
fi

# Run the docker container
echo "Running the docker container..."

# Check if the docker container is run successfully
if ! docker run -it --rm --name run-df demake-finder "$1" "$2"; then
    echo "Failed to run the docker container."
    exit 1
fi
