'''
Created on Jun 20, 2016

@author: nghind
'''
n = int(raw_input('Enter a number: '))
if n % 2 == 0:
    print n, ' is not a prime number'
else:
    m = 3
    while m * m <= n and n % m != 0:
        m = m + 2
    if m * m <= n:
        print n, ' is not a prime number'
    else:
        print n, ' is a prime number'