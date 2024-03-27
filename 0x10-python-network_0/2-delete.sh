#!/bin/bash
# Sends DELETE req to URL passed as arg
url="$1"; curl -s -X DELETE "$url"
