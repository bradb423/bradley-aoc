# need to use the bracket in the input file to find what floor santa is on
# ( is up one floor, ) is down one floor
filepath = "advent_of_code/problem1/input.txt"

def reader(filepath: str):
    result_string = ""
    with open(filepath,"r") as inputdata:
        for line in inputdata:
            result_string += line.strip()
    inputdata.close()
    return result_string

full_string = reader(filepath)

def total_floors_for_santa(filepath):
    floor_level = 0
    full_string = reader(filepath)
    for bracket in full_string:
        if bracket == "(":
            floor_level += 1
        elif bracket == ")":
            floor_level += -1
    return floor_level

# print(total_floors_for_santa(filepath))

def how_long_till_basement(filepath):
    # find out at what position he goes to floor -1
    floor_level = 0
    position = 1
    full_string = reader(filepath)
    for bracket in full_string:
        if bracket == "(":
            floor_level += 1
        elif bracket == ")":
            floor_level += -1
        if floor_level == -1:
            return position
            break
        position += 1

# print(how_long_till_basement(filepath))
