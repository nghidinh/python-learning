'''
Created on Jul 11, 2016

@author: nghind
'''
# coding: UTF‐8
曜日= [‘Wed.’, ‘Thu.’, ‘Fri.’, ‘Sat.’, ‘Sun.’, ‘Mon.’, ‘Tue.’]
月名= ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']
日数= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
月始め= [1, ]*13
for i in range(1, 13):
月始め[i] = 月始め[i‐1] + 日数[i‐1]
年初からの日数= int(raw_input(‘年初からの日数'))
if 年初からの日数> 365: print 'out of days'
for i in range(2, 13):
if 年初からの日数< start[i]:
break
print 月名[i‐1], 年初からの日数– 月始め[i‐1] + 1, 曜日[年初からの日数% 7]