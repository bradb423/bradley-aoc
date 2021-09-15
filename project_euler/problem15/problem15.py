#!usr/bin/env python3
# this script aims to find the number of paths in a 20,20 grid

from functools import lru_cache


@lru_cache(maxsize=None)
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


# this is a fairly simple problem, and has a formula in combinatorics
# if i am right then it is: (2*n)!/(n!**2) for an n*n grid


def how_many_paths(n):
    return int(fact(2 * n) / (fact(n) ** 2))


print(how_many_paths(20))
