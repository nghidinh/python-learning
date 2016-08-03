s = raw_input('Enter a binary string: ')
decimal = 0
p = 1
for i in range(len(s) - 1, -1, -1):
    decimal += p*int(s[i])
    p *= 2
print decimal