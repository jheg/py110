def word_sizes(string):
    words = []
    word_count_instances = {}
    for word in string.split():
        cleaned_word = ''
        for char in word:
            if char.isalnum():
                cleaned_word += char
        words.append(cleaned_word)

    for word in words:
        count = len(word)
        word_count_instances.setdefault(count, 0)
        word_count_instances[count] += 1

    return word_count_instances


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})