text = open('twain.txt')

dict_words = {}
count = 0

for line in text:
    line = line.rstrip()
    words = line.split(" ")
    for word in words:
        dict_words[word] = dict_words.get(word, 0) + 1
# print(dict_words)

for word in dict_words:
    print(word, dict_words[word])
