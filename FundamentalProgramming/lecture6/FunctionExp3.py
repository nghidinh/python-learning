'''
Created on Jun 20, 2016

@author: Administrator
'''
def middle3_vs1(x, y, z):
    if x > y:
        if y > z:
            return y
        elif x > z:
            return z
        else:
            return x
    elif x > z:
        return x
    elif y > z:
        return z
    else:
        return y
    
def middle3_vs2(x, y, z):
    if x < y:
        x, y = y, x
    if x < z:
        x, z = z, x
    if y < z:
        y, z = z, y
    return y

print middle3_vs2(6, 2, 4)

def middle4(a, b, c, d):
    if a > b: a, b = b, a
    if b > c: b, c = c, b
    if c > d: c, d = d, c
    if a > b: a, b = b, a
    if b > c: b, c = c, b
    return c
print middle4(2, 4, 1, 3)
print middle4(3, 4, 1, 2)
print middle4(4, 3, 2, 1)