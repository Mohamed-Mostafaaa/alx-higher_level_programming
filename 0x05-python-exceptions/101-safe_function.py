#!/usr/bin/python3
import sys

def safe_function(func, *args):
    """Executes a function safely.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to func.
    """
    try:
        result = func(*args)
        return result
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return None
