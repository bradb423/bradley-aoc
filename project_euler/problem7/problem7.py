# this script wants to find the 10001st prime

def find_nth_prime(n):
    """aims to find the nth prime number
    should be sufficient to generate a list of primes and test each value
    to see if they are divisible by any of the existing primes

    Args:
        n ([int]): [whichprime you want eg: 1st, 2nd etc]
    """
    # initialise with the first prime number
    step = 3
    prime_list = [2]
    while len(prime_list) < n:
        count = 0
        for prime in prime_list:
            if step%prime == 0:
                count += 1
        if count == 0:
            prime_list.append(step)
        step += 1
    return prime_list[-1]

# print(find_nth_prime(10001))

# this code is not the most efficient, i will come back to this later and speed it up