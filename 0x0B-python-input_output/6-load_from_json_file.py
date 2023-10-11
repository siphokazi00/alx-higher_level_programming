#!/usr/bin/python3
"""Defines a func that creates an object from json file"""

import json


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)
