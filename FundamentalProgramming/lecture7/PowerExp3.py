'''
Created on Jun 23, 2016

@author: nghind
'''
def pow(x, n):
    power, t = 1, x
    while n > 0:
        if n % 2 == 1:
            print 'power = power * t <=>', 'power', '=', power, '*', t
            power = power * t
        print 'n = n / 2 <=> ', 'n', '=', n, '/', 2
        n = n / 2
        print 't = t * t <=>', 't', '=', t, '*', t
        t = t * t
    return  power
x = int(raw_input('Enter a positive integer: '))
n = int(raw_input('Enter a positive integer: '))
print pow(x, n)
x = float(raw_input('Enter a value: '))
print pow(x, n)