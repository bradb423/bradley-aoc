from advent_of_code.year_2015.problem9.problem9 import (
    parse_file,
    shortest_distance,
    longest_distance,
)


def test_part_1():
    filepath = "advent_of_code/year_2015/problem9/test_data.txt"
    city_names, pair_distance_dict = parse_file(filepath)

    assert shortest_distance(pair_distance_dict, city_names) == 605


def test_part_2():
    filepath = "advent_of_code/year_2015/problem9/data.txt"
    city_names, pair_distance_dict = parse_file(filepath)
    assert shortest_distance(pair_distance_dict, city_names) == 207


def test_part_3():
    filepath = "advent_of_code/year_2015/problem9/test_data.txt"
    city_names, pair_distance_dict = parse_file(filepath)

    assert longest_distance(pair_distance_dict, city_names) == 982


def test_part_4():
    filepath = "advent_of_code/year_2015/problem9/data.txt"
    city_names, pair_distance_dict = parse_file(filepath)
    assert longest_distance(pair_distance_dict, city_names) == 804
