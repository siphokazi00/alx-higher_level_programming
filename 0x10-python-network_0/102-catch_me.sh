#!/bin/bash
# Makes a req to 0.0.0.0:5000/catch_me
HTTP_CODE=$(curl --write-out "%{http_code}\\n" "http://0.0.0.0:5000/catch_me")

if [[ "$HTTP_CODE" -eq 200 ]]; then
    echo "You got me!"
else
    echo "Oops, something went wrong!"
fi
