'''
Python program to swap two elements in a list

Given a list in Python and provided the positions of the elements,
    write a program to swap the two elements in the list.

Example:
    Input : List = [23, 65, 19, 90], pos1 = 0, pos2 = 2
    Output : [19, 65, 23, 90]

    Input : List = [1, 2, 3, 4, 5], pos1 = 1, pos2 = 4
    Output : [1, 5, 3, 4, 2]
'''

def swap_two_positions(the_list, pos1, pos2):
    first, second = the_list.pop(pos1), the_list.pop(pos2)
    the_list.insert(pos1, second)
    the_list.insert(pos2, first)
    print(the_list)

the_list = [1, 2, 3, 4, 5]
pos1 = 1
pos2 = 4

swap_two_positions(the_list, pos1-1, pos2-1)