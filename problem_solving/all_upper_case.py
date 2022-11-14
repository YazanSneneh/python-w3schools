
""" CHALLENGE 3
Write a function named `all_upper_case` that takes an array of strings,
and returns a new array of the strings converted to upper case.
"""
upper_case_words = ("one", "two", "three", "four", 'Five')
def all_upper_case(*words):
  result = []
  for word in words:
    result.append(word.upper())
  return result

print(all_upper_case(*upper_case_words))