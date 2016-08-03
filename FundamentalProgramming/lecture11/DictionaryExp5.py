'''
Created on Jun 26, 2016

@author: NghiDinh
'''
phone = {'Dinh Nghi':'0975111814', 'Bich Ha':'01666786034', 'Van X':'0165243521'}
name = phone.keys()
def cmp(name1, name2):
    (first1, last1) = name1.split()
    (first2, last2) = name2.split()
    if last1 < last2:
        return -1
    else:
        return 1
name.sort(cmp)
for words in name:
    print words, phone[words]