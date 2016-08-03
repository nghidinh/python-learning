'''
Created on Jun 20, 2016

@author: nghind
'''
n = int(raw_input('Enter n = '))
sum, total_sum = 0, 0
for k in range(1, n + 1):
    sum += k
    total_sum += sum
print 'sum = ', total_sum