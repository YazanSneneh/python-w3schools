""" CHALLENGE 1
Write a function named `add_one` that takes an array of numbers and returns a new array of the numbers, incremented by 1.
Push the new value into a local array. Return the local array
"""
numbers = (1, 2, 3, 4, 5)
def add_one(*numbers):
  result = []
  for number in numbers:
    result.append(number+1)
  return result

print(add_one(*numbers))
