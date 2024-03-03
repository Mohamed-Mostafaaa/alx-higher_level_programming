#!/usr/bin/python3
""" Finds Peak values """


def find_peak(list_of_integers):
    """Find the peak"""
    list_l = len(list_of_integers)
    if list_l is 0:
        return None
    peak = binary_search(list_of_integers, 0, list_l - 1)
    return list_of_integers[peak]


""" binary search algorithim """


def binary_search(lis, fir, last):
    """Recursive binary search of the peak"""
    if fir >= last:
        return fir
    mid = ((last - fir) // 2) + fir
    if lis[mid] > lis[mid + 1]:
        return binary_search(lis, fir, mid)
    else:
        return binary_search(lis, mid + 1, last)
