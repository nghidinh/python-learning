'''
Created on Jul 23, 2016

@author: nghind
'''
commonFile = open('common.txt', 'r')
commonWord = []
for line in commonFile.readlines():
    words = line.split()
    for word in words:
        commonWord.append(word)
        
def eword(word):
    out = ''
    for i in range(0, len(word)):
        if 'a' <= word[i] <= 'z':
            out = out + word[i]
    return out

filename = raw_input('Enter file name: ')
f = open(filename, 'r')
dict = {}
for line in f.readlines():
    words = line.split()
    for word in words:
        word = word.lower()
        if word in commonWord:
            continue
        if 'a' <= word[0] <= 'z':
            word = eword(word)
            try:
                dict[word] = dict[word] + 1
            except:
                dict[word] = 1
word_list = dict.keys()
word_list.sort()
for word in word_list:
    print word, dict[word]
f.close()