names = [
    'Jason',
    'Victoria',
    'Charlie',
    'Annie'
    ]

for (idx, name) in enumerate(names):
    print(f'{idx}: {name}')

# works without parentheses
for idx, name in enumerate(names):
    print(f'{idx:^5}: {name}')