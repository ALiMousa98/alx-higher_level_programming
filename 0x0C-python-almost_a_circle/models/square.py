#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
Class Square that inherits from Rectangle
Base is a super class

"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.width))

    @property
    def size(self):
        """property to retrieve private instance size"""
        return (self.width)

    @size.setter
    def size(self, size):
        """to set private instance size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            my_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if i < len(my_list):
                    setattr(self, my_list[i], args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dicti = {'id': self.id, 'size': self.width,
                 'x': self.x, 'y': self.y}
        return dicti
