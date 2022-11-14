'''
Python Lambda
    anonymous function (meaning that no name for this function)
    function can take any number of arguments, but can only have one expression.

- it returns an expression syntax
- use lambda functions when an anonymous function is required for a short period of time

Syntax
lambda arguments : expression 

Example:
'''
from typing import Tuple


print_name_with_lambda = lambda name : "the name is "+ name
print(print_name_with_lambda('Yazan'))

a, b, c = tuple((1, 2, 3))
print(a)
print(b)
print(c)