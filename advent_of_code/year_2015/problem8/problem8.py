import sys


def parse_file(filepath):
    parsed_file = []
    with open(filepath, "r") as f:
        for line in f:
            parsed_file.append(line.strip())
    return parsed_file


def raw_character_count(line):
    return len(line)


def memory_character_count(line):
    return len(eval(line))


def different_count(parsed_file):
    sum = 0
    for line in parsed_file:
        sum += raw_character_count(line) - memory_character_count(line)
    return sum


def length_extended_line(line):
    # don't need to do the subtraction, I just need to find how much it increased by
    # the four comes from the speech marks at the beginning and end being replaced as the following: "..." -> "\"...\""
    # have to do count "\\" because python registers it as an excape character
    return 4 + line.count("\\") + line[1:-1].count('"')


def new_difference_count(parsed_file):
    sum = 0
    for line in parsed_file:
        sum += length_extended_line(line)
    return sum


def main():
    filelpath = sys.argv[1]
    parsed_file = parse_file(filepath=filelpath)

    # part 1
    print(different_count(parsed_file))

    # part 2
    print(new_difference_count(parsed_file))


if __name__ == "__main__":
    main()
