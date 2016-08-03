'''
Created on Jun 26, 2016

@author: NghiDinh
'''
phone = {'Nghi':'0975111814', 'Ha':'01666786034'}
name = ''
while name != 'end':
    name = raw_input('name?')
    if name != 'end':
        print phone[name]