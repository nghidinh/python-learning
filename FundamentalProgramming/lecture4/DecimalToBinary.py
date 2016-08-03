number = int(raw_input('Enter an integer: '))
binary = ''
while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number = number / 2
print binary