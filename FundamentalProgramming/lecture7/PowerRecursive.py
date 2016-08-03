'''
Created on Jun 23, 2016

@author: nghind
'''
#Cách 1: Gọi pow(x, n / 2) nhiều lần
def pow(x, n):
    if n == 1:
        return x % 1000
    if n % 2 == 0:
        return (pow(x, n / 2) * pow(x, n / 2)) % 1000
    else:
        return (pow(x, n / 2) * pow(x, n / 2) * x) % 1000

x = int(raw_input('Enter a positive integer: '))
n = int(raw_input('Enter a positive integer: '))
print pow(x, n)

#Cách 2: Giảm lãng phí bằng cách lưu giá trị của pow(x, n/2) vào biến half
def pow_vs2(x, n):
    if n == 1:
        return x % 1000
    half = pow(x, n / 2)
    if n % 2 == 0:
        return (half * half) % 1000
    else:
        return (half * half * x)%1000