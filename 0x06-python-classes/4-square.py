#!/usr/bin/python3
"""Square module that has a class to create square object."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
 	Args:
            size (int): Size of the new square.
	Raises:
            TypeError: if `size` is not an `int`.
            ValueError: If `size` is < 0.
        """
        if not isinstance(size), int):
           raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
	self.__size = size

   def area(self):
       """Get area of square.

       Returns:
           Area (`int`) : size * size.
       """
       return self.__size * self.__size

   @property
   def size(self):
       """:obj:int:Returns `size` of a square'

       Setter raise an `TyprError` if `value` is not int
       or raise `ValueError` if `value` < 0
       """
       return self.__size

  @size.setter
  def size(self, value):
      if not isinstance(value, int):
         raise TypeError("size must be an integer")
      if value < 0:
          raise ValueError("size must be >= 0")
      self.__size = value
