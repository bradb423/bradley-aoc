# this should sum the digits of 2**1000
def sumdigits(n):
    return sum(map(int, str(n)))


print(sumdigits(2 ** 1000))
