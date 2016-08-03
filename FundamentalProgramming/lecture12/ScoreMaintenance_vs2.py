'''
Created on Jun 27, 2016

@author: NghiDinh
'''
score = {}
filename = raw_input('Enter file name: ')
file = open(filename)
line = file.readlines()
print line
for student in line:
    student = student.strip()
    score[student] = -2
print score
while True:
    studentID = raw_input('Student ID: ')
#     if studentID in score:
    if score.has_key(studentID):
        score[studentID] = int(raw_input('score'))
    else: 
        print 'no such student is registered'
for student in score:
    if score[student] == -2:
        print 'score for student', student, 'is missing'
