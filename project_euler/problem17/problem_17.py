#!usr/bin/env python3
# this script finds the sum of all the lengths of the words for numbers
import inflect


def number_letter_counts(n):
    list_of_words = []
    p = inflect.engine()  # setting the text engine up
    for i in range(1, n + 1):
        words = p.number_to_words(i)
        words = words.replace(" ", "").replace("-", "")
        list_of_words.append(words)
    return sum([len(sentence) for sentence in list_of_words])


print(number_letter_counts(1000))
