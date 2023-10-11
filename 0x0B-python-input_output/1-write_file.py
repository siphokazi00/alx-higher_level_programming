#!/usr/bin/python3
"""Def func that wr str to txtfile and returns no. of chars written"""


def write_file(filename="", text=""):
    """Writes a text file and returns number of chars written.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write the file.
    Returns:
        The number of chars written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
