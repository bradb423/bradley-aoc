from advent_of_code.year_2015.problem8.problem8 import parse_file, different_count, new_difference_count

def test_part_1():
    filepath = "advent_of_code/problem8/test_data.txt"
    parsed_file = parse_file(filepath)
    assert different_count(parsed_file) == 12

def test_part_2():
    filepath = "advent_of_code/problem8/test_data.txt"
    parsed_file = parse_file(filepath)
    assert new_difference_count(parsed_file) == 19