""" CHALLENGE 5
Write a function named create_list that takes in a list of the current store inventory.
The inventory is formatted like this:
[
  { name: 'apples', available: true },
  { name: 'pears', available: true },
  { name: 'oranges', available: false },
  { name: 'bananas', available: true },
  { name: 'blueberries', available: false }
]
 This function should use loop to populate grocery list based on the store's inventory.
 If the item is available, add it to list. 
 Return the final list.
"""

items = (
  { 'name': 'apples', 'available': True },
  { 'name': 'pears', 'available': True},
  { 'name': 'oranges', 'available': True },
  { 'name': 'bananas', 'available': True },
  { 'name': 'blueberries', 'available': False }
)

def create_list(*store):
    online_store = []
    for item in store[0]:
        is_available = item.get('available')
        if is_available:
            online_store.append(item)
    return online_store

print(create_list(items))