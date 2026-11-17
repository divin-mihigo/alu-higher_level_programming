#!/usr/bin/python3
"""Module that defines the class Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width: the width of the rectangle (positive integer).
            height: the height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
