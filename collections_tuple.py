''' 
- everything applied on list is also applied on tuple.
- append remove or update wont work on tuple unless i transfer it to list then do my changes
- tuples are ordered, example tuple(1,2,3)   output: (1,2,3)
    - sets are not ordered so result would be in sets : {2,1,3}
- tuples allow douplicate: since it's indexed because we refer to item in index
- tuples unchangeable - meaning that once it's defined, i can't update it's value
'''

myTuple = (2, 4, 1, 5, 2 ,2)
myTuple2 = 1,   # tupe with one item
# unpacking collections list and tuples
# [*unpacking] = myTuple
# print(unpacking[1])

# ======= unchangeable example ========
# myTuple2.append(22) TypeError: 'tuple' object does not support append
# myTuple2[0] = 22 # TypeError: 'tuple' object does not support item assignment
# myTuple2.pop(0)   no support for pop or remove
print(type(myTuple2))
print(myTuple2)
print(f"count method result on 2 value: {myTuple.count(2)}")
print(f" find value by it's index, it will result first appearance index {myTuple.index(2)}")
# Using Asterisk*
# it's useful when i don't know how many elements i have inside tuple.
# when values and variables i use to unpack do not match i receive an error.
# so using asterisk will unpack values and assign values to all variables, but
    # for the variable with asterisk will assign all values as list.
(val1, *val2, val3) = myTuple
print("======================= unpack tuple=====================")
print(val1)
print(val2)
print(val3)

