#!usr/bin/env python3
# This script aims to add up all the even terms of the Fibonacci sequence


def fibb(limit: int):
    x = 1
    y = 2
    z = 0
    result = 2  # remember because the second position is 2 to begin with
    while z < limit:
        z = x + y
        x = y
        y = z
        if z % 2 == 0 and z <= limit:
            result += z
    return result


print(fibb(4000000))
