from project_euler.problem26.problem26 import reciprocal_length, longest_reciprocal, sieve

def test_reciprocal_length():
    assert reciprocal_length(13) == 6
    assert reciprocal_length(7) == 6
    assert reciprocal_length(17) == 16
    assert reciprocal_length(19) == 18

def test_longest_reciprocal():
    prime_array = [983]
    assert longest_reciprocal(prime_array) == (983,982)