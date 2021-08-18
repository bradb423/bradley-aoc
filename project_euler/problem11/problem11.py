import numpy as np

filepath = "project_euler/problem11/inputdata.txt"

# clean data
def reader(filepath):
    full_array = []
    with open(filepath, "r") as file:
        for line in file:
            row = line.strip("\n").split(" ")
            row = [int(x) for x in row]
            full_array.append(row)
    return full_array


# the above creates a nice matrix which represents the grid

# the product is always four numbers, so i need to loop but only go to the length of the grid -4 to not go over
def biggest_product(array):
    biggestproduct = 1
    for i in range(0, 16):
        for j in range(0, 16):
            # the vertical, starting at [i,j] and going downwards
            vertical = array[i][j] * array[i + 1][j] * array[i + 2][j] * array[i + 3][j]
            if vertical > biggestproduct:
                biggestproduct = vertical

            # the horizontal, starting at [i,j] and going to the right
            horizontal = (
                array[i][j] * array[i][j + 1] * array[i][j + 2] * array[i][j + 3]
            )
            if horizontal > biggestproduct:
                biggestproduct = horizontal

            # the diagonal to the right, starting at [i,j] and going downwards and to the right
            right_diagonal = (
                array[i][j]
                * array[i + 1][j + 1]
                * array[i + 2][j + 2]
                * array[i + 3][j + 3]
            )
            if right_diagonal > biggestproduct:
                biggestproduct = right_diagonal

            # the diagonal to the left, starting at [19-i,j] and going upwards and to the right (to avoid looping over the edge at the bottom)
            left_diagonal = (
                array[19 - i][j]
                * array[18 - i][j + 1]
                * array[17 - i][j + 2]
                * array[16 - i][j + 3]
            )
            if left_diagonal > biggestproduct:
                biggestproduct = left_diagonal
    return biggestproduct


input_array = reader(filepath)
print(biggest_product(input_array))
