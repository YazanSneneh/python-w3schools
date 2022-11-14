# A dictionary is a collection which is 
    # ordered*.
    # changeable.
    # do not allow duplicates.
# store values in key pair value
mydict = {
  "a": "Excellent",
  'b': 'Very Good',
  'c': 'good',
  'd': 'Weak',
  'f': 'Fail',
  'a': 'peace'
}

# access dictionary items
# mydict[key]
# mydict.get(key)
# mydict.get('key') vs mydict['key']
    # - mydict[key] - if keydoes not exist my application will crash.
    # - mydict.get(key) - if key does not exist i will receive None value
print(mydict['a'])  # a way to get items from dict by key
print(mydict.get('a')) # a way to get items from dict .get()

# type of dictionary
print(type(mydict))
print(type(mydict['a']))

#keys() method return keys in dict values() return values in dict
keys = mydict.keys()
values = mydict.values()
print(f'keys in mydict:  {keys}')
print(f'values in mydict:  {values}')

# loop on keys
for key in mydict.keys():
  print(mydict.get(key))

# loop over values
for value in mydict.values():
  print(value)

# loop over item and get key and value
for key, value in mydict.items():
  print(f'Key: {key}, and value: {value}')

# to add new key to dict i either add new key with value like so:  ---> 
# also update can be used to do the same
mydict['x'] = 'invalid mark'
mydict.update({'y': 'invalid character'})
print(f"new valye x: {mydict.get('x')}")
print(f"new value y: {mydict.get('y')}")

# I can delete item by using .pop() or using del keyword
del mydict['y']
mydict.pop('x')
print(mydict)