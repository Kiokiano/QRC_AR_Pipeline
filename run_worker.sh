#!/bin/bash
# run_worker.sh - Simple polling listener for incoming GLB files

WATCH_DIR="incoming"
PROCESSED_DIR="processed"

echo "Pipeline worker started. Watching $WATCH_DIR..."

while true; do
    for file in "$WATCH_DIR"/*.glb; do
        if [ -e "$file" ]; then
            echo "Processing $(basename "$file")..."
            blender -b -P scripts/process_helmet.py -- "$file"
            mv "$file" "$PROCESSED_DIR/"
            echo "Done."
        fi
    done
    sleep 5
done
