# a  = [5, 9, 'Three', 2, 'Six']
# print a[3:]
# print a[:4]
# print a[2:5]
# print a[4]
# print a[-1]
# 
# score = [65, 78, 90, 85, 50]
# k = int(raw_input('Student number '))
# if k < 150001 or k > 150005:
#     print 'No such student number'
# else:
#     print 'score = ', score[k - 150001]
#     
    
# score = [-2, -2, -2, -2, -2]
# while True:
#     stID = int(raw_input('Student ID'))
#     if 150001 <= stID <= 150005:
#         score[stID - 150001] = int(raw_input('seiseki '))
#     else: break
# print score

# score = [-2,]*5
# while True:
#     stID = int(raw_input('Student ID'))
#     if 150001 <= stID <= 150005:
#         score[stID - 150001] = int(raw_input('seiseki '))
#     else: break
# print score
# while True:
#     studentID = int(raw_input('StID'))
#     if 150001 <= studentID <= 150005:
#         print score[studentID - 150001] 
#     else: break
    
    
# stID1 = int(raw_input('First Student ID')) #the first student
# stID2 = int(raw_input('First Student ID')) #the first student
# score = [-2,]*(stID2 - stID1 + 1)
# while True:
#     stID = int(raw_input('Student ID'))
#     if 150001 <= stID <= 150005:
#         score[stID - 150001] = int(raw_input('seiseki '))
#     else: break
# print score
# while True:
#     studentID = int(raw_input('StID'))
#     if 150001 <= studentID <= 150005:
#         print score[studentID - 150001] 
#     else: break
#     
    
#Detecting which students's scores are missing
# stID1 = int(raw_input('First Student ID')) #the first student
# stID2 = int(raw_input('First Student ID')) #the first student
# score = [-2,]*(stID2 - stID1 + 1)
# while True:
#     stID = int(raw_input('Student ID'))
#     if 150001 <= stID <= 150005:
#         score[stID - 150001] = int(raw_input('seiseki '))
#     else: break
# #If all the scores are input and some scores remain -2, then ouput them.
# for stID in range(stID1, stID2 + 1):
#     if score[stID - stID1] == -2:
#         print 'score for', stID, 'is missing'
    
    
#Detecting duplicate registrations of scores
# stID1 = int(raw_input('First Student ID '))
# stID2 = int(raw_input('Last Student ID '))
# score = [-2] * (stID2 - stID1 + 1)
# while True:
#     stID = int(raw_input('Student ID'))
#     if stID1 <= stID <= stID2:
#         if score[stID - stID1] != -2:
#             print stID, 'Score is already registered '
#             continue
#         score[stID - stID1] = int(raw_input('seiseki '))
#     else: break
# for stID in range(stID1, stID2+1):
#     if score[stID - stID1] == -2:
#         print 'score for', stID, 'is missing'
#         
        

# IDs = [0, 0]; IDe = [0, 0]
# IDs[0] = int(raw_input('From 14xxxx: '))
# IDe[0] = int(raw_input('To 14xxxx: '))
# IDs[1] = int(raw_input('From 15xxxx: '))
# IDe[1] = int(raw_input('To 15xxxx: '))
# score14 = [-2,] * (IDe[0] - IDs[0] + 1)
# score15 = [-2,] * (IDe[1] - IDs[1] + 1)
# 
# while True:
#     stID = int(raw_input('Student ID: '))
#     if IDs[0] <= stID <= IDe[0]:
#         if score14[stID - IDs[0]] != -2:
#             print stID, 'Score is already registered'
#         else:
#             score14[stID - IDs[0]] = int(raw_input('seiseki'))
#     elif IDs[1] <= stID <= IDe[1]:
#         if score15[stID - IDs[1]] != -2:
#             print stID, 'Score is already registered'
#         else:
#             score15[stID - IDs[1]] = int(raw_input('seiseki'))
#     else: break
# 
# for stID in range(IDs[0], IDe[0] + 1):
#     if score14[stID - IDs[0]] == -2:
#         print 'score for', stID, 'is missing'
# for stID in range(IDs[1], IDe[1] + 1):
#     if score15[stID - IDs[1]] == -2:
#         print 'score for', stID, 'is missing'
#         


n = int(raw_input('How many? ')) 
IDs = [0, ]* n; IDe = [0, ]*n

for i in range(0,  n):
    IDs[i] = int(raw_input('From ')) 
    IDe[i] = int(raw_input('To '))
for i in range(0,  n):
    score[i] = [-2,] * (IDe[i] - IDs[i] + 1)
while True:
    stID = int(raw_input('Student ID'))
    for i in range(0,  n):
        if IDs[i] <= stID <= IDe[i]:
            if score[i][stID - IDs[i]] != -2:
                print stID, 'Score is already registered ' 
            else:
                score[i][stID - IDs[i]] = int(raw_input('seiseki '))
        else: break
for i in range(0,  n):
    for stID in range(IDs[i], IDe[i]+1):
        if score[i][stID - IDs[i]] == -2:
            print 'score for ', stID, 'is missing'
