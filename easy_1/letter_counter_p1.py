def word_sizes_v1(string):
    words = string.split()
    word_count_instances = {}

    for word in words: 
        count = len(word)
        if count not in word_count_instances.keys():
            word_count_instances[count] = 1
        else:
            word_count_instances[count] += 1

    return word_count_instances


def word_sizes(string):
    words = string.split()
    word_count_instances = {}

    for word in words: 
        count = len(word)
        word_count_instances.setdefault(count, 0)
        word_count_instances[count] += 1

    return word_count_instances

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})