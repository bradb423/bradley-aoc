#!usr/bin/env python3
# need  to find a quadratic formula for which it generates the largest number of primes
# and then get the product of the coefficients

import numpy as np

# first let's check if a value is prime
def is_prime(x: int):
    try:
        lower_bound = int(x ** 0.5)
    except TypeError:
        return False # return false if the result of the quadratic is negative (it's not prime)
    count = 0
    for i in range(2, lower_bound + 1):
        if x % i == 0:
            return False
    if count == 0:
        return True


def quadratic(a: int, b: int, n: int):
    x = n ** 2 + (a * n) + b
    return x


def find_best_product_of_a_and_b():
    longest_n = 0
    for a in range(-1000, 1000 + 1):
        for b in range(-1000, 1000 + 1):
            n = 0
            while is_prime(quadratic(a, b, n)):
                n += 1
            if n > longest_n:
                longest_n = n
                best_product = a * b
    return best_product


def main():
    print(find_best_product_of_a_and_b())


if __name__ == "__main__":
    main()
