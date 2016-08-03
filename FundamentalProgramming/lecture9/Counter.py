'''
Created on Jun 26, 2016

@author: NghiDinh
'''

# n = int(raw_input('Enter n: '))
# a =[]
# count = [0,]*n
# j = 0
# while n > 0:
#     x = int(raw_input('Enter x: '))
#     for i in range(0, len(a)):
#         if a[i] == x: count[j] = count[j] + 1
#     j += 1
#     a.append(x)
#     n = n - 1
# print a
# print count


#METHOD A
# seq = [0,]*1001
# count = [0,]*1001
# n = 0
# while True:
#     x = int(raw_input('Enter a number '))
#     if x == 0:
#         break
#     found = False
#     for i in range(0, n):
#         if seq[i] == x:
#             print x, 'appeared ', count[i], 'times'
#             count[i] = count[i] + 1
#             found = True
#     if not found:
#         print x, 'appeared 0 times'
#         seq[n] =x
#         count[n] = 1
#         n = n + 1

#METHOD B
# seq = []
# count = []
# while True:
#     x = int(raw_input('Enter a number '))
#     if x == 0:
#         break
#     found = False
#     for i in range(0, len(seq)):
#         if seq[i] == x:
#             print x, 'appeared ', count[i], 'times'
#             count[i] = count[i] + 1
#             found = True
#         if not found:
#             print x, 'appeared 0 times '
#             seq.append(x)
#             count.append(1)

# seq = []
# count = []
# while True:
#     x = int(raw_input('Enter a number '))
#     if x == 0:
#         break
#     found = False
#     if x in seq:
#         i = seq.index(x)
#         print x, 'appeared ', count[i], 'times'
#         count[i] = count[i] + 1
#     else:
#         print x, 'appeared 0 times '
#         seq.append(x)
#         count.append(1)


#METHOD C
count = [0,]*1001
n = 0
while True:
    x = int(raw_input('Enter a number '))
    if x == 0:
        break
    print x, 'appeared ', count[x], 'times'
    count[x] = count[x] + 1