'''
Python program to interchange first and last elements in a list

Problem:
    - Given a list, write a Python program to swap first and last element of the list.

    - Examples: 
        Input : [12, 35, 9, 56, 24]
        Output : [24, 35, 9, 56, 12]

        Input : [1, 2, 3]
        Output : [3, 2, 1]

Algorithm:
    1. create a variable that holds the first array element.
    2. assign the last element in the array to the first index in the array.
    3. assign the temporary value to the last index in the array.
'''

print("- - - - ---------------------------------- list[-1] approach---------------------------- - - - -")
def exchange_first_last_reverse_index(list_1 = None):
    temporary = list_1[0]
    list_1[0] = list_1[-1]
    list_1[-1] = temporary
    print(list_1)


list_1 = [12, 35, 9, 56, 24]
exchange_first_last_reverse_index(list_1)

print("- - - - ---------------------------------- len(list) Approach---------------------------- - - - -")

def exchange_first_last_len_method(list_1 = None):
    temporary = list_1[0]
    last_index = len(list_1) - 1
    list_1[0] = list_1[last_index]
    list_1[-1] = temporary
    print(list_1)

l = [1, 12, 35, 9, 56, 24, 99]
exchange_first_last_len_method(l)

print("- - - - ---------------------------------- iterable Approach---------------------------- - - - -")
def exchange_first_last_iterable_method(list_1 = None):
    swapped_items = list_1[-1], list_1[0]
    list_1[0], list_1[-1] = swapped_items
    print(list_1)

third = ["apple", "Banana", "Cucumber", "pineapple"]
exchange_first_last_iterable_method(third)

print("- - - - ---------------------------------- pop, insert, append Approach---------------------------- - - - -")
def exchange_first_last_unpack_method(list_1 = None):
    first, last = list_1.pop(0) , list_1.pop(-1)
    list_1.insert(0, last)
    list_1.append(first)
    print(list_1)

fourth = [True, False, 1, 2, 3, 4]
exchange_first_last_unpack_method(fourth)