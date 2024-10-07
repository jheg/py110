"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

"""
START 
Input: string
Output: list of strings or an empty list 
Rules: 
	Explicit Requirements : 
	- Every sub-string palindrome containing two or more characters in the string should be added to the list.
	- Palindromes are case sensitive 
	Implicit Requirements :		
	- If no palindromes exist return an empty list 
Algorithm:
    - X Create a palindrome_substrings function
    - X Declare a result variable and initialise it to an empty list 
    - X Declare a substrings variable and initialise it to an empty list
    - X Add string to substrings
    - X Add to substrings all the substrings of string containing 2 or more characters
        Example word: "abba"
        Substrings: 
        "abba", [0:4]
        "abb", [0:3]
        "ab", [0:2]

        "bba" [1:4]
        "bb", [1:3]

        "ba", [2:4]

        - 1. Declare a start variable to 0
        - 2. Declare a end variable to the length of string
        - 3. While end - start is > 1
            - While end - start is > 1
                - Add string[x:y] substring to substrings
                - Decrease end by 1
            - Increase start by 1
            - Reassign end to length of string

    - X Add to result all palindromes in substrings
    - X Return result
END
"""
def get_substrings(string):
    substrings = []
    start = 0
    end = len(string)
    while end - start > 1:
        while end - start > 1: 
            substrings.append(string[start:end])
            end -= 1
        start += 1
        end = len(string)

    return substrings

def get_palindromes(substrings):
    result = []
    for item in substrings: 
        if item == item[::-1]:
            result.append(item)
    return result

def palindrome_substrings(string):
    substrings = get_substrings(string)
    result = get_palindromes(substrings)
    print(f'{result = }')


# Test cases:
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]