from itertools import groupby


def look_and_say(number_string: str, iterations: int):
    # loop through each iteration
    for i in range(0, iterations):
        # group by, get the key for each value and get the nuber of times as the length of the group
        number_string = "".join(
            [str(len(list(group))) + str(key) for key, group in groupby(number_string)]
        )
    return number_string


def main():
    print(len(look_and_say("1113222113", 40)))
    print(len(look_and_say("1113222113", 50)))


if __name__ == "__main__":
    main()
