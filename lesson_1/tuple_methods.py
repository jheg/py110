# Tuple unpacking
shades = ('crimson', 'emerald', 'azure')
r, g, b = shades

print(f'{r = }, {g = }, {b = }') # r = 'crimson', g = 'emerald', b = 'azure'

# tuple.count()
shades = ('crimson', 'emerald', 'azure')
print(shades.count('crimson')) # 1
print(shades.count('red')) # 0

# tuple.index()
shades = ('crimson', 'emerald', 'azure', 'crimson')

print(shades.index('crimson')) # 0
print(shades.index('crimson', 1)) # 3
# print(shades.index('crimson', 1, 3)) # ValueError: 'crimson' not in tuple
# print(shades.index('red')) # ValueError: 'red' not in tuple

name = "Jason Lee Hegarty"
name_tuple = tuple(name)
print(name_tuple) # ['J', 'a', 's', 'o', 'n', ' ', ...]

person = {
	"name": "Jason Hegarty",
	"dob": "30/11/1976",		  
}

kv_tuple = tuple(person.items())

# This will create a window into the dictionary. Any changes to the dict will 
# be reflected in k_window
k_window = person.keys()
v_tuple = tuple(person.values())
print(kv_tuple) # (('name', 'Jason Hegarty'), ('dob', '30/11/1976'))
print(k_window) # ('name', 'dob')
print(v_tuple) # ('Jason Hegarty', '30/11/1976')

person['name2'] = "Victoria Rance"
person['dob2'] = "06/12/1977"
print(kv_tuple) # (('name', 'Victoria Rance'), ('dob', '06/12/1977'))
print(k_window) # ('name', 'dob', 'name2', 'dob2')
print(v_tuple) # ('Victoria Rance', '06/12/1977')

shades = ('crimson', 'emerald', 'azure', 'crimson')

for color in shades: 
    print(color)

for (index, color) in enumerate(shades):
    print(f'{index = } {color = }')