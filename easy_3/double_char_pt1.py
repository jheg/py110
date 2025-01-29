def repeater(text):
    text_list = list(text)
    list_of_repeats = []
    for char in text_list: 
        list_of_repeats.append(char * 2)

    return "".join(list_of_repeats)

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True