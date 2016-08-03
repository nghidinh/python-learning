n = int(raw_input('Enter n = '))
total_sum = 0
for k in range(1, n + 1):
    sum = 0
    for i in range(1, k + 1):
        sum += i
    total_sum += sum
print 'sum = ', total_sum