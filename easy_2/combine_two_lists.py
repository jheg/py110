def interleave(first_list, second_list):
    combined_list = []
    for i in range(len(first_list)):
        combined_list.extend([first_list[i], second_list[i]])
        # combined_list.append(second_list[i])
    return combined_list


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True