# mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
# 'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake']
# height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101]
# f = open('test_write.txt', "w")
# str = '%s: height is %d\n'
# for i in range(0, len(mountain)):
#     f.write(str % (mountain[i], height[i]))
    
# file = open('test_write.txt', "r")
# n, sum = 0, 0
# for line in file.readlines():
#     (mountain, word1, word2, height_data) = line.split()
#     height = int(height_data)
#     sum = sum + height
#     n = n + 1
# print 'average = ', float(sum)/float(n)
# file.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
f = open("jprogram.txt", "r")
s = f.read();
s = s.replace('曜日', 'dayoftheweek')
s = s.replace('年初からの日数', 'numberofdays')
s = s.replace('月名', 'month')
s = s.replace('日数', 'dates')
s = s.replace('月始め', 'start')
s = s.replace('曜日', 'dayoftheweek')
print s
f.close()