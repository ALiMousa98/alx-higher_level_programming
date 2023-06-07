#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module have a function that prints a square with the character #
prototype: def print_square(size):
"""


def print_square(size):
    """ function that prints a square with the character #

    size is the size length of the square
    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    if size is a float and is less than 0, raise a TypeError
    exception with the message size must be an integer
    Do not allowed to import any modue

    Args:
        size: size of the square

    Raises:
        TypeError: size must be an integer
        TypeError: size must be an integer
        ValueError: size must be >= 0

    """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size - 1):
            print("#", end="")
        print("#")
