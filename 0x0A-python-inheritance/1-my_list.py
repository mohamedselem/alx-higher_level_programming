#!/usr/bin/python3
"""Defines  inherited liist class MyList."""


class MyList(list):
    """Implements sorted printing for the built_in list class."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
