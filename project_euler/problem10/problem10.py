# this script aims to find the sum of the primes below 2000000
limit = 2000000

# best to employ the seive of erastothenes here, becuase we're just finding primes up to a given limit
# so i looked online for the fastest one possible in python
# this came from: https://stackoverflow.com/questions/49936222/an-efficient-sieve-of-eratosthenes-in-python
import numpy as np


def sieve(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        # We could use a lower upper bound for this loop, but I don't want to bother with
        # getting the rounding right on the sqrt handling.
        if flags[i]:
            flags[i * i :: i] = False
    return np.flatnonzero(flags)


print(np.sum(sieve(limit)))
