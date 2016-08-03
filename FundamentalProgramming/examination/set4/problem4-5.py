'''
Created on Jul 11, 2016

@author: nghind
'''
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
print factorial(5)