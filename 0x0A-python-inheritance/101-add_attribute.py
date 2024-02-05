#!/usr/bin/python3


def add_attribute(obj, name, value):
    """ Function add new attribute if possible (object has __dict__()) """

    if not hasattr(obj, "__dict__"):
        msg = "can not add new attribute"
        raise TypeError(msg)
    setattr(obj, name, value)
