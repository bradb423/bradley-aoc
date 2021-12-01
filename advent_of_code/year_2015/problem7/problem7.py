import functools
import sys


def parse_file(filepath):
    inputdata = {}
    with open(filepath, "r") as f:
        for line in f:
            # the command is always on the lhs of the ->
            # the key to the value is always on the rhs of the ->
            command, key = line.split("->")
            inputdata[key.strip()] = command
    return inputdata


# the function below is recursive and so i should probably use the cache to
# speed this up
@functools.lru_cache(maxsize=None)
def find_value(key):
    try:
        return int(key)
    except ValueError:
        pass

    # split the command up a little
    # by the space
    # so that you can take the inputs of each command
    command = inputdata[key].split(" ")

    if "NOT" in command:
        # the input comes after the NOT so position 1 in the list
        # also need the bitwise NOT, "~"
        return ~find_value(command[1])
    elif "AND" in command:
        return find_value(command[0]) & find_value(command[2])
    elif "OR" in command:
        return find_value(command[0]) | find_value(command[2])
    elif "LSHIFT" in command:
        return find_value(command[0]) << find_value(command[2])
    elif "RSHIFT" in command:
        return find_value(command[0]) >> find_value(command[2])
    else:
        return find_value(command[0])

    # the file should be run as:
    # python3 .../problem7.py filepath_to_input_file


filepath = sys.argv[1]
inputdata = parse_file(filepath)

# part 1
print(find_value("a"))
# gives a value of 46065

# part 2
inputdata["b"] = "46065"
# don't forget to clear the cache! Looks like i made that mistake
find_value.cache_clear()
print(find_value("a"))
