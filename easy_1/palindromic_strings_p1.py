def is_palindrome(string_input):
    reversed_string = string_input[::-1]
    return True if reversed_string == string_input else False

# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)