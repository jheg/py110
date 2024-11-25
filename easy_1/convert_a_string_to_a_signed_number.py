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

def string_to_signed_integer(string):
    is_negative = False
    if string[0] == '-':
        is_negative = True

    total = 0
    multiplier = 1
    list_of_characters = list(string)
    list_of_characters.reverse()
    if list_of_characters[-1] in ['-', '+']:
        list_of_characters.pop(-1)

    for char in list_of_characters:
        total += numbers[char] * multiplier
        multiplier *= 10
    
    if is_negative:
        total = total - (total + total)
    
    return(total)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True