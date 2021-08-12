import hashlib as h
import itertools as iter

first_part = "ckczppom"

# need to find the lowest number to add to the input so that the has has five zeros
def lowest_value(first_part):
    for i in iter.count(1): # feels better than doing a while loop
        # add the strings, encode them, run them through the hash and check it starts with five zeros
        if h.md5(first_part.encode()+str(i).encode()).hexdigest().startswith("00000"):
            return i

# print(lowest_value(first_part))

def six_zeroes(first_part):
    for i in iter.count(1):
        if h.md5(first_part.encode()+str(i).encode()).hexdigest().startswith("000000"):
            return i

print(six_zeroes(first_part))