#!/usr/bin/python3
"""Defines file Writing function."""


def write_file(filename="", text=""):
    """Write  string to a UTF8 File.

    Args:
        filename (str): The name of file to be write.
        text (str): text to write to the file.
    Returns:
        The number of THE characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
