"""
Given a list of strings, return a new list where the strings are sorted based 
on the highest number of adjacent consonants a string contains. If two strings 
contain the same highest number of adjacent consonants, they should retain 
their original order in relation to each other. Consonants are considered 
adjacent if they are next to each other in the same word or if there is a 
space between two consonants in adjacent words.

Input: list of strings
Output: list of strings

Rules: 
Explicit Rules:
- Case is not important
- Strings are not empty
- Consonants are considered adjacent if they are next to each other in the 
  same word or; 
- if there is a space between two consonants in adjacent words
- Sorted list:
    - List must be sorted in descending order
    - Must be sorted by highest number of adjacent consonants
    - If two strings have the same number then their original position 
      relative to each other should be maintained.

Implicit Rules:
- Strings can contain multiple words

Clarify: 
- Sort order (asc or desc) --> Descending
- Does case sensitivity matter? --> No
- Can a string be empty? --> No

Notes on counting adjacent consonants:
'xaaa' should return 0 whereas 'xxaa' should return 2. This means 1 should 
never get returned so this must be handled while tracking the count during the 
loop.

Data Structures: 
- list containing strings
- Some way of tracking the highest number of consonants in each string, perhaps 
  a dictionary:
    'string 1': 4,
    'string 2': 2,
    'string 3': 5,
    ...
- integer to store highest adjacent consonants
- integer to track the current count of adjacent consonants 

Algorithm:
- Record the highest number of adjacent consonants for each string in a list
-- For a given string calculate and return the highest number of adjacent 
   consonants anywhere in that string.

   Input: string containing one or more words
   Output: An integer representing the maximum number of adjacent consonants 
   within the string

   Algorithm:
   - Set highest number of consonants to 0
   - Set current count to 0
   - Strip all spaces from string
   - For each letter in the string:
    - If its a consonant:
        - increment current count by 1
        - if current count is > 1:
            - Set highest number of consonants to count if count is higher
    - If its a vowel:
        - Reset current count to 0
    - Return highest number

- Sort the list in descending order of highest number of adjacent consonants
- Return the list
"""
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def count_max_adjacent_consonants(string):
    highest_number_of_consonants = 0
    letters = string.split(' ')
    string_without_spaces = ''.join(letters)
    current_count = 0
    for letter in string_without_spaces:
        if letter in CONSONANTS:
            current_count += 1
            if current_count > 1:
                if current_count > highest_number_of_consonants:
                    highest_number_of_consonants = current_count
        elif letter not in CONSONANTS:
            current_count = 0
    
    return highest_number_of_consonants

# Test Cases for help function
# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4

def sort_by_consonant_count(strings):
    strings = sorted(strings, key=count_max_adjacent_consonants, reverse=True)

    # list_results = {}
    # for string in strings:
    #     list_results[string] = count_max_adjacent_consonants(string)

    # sorted_list = sorted(list_results.keys(), key=lambda k: list_results[k], reverse=True)
    return strings

# Test Cases:
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']
# 3, 2, 0, 0

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']
# 3, 2, 2, 0

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']
# 0, 0, 0, 0

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']
# 3, 0, 0, 0

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
# 4, 4, 3


