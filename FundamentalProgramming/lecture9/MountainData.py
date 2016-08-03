'''
Created on Jun 26, 2016

@author: NghiDinh
'''
mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake',
'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake',
'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090,
3084, 3083, 3067, 3051, 3046, 3032, 3032, 3026, 3015]

#Enumerate all the mountains exceeding 3100 meters
for i in range(0, len(mountain)):
    if height[i] >= 3100:
        print mountain[i], 'height = ',height[i]
    else: break
    
#Which mountain is closest to 3100 meter in its height?
for i in range(0, len(mountain)):
    if height[i] < 3100:
        break
if height[i - 1] - 3100 < 3100 - height[i]:
    print 'Which mountain is closest to 3100 meter in its height?',  mountain[i - 1], 'height = ', height[i - 1]
else:
    print 'Which mountain is closest to 3100 meter in its height?', mountain[i], 'height = ', height[i - 1]