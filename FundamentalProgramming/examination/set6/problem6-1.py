'''
Created on Jul 15, 2016

@author: nghind
'''
# def inverse(n):
#     if n == 1: return 1
#     decimal = 1
#     result = '' 
#     residue = [decimal]
#     while decimal != 0:
#         decimal = decimal * 10
#         result = result + str(decimal / n)
#         decimal = decimal % n
#         if decimal in residue:
#             index = residue.index(decimal)
#             result = result.replace(result[index], '#' + result[index], 1)            
#             return '0.' + result +'#'
#         residue.append(decimal)
#     return '0.' + result
# n = int(raw_input('Enter n: '))
# print inverse(n)
# # x = 1
# # print float(x/121)

print (-4 + 6*2**10 - 4 * 3**10 + 4**10)/24