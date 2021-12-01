# want to add up the total area and for each package, i need to add a little extra (the area of the smallest side)

filepath = "advent_of_code/year_2015/problem2/data.txt"


def parser(filepath: str):
    fulldata = []
    with open(filepath, "r") as inputdata:
        for line in inputdata:
            nice_list = line.strip().split("x")
            nice_list = [int(x) for x in nice_list]
            fulldata.append(nice_list)
    inputdata.close()
    return fulldata


def area_needed(parsed_data):
    total = 0
    for box in parsed_data:
        area = 2 * (
            (box[0] * box[1]) + (box[0] * box[2]) + (box[1] * box[2])
        )  # adding up all sides of the prism
        little_extra = min(
            box[0] * box[1], box[0] * box[2], box[1] * box[2]
        )  # finding the smallest side to add on
        required_paper = area + little_extra
        total += required_paper
    return total


parsed_data = parser(filepath=filepath)
# print(area_needed(parsed_data=parsed_data))


def ribbon_needed(parsed_data):
    total_ribbon = 0
    for box in parsed_data:
        # to get the face with the smallest perimeter
        # find the smallest two sides, then do 2*sum(side1,side2)
        sorted_data = sorted(box)
        perimeter = 2 * (sorted_data[0] + sorted_data[1])
        # the amount of ribbon for the bow is equal to the volume of the present
        bow = box[0] * box[1] * box[2]
        required_ribbon = perimeter + bow
        total_ribbon += required_ribbon
    return total_ribbon


# print(ribbon_needed(parsed_data))
