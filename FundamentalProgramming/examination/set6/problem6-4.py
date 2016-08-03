'''
Created on Jul 23, 2016

@author: nghind
'''
dict = {}
while True:
    x = int(raw_input('Enter integer: '))
    if x == 0:
        break
    try:
        dict[x] = dict[x] + 1
    except:
        dict[x] = 0
    print x, 'appeared', dict[x], 'times'