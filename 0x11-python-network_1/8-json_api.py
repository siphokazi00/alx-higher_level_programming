#!/usr/bin/python3
"""
    Takes in a letter and sends POST req to http://0.0.0.0:5000/search_user
"""
import requests
import sys


def search_user_by_letter(letter):
    """
    Sends POST req to http://0.0.0.0:5000/search_user with given letter.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            user_id = data.get('id')
            user_name = data.get('name')
            return f"[{user_id}] {user_name}"
        else:
            return "No result"
    except ValueError:
        return "Not a valid JSON"
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    letter_to_search = sys.argv[1] if len(sys.argv) > 1 else ""
    result = search_user_by_letter(letter_to_search)
    print(result)
