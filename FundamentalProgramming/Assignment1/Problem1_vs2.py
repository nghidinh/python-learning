
'''
Created on Jun 25, 2016

@author: Nghi Dinh
'''
date = int(raw_input('Enter a date: '))
month = int(raw_input('Enter a month: '))
year = int(raw_input('Enter a year: '))

def display(year, japanCal):
    if japanCal == 'Meji':
        dif = year - 1868
    elif japanCal == 'Taisho':
        dif = year - 1912
    elif japanCal == 'Shouwa':
        dif = year - 1926
    elif japanCal == 'Heisei':
        dif = year - 1989
        
    if dif % 10 == 1:
        print str(date) + '/' + str(month) + '/' + str(year), japanCal, str(dif) + 'st year'
    if dif % 10 == 2:
        print str(date) + '/' + str(month) + '/' + str(year), japanCal, str(dif) + 'nd year'
    if dif % 10 == 3:
        print str(date) + '/' + str(month) + '/' + str(year), japanCal, str(dif) + 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print str(date) + '/' + str(month) + '/' + str(year), japanCal, str(dif) + 'th year'

if (year == 1868 and month == 9 and date >= 8) or (year == 1868 and month > 9) or (1869 <= year <= 1911):
    display(year, 'Meji')
elif year == 1912:
    if  month <= 6:
        display(year, 'Meji')
    elif month == 7:
        if  date < 30:
            display(year, 'Meji')
        else: display(year, 'Taisho')
    elif month > 7: display(year, 'Taisho')
elif 1913 <= year <= 1925: display(year, 'Taisho')
elif year == 1926:
    if month < 12: display(year, 'Taisho')
    elif month == 12:
        if date < 25: display(year, 'Taisho')
        else: display(year, 'Shouwa')
elif 1927 <= year <= 1988:
    display(year, 'Shouwa')
elif year == 1989:
    if month == 1:
        if date < 7:
            display(year, 'Shouwa')
        else: display(year, 'Heisei')
    elif month > 1: display(year, 'Heisei')
elif year > 1989: display(year, 'Heisei')
        
        
        



        
