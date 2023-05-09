
from firstscript import * 


def test_add_odds():
    a,b = 100,200
    actual_output = add_odds(a,b)
    expected_output = 7500
    assert actual_output == expected_output
test_add_odds()


def test_add_odds_1():
    a,b = 1,1
    actual_output = add_odds(a,b)
    expected_output = 1
    assert actual_output == expected_output
test_add_odds()


def test_add_odds_highlow():
    a,b = 10,1
    actual_output = add_odds(a,b)
    expected_output = "First number must be less than the second number" 
    assert actual_output == expected_output
test_add_odds()

def test_same():
    a,b = 1,1 
    actual_output = add_odds(a,b)
    expected_output = "Numbers must be different" 
    assert actual_output == expected_output 
test_add_odds() 

def test_decimals():
    a,b = 0.5,12.2
    actual_output = add_odds(a,b)
    expected_output = "Numbers can not be decimals" 
    assert actual_output == expected_output 
test_add_odds() 

def test_decimals():
    a,b = 10,-1
    actual_output = add_odds(a,b)
    expected_output = "Numbers can not negative" 
    assert actual_output == expected_output 
test_add_odds() 