#!usr/bin/env python3
from functools import reduce
from itertools import permutations


def sum_of_divisors(n: int):
    return (
        sum(
            set(
                reduce(
                    list.__add__,
                    ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
                )
            )
        )
        - n
    )


# perfect number: n = sum_of_divisors(n) eg: 28
# abundant number: n < sum_of_divisors(n) eg: 12
# deficient number: n > sum_of_divisors(n)

# all numbers above 28123 are a sum of two abundant numbers
# so find all the values that are not the sum of two abundant numbers


def is_abundant(n: int):
    return n < sum_of_divisors(n)


def find_abundant(limit: int):
    abundant_list = []
    for i in range(1, limit):
        if is_abundant(i):
            abundant_list.append(i)
    return abundant_list


def sum_of_abundants(abundant_list, limit):
    permutation_list = list(permutations(abundant_list, 2))
    sums = [sum(x) for x in permutation_list]
    sums = set(sums)
    sums = [x for x in sums if x < limit]
    return sums


def not_sum_of_abundant(limit: int, sums: list):
    not_abundant_sum = 0
    for i in range(1, limit):
        if i not in sums:
            not_abundant_sum += i
    return not_abundant_sum


# Note: why is this consistently 64 more than what it should be?
def main():
    limit = 28123
    abundant_list = find_abundant(limit)
    sums = sum_of_abundants(abundant_list, limit)
    print(not_sum_of_abundant(limit, sums))


if __name__ == "__main__":
    main()
