#!/usr/bin/python3
"""Define Object attributes lookup function."""


def lookup(obj):
    """Return the list of object's available attributes."""
    return (dir(obj))
