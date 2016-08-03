'''
Created on Jul 4, 2016

@author: nghind
'''
a = raw_input("a = ")
b = raw_input("b = ")
c = raw_input("c = ")
d = raw_input("d = ")
if a > b:
    a, b = b, a
if c > d: 
    c, d = d, c
if d < a or b < c:
    print 'no intersect'
else:
    print 'intersect'