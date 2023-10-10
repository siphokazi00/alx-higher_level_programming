#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


class BaseGeometry:
    """Represent a rectangle using a BaseGeometry."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represent a rectangle using a BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
