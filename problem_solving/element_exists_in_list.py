'''
Check if element exists in list in Python
Example:

    list = test_list = [1, 6, 3, 5, 3, 4]
    Input: 3  # Check if 3 exist or not.
    Output: True

    Input: 7  # Check if 7 exist or not.
    Output: False
    
solution:
    - write a method takes two arguments element and a list.
    - check if element exist in the list.
    -return true or false depends if element exist or not.
'''
items = [1, 2, 3, 4, 5, 6]
def check_element_exists(item = None, items = []):
    return item in items

print('using if statemenet: ', check_element_exists(item = 5, items= items))