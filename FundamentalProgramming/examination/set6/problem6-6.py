'''
Created on Jul 23, 2016

@author: nghind
'''
f = open('hotels.txt', 'r')
list = []
def cmp1(listi, listj):
    if listi[1] < listj[1]:
        return -1
    else:
        return 1
def cmp2(listi, listj):
    if listi[2] < listj[2]:
        return -1
    else:
        return 1
for line in f.readlines():
    (name, rate, area) = line.split()
    list.append((name, rate, area))
list.sort(cmp2)
for i in range(0, len(list)):
    print list[i][0], list[i][1], list[i][2]