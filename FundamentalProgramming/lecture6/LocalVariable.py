'''
Created on Jun 20, 2016

@author: Administrator
'''
def middle3(x, y, z):
    if x < y:
        x, y = y, x
    if x < z:
        x, z = z, x
    if y < z:
        y, z = z, y
    return y
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
print middle3(x, y, z)
print x, y, z