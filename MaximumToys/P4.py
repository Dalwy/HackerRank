import os
import sys


def maximumToys(prices, k):
    prices.sort()
    i = 0
    while k > 0:
        k -= prices[i]
        i += 1
    return i - 1

if __name__ == '__main__':
    ar = [1, 12, 5, 111, 200, 1000, 10]
    result = maximumToys(ar, k=50)
    print(str(result) + '\n')
