"""
Write a function that takes a string of digits and returns the appropriate 
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result by 
using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about 
invalid characters; assume all characters are numeric.

Input: string
Output: integer

Create a dictionary of key value pairs with a key string representaion of 0 to 9
and it's corresponding number.



Algorythm:

"""

numbers = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

def string_to_integer(string):
    total = 0
    multiplier = 1
    list_of_characters = reversed(list(string))
    
    for char in list_of_characters:
        total += numbers[char] * multiplier
        multiplier *= 10
    
    return(total)

def hexadecimal_to_integer(string):
    return(int(string, 16))

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(hexadecimal_to_integer('4D9f') == 19871)  # True