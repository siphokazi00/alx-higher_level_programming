#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.info()
            x_request_id = headers.get("X-Request-Id")
            if x_request_id:
                print(x_request_id)
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print("Error fetching URL:", e.reason)
