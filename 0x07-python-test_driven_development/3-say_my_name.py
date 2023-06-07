#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module have a function that prints My name is <first name> <last name>
prototype: def say_my_name(first_name, last_name=""):

"""


def say_my_name(first_name, last_name=""):
    """ function that prints My name is <first name> <last name>

    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message first_name must be a string
    or last_name must be a string
    Do not allowed to import any module

    Args:
        first name: first parameter
        lasta name: second parameter

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
