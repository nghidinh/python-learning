'''
Created on Jun 26, 2016

@author: NghiDinh
'''
dic = {'Nghi': 23, 23: 'Nghi', 'Long': 25, 'Hao': 24, 'Dat': 23, 'Trinh': 24, 'Viet': 23}
for n, v in dic.items():
    print 'n =',n, 'v =', v
print '=============================='
for n in dic.keys():
    print dic[n]
print '=============================='
for v in dic.values():
    print v
    
# phone = {}
# f = open('TableDef.txt', "r")
# name = ''
# while name != 'end':
#     name = f.readline()
#     name = name.rstrip('\n')
#     number = f.readline();
#     number = number.rstrip('\n')
#     phone[name] = number
#     phone[number] = name
# f.close()
# str = ''
# print phone
# while str != 'end':
#     str = raw_input()
#     if str != 'end':
#         try:
#             print phone[str]
#         except:
#             print 'no such name or phone'