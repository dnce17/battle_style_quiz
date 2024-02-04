import pytest
from quiz import Quiz, Quizzee

@pytest.fixture
def q():
    return Quiz()

@pytest.fixture
def quizzee():
    return Quizzee()

def test_valid_ans(q):
    total_choices = 5
    assert q._validate_ans("1", total_choices) == True
    assert q._validate_ans("5", total_choices) == True
    assert q._validate_ans("3", total_choices) == True

def test_invalid_ans(q):
    total_choices = 8
    tests = ["0", "9", "3.5" "bob", "@#", "", "   "]
    for t in tests:
        assert q._validate_ans(t, total_choices) == False

def test_add_role_pts(quizzee):
    valid_tests = [
        "attacker", 
        "all-rounder", 
        "defender", 
        "supporter",
        "   attacker  ",
        "  DEFenDer",
        "SUPPORTER   "
    ]
    quizzee._add_role_pts(*valid_tests)
    assert quizzee._attacker == 2
    assert quizzee._all_rounder == 1
    assert quizzee._defender == 2
    assert quizzee._supporter == 2