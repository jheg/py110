"""
This program takes a list and counts the occurances of each element and stores 
them in a dictionary. 
"""
def count_occurrences(my_vehicles):
    occurences = {}
    for element in my_vehicles:
        if element not in occurences.keys():
            element = element.lower()
            occurences.update({element: 1})
        else:
            occurences[element] += 1

    for key, value in occurences.items():
        print(f"{key} => {value}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'suv', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
