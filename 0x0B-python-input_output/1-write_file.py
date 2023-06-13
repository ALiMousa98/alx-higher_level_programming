#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) and
   returns the number of characters written"""


def write_file(filename="", text=""):
    """Return the char numbers of the contents of a UTF8 text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

    return text
