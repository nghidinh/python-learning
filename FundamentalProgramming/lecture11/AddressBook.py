'''
Created on Jul 14, 2016

@author: nghind
'''
#coding:UTF-8
dic = {}
f = open('address.txt', 'r')
while True:
    name = f.readline()
    if name == '': 
        break
    name = name.strip()
    address = f.readline()
    address = address.strip()
    dic[name] = address
f.close()
for name in dic:
    print name, dic[name]
