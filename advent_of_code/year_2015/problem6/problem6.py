import numpy as np
import re

filepath = "advent_of_code/problem6/inputdata.txt"

# 0 is off, 1 is on
lightgrid = np.zeros((1000, 1000))
# first need to find a way of reading this
def parser(filepath):
    instructions = []
    with open(filepath, "r") as file:
        for line in file:
            # get the ranges
            ranges = re.findall(r"\d+", line)
            ranges = [int(x) for x in ranges]

            if "turn off" in line:
                ranges.append("off")
            if "turn on" in line:
                ranges.append("on")
            if "toggle" in line:
                ranges.append("toggle")

            instructions.append(ranges)
    return instructions


# define the light switches on the grid
def turn_on(instruction, lightgrid):
    for i in range(
        instruction[0], instruction[2] + 1
    ):  # the +1 is because of python loops always stopping one before you actually ask them to
        for j in range(instruction[1], instruction[3] + 1):
            if lightgrid[i][j] == 0:
                lightgrid[i][j] = 1


def turn_off(instruction, lightgrid):
    for i in range(instruction[0], instruction[2] + 1):
        for j in range(instruction[1], instruction[3] + 1):
            if lightgrid[i][j] == 1:
                lightgrid[i][j] = 0


def toggle(instruction, lightgrid):
    for i in range(instruction[0], instruction[2] + 1):
        for j in range(instruction[1], instruction[3] + 1):
            if lightgrid[i][j] == 0:
                lightgrid[i][j] = 1
            elif lightgrid[i][j] == 1:
                lightgrid[i][j] = 0


def reading_instructions(instructions, lightgrid):
    for instruction in instructions:
        if instruction[4] == "on":
            turn_on(instruction=instruction, lightgrid=lightgrid)
        elif instruction[4] == "off":
            turn_off(instruction=instruction, lightgrid=lightgrid)
        elif instruction[4] == "toggle":
            toggle(instruction=instruction, lightgrid=lightgrid)
    return lightgrid


def how_many_lights_are_lit(lightgrid):
    return len(np.flatnonzero(lightgrid))


#### implementing part 1

# instructions = parser(filepath)
# resulting_lightgrid = reading_instructions(instructions=instructions, lightgrid=lightgrid)
# print(how_many_lights_are_lit(lightgrid))

# part 2
def new_turn_on(instruction, lightgrid):
    for i in range(instruction[0], instruction[2] + 1):
        for j in range(instruction[1], instruction[3] + 1):
            lightgrid[i][j] += 1


def new_turn_off(instruction, lightgrid):
    for i in range(instruction[0], instruction[2] + 1):
        for j in range(instruction[1], instruction[3] + 1):
            if lightgrid[i][j] == 0:
                continue
            else:
                lightgrid[i][j] += -1


def new_toggle(instruction, lightgrid):
    for i in range(instruction[0], instruction[2] + 1):
        for j in range(instruction[1], instruction[3] + 1):
            lightgrid[i][j] += 2


def new_reading_instructions(instructions, lightgrid):
    for instruction in instructions:
        if instruction[4] == "on":
            new_turn_on(instruction=instruction, lightgrid=lightgrid)
        elif instruction[4] == "off":
            new_turn_off(instruction=instruction, lightgrid=lightgrid)
        elif instruction[4] == "toggle":
            new_toggle(instruction=instruction, lightgrid=lightgrid)
    return lightgrid


def total_brightness(lightgrid):
    return np.sum(lightgrid)


#### implementing part 2
instructions = parser(filepath)
resulting_lightgrid = new_reading_instructions(
    instructions=instructions, lightgrid=lightgrid
)
print(total_brightness(lightgrid=lightgrid))

#### notes:
# upon reflection, this one is quite slow, i need to look at ways to speed this up
