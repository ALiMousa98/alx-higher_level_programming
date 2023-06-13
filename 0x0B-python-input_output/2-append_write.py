#!/usr/bin/python3
"""
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    """


def append_file(filename="", text=""):
    """Return the char numbers of the contents of a UTF8 text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
