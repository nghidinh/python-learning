'''
Created on Jul 11, 2016

@author: nghind
'''
# def diff(a, b, c):
#     if a > b: 
#         a, b = b, a
#     if b > c:
#         b, c = c, b
#     if a > b: 
#         a, b = b, c
#     if a == b == c:
#         return 0
#     elif a == b < c:
#         return c - b - 1
#     elif a < b == c:
#         return b - a - 1
#     elif a < b < c:
#         return c - a - 2
# print diff(4, 4, 9)

def diff(a, b, c):
    if a == b == c:
        return 1
    elif (a == b) or (b == c) or (a == c):
        return 2
    else: return 3
    
print diff(2, 5, 7)