#!/usr/bin/env python3

# Excercise 2:

def mysum (*args):
    
    add = 0
    
    for argument in args:
        add += argument
    
    return add

# function test:

print(f'Sum of 1+5+7 is {mysum(1,5,7)}')


# if we want to put a list of number into the function and then iterate over it we can do it
# with "*" Example:
# mysum(*[1, 2, 3, 4]) - star will tell Python to iterate over intigers inside the list. 
