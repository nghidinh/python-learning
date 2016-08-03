'''
Created on Jun 23, 2016

@author: nghind
'''
n = (int(raw_input('Enter a positive number: ')))
power = 1
for k in range(0, 10000000):
    power = (power*n) % 1000
print power%1000
