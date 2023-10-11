#!/usr/bin/python3
"""Defines a func that returns an object rep'd by a json string"""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string."""
    return json.loads(my_str)
