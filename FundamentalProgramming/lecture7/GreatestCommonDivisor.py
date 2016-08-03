'''
Created on Jun 23, 2016

@author: nghind
'''
x = int(raw_input('Enter a positive integer'))
y = int(raw_input('Enter a positive integer'))
z = x
if x < y:
    z = y
for k in range(2, z / 2 + 1):
    if x % k == 0 and z % k == 0:
        print k, 'is a common divisor'
        
        
x = int(raw_input('Enter a positive integer'))
y = int(raw_input('Enter a positive integer'))
z = x
if x < y:
    z = y
for k in range(z / 2, 1, -1): 
    if x % k == 0 and y % k == 0:
        print k, 'is the GCD'
        break