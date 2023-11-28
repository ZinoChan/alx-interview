#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """returns the pascal triangle"""
    base = [[1], [1, 1]]

    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return base

    start = 2
    while start < n:
        array_to_push = [1]
        for i in range(1, start):
            array_to_push.append(base[start - 1][i - 1] + base[start - 1][i])
        base.append(array_to_push + [1])
        start += 1
    return base
