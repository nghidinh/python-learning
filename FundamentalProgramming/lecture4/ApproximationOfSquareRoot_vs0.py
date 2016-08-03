'''
Created on Jun 20, 2016

@author: nghind
'''
t = float(raw_input('Enter a positive number: '))
x = t
while x**2 - t > 0.001 or x**2 - t < -0.001:
    print 'guessed value = ',x
    x = (x + t / x) / 2
print 'guessed value = ', x