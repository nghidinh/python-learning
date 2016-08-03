# number = int(raw_input())
# if number < 0:
#     number = -number
# else:
#     number += 3
# print number
# 
# number = int(raw_input())
# digit1 = number%10
# digit10 = number/10
# print 'number = ', number
# print 'digit1 + digit10 = ', digit1 + digit10
# if number % (digit1 + digit10) == 0:
#     print number, 'is divisible.'
# else:
#     print number, 'is not divisible.'
# 
# year = int(raw_input())
# if 1868 <= year < 1912:
#     print 'Meiji'
# if 1912 <= year < 1926:
#     print 'Taisho'
# if 1926 <= year < 1989:
#     print 'Showa'
# if 1989 <= year:
#     print 'Heisei'

year = int(raw_input())
if 1868 <= year <= 1912:
    dif = year - 1868
    if dif % 10 ==1:
        print year, 'is Meiji', dif, 'st year'
    if dif % 10 == 2:
        print year, 'is Meiji', dif, 'nd year'
    if dif % 10 == 3:
        print year, 'is Meiji', dif, 'rd year'
    if dif % 10 != 1 and dif % 10 != 2 and dif % 10 != 3:
        print year, 'is Meiji', dif, 'th year'
if 1912 <= year <= 1926:
    print year, 'is Taisho', year - 1912, 'th year'
if 1926 <= year <= 1989:
    print year, 'is Shouwa', year - 1926, 'th year'
if 1989 <= year:
    print year, 'is Heisei', year - 1989, 'th year'

# x1 = float(raw_input('x1 '))
# y1 = float(raw_input('y1 '))
# x2 = float(raw_input('x2 '))
# y2 = float(raw_input('y2 '))
# x3 = float(raw_input('x3 '))
# y3 = float(raw_input('y3 '))
# x4 = float(raw_input('x4 '))
# y4 = float(raw_input('y4 '))
# if x1 > x2:
#     x1, x2 = x2, x1
# if y1 > y2:
#     y1, y2 = y2, y1
# if x3 > x4:
#     x3, x4 = x4, x3
# if y3 > y4:
#     y3, y4 = y4, y3
# if x4 < x1 or x2 < x3 or y4 < y1 or y2 < y3:
#     print 'No intersection'
# else:
#     print 'Non-empty intersection'



