#!/bin/bash
# Takes URL, sends GET req to it and displays response body
url="$1"; curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q 200 && curl -s "$url"
