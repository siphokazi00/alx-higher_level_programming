#!/usr/bin/python3
"""Defines a function that returns a list of lists of ints"""


def print_triangle(triangle):
    """Represents Pascal's Triangle of size n."""

    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
