VOWELS = 'aeiou'

def double_consonants(text):
    converted_list = []
    for char in list(text):
        if not (char in VOWELS) and (char.isalpha()):
            converted_list.append(char * 2)
        else:
            converted_list.append(char)

    return "".join(converted_list)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")