#!python3
"""
Example of default parameters in a function.
Optional parameters that can be input to a function have an
equals assignment operators and a value.  These are the values that
the function will use if the optional parameter is not included in the
initial function call.
"""
def order(myList, by="ascending"):
    # inputs:
    # myList : list or tuple 
    # by: optional parameter, default value is ascending, but it could be descending
    # return value: list
    # function will take a list or tuple and convert it to a list.  Then
    # it will sort it in either ascending or descending order, depending on the 
    # optional parameter

    # converts to list in case it was a tuple:
    myList = list(myList)

    # this sorts the list into ascending values
    myList.sort()

    # if the optional parameter is set to "descending" then the 
    # list is reversed
    if by == "descending":
        myList.reverse()

    return myList

x = (3, 5, 4)

print("=====")
# ascending order.  This does not use the optional input parameter,
# so the default value of "ascending" will be used
a = order(x)
print(a)

print("\n=====")
# descending order.  This DOES use the optional input parameter, so
# the default value will not be used in the function
b = order(x, by="descending")
print(b)