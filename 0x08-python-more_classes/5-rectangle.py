#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.width = width
        self.height = height
   
    @property
    def width(self):
        """
        gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """
        gets the height of the rectangle
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value
    
    def area(self):
        """returns the are of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        return the printable representation of teh rectangle
        represents the rectangle w #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return("".join(rect))

    def __repr__(self):
        """
        Returns the string representation of the rectangle
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    
    def __del__(self):
        """
        prints a message for
        every deletion of 
        a rectangle
        """
        print("Bye rectangle...")
