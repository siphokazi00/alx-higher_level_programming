#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Reads a text file with UTF8 encoding and prints it to stdout."""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end"")
