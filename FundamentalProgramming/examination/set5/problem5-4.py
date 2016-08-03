'''
Created on Jul 24, 2016

@author: nghind
'''
year = int(raw_input())
dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayOfWeeks = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days = year + int((year - 1) / 4) - int((year - 1) / 100) + int((year - 1) / 400)
if ((year % 4 == 0) and (year % 100) != 0 or (year % 400) == 0):
    dates[2] = 29
firstDay = days % 7
print dayOfWeeks[firstDay]