'''
Created on Jul 14, 2016

@author: nghind
'''
s = set([1, 3, 5, 7])
print s
t = set([7, 5, 3, 1])
print t
w = set([2, 4, 6, 8])
print w
print s.union(w)
for i in s:
    print i
print '==================='
print w
for i in w:
    print i
    
print s.difference(t)
s.add(8)
s.remove(7)
print s
print len(s)
print s.intersection(t)