# define the filepath to be used
filepath = "advent_of_code/year_2015/problem3/data.txt"


def reader(filepath):
    instructions = ""
    with open(filepath, "r") as datafile:
        for line in datafile:
            instructions += line.strip()
    datafile.close()
    return instructions


### part 1
def reading_instructions(instructions):
    santas_position = (
        "0,0"  # easiest way to use coordinates here, also, I can make a set out of it
    )
    position_list = [santas_position]
    santas_position_coord = [0, 0]  # easiest form to manipulate
    for instruction in instructions:
        if instruction == "^":
            santas_position_coord[1] += 1
        elif instruction == "v":
            santas_position_coord[1] += -1
        elif instruction == ">":
            santas_position_coord[0] += 1
        elif instruction == "<":
            santas_position_coord[0] += -1
        position_list.append(
            str(santas_position_coord[0]) + "," + str(santas_position_coord[1])
        )
    return position_list  # please work...


def unique_positions(position_list):
    return set(position_list)  # visited at least once


def at_least_once(unique_positions):
    return len(unique_positions)


### part 2


def santa_vs_robosanta(instructions):
    santas_position = "0,0"
    robosantas_position = "0,0"
    n = len(instructions)
    santa_position_list = [santas_position]
    robosanta_position_list = [robosantas_position]
    santas_position_coord = [0, 0]
    robosantas_position_coord = [0, 0]

    for i in range(n):
        if i % 2 == 0:
            # santas turn
            if instructions[i] == "^":
                santas_position_coord[1] += 1
            elif instructions[i] == "v":
                santas_position_coord[1] += -1
            elif instructions[i] == ">":
                santas_position_coord[0] += 1
            elif instructions[i] == "<":
                santas_position_coord[0] += -1
            santa_position_list.append(
                str(santas_position_coord[0]) + "," + str(santas_position_coord[1])
            )
        elif i % 2 != 0:
            # robosantas turn
            if instructions[i] == "^":
                robosantas_position_coord[1] += 1
            elif instructions[i] == "v":
                robosantas_position_coord[1] += -1
            elif instructions[i] == ">":
                robosantas_position_coord[0] += 1
            elif instructions[i] == "<":
                robosantas_position_coord[0] += -1
            robosanta_position_list.append(
                str(robosantas_position_coord[0])
                + ","
                + str(robosantas_position_coord[1])
            )
    full_list = santa_position_list + robosanta_position_list
    return len(set(full_list))


# part 1 answer
# instructions = reader(filepath)
# position_list = reading_instructions(instructions)
# uniques = unique_positions(position_list)
# print(at_least_once(unique_positions=uniques))


# part 2 answer
instructions = reader(filepath)
print(santa_vs_robosanta(instructions))
