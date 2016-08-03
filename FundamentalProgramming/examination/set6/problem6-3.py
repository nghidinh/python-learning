'''
Created on Jul 15, 2016

@author: nghind
'''
# f1 = open('table1.txt', 'r')
# f2 = open('table2.txt', 'r')
# f3 = open('table3.txt', 'w')
# for line in f1.readlines():
#     f3.write(line)
# for line in f2.readlines():
#     f3.write(line)
# f1.close()
# f2.close()
# f3.close()


s = ''
f1 = open('table1.txt', 'r')
for line in f1.readlines():
    s += line
f2 = open('table2.txt', 'r')
for line in f2.readlines():
    s += line
f3 = open('table3.txt', 'w')
f3.write(s)
f1.close()
f2.close()
f3.close()