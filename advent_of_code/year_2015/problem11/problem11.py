import re

# condition 1
def straight_line_of_letters(password: str):
    count = 0
    for i in range(len(password) - 2):
        if (ord(password[i]) + 1 == ord(password[i + 1])) and (
            ord(password[i]) + 2 == ord(password[i + 2])
        ):
            count += 1
    if count >= 1:
        return True
    else:
        return False


# condition 2
def no_i_o_l(password: str):
    if ("i" in password) or ("o" in password) or ("l" in password):
        return False
    else:
        return True


# condition 3
def two_pairs(password: str):
    return bool(
        re.findall(r"^.*(.)\1.*(.)\2.*$", password)
    )  # the bool just checks that it has returned something, that being the two pairs


def is_it_valid(password: str):
    if (
        straight_line_of_letters(password)
        and no_i_o_l(password)
        and two_pairs(password)
    ):
        return True
    else:
        return False


def increment_password(password: str):
    # reverse the string
    # add one to the first character, if z, convert to a
    # and the next applies to the 2nd character and so on
    r = list(password)[::-1]
    i = 0
    for c in r:
        if c == "z":
            r[i] = "a"
        else:
            r[i] = chr(ord(c) + 1)
            break
        i += 1
    password = "".join(r[::-1])
    return password


def next_password(password: str):
    # just in case we start on a password that is already valid
    password = increment_password(password)
    while is_it_valid(password) == False:
        password = increment_password(password)
    return password


def main():
    print(next_password("cqjxjnds"))
    # yeilded cqjxxyzz
    print(next_password("cqjxxyzz"))


if __name__ == "__main__":
    main()
