#!/usr/bin/python3
"""1-Rectangle"""


class Rectangle:
    """Rectangle(width, height)"""

    def __init__(self, width=0, height=0):
        """Rectangle __init__"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        new_list = ""
        for row in range(self.__height):
            for col in range(self.__width):
                new_list += "#"
            new_list += "\n"
        return new_list[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
