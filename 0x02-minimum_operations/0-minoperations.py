#!/usr/bin/python3
"""Min operation to print n of H"""


def minOperations(n, curr=2, topast=1, op=2):
    """Min Operation"""
    if n <= 1:
        return 0
    if curr >= n:
        return op
    return min(minOperations(n, curr + curr, curr, op + 2),
               minOperations(n, curr + topast, topast, op + 1))
