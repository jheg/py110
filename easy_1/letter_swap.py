# Letter Swap

"""
Given a string of words separated by spaces, write a function that swaps the 
first and last letters of every word.

You may assume that every word contains at least one letter, and that the 
string will always contain at least one word. You may also assume that each 
string contains nothing but words and spaces, and that there are no leading, 
trailing, or repeated spaces.
"""

# Inputs: String
# Outputs: String

# Rules
# Explicit:
# - strings contain one or more words
# - Words contain one or more letters
# - Words are separated by a single space
# - No leading , trailing or repeated spaces 
# Implicit:  

# Algorithm 1
# - Create a variable called modified_string and assign it an empty string
# - for each word in string swap the last letter with the first letter
# -- See Algorithm 2
# - Add the modified_word to modified_string
# - Return modified_string

# Algorithm 2
# Split all words of a string into a list of words
# For each word in the list
#   Create a valiable called list_of_characters and assign to characters of word  
#   create a variable called processed_word and assign to an empty string
#   Create a variable called start_character and initialise to list[0]
#   Reasign list[0] to the value at list[-1]
#   Reasign list[-1] to start_character
#   Reassign processed_word to the string value of joining the list_of_characters
#   Return processed_word

def swap(string):
    words = string.split()
    modified_string = ''
    for word in words:
        modified_word = process_word(word)
        modified_string += (modified_word + ' ')
    modified_string = modified_string.rstrip()
    
    return modified_string

def process_word(word):
    list_of_characters = list(word)
    modified_word = ''
    start_character = list_of_characters[0]
    list_of_characters[0] = list_of_characters[-1]
    list_of_characters[-1] = start_character
    modified_word = ''.join(list_of_characters)

    return modified_word

# Examples
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
