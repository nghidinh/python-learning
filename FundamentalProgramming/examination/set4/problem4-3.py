'''
Created on Jul 11, 2016

@author: nghind
'''
# def pow100(x):
#     def pow10(x):
#         x2 = x * x
#         x4 = x2 * x2
#         x8 = x4 * x4
#         return x8 * x2
#     power = pow10(x)
#     power = pow10(power)
#     return power
# print pow100(2)

def pow100(x):
    n = 100
    power, t = 1, x
    while n > 0:
        if n % 2 == 1:
            power = power * t
        
        n = n / 2
        t = t * t
    return power