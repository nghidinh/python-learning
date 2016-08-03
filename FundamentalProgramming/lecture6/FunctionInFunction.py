'''
Created on Jun 20, 2016

@author: NghiDinh
'''
#Chuong trinh khong dung do local variable khong anh huong toi outside variable
# def middle3(x, y, z):
#     def exchange(a, b):
#         if a < b:
#             a, b = b, a
#     exchange(x, y)
#     print 'x = ', x, ' y = ', y
#     exchange(x, z)
#     print 'x = ', x, ' z = ', z
#     exchange(y, z)
#     print 'y = ', y, ' z = ', z
#     return y
# a = int(raw_input())
# b = int(raw_input())
# c = int(raw_input())
# print middle3(a, b, c)

#chuong trinh sai khi nhap 3 1 5
def middle3(a, b, c):
    def min2(x, y):
        if x < y:
            return x
        else:
            return y
    x = min2(a, b)
    y = min2(b, c)
    if x > y: return x
    else: return y
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
print middle3(a, b, c)