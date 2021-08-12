# want the first 10 digits of the sum of the values in the file

filepath = "project_euler/problem13/inputdata.txt"

def last_10_digits(filepath):
    total = 0
    with open(filepath,"r") as file:
        for line in file:
            number = int(line.strip())
            total = total + number
    return str(total)[0:10]

print(last_10_digits(filepath))