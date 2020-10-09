#! python3
# module definition
# Note: This file contains only function definitions and variables
# the functions are also called "METHODS" and the variables are called "PROPERTIES"

black = "Benjamin"
tabby = "Casey"

def plusOne(number):
    # input: any variable type
    # returns: 
    #   the number +1 if the number is an integer
    #   0 if the number is not an integer
    if type(number) == int:
        return number + 1
    else:
        return 0

def timesTwo(number):
    # input: any float
    # returns
    #   the number * 2 if the number is a float or integer
    #   0 if the number is not a float or integer
    if type(number) == int or type(number) == float:
        return number * 2
    else:
        return 0

def zeroMyHero(number):
    # input: any variable type
    # returns 0 no matter what the type is for the input
    return 0
      

