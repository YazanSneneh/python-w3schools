""" CHALLENGE 4
1. Write a function named add_values that takes in an array and a value.
and pushes the value into the array.

part 2 ==================================
Then, write a function named add_numbers that takes in four arguments:
  - A number to be added to an array
  - An array into which the number should be added
  - The number of times the number should be added
  - A callback function to use to add the numbers to the array (Hint: you already defined it)
Within the addNumbers function, invoke the callback function as many times as necessary,
 based on the third argument of the addNumbers function.
Return the modified array.
"""
from random import randrange


myList = []
value = 5
times = 4
def add_values(value, myList):
  myList.append(value)

def add_numbers(number, add_times, add_values, myList=[]):
#   for i in range(add_times):
#     add_values(number, myList)
    [add_values(number, myList) for i in range(add_times)]


add_numbers(value, times, add_values, myList)
print(myList)