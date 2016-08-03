'''
Created on Jul 14, 2016

@author: nghind
'''
birth_data1 = [('Soichiro Honda', 2000, 8, 25),
('Gontaro Nissan', 2001, 7, 20),
('Kazuo Hitachi', 2002, 9, 22),
('Saburo Hashiba', 2004, 10, 3),
('Wataru Ishibashi', 2000, 2, 25)]
birth_data2 = [('Saburo Hashiba', 2004, 10, 3),
('Toru Udeno', 2003, 9, 21),
('Yasuhiro Todaiji', 2003, 7, 20)]
s = set(birth_data1)
t = set(birth_data2)
birth_data = s.union(t)
for list in birth_data:
    print list[0], 'was born in ', list[1], 'month', list[2]