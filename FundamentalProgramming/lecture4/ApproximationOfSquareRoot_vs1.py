'''
Created on Jun 20, 2016

@author: nghind
'''
x = float(raw_input('Enter a positive number: '))
low, high = 0, x
guess = (low + high) / 2
while 0.01 < guess**2 - x or guess**2 - x < -0.01:
    print 'guessed value = ', guess
    if guess**2 - x > 0:
        high = guess
    else:
        low = guess
    print 'low, high = ', low, high
    guess = (low + high) / 2
print guess