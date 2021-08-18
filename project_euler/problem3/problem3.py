# need to find the largest prime factor of a number


def is_prime(x: int):
    lower_bound = int(x ** 0.5)
    count = 0
    for i in range(2, lower_bound + 1):
        if x % i == 0:
            return False
            break
    if count == 0:
        return True


def largest_prime_factor(n: int):
    sqrt = int(n ** 0.5)
    largest = 1
    if is_prime(n):
        return n
    for i in range(2, sqrt + 1):
        if n % i == 0:
            if is_prime(i):
                if i > largest:
                    largest = i
    return largest


print(largest_prime_factor(600851475143))
