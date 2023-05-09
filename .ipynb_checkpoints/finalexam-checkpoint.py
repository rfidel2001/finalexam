#!/usr/bin/env python3

import sys 

def count_observed_substrings(string, k):
    '''
defines the function to count the observed substrings , and it takes two arguments 
Which  represents the input string, and k representing the size of the substrings.
    
    '''
    # if k is less than 0, the function returns None
    if k < 0:
        return None
    
    #This line creates an empty set  to store the observed substrings.
    substrings = set()
    #This line starts a loop that iterates i from 0 to len(string) - k, which represents the starting index of #each substring. 
#The range() function is used to generate the indices.
    for i in range(len(string) - k + 1):
        #this line extracts a substring from the input string by slicing, 
        #it starts at the index I and ends at #index I+k and creates the substring of size ‘k’ 
        substring = string[i:i+k]
        #This line adds the extracted substring to the substrings set.  
        #sets only store unique elements, so It #makes it so that each observed substring is added only once.
        substrings.add(substring)
        #this returns the count of the observed substrings by  returning the length of the substrings set
    return len(substrings)


def count_possible_substrings(string, k):
    '''
    This  defines a function called count_possible_substrings that takes the two arguments: string 
    represents the input string, and k represents the size of the substrings.
    
    '''
    #This line checks if the value of k is less than 1 or greater than the length of the input string string. If either of the conditions are true, 
    #it means that the value of k is invalid for the given string.
    #If the value of k is invalid for the given string, the function immediately returns 0, indicating that there are no possible substrings.
    if k < 1 or k > len(string):
        return 0
    #This line checks if the value of k is 1.
# which means each individual character of the string can be considered as a substring of size 1. 
#the function returns the length of the string as the count of possible substrings , since the number #of possible substrings is equal to the length of the string when k is 1 
    elif k == 1:
        return len(string)
    #the line is reached when k is a valid value (within range of the string length) 
    #and returns the count as the result 
    else:
        return len(string) - k + 1

    
#testing linguistic complexity on example string
#setting variable equal to a sequence
dna_sequence = "ATTTGGATT"    

#answering part one and counting the number of different observed substrings of size 2 in the example
print("counting the number of different observed substrings of size 2 in the example")
print(count_observed_substrings(dna_sequence,2))
#answering part one and counting the number of different observed substrings of any size
print("counting the number of different observed substrings of any size ")
print(count_observed_substrings(dna_sequence,3))
#Extending this work to count the number of different observed substrings of all possible sizes.
print("Extending this work to count the number of different observed substrings of all possible sizes")
print(count_possible_substrings(dna_sequence, 2))

#defines the function linguistic complexity , and takes string and k as an argument
def linguistic_complexity(string, k):
    #saving the observed number of substrings calculation to a variable
    observed = count_observed_substrings(string, k)
    #saving the possible number of substrings calculation to a variable
    possible = count_possible_substrings(string, k)
    #if possible = 0 , return 0 
    if possible == 0:
        return 0
    #or else return the calculation for linguisitc complexity which is # of observed substrings/# of possible substring
    else:
        return observed / possible
    

#setting the number k 
k = 3
#calculating the linguistic complexity of the sequence using the linguistic complexity function
result = linguistic_complexity(dna_sequence, k)
#printing the results 
print("Linguistic Complexity of dna sequence example:", result)


#this line imports pathlib as Path
from pathlib import Path
#this reads the text file and saves it to the variable txt
txt = Path('sequence.txt').read_text()


#setting the size of k 
k = 2
#calculating the observed substrings for the text file 
observed_count = count_observed_substrings(txt, k)
#calculating the possible # substrings for the text file 
possible_count =  count_possible_substrings(txt, k)
#calculating the possible # substrings for the text file 
lcforfile =  linguistic_complexity(txt, k)
#printing observed count, possible count , and linguistic complexity
print("Observed Count of sequence file:", observed_count)
print("Possible Count of sequence file:", possible_count)
print("linguistic complexity of sequence file :",lcforfile)