'''
Created on Jul 11, 2016

@author: nghind
'''
def gcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    return gcd(y, x % y)
x = int(raw_input('Enter an integer '))
y = int(raw_input('Enter an integer '))
print  gcd(x, y)
print(x, y)