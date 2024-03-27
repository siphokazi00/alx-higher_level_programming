#!/usr/bin/env python3
"""
    Takes in URL and email, send POST request to it with email as parameter.
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email parameter.
    """
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        with urllib.request.urlopen(url, data=data) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        return f"Error fetching URL: {e.reason}"


if __name__ == "__main__":
    # Example usage:
    target_url = "http://0.0.0.0:5000/post_email"
    user_email = "hr@holbertonschool.com"

    response_body = send_post_request(target_url, user_email)
    print("Response body:")
    print(response_body)
