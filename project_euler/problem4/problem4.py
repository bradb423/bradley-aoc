def is_palindrome(x):
    strx = str(x)
    rev_strx = strx[::-1]
    if rev_strx == strx:
        return True
    else:
        return False


def largest_palindrome(n):
    # n here is the order of magnitude
    largest = 1
    for x in range(10 ** (n - 1), 10 ** n):
        for y in range(10 ** (n - 1), 10 ** n):
            z = x * y
            if is_palindrome(z):
                if z > largest:
                    largest = z
    return largest


largest_palindrome(3)
