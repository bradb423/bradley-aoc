#!usr/bin/env python3
# this script aims to find the pythoagroean triplet
# a^2 + b^2 = c^2
# with a+b+c = 1000

# wlog: a,b,c < 1000 and c = 1000-a-b so we can remove one loop
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(a * b * c)
# the above should print the answer out twice beacause of the two loops
