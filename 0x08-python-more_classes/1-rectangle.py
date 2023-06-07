#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
1-rectangle.py: has a class Rectangle that defines a rectangle

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
