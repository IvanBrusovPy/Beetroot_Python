sentence = input("Type a sentence:\n").split()
words_count = {}
for i in sentence:
    a = sentence.count(i)
    words_count[i] = a
print(words_count)