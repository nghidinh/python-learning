'''
Created on Jun 23, 2016

@author: nghind
'''
def pow(x, n):
    power, t = 1, x
    while n > 0:
        if n % 2 == 1:
            power = (power * t)
        n = n / 2
        t = (t * t)
    return power

x = int(raw_input('Enter x: '))
n = int(raw_input('Enter n: '))
print pow(x, n)