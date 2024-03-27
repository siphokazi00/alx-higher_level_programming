#!/bin/bash
# Sends req to URL passed as arg, displays response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
