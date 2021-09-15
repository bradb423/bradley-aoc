#!usr/bin/env python3
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def no_of_digits(x):
    return len(str(x))


def main():
    limit = 1000
    n = 3
    while no_of_digits(fibonacci(n)) < limit:
        n += 1
    print(n)


if __name__ == "__main__":
    main()
