'''
Created on Jul 21, 2016

@author: nghind
'''
n = int(raw_input('Enter a number '))
if n % 2 == 0:
    print n, 'is not a prime number'
else:
    for m in range(3,n/2+1, 2):
        if n % m == 0:
            print n, 'is not a prime number'
            m = 0 #bo sung
            break
#     if m >= n/2:
    if m != 0:
        print n, 'is a prime number'