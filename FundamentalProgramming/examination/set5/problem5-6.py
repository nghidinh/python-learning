'''
Created on Jul 13, 2016

@author: nghind
'''
def min(a, b):
    if a == b:
        return L[a]
    elif L[b] < min(a, b-1):
        return L[b]
    else:
        return min(a, b-1)
n = int(raw_input('Enter number of data '))
L = [0.0,]*n
for j in range(0, n):
    L[j] = int(raw_input('Enter a data '))
print min(0, n-1)