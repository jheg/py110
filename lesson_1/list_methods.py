# List unpacking
shades = ['crimson', 'emerald', 'azure']
r, g, b = shades

print(f'{r = }, {g = }, {b = }') # r = 'crimson', g = 'emerald', b = 'azure'

# list.count(object)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1]
print(nums.count(1)) # 3

# returns list if object not present in list 
print(nums.count(11)) # 0

# list.index()
print(nums.index(1)) # 0

# Can take optional start and end arguments
print(nums.index(1, 10, 11)) # 10

# Raises an error if object not present in list
# print(nums.index(10)) # ValueError: 10 is not in list

# list.append() => Adds an item to the end of the list
nums.append('A') 
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A']

# list.insert() => Inserts an element into the specified position 
nums.insert(0, 'A') 
print(nums) # ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A']

# list.extend() => Adds the contents of another iterable to the list
nums.extend(['Jason', 'Vic'])
print(nums) # ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A', 'Jason', 'Vic']

# list.remove()
nums.remove('A')
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A', 'Jason', 'Vic']

# nums.remove('B') # ValueError: 'B' not in list

# list.pop()
nums.pop() # 'Vic'
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A', 'Jason']

nums.pop(0) # 1
print(nums) # [2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 'A', 'Jason']

# [].pop() # IndexError: pop from empty list

# list.reverse()
nums.reverse()
print(nums) # ['Jason', 'A', 1, 1, 9, 8, 7, 6, 5, 4, 3, 2]

# list.sort()
rates = ['1.18', '22.18', '1.68', '4.18', '12.18']

rates.sort()
print(rates) # ['1.18', '1.68', '12.18', '22.18', '4.18']

# sort takes optional keyword arguments
rates.sort(key=float)
print(rates) # ['1.18', '1.68', '4.18', '12.18', '22.18']

rates.sort(key=float, reverse=True)
print(rates) # [ '22.18', '12.18', '4.18', '1.68', '1.18']

names = ['Victoria', 'annie', 'Charlie', 'pixie', 'JASON']
names.sort()
print(names)

# Now let's do a case insensitive sort
names.sort(key=str.casefold)
print(names) # ['annie', 'Charlie', 'JASON', 'pixie', 'Victoria']

mixed_list = [1, 2, 'House']
# mixed_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str'