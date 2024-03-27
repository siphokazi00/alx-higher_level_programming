#!/usr/bin/python3
"""
    Takes 2 args, and lists 10 commits (from most recent) of the repo "rails"
"""
import requests
import sys


def get_recent_commits(owner, repo):
    """
    Fetches the 10 most recent commits from the specified repository.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()
        return commits[:10]
    except requests.RequestException as e:
        print(f"Error fetching commits: {e}")
        sys.exit(1)


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    recent_commits = get_recent_commits(owner_name, repo_name)

    for commit in recent_commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")
