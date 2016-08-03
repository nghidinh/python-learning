'''
Created on Jul 13, 2016

@author: nghind
'''
def fibo(n):
    if n <= 1: 
        return n
    else: 
        return (fibo(n - 1) + fibo(n - 2))
n = int(raw_input('Enter n: '))
for i in range(n):
    print fibo(i)