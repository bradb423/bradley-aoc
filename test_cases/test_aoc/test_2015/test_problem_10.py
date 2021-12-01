from advent_of_code.year_2015.problem10.problem10 import look_and_say

def test_1():
    assert look_and_say("1",1) == "11"

def test_2():
    assert look_and_say("11",1) == "21"

def test_3():
    assert look_and_say("21",1) == "1211"

def test_4():
    assert look_and_say("1211",1) == "111221"

def test_5():
    assert look_and_say("111221",1) == "312211"