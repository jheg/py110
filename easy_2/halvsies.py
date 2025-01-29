def halvsies(undivided_list):
    returned_list = [[],[]]

    # cacl halfway point of undivided_list
    if len(undivided_list) % 2 == 0:
        half = len(undivided_list) // 2
    else:
        half = (len(undivided_list) // 2) +1
    
    returned_list[0] = undivided_list[0:half]
    returned_list[1] = undivided_list[half:]

    return(returned_list)

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])