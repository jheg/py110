"""
Selection and transformation both use the basics of looping: a loop, a counter, 
a way to retrieve the current value, and a way to exit the loop. Keep those 
four things in mind. 
"""
numbers = [1, 3, 9 ,11, 1, 4, 1]
ones = []

for num in numbers: 
    if num == 1:
        ones.append(num)

print(ones)

fruits = ['apple', 'orange', 'lemon']
transformed_fruits = []

for fruit in fruits:
    transformed_fruits.append(fruit + 's')

print(transformed_fruits)

index = 0
for fruit in fruits:
    fruits[index] = fruit + 's'
    index += 1

print(fruits)

def select_vowels(s):
    vowels = ''

    for char in s: 
        if char in 'aeiouAEIOU':
            vowels += char
    
    return vowels

print(select_vowels('Jason'))
print(select_vowels('Victoria'))
print(select_vowels('Charlie'))
print(select_vowels('Annie'))
print(select_vowels('Pixie'))

print(len(select_vowels('Victoria')))


produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(dict):
    fruits = {}
    for k,v in dict.items(): 
        if v == 'Fruit':
            fruits.update({k:v})

    return fruits

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

def double_numbers(nums):
    doubled_numbers = []
    for num in nums:
        doubled_numbers.append(num * 2)
    
    return doubled_numbers

print(double_numbers([1,2,3,4,5]))

def mut_double_numbers(nums):
    i = 0
    for num in nums:
        nums[i] = num * 2
        i += 1
    
    return nums

print(mut_double_numbers([1,2,3,4,5]))