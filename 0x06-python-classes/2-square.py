#!/usr/bin/python3
"""Python executing script"""


class Square:
    """Defining a class square."""

    def __init__(self, size=0):
        """Initializing a new Square.

        Args:
        size (int): The size of each side of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
