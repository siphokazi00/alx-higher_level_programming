#!/bin/bash
# Makes a req to 0.0.0.0:5000/catch_me
curl -s -X PUT -d "status=You got me!" 0.0.0.0:5000/catch_me >/dev/null
