#!/usr/bin/python3
"""square"""


class Square:
    """square"""

    def __init__(self, size=0):
        """initializing class
        args: size
        raises: Type and value errors
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        7sb missa7a dyal morba3
        return: lmissa7a li7sbti
        """

        return (self.__size ** 2)
