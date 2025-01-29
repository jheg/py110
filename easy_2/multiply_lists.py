def multiply_list(l1, l2):
    list_of_products = []
    for position in range(0, len(l1)):
        list_of_products.append(l1[position] * l2[position])
    
    return list_of_products

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True