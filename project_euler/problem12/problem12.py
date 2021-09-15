#!usr/bin/env python3
# need to find the first triangle number to have 500 divisors
import itertools as iter
from functools import reduce


# look for the fastest method to get divisors, it's a fairly simple problem i have done many times before
# best i found is here: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def how_many_divisors(x):
    return len(
        set(
            reduce(
                list.__add__,
                ([i, x // i] for i in range(1, int(x ** 0.5) + 1) if x % i == 0),
            )
        )
    )


print(how_many_divisors(28))


def which_triangle_number(n):
    # n is the number of divisors required
    for i in iter.count(1):
        triangle = int(0.5 * (i) * (i + 1))
        if how_many_divisors(triangle) >= n:
            return triangle


print(which_triangle_number(500))
