'''
Created on Jun 20, 2016

@author: nghind
'''
for n in range(3, 10001):
    div = 1
    for k in range(2, n):
        if n % k == 0:
            div += k
    if div == n:
        print n, ' is perfect number'