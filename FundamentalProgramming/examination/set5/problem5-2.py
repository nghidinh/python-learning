'''
Created on Jul 13, 2016

@author: nghind
'''
stockPrice = [105, 110, 103, 95, 101, 105, 91, 102]
for i in range(0, len(stockPrice)):
    if (stockPrice[i] < stockPrice[i + 1]):
        print 'buy', stockPrice[i]
    else:
        continue