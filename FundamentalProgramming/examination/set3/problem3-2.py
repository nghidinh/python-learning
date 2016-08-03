'''
Created on Jul 21, 2016

@author: nghind
'''
n = int(raw_input('Enter n: '))
sum = 0
squareSum = 0
for i in range(0, n):
    x = float(raw_input('Enter x: '))
    sum = sum + x
    squareSum = squareSum + x**2
print 'avg = ', sum / n
print 'square sum: ', squareSum - sum**2 / n