'''
Created on Jun 23, 2016

@author: nghind
'''
def gcd(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    return gcd(n, m % n)
print gcd(954, 288)