def parser(filepath):
    rows = []
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            row = line.split(" ")
            row = [int(x) for x in row]
            rows.append(row)
    return rows


def max_path(filepath):
    triangle = parser(filepath)
    """Return the maximum triangle path sum(bottom up)."""
    # Starting with the last row ...
    for row in range(len(triangle) - 1, 0, -1):
        # ... add maximum of adjacent entries to the corresponding entry
        # in the preceding row:
        for col in range(len(triangle[row]) - 1):
            maximum = max(triangle[row][col], triangle[row][col + 1])
            triangle[row - 1][col] += maximum
    return triangle[0][0]


# print(max_path("project_euler/problem18/inputdata.txt"))
