#!/usr/bin/python3
"""Min operation to print n of H"""


def minOperations(n):
    """Min Operation"""
    if n <= 1:
        return 0
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        min_copy_past = dp[i // 2] + 2
        min_past_prev = dp[i - 1] + 1
        dp[i] = min(min_copy_past, min_past_prev)
    return dp[n]
