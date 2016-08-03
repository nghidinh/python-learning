'''
Created on Jun 26, 2016

@author: NghiDinh
'''
phone = {}
f = open('TableDef.txt', 'r')
name = ''
while name != 'end':
    name = f.readline()
    name = name.rstrip('\n')
    number = f.readline();
    number = number.rstrip('\n')
    phone[name] = number
    phone[number] = name
f.close()
name = ''
while str != 'end':
    str = raw_input('name?')
    if str != 'end':
        try:
            print phone[str]
        except:
            number = raw_input('Enter a phone number: ')
            phone[str] = number
            phone[number] = str
             
