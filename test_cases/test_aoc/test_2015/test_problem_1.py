from advent_of_code.year_2015.problem1.problem1 import total_floors_for_santa, how_long_till_basement
def test_problem_1a_1():
    case1 = "advent_of_code/problem1/mock_input_1.txt"
    assert total_floors_for_santa(case1) == 0

def test_problem_1a_2():
    case2 = "advent_of_code/problem1/mock_input_2.txt"
    assert total_floors_for_santa(case2) == 3

def test_problem_1a_3():
    case3 = "advent_of_code/problem1/mock_input_3.txt"
    assert total_floors_for_santa(case3) == 3

def test_problem_1b_1():
    case4 = "advent_of_code/problem1/mock_input_4.txt"
    assert how_long_till_basement(case4) == 1

def test_problem_1b_2():
    case5 = "advent_of_code/problem1/mock_input_5.txt"
    assert how_long_till_basement(case5) == 5