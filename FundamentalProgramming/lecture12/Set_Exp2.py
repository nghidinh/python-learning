'''
Created on Jul 14, 2016

@author: nghind
'''
namelist = []
birth_data = {}
file = open('name_book.txt', 'r')
for list in file.readlines():
    (first, last, year, month, day) = list.split()
    namelist.append((last, first))
    birth_data[(last, first)] = (year, month, day)
file.close()
print namelist
print birth_data
                    