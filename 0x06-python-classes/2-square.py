#!/usr/bin/python3
"""defines a square """


class Square:
    """ square with private instance attribute size """

def __inint__(self, size=0):
    """
    Args:
        size: size of a square
    """

    if type(size) is int:
        if size < 0:
            raise ValueError('size must be an >= 0')
        else:
            self.__size = size
    else:
        raise TypeError('size must be an integer')
