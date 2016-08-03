
name = ['Nguyen Dinhh Nghi', 'Lai Dac Viet', 'Hoang Long']
phone = ['0975111814', '01666421521', '01652452143']
while True:
    person = raw_input('Enter a name: ')
    try:
        i = name.index(person)
        print phone[i]
    except:
        number = raw_input('Enter a telephone number: ')
        number.append(person)
        phone.append(number)