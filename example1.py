#! python3
"""
Example of a function that returns a tuple containing 2 values.
The 2 values are stored into 2 variables when the function is
called from the main block of code
"""

def squareAndRoot(number):
    # inputs: a float
    # outputs:
    #    tuple: ( float , float )
    #       float : the square root of the number
    #       float : the square of the number
    # this function takes a float input and then determines
    # both the square root and square of the number and then
    # returns it as a tuple
    # requires math module for square root
    import math
    sqrt = math.sqrt(number)
    square = number * number
    answer = ( sqrt , square )
    return answer



# we know that the function returns a tuple that contains 2 values
# we can store the entire tuple return value into a variable, in 
# which case, it becomes a tuple
x = squareAndRoot(3)
print(x)

# however, we can also store that return value into 2 variables
# at the same time. The first value in the tuple is stored in the first
# variable and the second return value is stored in the second variable
a,b = squareAndRoot(3)
print(a)
print(b)

# note that this function only returns a tuple with a length of 2
# if we try to store it into 3 variable, we will get an error:
# uncomment the next line to see what error we get
j,k,l = squareAndRoot(3)