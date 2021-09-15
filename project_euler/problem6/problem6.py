#!usr/bin/env python3
# this script finds the difference between the sum of squares and the square of the su


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6


def square_of_sum(n):
    return ((n ** 2) * (n + 1) ** 2) / 4


def difference_of_squares(n):
    return int(square_of_sum(n) - sum_of_squares(n))


print(difference_of_squares(100))
