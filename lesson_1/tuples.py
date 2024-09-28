"""
Tuples are order collections of elements but unlike lists they are immutable. 
This makes them suitable for representing fixed collections of objects.
"""

fruits = ("apple", "orange", "banana")
print(fruits[0]) # apple
print(fruits[-1]) # banana
# print(fruits[-4]) # IndexError: tuple index out of range
# fruits[0] = "cherry" # TypeError: 'tuple' object does not support item 
# assignment

# tuples can still be reassigned
fruits = ("strawberry", "grapes", "mango")
print(fruits)