'''
Created on Jun 25, 2016

@author: Nghi Dinh
'''

# def prime(n):
#     m = 1
#     if n % 2 == 0:
#         return False
#     else:
#         for i in range(3, n / 2 + 1, 2):
#             if n % i == 0:
#                 m = 0
#                 break
#         if m == 1:
#             print n, 'is a prime number'
#             
n = int(raw_input('Enter n: '))
if n <= 0: n = 1 
count = 0
while count < 10:
    n = n + 1
    if n == 2: 
        print n, 'is a prime number'
        count += 1
        continue
    m = 1
    if n % 2 == 0:
        continue
    else:
        for i in range(3, n / 2 + 1, 2):
            if n % i == 0:
                m = 0
                break
        if m == 1:
            print n, 'is a prime number'
            count = count + 1
