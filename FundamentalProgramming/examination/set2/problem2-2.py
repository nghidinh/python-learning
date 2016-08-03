'''
Created on Jul 13, 2016

@author: nghind
'''
x = int(raw_input('Enter an integer '))
y = int(raw_input('Enter an integer '))
z = int(raw_input('Enter an integer '))
if x > y:
    if y > z:
        print y, 'is the second largest.'
    elif x < z:
        print x, 'is the second largest.' #da sua
    else:
        print z, 'is the second largest.' #da sua
elif x > z:
    print x, 'is the second largest.'
elif y > z:
    print z, 'is the second largest.'
else:
    print y, 'is the second largest.'