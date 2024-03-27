#!/bin/bash
# Sends req to URL passed as arg, displays response status code
url="$1" | curl -s -o /dev/null -w "%{http_code}" "$url"
