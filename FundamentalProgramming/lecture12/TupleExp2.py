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
def between(year1, month1, year2, month2, list):
    if year1 > list[1] or year1 == list[1] and month1 > list[2]:
        return False
    if year2 < list[1] or year2 == list[2] and month2 < list[2]:
        return False
    else: return True
    
# def between(year1, month1, year2, month2, list):
#     if (year1, month1) <= (list[1], list[2]) <= (year2,month2):
#         return True
#     else: return False
for list in birth_data:
    if between(1991, 2, 1993, 4, list) > 0:
        print list[0], 'was born in ', list[1], list[2]