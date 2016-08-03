'''
Created on Jul 4, 2016

@author: nghind
'''
a = int(raw_input("a = "))
b = int(raw_input("b = "))
x = int(raw_input("x = "))
if a > b:
    a, b = b, a
if a <= x <= b:
    print 'x is included in the interval [' + str(a) + ', ' + str(b) + ']'
else:
    print 'x is not included in the interval [' + str(a) + ', ' + str(b) + ']'