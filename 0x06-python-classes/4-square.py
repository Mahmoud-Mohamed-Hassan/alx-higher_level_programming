#!/usr/bin/python3

"""Square Task"""


class Square:

    """ Empty """
    def __init__(self, size=0):
        """Exceptions are documented in the same way as classes.
        Attributes:
        size (int): Size of the Square.
    """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Exceptions are documented in the same way as classes.

    Attributes:
        self (obj): Area of the Square.
    """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method return The size value
    """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Exceptions are documented in the same way as classes.

    Attributes:
        size (int): Size of the Square.
    """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(value)
