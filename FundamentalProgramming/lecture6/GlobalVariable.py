'''
Created on Jun 20, 2016

@author: Administrator
'''
def min2(x, y):
    global count
    count += 1
    if x < y:
        return x
    else:
        return y
count = 0
x = int(raw_input())
y = int(raw_input())
z = min2(x, y)
for i in range(0, 5):
    x = int(raw_input())
    z = min2(x, z)
print 'count = ', count
print 'minimum = ', z