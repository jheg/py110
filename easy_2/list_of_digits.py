def digit_list(number):
    list_of_digits = []

    while number > 0:
        number, remainder = divmod(number, 10)
        list_of_digits.append(remainder)

    return(list(reversed(list_of_digits)))

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True