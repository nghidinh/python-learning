'''
Created on Jul 13, 2016

@author: nghind
'''
def Hanoi(n, A, B, C):
    if n == 1:
        print '    Move D[ 1 ] from', A, 'to ', B
    else:
        print 'Hanoi(', n - 1, ',', A, ',', C, ',', B, ')'
        Hanoi(n-1, A, C, B)
        print '    Move D[', n, '] from', A, 'to ', B
        print 'Hanoi(', n - 1, ',', C, ',', B, ',', A, ')'
        Hanoi(n-1, C, B, A)
n = int(raw_input('Enter number of boards '))
Hanoi(n,'A', 'B', 'C')