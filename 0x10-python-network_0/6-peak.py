#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    size = len(list_of_integers)

    if size == 0:
        return None

    m = size // 2

    if (m == size - 1 or list_of_integers[m] >= list_of_integers[m + 1]) and \
       (m == 0 or list_of_integers[m] >= list_of_integers[m - 1]):
        return list_of_integers[m]

    if m != size - 1 and list_of_integers[m + 1] > list_of_integers[m]:
        return find_peak(list_of_integers[m + 1:])

    return find_peak(list_of_integers[:m])
