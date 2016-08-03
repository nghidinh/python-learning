'''
Created on Jul 21, 2016

@author: nghind
'''
def pow(x, n):
    power, t = 1, x
    while n > 0:
        if n % 2 == 1:
            power = power * t
        n = n / 2
        t = t * t
    return power
    
n = int(raw_input('Enter n: '))
t, sum = 1, 1
for i in range(2, n + 1):
    t = t + pow(2, i)
    print 't =', t
    sum += t
    print 'sum =', sum
print sum