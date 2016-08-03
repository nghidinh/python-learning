'''
Created on Jun 25, 2016

@author: Nghi Dinh
'''
date = int(raw_input('Enter a date: '))
month = int(raw_input('Enter a month: '))
year = int(raw_input('Enter a year: '))

if (year == 1868 and month == 9 and date >= 8) or (year == 1868 and month > 9) or (year == 1912 and month == 7 and date < 30) or (year == 1912 and month <= 6) or (1869 <= year <= 1911):
    dif = year - 1868
    if dif % 10 == 1:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Meji', str(dif) + 'st year'
    if dif % 10 == 2:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Meji', str(dif) + 'nd year'
    if dif % 10 == 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Meji', str(dif) + 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Meji', str(dif) + 'th year'
        
elif (year == 1912 and month == 7 and date >= 30) or (year == 1912 and month > 7) or (year == 1926 and month == 12 and date < 25) or (year == 1926 and month < 12) or (1913 <= year <= 1925):
    dif = year - 1912
    if dif % 10 == 1:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Taisho', str(dif) + 'st year'
    if dif % 10 == 2:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Taisho' + str(dif), 'nd year'
    if dif % 10 == 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Taisho', str(dif) + 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Taisho', str(dif) + 'th year'

elif (year == 1926 and month == 12 and date >= 25) or (year == 1989 and month == 1 and date < 7) or (1927 <= year <= 1988):
    dif = year - 1926
    if dif % 10 == 1:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Shouwa', str(dif) + 'st year'
    if dif % 10 == 2:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Shouwa', str(dif) + 'nd year'
    if dif % 10 == 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Shouwa', str(dif) + 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Shouwa', str(dif) + 'th year'

elif (year == 1989 and month == 1 and date >= 7) or (year == 1989 and month >= 2) or year > 1989:
    dif = year - 1989
    if dif % 10 == 1:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Heisei', str(dif) + 'st year'
    if dif % 10 == 2:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Heisei', str(dif) + 'nd year'
    if dif % 10 == 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Heisei', str(dif) + 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print str(date) + '/' + str(month) + '/' + str(year), 'is Heisei', str(dif) + 'th year'
        
        
        
