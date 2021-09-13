from itertools import permutations


# the permutations functions already puts it into lexicographic order
def main():
    digits = [0,1,2,3,4,5,6,7,8,9]
    lexicographic_order = list(permutations(digits))
    print(lexicographic_order[999999])

if __name__ == '__main__':
    main()