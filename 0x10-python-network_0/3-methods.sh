#!/bin/bash
# Takes URL and displays HTTP methods the server will accept
url="$1"; curl -sI "$url" | grep -i "^Allow:" | awk '{print $2}'
