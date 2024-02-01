#!/usr/bin/python3
"""Making change"""


def make_change(coins, total):
    """Making change
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_idx >= num_coins:
            return -1

        if remaining_amount >= sorted_coins[coin_idx]:
            remaining_amount -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
