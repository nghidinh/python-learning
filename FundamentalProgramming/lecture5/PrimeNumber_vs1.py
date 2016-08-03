'''
Created on Jun 20, 2016

@author: nghind
'''
n = int(raw_input('Enter a number: '))
for m in range(2, n):
    if n % m == 0:
        print n, 'is not a prime number'
        break
if m == n - 1:
    print n,' is a prime number'