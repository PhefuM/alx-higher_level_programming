#!/usr/bin/python3
"""Square module that has a class to create a square object."""


class Square:
    """An empty square class."""

    def __inint__(self, size=0):
	"""Init method for the square class.
    Args:
	size (:obj:'int', optional): size of a square.
     
    Raises:
	TypeError: if 'size' is not an 'int'.
	ValueError: if 'size is < 0.
    """
    if not isinstance(size, int):
	raise TypeError("size must be an integer")
    if size < 0:
	raise ValueError("size must be an integer")
    self.__size = size	
   
