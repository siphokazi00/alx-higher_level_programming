#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Override == operator with != behaviour."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return super().__eq__(other)
