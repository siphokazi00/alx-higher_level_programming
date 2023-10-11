#!/usr/bin/python3
"""Defines a func that returns JSON reps of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string."""
    return json.dumps(my_obj)
