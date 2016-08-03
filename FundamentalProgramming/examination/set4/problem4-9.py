'''
Created on Jul 11, 2016

@author: nghind
'''
n = int(raw_input("Enter n: "))
list = []
for i in range(0, n):
    x = int(raw_input("Enter an element: "))
    list.append(x)
#     list.append(i)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if list[i] > list[j]:
            print "pair(" + str(list[i]) + "," + str(list[j]) + ") is an inversion"
