#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
3-rectangle.py: has a class Rectangle that defines a rectangle

"""


class Rectangle:
    """Class Rectangle that defines a Rectangle
    Attributes:
        width: width of Rectangule
        height: height of rectangule

    """

    def __init__(self, width=0, height=0):
        """Initializer with default width and height equal 0"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retrieve private instance width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """to set private instance width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """property to retrieve private instance height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set private instance height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """public instance method that returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """public instance method that returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """str instance method that returns the rectangule to print with # """
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return (new_str)
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += '#'
                if i in range(self.__height - 1):
                    new_str += '\n'
            return (new_str)

    def __repr__(self):
        """repr instance method returns string representation of rectangule """
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)
