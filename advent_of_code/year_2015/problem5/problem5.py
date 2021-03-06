import itertools as iter
import re

filepath = "advent_of_code/year_2015/problem5/inputdata.txt"
vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvwxyz"


def is_nice(filepath):
    nice_count = 0

    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            has_three_vowels = False
            has_double_letter = False
            no_bad_pairs = False

            # check for the vowels
            vowel_count = 0
            for letter in line:
                if letter in vowels:
                    vowel_count += 1
            if vowel_count >= 3:
                has_three_vowels = True

            # two consonants check
            for letter in alphabet:
                if letter * 2 in line:
                    has_double_letter = True

            # check it doesn't have the bad pairs in
            if (
                "ab" not in line
                and "cd" not in line
                and "pq" not in line
                and "xy" not in line
            ):
                no_bad_pairs = True

            if no_bad_pairs and has_double_letter and has_three_vowels:
                nice_count += 1
    file.close()
    return nice_count


# print(is_nice(filepath=filepath))

# maybe the regex package would help?
# let's read the documentation
def is_nice_2(filepath):
    count = 0
    with open(filepath, "r") as file:
        for line in file:
            has_a_pair = False
            has_the_gap = False
            line = line.strip()

            # check for the pair of letters repeating
            how_many_pairs = len(re.findall(r"([a-z]{2}).*\1", line))  # please work...
            if how_many_pairs >= 1:
                has_a_pair = True

            # check for the repeating letter with a gap
            if len(re.findall(r"([a-z]).\1", line)) >= 1:
                has_the_gap = True

            if has_the_gap and has_a_pair:
                count += 1
    file.close()
    return count


print(is_nice_2(filepath))
