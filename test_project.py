import pytest
from quiz import Quiz

@pytest.fixture
def q():
    return Quiz()

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

    

    






