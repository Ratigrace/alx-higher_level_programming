#!/usr/bin/python3
'''A script that runs python'''


class Square:
    '''Defining a class Square'''

    def __init__(self, size=0):
        '''Initializing a new square.

        Args:
        size (int): The size of each side of the new square.
        '''
        self.size = size

    @property
    def size(self):
        '''Geting the current size of the square.'''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the current area of the square.'''
        return (self.__size * self.__size)