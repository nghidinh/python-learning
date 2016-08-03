'''
Created on Jul 4, 2016

@author: nghind
'''
low, high = 1.5, 3.0
guess = (low + high) / 2
while not -0.01 < guess * guess - 3.0 * guess + 1 < 0.01:
#     print '=========', guess * guess - 3.0 * guess + 1
    if guess * guess - 3.0 * guess + 1 > 0:#da sua
        high = guess
        print 'high = ', high
    else:
        low = guess
        print 'low = ', low
    guess = (low + high) / 2
print guess