#!/usr/bin/python3
"""Def func that wr str to txtfile and returns no. of chars written"""


def wrtie_file(filename="", text=""):
    """Writes a text file and returns number of chars written."""
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
