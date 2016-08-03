'''
Created on Jul 11, 2016

@author: nghind
'''
# three lowest digit of 10th power

#Cách 1: mất 10 lần tính toán, biến power sẽ rất lớn
n = int(raw_input('Enter a positive number '))
power = 1
for k in range(0, 10):
    power = power * n
print power % 1000

#Cách 2: mất 10 lần tính toán, biến power lưu dữ liệu nhỏ hơn
n = int(raw_input("Enter a positive number: "))
power = 1
for k in range(0, 10):
    power = (power * n) % 1000
print power

#Cách 3: mát 4 lần tính toán, nếu gọi hàm 7 lần ta tính được 10000000 power
def pow10(x):
    x2 = (x * x) % 1000
    x4 = (x2 * x2) % 1000
    x8 = (x4 * x4) % 1000
    return (x8 * x2) % 1000
n = int(raw_input("Enter a positive number: "))
power = n
for k in range(0, 7):       # chỉ mất 7 x 4 = 28 lần tính toán
    power = pow10(power)
print power