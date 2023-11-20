#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return ret
