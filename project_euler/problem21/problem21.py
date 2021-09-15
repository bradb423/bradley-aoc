#!usr/bin/env python3
from functools import reduce

def sum_of_divisors(n):
    return sum(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n



def sum_of_amicables(n):
    amicables_list = []
    # n here is the upper limit that we will find amicable numbers under
    for i in range(3,n+1):
        possible_pair = sum_of_divisors(i)
        if possible_pair != i:
            if sum_of_divisors(possible_pair) == i:
                amicables_list.append((i,possible_pair))
    amicables_list = list(set(amicables_list))
    amicables_list = [sum(x) for x in amicables_list]
    return sum(set(amicables_list))


print(sum_of_amicables(10000))
