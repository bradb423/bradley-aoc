import sys
import itertools
from collections import defaultdict


def parse_file(filepath):
    pair_distance_dict = defaultdict(dict)
    city_names = []
    with open(filepath, "r") as f:
        for line in f:
            combination_list = line.strip().split(" = ")
            distance = int(combination_list[1])
            two_cities = combination_list[0].split(" to ")
            if two_cities[0] not in city_names:
                city_names.append(two_cities[0])
            if two_cities[1] not in city_names:
                city_names.append(two_cities[1])
            pair_distance_dict[two_cities[0]][two_cities[1]] = distance
    return city_names, pair_distance_dict


def shortest_distance(pair_distance_dict, city_names):
    lengths = []
    # need all the permutations of length 6 of the city_names to iterate over
    permutation_list = list(itertools.permutations(city_names))
    for permutation in permutation_list:
        permutation_length = 0
        n = len(permutation)
        for i in range(0, n - 1):
            permutation_length += pair_distance_dict[permutation[i]].get(
                permutation[i + 1], 0
            )
            permutation_length += pair_distance_dict[permutation[i + 1]].get(
                permutation[i], 0
            )
        if permutation_length != 0:
            lengths.append(permutation_length)
    return min(lengths)


def longest_distance(pair_distance_dict, city_names):
    lengths = []
    # need all the permutations of length 6 of the city_names to iterate over
    permutation_list = list(itertools.permutations(city_names))
    for permutation in permutation_list:
        permutation_length = 0
        n = len(permutation)
        for i in range(0, n - 1):
            permutation_length += pair_distance_dict[permutation[i]].get(
                permutation[i + 1], 0
            )
            permutation_length += pair_distance_dict[permutation[i + 1]].get(
                permutation[i], 0
            )
        if permutation_length != 0:
            lengths.append(permutation_length)
    return max(lengths)


def main():
    filepath = sys.argv[1]
    city_names, pair_distance_dict = parse_file(filepath)
    ### Part 1
    print(shortest_distance(pair_distance_dict, city_names))
    ### Part 2
    print(longest_distance(pair_distance_dict, city_names))


if __name__ == "__main__":
    main()
