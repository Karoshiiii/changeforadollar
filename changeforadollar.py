# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 17:16:58 2023

@author: sherr
"""

def count_ways_to_make_change(amount):
    ways = [0] * (amount + 1)
    ways[0] = 1

    coins = [1, 5, 10, 25, 50]  # Exclude the 100 cent coin

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]

amount = 100
num_ways = count_ways_to_make_change(amount)
print("Number of ways to make change for $1.00:", num_ways)