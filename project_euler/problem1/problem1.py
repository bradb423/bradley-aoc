#!usr/bin/env python3
# This script aims to find the sum of all multiples of 3 or 5 below 1000


def sum_three_five(n: int):
    count = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


print(sum_three_five(1000))
