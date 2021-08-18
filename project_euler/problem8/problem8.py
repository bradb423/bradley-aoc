# this script takes a given number and finds the largest product of digits
# within the number itself
# i have put the nuber in a text file for this case

filepath = "project_euler/problem8/input.txt"


def reader(filepath):
    full_number = ""
    with open(filepath, "r") as numberfile:
        for line in numberfile:
            full_number += line.strip()
    full_number = [int(x) for x in list(full_number)]
    return full_number


def list_multiplier(input_list):
    prod = 1
    for item in input_list:
        prod *= item
    return prod


number = reader(filepath)


def largest_product_of_digits(number: list, n: int):
    largest_product = 1
    if type(number) == int:
        number = [int(x) for x in list(str(number))]
    length = len(number)
    for i in range(0, length - n):
        product = list_multiplier(number[i : i + n])
        if product > largest_product:
            largest_product = product
    return largest_product


print(largest_product_of_digits(number, n=13))
