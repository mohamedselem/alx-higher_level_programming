#!/usr/bin/python3
"""Module for matrix divided method."""


def matrix_divided(matrix, div):
    """Divides THE elements of matrix by div.
    Args:
        matrix: List of the lists contain int or float.
        div: numbers to the divide matrix by.
    Returns:
        list: List of the lists Represent the divided matrix.
    Raises:
        TypeError: If matrix is not list contains int or float.
        TypeError: If sublists sizes are not equals.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is Zer0.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("the div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("the matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("each row of the matrix must have Same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
