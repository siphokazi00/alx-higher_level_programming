#!/usr/bin/python3
"""
    Takes in URL, send rew to it and displays value of X-Request_Id
"""
import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches the X-Request-Id header value from the specified URL.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get("X-Request-Id")
        if x_request_id:
            return x_request_id
        else:
            return "X-Request-Id header not found in the response."
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    target_url = sys.argv[1]
    x_request_id_value = fetch_x_request_id(target_url)
    print(x_request_id_value)
