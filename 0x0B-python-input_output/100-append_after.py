#!/usr/bin/python3
"""Defines a fucntion that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given str in a file."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

    except FileNotFoundError:
        pass  # File not found, do nothing


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
