def is_palindrome(string_input):
    reversed_string = string_input[::-1]
    return True if reversed_string == string_input else False

def is_real_palindrome(string_input):
    alphanumerics = []
    for char in string_input:
        if char.isalnum():
            alphanumerics.append(char.casefold())
    
    alphanumeric_string = ''.join(alphanumerics)

    return is_palindrome(alphanumeric_string)
    

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Launch School solution which is simpler than my approach of using a list 
def is_real_palindrome_v2(string_input):
    alphanumerics = ''
    for char in string_input:
        if char.isalnum():
            alphanumerics += char.casefold()

    return is_palindrome(alphanumerics)