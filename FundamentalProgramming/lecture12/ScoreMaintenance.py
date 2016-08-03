score = {'H15001':-2, 'H15002':-2, 'H15003':-2, 'H15004':-2, 'H15005':-2}
while True:
    student = raw_input('Student ID: ')
    if student in score:
        score[student] = int(raw_input('score'))
    else: break
for student in score:
    if score[student] == -2:
        print 'score for student', student, 'is missing'