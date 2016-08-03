'''
Created on Jun 27, 2016

@author: NghiDinh
'''
year = int(raw_input('Enter a year '))
month = int(raw_input('Enter a month '))
day = int(raw_input('Enter a day '))
if 1968 <= year < 1912: print 'Meiji', year - 1868 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif 1913 <= year < 1926: print 'Taisho', year - 1912 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif 1927 <= year < 1989: print 'Showa', year - 1926 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif year > 1989: print 'Heisei', year - 1989 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif year == 1912:
    if (month, day) <= (7, 29):
        print 'Meiji', year - 1868 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
    else:
        print 'Taisho', year - 1912 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif year == 1926:
    if (month, day) <= (12, 24):
        print 'Taisho', year - 1912 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
    else:   
        print 'Showa', year - 1926 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
elif year == 1989:
    if (month, day) <= (1, 7):
        print 'Showa', year - 1926 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
    else:
        print 'Heisei', year - 1989 + 1, 'Nen', month, 'Gatsu', day, 'Nichi'
