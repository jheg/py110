my_dict1 = {
    1 : "Jay", 
    1 : "Jason", # Does this reassign 1?
    1 : "Mr", # and again?
    "name": "Hegarty",
    2.3: "Lee",
    (1, 2, 3): "tuple",
    # [1, 2, 3]: "list", # Raises a TypeError: unhashable type: 'list' 
    # {"key": "value"}: "dict", # Raises a TypeError: unhashable type 'dict'
    "01/01/2024": {"value": 100000}, 
}
print(my_dict1)
print(my_dict1[2.3]) # "Lee"
# print(my_dict1[2.4]) # KeyError: 2.4
# Using get() avoids a KeyError if the key does not exist
print(my_dict1.get(2.4)) # None

# You can also pass in your own default return msg 
print(my_dict1.get(2.4, "Nope not here!")) # Nope not here!

# To check if a dict has a particular key you can use the in and not in keywords
print(2.3 in my_dict1) # True
print(2.3 not in my_dict1) # False

# Hashing
# In Python objects are hashable if it has a stable and mostly unique identifier
# known as a hash value.

fruit_and_veg = {
    "apple": "produce",
    "banana": "produce",
    "carrot": "produce",
    "onion": "produce",
}

fruit_and_veg['apple'] = "fruit"
fruit_and_veg['banana'] = "fruit"
fruit_and_veg['carrot'] = "vegatable"
fruit_and_veg['onion'] = "vegatable"
print(fruit_and_veg)
fruit_and_veg['lemon'] = "fruit"
print(fruit_and_veg)
del fruit_and_veg['apple']
print(fruit_and_veg)

# sets
# set are mutable but;
# can only contain unique immutable objects
# Can not be indexed and are not ordered
my_set = {1, 2, 3, 4, 5}

# trying to access using an index will raise a TypeError
# print(my_set[0]) # TypeError: 'set' object is not subscriptable

print(1 in my_set) # True

my_set.add(6)
print(my_set)

my_set.add(6) # will not raise an error but will not be added
# my_set.remove(7) # KeyError: 7

# Will not raise a KeyError like remove() does if the element doesn't exist
my_set.discard(7) # removes the object if it exists else does nothing

# frozen set
# Like sets except they are set in stone, they are immutable
my_frozen_set = frozenset(my_set)
print(my_frozen_set)

# my_dict1.clear()
# print(my_dict1) # {}
# my_set.clear()
# print(my_set) # set()

# iteration 
print("____________")
for key in my_dict1:
    print(key)
print("____________")
for hashabale in my_set:
    print(hashabale)

print("____________")
for item in my_frozen_set:
    print(item)

my_set.add(7)
print(my_set) # {1, 2, 3, 4, 5, 6, 7}
zipped_pairs = zip(my_frozen_set, my_set) 
new_dict = dict(zipped_pairs)
print(new_dict) # {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
