DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    """
    This function takes a whole number (an integer) and converts it to a string 
    represntation of that number. 
    """
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result


def signed_integer_to_string(number):
    if number < 0:
        number = abs(number)
        result = integer_to_string(number)
        result = '-' + result
    elif number > 0:
        result = integer_to_string(number)
        result = '+' + result
    else:
        result = '0'
    
    return result


print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True