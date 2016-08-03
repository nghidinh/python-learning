'''
Created on Jun 25, 2016

@author: NghiDinh
'''
# from random import *
# count = [0,]*6
# for i in range(0,1000000):
#     r = int(random() * 6)
# #     r = int(randint(0, 5))
#     print r
#     count[r] = count[r] + 1
# print count

from random import *
n = int(raw_input('Enter a number '))
perm = [0,]*n
for k in range(0, n):
    perm[k] = k
for k in range(n - 1, 1, -1):
    r = int(random() * (k+1))
    print 'r = ', r
    perm[k], perm[r] = perm[r], perm[k]
print perm