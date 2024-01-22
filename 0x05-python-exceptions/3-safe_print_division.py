#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns THE division of A by B"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
