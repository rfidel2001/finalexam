#!/usr/bin/env python3

import sys 

def add_odds(a,b):
    '''
    Add up all odd numbers between a and b (inclusive of b)
    
    Args:
        a:an int less than b and 10000
        b:an int greater than a and less than 10000
    
    Return: 
        int: sum of odd numbers between a and b 
    
    '''
    if a > b:
        return("First number must be less than the second number")
    if b <= 10000:
        return("The numbers must be less than 10000")

    total = 0 #keep track of sum 
    for i in range(a,b+1): 
        if i % 2 ==1: #check if its odd by checking the remainder when dividing by 2 
            total = total + i #add the odd integer to total
    return(total)   

if __name__ == "__main__": 

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    print(add_odds(num1,num2))
