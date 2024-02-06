#!/usr/bin/python3
"""Defines Text file reading function."""


def read_file(filename=""):
    """Print content of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
