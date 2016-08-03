'''
Created on Jul 11, 2016

@author: nghind
'''
# count = [0,] * 101
# while True:
#     x = int(raw_input("Enter an integer: "))
#     if x < 1 or x > 100:
#         break
#     if count[x] >= 1:
#         print x, 'appear again'
#         break
#     count[x] = count[x] + 1
    

count = []
while True:
    x = int(raw_input())
    if x < 1 or x > 100:
        break
    if x in count:
        print x, 'appeared again'
        break
    else:
        count.append(x)
    