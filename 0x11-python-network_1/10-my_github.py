#!/usr/bin/python3
"""
    Takes GitHub credentials and uses GitHub API to display id
"""
import requests
import sys


def get_github_user_id(username, token):
    """
    Fetches GitHub user ID using Basic Authentication with a PAT.
    """
    try:
        url = "https://api.github.com/user"
        response = requests.get(url, auth=(username, token))
        data = response.json()
        return data.get("id")
    except requests.RequestException as e:
        return f"Error fetching user ID: {e}"


if __name__ == "__main__":
    github_username = sys.argv[1]
    personal_access_token = sys.argv[2]
    user_id = get_github_user_id(github_username, personal_access_token)
    print(user_id)
