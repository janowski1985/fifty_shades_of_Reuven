#!/usr/bin/env python3

# Excercise 2:

def mysum (*args):
    
    add = 0
    
    for argument in args:
        add += argument
    
    return add

# function test:

print(f'Sum of 1+5+7 is {mysum(1,5,7)}')



