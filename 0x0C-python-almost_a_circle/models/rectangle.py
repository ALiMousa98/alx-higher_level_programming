#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class Rectangle that inherits from Base

"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.validate_int(width, 'width')
        self.validate_int(height, 'height')
        self.validate_int(x, 'x')
        self.validate_int(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """property to retrieve private instance width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """to set private instance width"""
        self.validate_int(width, 'width')
        self.__width = width

    @property
    def height(self):
        """property to retrieve private instance height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """to set private instance height"""
        self.validate_int(height, 'height')
        self.__height = height

    @property
    def x(self):
        """property to retrieve private instance x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """to set private instance x"""
        self.validate_int(x, 'x')
        self.__x = x

    @property
    def y(self):
        """property to retrieve private instance y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """to set private instance y"""
        self.validate_int(y, 'y')
        self.__y = y

    def validate_int(self, value, arg):
        """method to validate if is integer and > 0"""
        if type(value) is not int:
            raise TypeError(arg + ' must be an integer')
        if arg not in ('x', 'y'):
            if value <= 0:
                raise ValueError(arg + ' must be > 0')
        else:
            if value < 0:
                raise ValueError(arg + ' must be >= 0')

    def area(self):
        """ return rectangel area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle with # symbol"""
        new_str = ""
        for i in range(self.__y):
            new_str += '\n'
        for i in range(self.__height):
            for i in range(self.__x):
                new_str += ' '
            for j in range(self.__width):
                new_str += '#'
            print(new_str)
            if i in range(self.__height - 1):
                new_str += '\n'
            new_str = ""

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' +
                str(self.__y) + ' - ' + str(self.__width) + '/' +
                str(self.__height))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            my_list = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                if i < len(my_list):
                    setattr(self, my_list[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dicti = {'id': self.id, 'width': self.__width, 'height': self.__height,
                 'x': self.__x, 'y': self.__y}
        return dicti
