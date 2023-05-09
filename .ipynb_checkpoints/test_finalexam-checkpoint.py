from finalexam import * 

#creating test function that shows what it would look like normally for count_observed_substrings
def test_count_observed_substrings():
    #setting string value and k value
    string = "ATTTGGATT"
    k = 2
    #setting actual output and expected output 
    actual_output = count_observed_substrings(string,k)
    expected_output = 5
    #asserting output 
    assert actual_output == expected_output
#calling the test function
test_count_observed_substrings()


#creating test function that shows what it would look like normally for count_possible_substrings
def test_count_possible_substrings():
    string = "ATTTGGATT"
    k = 2
    actual_output = count_possible_substrings(string,k)
    expected_output = 8
    assert actual_output == expected_output
test_count_possible_substrings()


#creating test function that shows what it would look like normally for linguistic_complexity
def test_linguistic_complexity():
    string = "ATTTGGATT"
    k = 2
    #saving the observed number of substrings calculation to a variable
    observed = count_observed_substrings(string, k)
    #saving the possible number of substrings calculation to a variable
    possible = count_possible_substrings(string, k)
    actual_output = linguistic_complexity(string,k)
    expected_output = 0.625
    assert actual_output == expected_output
test_count_possible_substrings()

#creating test function that produces message when k is negative for count_observed_substrings
def test_negatives_observed_substrings():
    string = "ATTTGGATT"
    k = -2
    actual_output = count_observed_substrings(string,k)
    expected_output = None
    assert actual_output == expected_output
test_negatives_observed_substrings()

#creating test function when k is negative for count_possible_substrings ,makes the output 0
def test_negatives_possible_substrings():
    string = "ATTTGGATT"
    k = -2
    actual_output = count_possible_substrings(string,k)
    expected_output = 0
    assert actual_output == expected_output
test_negatives_possible_substrings()

#test empty string for count_possible_substrings
def test_empty_observed_substrings():
    string = ""
    k = 2
    actual_output = count_possible_substrings(string,k)
    expected_output = 0
    assert actual_output == expected_output
test_empty_observed_substrings()

#test empty string for count_observed_substrings, makes it so that output is 0 
def test_empty_possible_substrings():
    string = ""
    k = 2 
    actual_output = count_observed_substrings(string,k)
    #putting what expected output should be
    expected_output = 0
    assert actual_output == expected_output #asserting output 
test_empty_possible_substrings()

#test empty string and negative k for count_possible_substrings
def test_emptynegative_possible_substrings():
    #setting empty value for string and negative # for k 
    string = "" #empty string
    k = -2 #negative number 
    actual_output = count_possible_substrings(string,k)
    #putting what expected output should be 
    expected_output = 0 
    assert actual_output == expected_output #asserting output 
test_emptynegative_possible_substrings()

#test empty string and negative k for count_possible_substrings
def test_emptynegative_observed_substrings():
    #setting empty value for string and negative # for k 
    string = "" #empty string
    k = -2 #negative #
    actual_output = count_observed_substrings(string,k)
    expected_output = None 
    assert actual_output == expected_output
test_emptynegative_possible_substrings()

