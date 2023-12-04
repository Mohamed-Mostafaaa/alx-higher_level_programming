#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks obj's class matches a_class.

    Returns:
        True if obj's class exactly matches a_class.
        False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
