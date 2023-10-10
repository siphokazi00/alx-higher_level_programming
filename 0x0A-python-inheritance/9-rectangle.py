#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Return the area of the rectangle"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init(self, width, height):
        """Initialize a new Rectangle"""

        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.height)
