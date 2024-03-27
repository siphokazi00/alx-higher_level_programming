#!/usr/bin/python3
"""
    Takes in URL, send request to it and displays response in utf-8.
"""
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Fetches the content of a URL and displays it.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    target_url = sys.argv[1]
    response_body = fetch_url_content(target_url)
    print(response_body)
