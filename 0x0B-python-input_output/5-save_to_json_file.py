#!/usr/bin/python3
"""Defines a func that writes an object to a text file using json."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
