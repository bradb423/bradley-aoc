from os import nice


# want to add up the total area and for each package, i need to add a little extra (the area of the smallest side)

filepath = "./data.txt"

def parser(filepath: str):
    fulldata = []
    with open(filepath,"r") as inputdata:
        for line in inputdata:
            nice_list = line.strip().split("x")
            nice_list = [int(x) for x in nice_list]
            fulldata.append(nice_list)
    return fulldata

def area_needed(parsed_data):
    total = 0
    for box in parsed_data:
        area = 2*((box[0]*box[1])+(box[0]*box[2])+(box[1]*box[2])) # adding up all sides of the prism
        little_extra = min(box[0]*box[1], box[0]*box[2], box[1]*box[2]) # finding the smallest side to add on
        required_paper = area + little_extra
        total += required_paper
    return total

# parsed_data = parser(filepath=filepath)
# print(area_needed(parsed_data=parsed_data))

