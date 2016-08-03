'''
Created on Jul 23, 2016

@author: nghind
'''
sum = 0
while True:
    x = int(raw_input('Enter an integer: '))
    if x == 0: break
    sum += x**2
print sum
    