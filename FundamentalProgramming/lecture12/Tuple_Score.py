'''
Created on Jun 27, 2016

@author: NghiDinh
'''
score = {'H15001':70, 'H15002': 65, 'H15003': 90, 'H15004': 82, 'H15005':55}
tuple = []
for student in score:
    tuple.append((student, score[student]))
print tuple
def cmp(listi, listj):
    if listi[1] > listj[1]:
        return -1
    else:
        return 1
tuple.sort(cmp)
for i in range(0, len(tuple)):
    print tuple[i][0], tuple[i][1]