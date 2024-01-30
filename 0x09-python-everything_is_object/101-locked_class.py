#!/usr/bin/python3
"""Defines tHE locked CLAass."""


class LockedClass:
    """
    Prevent a user from instantiate new LockedClass attributes
    for anything except attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
