#!usr/bin/env python3
# find the largest value of d<1000 that gives the longest reciprocal cycle
# The reciprocals generally appear when diving by a multiple of a prime
# perhaps there's a way of factoring that into it?
# max reciprocal length of d is d-1
# eg: 1/7 has a length of 7-1=6
# maybe there is something to do with the remainder

import numpy as np

# first let's generate the prime numbers
def sieve(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i * i :: i] = False
    return np.flatnonzero(flags)


# turns out there's a neat algorithm for this, let's code it
# the algorithm can be found by researching full reptend primes
# where 10^k % p == 1 and k = p-1
def reciprocal_length(d):
    length = 1
    while (10**length)%d != 1:
        length +=1
        if length > d:
            return 0 # probably not worth looking at if it's not a reptend prime
    return length

def longest_reciprocal(prime_sieve):
    final_d_value = 1
    longest_length = 1

    for d in prime_sieve:
        length = reciprocal_length(d)
        if length > longest_length:
            longest_length = length
            final_d_value = d
    

    return final_d_value, longest_length

def main():
    limit = 1000
    prime_sieve = sieve(limit)
    print(longest_reciprocal(prime_sieve))

if __name__ == '__main__':
    main()

