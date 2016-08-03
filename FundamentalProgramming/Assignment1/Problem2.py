'''
Created on Jun 25, 2016

@author: Nghi Dinh
'''

s = raw_input("Enter a string: ");
while s != 'end':
    size = len(s)
    out = ''
    for k in range(size - 1, -1, -1):
        out = out + s[k]
    print out
    s = raw_input("Enter a string: ");
