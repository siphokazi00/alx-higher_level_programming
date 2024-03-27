#!/bin/bash
# Takes URL, sends POST req to it and displays response body
url="$1"; email="test@gmail.com"; subject="I will always be here for PLD"; curl -s -X POST -d "email=$email&subject=$subject" "$url"
