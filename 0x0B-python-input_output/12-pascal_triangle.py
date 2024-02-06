#!/usr/bin/python3
"""Defines Pascal's Triangle function."""


def pascal_triangle(z):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if z <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != z:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
