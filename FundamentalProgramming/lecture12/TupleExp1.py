'''
Created on Jun 27, 2016

@author: NghiDinh
'''

birth_data = [('Dinh Nghi', 1993, 1, 9),
              ('Khanh Trinh', 1992, 3, 5),
              ('Hoang Long', 1991, 8, 14),
              ('Minh Dat', 1993, 2, 4),
              ('Dac Viet', 1993, 9, 24),
              ('Le Hao', 1992, 7, 14),]
for list in birth_data:
    if 1993 <= list[1] <= 1995:
        print list[0], 'was born in ', list[1]