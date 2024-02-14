#!/usr/bin/python3
"""
Defines isWineer
"""


def isWinner(x, nums):
    """Determines the winner of multiple rounds of the prime number game."""

    if x is None or nums is None or x == 0 or nums == []:
        return None
    maria_count = ben_count = 0
    for n in nums:
        prime_list = []
        sieve = [True] * (n + 1)
        for p in range(2, n + 1):
            if sieve[p]:
                prime_list.append(p)
                for i in range(p, n + 1, p):
                    sieve[i] = False

        if len(prime_list) % 2 == 0:
            ben_count += 1
        else:
            maria_count += 1
    if maria_count > ben_count:
        return 'Maria'
    elif ben_count > maria_count:
        return 'Ben'
    return None
