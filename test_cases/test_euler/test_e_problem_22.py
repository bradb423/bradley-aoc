from project_euler.problem22.problem22 import parse_file, get_alphabet_values, get_name_score, sum_of_name_scores

def test_example():
    alphabet_values = get_alphabet_values()
    name = "COLIN"
    position = 938
    assert get_name_score(name,position,alphabet_values) == 49714