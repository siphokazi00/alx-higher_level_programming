#!/bin/bash
# Gets the size of the response body in bytes
url="$1"; curl -sI "$url" | grep -i "Content-Length" | awk '{print $2}'
