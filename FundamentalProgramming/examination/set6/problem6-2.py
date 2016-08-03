'''
Created on Jul 15, 2016

@author: nghind
'''
listBook = []
f = open('book.txt', 'r')
for line in f.readlines():
    (title, author, publishingCompany, year, numberOfPages) = line.split(',')
    listBook.append((title, author, publishingCompany, year, numberOfPages))
n = int(raw_input('Enter a number: '))
if n == 1:
    s = raw_input('Enter title: ')
    for i in range(0, len(listBook)):
        if s in listBook[i][0]:
            print listBook[i]
if n == 2:
    s = raw_input('Enter author name: ')
    for i in range(0, len(listBook)):
        if s in listBook[i][1]:
            print listBook[i]