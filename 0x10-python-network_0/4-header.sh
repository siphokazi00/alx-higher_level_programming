#!/bin/bash
# Takes URL as arg, sends GET req to it and displays response body
url="$1"; curl -s -H "X-School-User-Id: 98" "$url"
