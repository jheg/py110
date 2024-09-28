my_string = "Jason Hegarty"
my_list = [1, 2, 3, 4, 5, 6]
my_tuple = (1, 2, 4, 5, 6)
my_range = range(0,10)

# slicing start:stop:step
print(my_string[0:len(my_string):1])    # Jason Hegarty
print(my_string[::-1])                  # ytrageH nosaJ    
print(my_list[1::2])                    # [2, 4, 6]
print(my_list[::-1])                    # [6, 5, 4, 3, 2, 1]
print(my_list[:3])                      # [1, 2, 3]
print(list(my_range[0:]))               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sequence length len()
print(len(my_range))                    # 10

# Iterating over sequences
for item in my_string: 
    print(item) 
# J
# a
# ... y

for item in my_range: 
    print(item)
# 0
# 1
# ... 9

i = 0 
while i < len(my_string):
    print(f"Item {i}: {my_string[i]}")
    i += 1

# The + operator can concatenate sequences of the same type and return a new 
# sequence
concat_list = my_list + [10, 11, 12]
print(concat_list)

concat_string = my_string + " & " + "Victoria Rance"
print(concat_string)

concat_tuple = my_tuple + (True, [1, 2, 3], "Bob")
print(concat_tuple)

# You cannot use the + operator on ranges it will raise a TypeError
# concat_range = my_range + range(10, 15) # TypeError: Unsupported operand 
# type(s) for +: 'range' and 'range'

# count and index

# count number of items (x) in sequence
print(my_string.count("a")) # 2

# index returns the first index position of the argument it finds in sequence
print(my_string.index("a")) # 1
# ValueError
# print(my_string.index("M")) # ValueError: substring not found
# print(my_list.index(10)) # ValueError: 10 is not in list
# print(my_list.index([3])) # ValueError: [3] is not in list

# min and max 
# Can be applied to all sequence types. 

# If the sequence contains strings, min and max compare strings 
# lexicographically. In other words, strings are compared character by 
# character using the Unicode values of their characters. The function returns 
# the character with the smallest or largest Unicode value:
print(min(my_string)) # 
print(max(my_string)) # y

print(min(my_list)) # 1
print(min(my_tuple)) # 1

print(min(my_range)) # 0
print(max(my_range)) # 9

# Converting to lists & tuples
tuple_list = tuple(my_list)
print(tuple_list) # (1, 2, 3, 4, 5, 6)
list_tuple = list(my_tuple)
print(list_tuple) # [1, 2, 4, 5, 6]

# using a comprehension to join not string types
print(", ".join([str(element) for element in my_list]))