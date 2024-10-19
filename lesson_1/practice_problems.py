# 1
# Given the tuple:
fruits = ("apple", "banana", "cherry", "date", "banana")

# How would you count the number of occurrences of "banana" in the tuple?

count = 0
for fruit in fruits:
    if fruit == "banana":
        count += 1

print(count)    

# or 
print(fruits.count('banana'))

# 2
# Consider the set:
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers)) # 5
print(numbers) # {1, 2, 3, 4, 5}

# What is the set's length? Try to answer without running the code.
# 1.  Python starts creating the set.
# 2.  It evaluates each element one by one.
# 3.  As it evaluates each element, it immediately adds unique elements to the 
#     set.
# 4.  If an element is already in the set (a duplicate), it's simply ignored.
# 5.  Once all elements have been evaluated and added (or ignored if 
#     duplicate), the set initialization is complete.

# 3
# Given two sets:

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = {8, 9, 10, 34}
# How would you obtain a set that contains all the unique values from both sets?
d = a | b | c
print(d)

e = a.union(b,c)
print(e)

# 4
# Given the following code, what would the output be? Try to answer without running the code.

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)
# {
#     "Fred": 0,
#     "Barney": 1,
#     ...
# }

# 5
# Calculate the total age given the following dictionary:

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = sum(ages.values())
print(total_age)

# 6
# Determine the minimum age from the above ages dictionary.

print(min(ages.values())) # 10

# 7 
# What would the following code output? Try to answer without running the code.

words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words) # ['bear']

# 8 
# Given the following string, create a dictionary that represents the frequency 
# with which each letter occurs. The frequency count should be case-sensitive:

statement = "The Flintstones Rock"


letter_analysis = {}
for char in statement: 
    if char in letter_analysis:
        letter_analysis[char] += 1
    else:
        letter_analysis[char] = 1

print(letter_analysis)

# post read up ...
letter_analysis2 = {}
statement = statement.replace(' ', '')

for char in statement:
    letter_analysis2[char] = letter_analysis2.get(char, 0) + 1

print(letter_analysis2)

# The output should resemble the following:

# Pretty printed for clarity
# {
#     'T': 1,
#     'h': 1,
#     'e': 2,
#     'F': 1,
#     'l': 1,
#     'i': 1,
#     'n': 2,
#     't': 2,
#     's': 2,
#     'o': 2,
#     'R': 1,
#     'c': 1,
#     'k': 1
# }

# 9 
# What is the return value of the list comprehension below? Try to answer 
# without running the code.

[print(num) for num in [1, 2, 3] if num > 1]
# 2
# 3

# 10
# What does the following code print and why?

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
# ('b', 'bear') 
# Removes and returns the last item as a tuple. Tuples are more efficient than 
# dictionaries so come with less overhead. 

# 11
# What does the following code return? Try to answer without running the code.

lst = [1, 2, 3, 4, 5]
lst[:2] # [1, 2]

# 12 
# What would be the output of the below code? Try to answer without running 
# the code.

frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)
print(frozen) # frozenset([1, 2, 3, 4, 5])


