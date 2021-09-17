#!usr/bin/env python3


def power_sequence(a_range, b_range):
    # a_range and b_range are the upper bounds of the ranges for the a and b values
    power_list = []
    for a in range(2, a_range + 1):
        for b in range(2, b_range + 1):
            power_list.append(a ** b)
    return len(set(power_list))


def main():
    print(power_sequence(5, 5))
    print(power_sequence(100, 100))


if __name__ == "__main__":
    main()
