""" CHALLENGE 6
Write a function named fizzbuzz that takes in a set of numbers.
Iterate over the set to determine the output based on several rules:
  - If a number is divisible by 3, add the word "Fizz" to the output array.
  - If the number is divisible by 5, add the word "Buzz" to the output array.
  - If the number is divisible by both 3 and 5, add the phrase "Fizz Buzz" to the output array.
  - Otherwise, add the number to the output array.
Return the resulting output array.
"""
fizzBuzzNumbers = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
def fizzbuzz(*numbers_list):
  output = []
  for number in numbers_list:
    if number%3 ==0 and number%5 ==0:
      output.append('Fizz Buzz')
    elif number%3 ==0:
      output.append("Fizz")
    elif number%5 ==0:
      output.append("Buzz")
    else:
      output.append(number)
  return output
print(fizzbuzz(*fizzBuzzNumbers))