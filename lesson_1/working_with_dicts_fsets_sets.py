outgoing = {
	"amount": 27.12,
	"frequency": "monthly"	
}
print(f'£{outgoing["amount"]}') # £27.12
# print(f'{outgoing["currency"]}') # KeyError: 'currency'

outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
}

del outgoing['category']
print(outgoing) # {'amount': 27.12, 'frequency': 'monthly'}
# del outgoing['currency'] # KeyError: 'currecny'

# Checking existence of Key
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
}

print('amount' in outgoing) # True
print('category' in outgoing) # True
del outgoing['category']
print('category' in outgoing) # False

# dict.copy()
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
	"payments": [27.12, 27.12, 27.12]
}
duplicate_outgoing = outgoing.copy()
del outgoing['category']

print(outgoing) # {'amount': 27.12, 'frequency': 'monthly'}
print(duplicate_outgoing) # {'amount': 27.12, 'frequency': 'monthly', 'category': 'subscription'}

outgoing['payments'].append(27.12)
print(outgoing) # {'amount': 27.12, 'frequency': 'monthly', "payments": [27.12, 27.12, 27.12, 27.12]}
print(duplicate_outgoing) # {'amount': 27.12, 'frequency': 'monthly', 'category': 'subscription', "payments": [27.12, 27.12, 27.12, 27.12]}

outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
}
print(outgoing.get('amount')) # 27.12
print(outgoing.get('payments')) # None
print(outgoing.get('currency', 'gbp'))
print(outgoing)

outgoing.setdefault('amount', 10.00 )
print(outgoing)

outgoing.setdefault('currency', 'gbp')
print(outgoing)

# Good example of a use case. Suppose you want to iterate over a string and 
# count the instances for each character without duplicating characters
name = "Jason Hegarty"
counts = {}
for char in name:
	counts.setdefault(char, 0)
	counts[char] += 1

print(counts)

# dict.pop()
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
}
previous_amount = outgoing.pop('amount')
# outgoing.pop('amount') # KeyError: 'amount'
print(previous_amount) # 27.12

# pass a default to avoid KeyError
amount = outgoing.pop('amount', 0)
print(amount)

# dict.popitem() returns a tuple of the last item in dict
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",
}
last_item = outgoing.popitem()
print(last_item) # ('category', 'subscription')

# dict.update(dict)
person = {
	"first_name": "Jason",
	"last_name": "Hegarty",
	"dob": "30/11/1976",
}
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",		
}
person.update(outgoing)
print(person)

# | merge operator returns a new dictionary 
person = {
	"first_name": "Jason",
	"last_name": "Hegarty",
	"dob": "30/11/1976",
}
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",		
}
merged_dict = person | outgoing
print(f'{merged_dict = }')

# |= update operator mutates dict1
person = {
	"first_name": "Jason",
	"last_name": "Hegarty",
	"dob": "30/11/1976",
}
outgoing = {
	"amount": 27.12,
	"frequency": "monthly",	
	"category": "subscription",		
}
# this is the same as person.update(outgoing)
person |= outgoing 
print(person)

list_of_pairs = [
	 ["name", "Jason"],
	 ["age", "47"],
	 ["location", "England"],
]

dict_conversion = dict(list_of_pairs)
print(dict_conversion)

tuple_of_pairs = (
	 ("name", "Jason"),
	 ("age", "47"),
	 ("location", "England"),
)

dict_conversion = dict(tuple_of_pairs)
print(dict_conversion)

# converting to set. Remember sets contain unique elements 
fruit = "apple"
my_list = ["name", "Jason"]
my_tuple = ("name", "Jason")

print(set(fruit)) # {'p', 'e', 'a', 'l'}
print(set(my_list))
print(set(my_tuple))
print(set(outgoing))

