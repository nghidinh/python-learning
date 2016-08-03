'''
Created on Jul 14, 2016

@author: nghind
'''
filename = raw_input('Enter filename: ')
f = open(filename, "r")
# words = []
# count = []
# for line in f.readlines():
#     line_word = line.split()
#     for word in line_word:
#         if 'a' <= word[0] <= 'z' or 'A' <= word[0] <= 'Z':
#             if word in words:
#                 i = words.index(word)
#                 count[i] += 1
#             else:
#                 words.append(word)
#                 count.append(1)
# for i in range(0, len(words)):
#     print words[i], '==>', count[i]
# f.close()

count = {}
for line in f.readlines():
    words = line.split()
    for word in words:
        word = word.lower()
        if 'a' <= word[0] <= 'z' or 'A' <= word[0] <= 'Z':
            try:
                count[word] = count[word] + 1
            except:
                count[word] = 1
for word in count:
    print word, count[word]
f.close()