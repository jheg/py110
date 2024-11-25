def swap(words):
    words_list = words.split()
    for idx in range(len(words_list)):
        words_list[idx] = swap_first_last(words_list[idx])

    return ' '.join(words_list)

def swap_first_last(word):
    if len(word) == 1:
        return word
    
    return word[-1] + word[1:-1] + word[0]


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True