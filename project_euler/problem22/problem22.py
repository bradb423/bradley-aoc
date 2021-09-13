import sys


def get_alphabet_values():
    alphabet_values = {}
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(alphabet)
    for i in range(0, length):
        character = alphabet[i]
        alphabet_values[character] = i + 1
    return alphabet_values


def parse_file(filepath):
    # return the parsed list of names
    name_list = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip().split(",")
            for name in line:
                name = name[1:-1]
                name_list.append(name)
    name_list.sort()
    return name_list


def get_name_score(name, position, alphabet_values):
    name_score = 0
    for character in name:
        name_score += alphabet_values[character]
    name_score *= position
    return name_score


def sum_of_name_scores(name_list, alphabet_values):
    score_sum = 0
    length = len(name_list)
    for i in range(0, length):
        position = i + 1
        name = name_list[i]
        score_sum += get_name_score(name, position, alphabet_values)
    return score_sum


def main():
    alphabet_values = get_alphabet_values()
    filepath = sys.argv[1]
    name_list = parse_file(filepath)
    print(sum_of_name_scores(name_list, alphabet_values))


if __name__ == "__main__":
    main()
