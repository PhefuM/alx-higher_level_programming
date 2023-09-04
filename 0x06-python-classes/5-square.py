#!/usr/bin/python3
"""Square module that has a class to create square object."""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the nescessary attributes for the square object

        Args:
            size (int): size of a square.

        """
        self.size = size

        @property 
	def size(self, value):
            """Get or set the size of the square."""
        return self.__size

        @size.setter
        def size(self, value):
            if type(value) is int:
                if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
	else:
	    raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character `#`."""
        if self.__size > 0:
            for x in range(self.__size):
		print('#' * self.__size)
        else:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
