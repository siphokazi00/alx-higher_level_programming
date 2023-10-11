#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string at end of file and returns no. of chars added."""
    with open(filename, "a", encoding="utf-8"):
        return file.write(text)
