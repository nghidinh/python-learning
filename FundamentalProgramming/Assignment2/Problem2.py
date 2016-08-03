'''
Created on Jul 15, 2016

@author: nghind
'''
f = open("info.txt", "r")
line1 = f.readline()
line1 = line1.strip()
line2 = f.readline()
line2 = line2.strip()
f1 = open(line1, "r")
f2 = open(line2, "a")
for s in f1.readlines():
    f2.write(s)
f2.close()
f1.close()
f.close()