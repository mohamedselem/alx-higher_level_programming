#!/usr/bin/python3
"""Defines file Appending FUnction."""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text file.

    Args:
        filename (str): Name of the file to BE appended to.
        text (str): String to be appended to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
