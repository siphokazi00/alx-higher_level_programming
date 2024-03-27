#/bin/bash
# Send JSON POST req to URL passed as first arg
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
