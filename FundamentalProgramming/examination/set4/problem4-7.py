'''
Created on Jul 11, 2016

@author: nghind
'''
# count = [0,]*101
# counter = 0
# while True:
#     x = int(raw_input())
#     if x < 1 or x > 100:
#         break
# #     print x, 'appeared', count[x], 'times'
# #     count[x] = count[x] + 1
#     if count[x] == 0:
#         counter = counter + 1
#         count[x] = count[x] + 1
#     else:
#         print counter
#         break
#          

count = []
while True:
    x = int(raw_input())
    if x < 1 or x > 100:
        break
    if x in count:
        print len(count)
        break
    else:
        count.append(x)
    