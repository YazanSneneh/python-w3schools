myList =[2, 4, 1, True]
myList2 = ['I am appeneded from another list, variable should be iterable']
print(f"the length of my List: {len(myList)}")
print(f"my List type method : {type(myList)}")
myList.sort()
print(f"asc sorted list {myList}")
myList.sort(reverse=True)
print(f"desc sorted list {myList}")
myList.reverse()
print(f"reversed list {myList}")
if True in myList:  # membership check
  print("False Does not Exist!")
  foundAt = myList.index(True) # get index of item 
  # insert into given index and shift current to right
  myList.insert(foundAt, 'I am replaced with True')

myList.append('Add To end of Array')
myList.extend(myList2)
print(myList)
print("=====loop over list using Comprehension=====")
new_list = [x for x in myList if type(x) == int]
print(f"new list : {new_list}")
myList.pop(0) # remove last element from list, if index provided it will remove that index
print(myList)
del myList2[0]
print(f"list2 length after del keyword my items {len(myList2)}")
del myList2
# print(myList2).  it will produce error because myList2 is no longer defined.
myList.clear()
print(f" method size after clear() {len(myList)}" )

myList =[2, 4, 1, 5]
list2 = myList.copy()
list2.append(22)
print(myList)
print(list2)