#!usr/bin/env python3
# this script aims to find the longest collatz sequence in the first million values


def collatz_sequence(n):
    """For a given value n, this function calculates thelength of the
    associated collatz sequence

    Args:
        n ([int]): [The starting point of the sequence]

    Returns:
        [count]: [The length of the associated collatz sequence]
    """

    count = 1
    while n != 4:  # easier here to stop at 4 rather than 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1

    return count + 2  # for the final two steps, 2...1


def longest_sequence(N):
    """Takes an upper bound N, and finds the longest collatz sequence below that number

    Args:
        N ([int]): [The upper bound to look below]

    Returns:
        [largest]: [The starting vlaue that yields the longest sequence]
    """
    longest_sequence_length = 1
    for i in range(3, N + 1):
        sequence_length = collatz_sequence(i)
        if sequence_length > longest_sequence_length:
            longest_sequence_length = sequence_length
            starting_number = i
    return starting_number


print(longest_sequence(1000000))
