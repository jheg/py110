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

# Good example of a use case. Suppose you want to iterate over a string and count the instances for each character without duplicating characters
name = "Jason Hegarty"
counts = {}
for char in name:
	counts.setdefault(char, 0)
	counts[char] += 1

print(counts)