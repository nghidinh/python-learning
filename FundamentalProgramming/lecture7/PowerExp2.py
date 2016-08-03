'''
Created on Jun 23, 2016

@author: nghind
'''
def power10(x):
    x2 = (x*x)%1000
    x4 = (x2*x2)%1000
    x8 = (x4*x4)%1000
    return (x2*x8)%1000
n = int(raw_input('Enter a positive number: '))
# power = power10(n)
# power = power10(power)
# power = power10(power)
# power = power10(power)
# power = power10(power)
# power = power10(power)
# power = power10(power)
# print power

power = n
for k in range(0, 7):
    power = power10(power)
print power