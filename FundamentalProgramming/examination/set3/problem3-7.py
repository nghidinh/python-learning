'''
Created on Jul 21, 2016

@author: nghind
'''
c = []
for n in range(1, 10000):
    a = [1]
    for i in range(2, n / 2 + 1):
        if n % i == 0:
            a.append(i)
    b = []
    for i in range(0, len(a)):
        b.append(0)
    sum = 0
    for i in range(len(a) - 1, -1, -1):
        sum = sum + a[i]
        if sum == n:
            c.append(n)
            b[i] = sum
            break
        elif sum < n:
            b[i] = sum
        else:
            b[i]= 0
            sum = sum - a[i]
print c

for n in range(1, 10000):
    a = [1]
    sum = 0
    for i in range(2, n / 2 + 1):
        if n % i == 0:
            a.append(i)
            sum += i
            if sum > n:
                print n
                break
