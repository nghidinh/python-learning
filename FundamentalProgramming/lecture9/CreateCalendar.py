'''
Created on Jun 26, 2016

@author: NghiDinh
'''

dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]; 
year = int(raw_input('Enter a year '))
month = int(raw_input('Enter a month '))
days = year + int((year-1)/4) - int((year-1)/100) + int((year-1)/400);
if ((year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0):
    dates[2] = 29;
i = 0
while (i < month ):
    days = days + dates[i]; i = i + 1
first_day = days % 7
last_date = dates[month];
print ' ', month, '/', year
print ' Su Mo Tu We Th Fr Sa'
i = 0;
while(i <= first_day - 1):
    print ' ',
    i = i + 1
date = 1;
while(date <= last_date):   
    print ' ',
#     if (date < 10): print '',
    print date,
    if((first_day + date -1) % 7 == 6): print
    date = date + 1