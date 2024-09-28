"""
Ranges represent sequences of integer numbers. A range is an immutable sequence 
of numbers commonly used while looping. 

Compared to lists and tuples, ranges are more efficient as they only store the 
start, stop, step and current values. The next value in the range is computed 
but not before it is needed. 
"""

numbers = range(10, 20)
print(numbers[3])
# print(numbers[99])  # IndexError: range object index is out of range
# numbers[0] = 11 # TypeError: 'range' object does not support item assignment

# Reassignment is fine
numbers = range(30, 40)

# The memory efficiency of ranges is why we need to use list() to expand the 
# range
print(list(numbers))