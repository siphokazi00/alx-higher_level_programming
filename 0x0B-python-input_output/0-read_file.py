#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Reads a text file UTF8 and prints it to stdout."""

    with open('UTF8') as file:
        print(file.read())
