#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    l = len(list_of_integers)

    if l == 0:
        return None

    m = l // 2

    if (m == l - 1 or list_of_integers[m] >= list_of_integers[m + 1]) and \
       (m == 0 or list_of_integers[m] >= list_of_integers[m - 1]):
        return list_of_integers[m]

    if m != l - 1 and list_of_integers[m + 1] > list_of_integers[m]:
        return find_peak(list_of_integers[m + 1:])

    return find_peak(list_of_integers[:m])
