#!/usr/bin/python3
"""
    Takes in URL, sends req to it and displays response body.
"""
import requests
import sys


def fetch_url_content(url):
    """
    Fetches the content of a URL and displays it.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    target_url = sys.argv[1]
    response_body = fetch_url_content(target_url)
    print(response_body)
