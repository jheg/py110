CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def count_max_adjacent_consonants(word):
    letters = word.split(' ')
    formatted_word = ''.join(letters)
    highest_count = 0 
    adjacent_characters = ''
    for character in formatted_word: 
        if character in CONSONANTS:
            adjacent_characters += character
            if (len(adjacent_characters) > highest_count) and (len(adjacent_characters) > 1):
                highest_count = len(adjacent_characters)
        elif (len(adjacent_characters) > highest_count) and (len(adjacent_characters) > 1):
            highest_count = len(adjacent_characters)
        
            adjacent_characters = ''
    
    return highest_count    

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa'] 

my_list = ['can can', 'toucan', 'batman', 'salt pan'] 
print(sort_by_consonant_count(my_list)) 
# ['salt pan', 'can can', 'batman', 'toucan'] 

my_list = ['bar', 'car', 'far', 'jar'] 
print(sort_by_consonant_count(my_list)) 
# ['bar', 'car', 'far', 'jar'] 

my_list = ['day', 'week', 'month', 'year'] 
print(sort_by_consonant_count(my_list)) 
# ['month', 'day', 'week', 'year'] 

my_list = ['xxxa', 'xxxx', 'xxxb'] 
print(sort_by_consonant_count(my_list)) 
# ['xxxx', 'xxxb', 'xxxa']



# print(count_max_adjacent_consonants('dddaa')) # 3 
# print(count_max_adjacent_consonants('ccaa')) # 2 
# print(count_max_adjacent_consonants('baa')) # 0 
# print(count_max_adjacent_consonants('aa')) # 0 
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4	  