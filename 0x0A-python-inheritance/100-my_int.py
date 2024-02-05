#!/usr/bin/python3
"""Defines Class My Int that inherits from integar."""


class MyInt(int):
    """Invert int OPERATORS == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
