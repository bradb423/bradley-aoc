#!usr/bin/env python3
# find the sum of the digits in the number 100!
# use my answers to qs 15 and 16

from functools import lru_cache


@lru_cache(maxsize=None)
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


def sumdigits(n):
    return sum(map(int, str(n)))


print(sumdigits(fact(10)))
