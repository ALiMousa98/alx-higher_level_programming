#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(list): List of integers to find peak of
    Returns: Peak element or None if not found
    """
    ln = len(list_of_integers)

    # Handle base cases
    if ln == 0:
        return None
    if ln == 1:
        return list_of_integers[0]
    if ln == 2:
        if list_of_integer[0] > list_of_integer[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    mid = ln // 2

    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
