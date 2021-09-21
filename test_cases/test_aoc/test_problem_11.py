from advent_of_code.problem11.problem11 import is_it_valid, next_password


def test_hijklmmn():
    assert is_it_valid("hijklmmn") == False


def test_abbceffg():
    assert is_it_valid("abbceffg") == False


def test_abbcegjk():
    assert is_it_valid("abbcegjk") == False


def test_abcdefgh():
    assert next_password("abcdefgh") == "abcdffaa"


def test_ghijklmn():
    assert next_password("ghijklmn") == "ghjaabcc"
