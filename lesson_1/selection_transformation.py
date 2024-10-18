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

def mut2_double_numbers(nums):
    for idx in range(len(nums)):
        nums[idx] *= 2

    return nums

print(mut2_double_numbers([1,2,3,4,5]))

def double_if_odd_idx(nums):
    transformed_nums = []

    for idx in range(len(nums)):
        if idx % 2 == 0:
            transformed_nums.append(nums[idx])
        else:
            transformed_nums.append(nums[idx] * 2)
    
    return transformed_nums

print(double_if_odd_idx([1,2,3,4,5]))


"""
Given a dictionary of produce, return the items that match the selection 
criterion. 
"""
def select_type(produce_list, selection_criterion):
    selected_items = {}

    for current_key, current_value in produce_list.items():
        if current_value == selection_criterion:
            selected_items[current_key] = current_value
        
    return selected_items

# Test cases
print(select_type(produce, 'Fruit'))
# {'apple': 'Fruit', 'pear': 'Fruit'}

print(select_type(produce, 'Vegetable'))
# {'carrot': 'Vegetable', 'broccoli': 'Vegetable'}

print(select_type(produce, 'Meat'))
# {}

"""
Given a list of numbers return a new list of numbers where each number is
multiplied by a given multiplier. 
"""

def multiply(nums, multiplier):
    multiplied_nums = []

    for num in nums:
        multiplied_nums.append(num * multiplier)

    return multiplied_nums

# Test case
my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]