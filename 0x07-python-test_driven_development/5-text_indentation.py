#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding TWO lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
