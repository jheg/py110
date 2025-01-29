def union(list1, list2):
    combined_list = list1 + list2
    return set(combined_list)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True