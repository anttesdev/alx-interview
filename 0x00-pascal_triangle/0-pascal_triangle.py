#!/usr/bin/python3
"""
This an implementation of the pascal triangle
"""


def pascal_triangle(n):
    """
    Generates a list of lists representing Pascal's Triangle of size n.

    Args:
    n: The number of rows in the triangle.

    Returns:
    A list of lists containing the Pascal's Triangle.
    An empty list if n is less than or equal to 0.
    """

    if n <= 0:
        return []

    pascal_t = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal_t[i - 1][j - 1] + pascal_t[i - 1][j])
        row.append(1)
        pascal_t.append(row)

    return pascal_t
