#!/bin/bash

# Destination directory
dst = "/home/ubuntu/apps/class-notes/pb/pb_public"

# Show a message to the user
echo "Starting the process..."

# Show the commands being run
echo "1. Deleting everything inside the '$dst' folder"
rm - rf "$dst"/*

echo "2. Copying the './images' folder to '$dst'"
cp - r ./images "$dst"

echo "3. Copying the './subjects' folder to '$dst'"
cp - r ./subjects "$dst"

# Success
echo "Process completed successfully!"
