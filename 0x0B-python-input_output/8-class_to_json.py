#!/usr/bin/python3
"""Defines a func that returns the dictionary descr for json object"""


def class_to_json(obj):
    """Returns dict descr w simple data structure"""
    # Get the attributes of the object
    obj_attrs = obj.__dict__

    # Filter out attributes that are not serializable
    serializable_attrs = {k: v for k, v in obj_attrs.items()
                          if isinstance(v, (list, dict, str, int, bool))}

    # Include the class name
    serializable_attrs['__class__'] = obj.__class__.__name__

    return serializable_attrs
