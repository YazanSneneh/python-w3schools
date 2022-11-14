# sets declared with curly braces
# sets do not allow duplicate values
# items in sets are unordered
# once set is created it's items cant be changed but i can add or remove items.
# set values are not indexed

myset = {1,2 ,3 ,4 ,5}

# add item to set
myset.add("add() method to set")

print(myset)

#add set to set
set2 = {True, False}
myset.update(set2) # add items set2 to myset - it add items from any iteritable
print(myset) # 1 value means true at index 1, and sets do not allow duplicates

myset.remove(1) # remove method raise error, discard method do nothing
myset.discard(False) # do not crash my app
myset.pop()
print(myset)
myset.clear()

# set1.join(set2) return new set will all items of set1, set2