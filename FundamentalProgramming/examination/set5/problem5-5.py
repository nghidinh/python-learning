# - *- coding: utf- 8 - *-
'''
Created on Jul 23, 2016

@author: nghind
'''
f = open('jprogram.txt', 'r')
s = f.read()
s = s.replace('日数', 'dates')
s = s.replace('曜日', 'dayoftheweek')
s = s.replace('年初からの日数', 'numberofdays')
s = s.replace('月名', 'month')
s = s.replace('月始め', 'start')
s = s.replace('曜日', 'dayoftheweek')
fw = open('list20.py','w')
fw.write(s)
fw.close()
f.close()