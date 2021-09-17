#!usr/bin/env python3


# don't necessaryily need to create an array and add the diagonals, which was the original approach
# just look at the pattern on the diagonals in the diagram:
# https://1.bp.blogspot.com/-gQmw4qjKOaQ/VytvMD5foTI/AAAAAAAAB3M/gju0TG7NNRwdgN6sNHenSKeMsza0FiOowCLcB/s1600/7x7%2Bnumber%2Bspiral%2Bmatrix.jpg
def sum_diagonals(size: int):
    diag_total = 1 # as the centrepoint is 1
    gap = 0
    end_of_four_diagonals = 1
    for i in range(1,(size//2)+1):
        gap += 2
        for j in range(1,5):
            end_of_four_diagonals += gap
            diag_total += end_of_four_diagonals
    return diag_total


def main():
    print(sum_diagonals(1001))

if __name__ == '__main__':
    main()
