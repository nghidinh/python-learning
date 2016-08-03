# coding: UTF‐8
dayoftheweek= ['Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.', 'Mon.', 'Tue.']
month= ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
'August', 'September', 'October', 'November', 'December']
dates= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start= [1, ]*13
for i in range(1, 13):
start[i] = start[i‐1] + dates[i‐1]
年初からのdates= int(raw_input('年初からのdates'))
if 年初からのdates> 365: print 'out of days'
for i in range(2, 13):
if 年初からのdates< start[i]:
break
print month[i‐1], 年初からのdates– start[i‐1] + 1, dayoftheweek[年初からのdates% 7]