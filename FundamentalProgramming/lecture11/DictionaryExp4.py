'''
Created on Jun 26, 2016

@author: NghiDinh
'''
phone = {'Nghi':'0975111814', 'Ha':'01666786034', 'X':'0165243521'}
name = phone.keys() #define a list name as a collection of the keys
name.sort() #sort in the alphabetical order
for words in name: #scan names in the sorted order
    print words, phone[words]
