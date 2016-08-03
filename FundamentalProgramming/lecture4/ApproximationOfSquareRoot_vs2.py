'''
Created on Jun 20, 2016

@author: nghind
'''
x = float(raw_input('Enter a positive number: '))
low, high = 0, x
while True:
    guess = (low + high) / 2
    print 'low = ',low, 'high = ', high, 'guess = ', guess
    if guess**2 - x > 0:
        high = guess
    else:
        low = guess
    if -0.001 <= guess**2 -x <= 0.001:
        break
    print guess