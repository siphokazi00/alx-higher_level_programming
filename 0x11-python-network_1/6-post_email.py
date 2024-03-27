#!/usr/bin/python3
"""
    Takes in URL and email address, send POST req to it with email as param.
"""
import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the given email parameter.
    """
    try:
        payload = {'email': email}
        response = requests.post(url, data=payload)
        return response.text
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    target_url = sys.argv[1]
    user_email = sys.argv[2]
    response_body = send_post_request(target_url, user_email)
    print(response_body)
