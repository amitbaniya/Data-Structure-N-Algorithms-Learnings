words_with_count = {}
with open('poem.txt', 'r') as f:
    count = 0
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            if word in words_with_count:
                words_with_count[word] += 1
            else:
                words_with_count[word] = 1


print(words_with_count)