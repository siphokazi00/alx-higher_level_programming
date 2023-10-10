#!/usr/bin/python3
"""Defines an inherited class-checking funtion."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class."""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
