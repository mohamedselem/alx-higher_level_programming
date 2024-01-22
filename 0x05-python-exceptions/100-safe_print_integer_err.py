#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Print Integer with "{:d}".format().

    If  ValueError message is present, a corresponding
    message is printed to explain error.

    Args:
        value (int): The integer to be printed.

    Returns:
        If a TypeError or ValueError happens - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
