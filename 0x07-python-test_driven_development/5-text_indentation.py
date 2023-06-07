#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module have a function that prints a text with 2 new lines
after each of these characters: ., ? and :
prototype: def text_indentation(text):

"""


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    text must be a string, otherwise raise a TypeErrorexception with the
    message text must be a string
    There should be no space at the beginning or the end of each printed line
    Do not allowed to import any module

    Args:
        text: text to modify

    Raises:
        TypeError: text must be a string

    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    i = 0
    new_str = ""
    while i < len(text):
        if text[i] == ' ' and i == 0:
            while text[i] == ' ':
                i += 1
        if text[i] in '.?:':
            new_str += text[i]
            new_str += '\n'
            new_str += '\n'
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        if i < len(text) and text[i] not in '.?:':
            new_str += text[i]
            i += 1
    print(new_str, end="")
