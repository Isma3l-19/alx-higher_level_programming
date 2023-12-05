#!/usr/bin/python3

"""defines Pascal's triangle function"""


def pascal_triangle(n):
    """n represents the size of pascal's triangle

    Returns:
        list of integers represnting the triangle
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        trii = tri[-1]
        tmp = [1]
        for i in range(len(trii) -1):
            tmp.append(trii[i] + trii[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
