'''
Created on Jun 25, 2016

@author: NghiDinh
'''
number = int(raw_input('Enter an integer: '))
remainder = []
while number > 0:
    remainder.append(number % 2)
    number = number / 2
remainder.reverse()
for i in range(0, len(remainder)):
    print remainder[i],
