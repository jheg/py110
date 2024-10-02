name = "Jason Hegarty"
print(name.index('Heg'))
print(name.find('Heg'))

sentence = "I am studying python to hopefully one day become a pythonista. I hope to achieve this by writing pythonic python!"

position = sentence.index('python')
# position2 = sentence.index('zzz')
print(position) # 14

position = sentence.find('python')
position2 = sentence.find('zzz') 
print(position) # 14
print(position2) # -1

substring_count = sentence.count('python')
print(substring_count) # 4

substring_count = sentence.count('ZZZ')
print(substring_count) # 0

name = "jason hegarty"
print(name.upper()) # JASON HEGARTY

name = "JASON HEGARTY"
print(name.lower()) # jason hegarty

name = "jason hegarty"
print(name.capitalize()) # Jason Hegarty

name = "Jason Hegarty"
print(name.swapcase()) # jASON hEGARTY

address = '1 Munic Straße'
print(address.swapcase())

address = '1 Munic Straße'
print(address.swapcase().swapcase()) # 1 Munic Strasse

# print(name.index('Z')) # ValueError: substring not found
# the find method differs from the index method in that if a substring is not 
# found it returns -1
print(name.find('Z'))

# you can pass in a start and stop argument into the method
print(name.find('a', 2)) # 9
print(name.find('a', 10)) # -1
print(name.find('a', 0)) # 1

print(name.count('a', 2)) # 1
name_set = set(name)
print(len(name_set))
print(len(name))

print(name.replace('a', 'i'))
print(name)

price = "£30.27"
amount = float(price.replace("£",""))
print(amount)

line1 = "The Low House"
line2 = "Norwich Road"
line3 = "Barham"
line4 = "Suffolk"
postcode = "IP6 0NU"

address = [line1, line2, line3, line4, postcode]
formatted_address = ", ".join(address)
print(formatted_address)

my_list = [1, 2, 3]
# print(', '.join(my_list)) # TypeError: ...
print(', '.join([str(num) for num in my_list])) # 1, 2, 3


line1 = "The Low House"
split_line1 = line1.split()
print(split_line1) # ['The', 'Low', 'House']

print(formatted_address.split(','))

numbers = "one-two-three-four"
print(numbers.split('-', 2)) # ['one', 'two', 'three-four']

fruit = " apple "
print(list(fruit)) # [' ', 'a', 'p', 'p', 'l', 'e', ' ']

print(fruit.strip()) # apple
print(fruit.lstrip()) # apple 
print(fruit.rstrip()) # apple 

fruit = 'apple'
print(fruit.lstrip('a')) # pple 
print(fruit.rstrip('e')) # appl

# str.startswith(substring)
name = "Jason Hegarty"

print(name.startswith('Jason')) # True
print(name.startswith('jason')) # False

name = "Jason"
print(name.isalpha()) # True

line1 = "10LancasterRoad"
print(line1.isalnum()) # True

age = "47"
print(age.isdigit()) # True

empty = "       "
print(empty.isspace()) # True

print(str(True)) # 'True'
print(str([1, 2, 3])) # '[1, 2, 3]'

for char in "Jason Hegarty":
    print(char)

name = "Jason"
index = 0 
while index < len(name):
    print(name[index])
    index += 1