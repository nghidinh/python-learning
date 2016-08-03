'''
Created on Jul 11, 2016

@author: nghind
'''
# def pow50(x):
#     def pow4(x):
#         x2 = x * x
#         x4 = x2 * x2
#     def pow10(x):
#         x8 = pow4(x) * pow4(x)
#         return x2 * x8
#     power = pow10(x)
#     power = pow4(power)
#     return power * pow10(x)
#     

def pow50(x):
    n = 50
    power, t = 1, x
    while n > 0:
        if n % 2 == 1:
            power = power * t
        
        n = n / 2
        t = t * t
    return power