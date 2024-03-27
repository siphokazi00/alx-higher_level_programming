#!/usr/bin/bash
# Get the size of the response body in bytes
url="$1"
response_size=$(curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}')

echo "Response size: $response_size bytes"
