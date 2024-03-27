#!/bin/bash
# Sends req to URL passed as arg, display response status code only
url="$1"; curl -s -o /dev/null -w "%{http_code}" "$url"
