'''
Created on Jun 26, 2016

@author: NghiDinh
'''
dayoftheweek = ['Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.', 'Mon.', 'Tue.']
month = ['none', 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'Septemper', 'Octover', 'November', 'December']
dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start = [1, ]*13

for i in range(1, 13):
    start[i] = start[i - 1] + dates[i - 1]
    #print 'start[' + str(i) + '] = ' + str(start[i])

numberofdays = int(raw_input('Enter number of days: '))
if numberofdays > 365: print 'out of days'
for i in range(2, 13):
    if numberofdays < start[i]:
        break
print month[i - 1], numberofdays - start[i - 1] + 1, dayoftheweek[numberofdays%7]