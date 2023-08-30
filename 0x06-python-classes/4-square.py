#!/usr/bin/python3
"""Square module that has a class to create square object."""


class Square:
    """Represent a square
    Attributes:
        __size (int): size of a size of the square
    """
    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): Size of the new square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates  area of square.
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
      self.__size = value
