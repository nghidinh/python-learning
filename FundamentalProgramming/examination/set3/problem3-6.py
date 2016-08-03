'''
Created on Jul 21, 2016

@author: nghind
'''
n = int(raw_input('Enter an integer: '))
s, t = 0, 0
for k in range(1, n + 1):
    s = s + float(1.0 / k)
    t = t + s
print t