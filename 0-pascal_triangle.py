#!/usr/bin/python3


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.

    Args
        n(int): number of rows in pascal_triangle
    """
    res = [[1]]

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)

    return res
