'''
Created on Jun 20, 2016

@author: Administrator
'''
def Max3(x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z
print Max3(12, 32, 24)