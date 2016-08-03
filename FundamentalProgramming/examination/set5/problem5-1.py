'''
Created on Jul 13, 2016

@author: nghind
'''

from math import fabs

mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake',
'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake',
'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090,
3084, 3083, 3067, 3051, 3046, 3032, 3034, 3026, 3015]
for i in range(len(height) - 1, 0, -1):
    for j in range(0, i):
        if height[j] > height[j + 1]:
            height[j], height[j + 1] = height[j + 1], height[j]
            mountain[j], mountain[j + 1] = mountain[j + 1], mountain[j]
for i in range(0, len(height)):
    print mountain[i], height[i]
    
h = int(raw_input('Enter height: '))

low, high = 0, len(height) - 1
while high - low > 1:
    mid = (low + high) / 2
    print 'mid = ', mid
    if (height[mid] < h):
        low = mid
        print 'low = ', low
    else:
        high = mid
        print 'high = ', high

if low == 0:
    print height[high], mountain[high]
    if h - height[low] < height[high + 1] - h:
        print height[low], mountain[low]
    else:
        print height[high + 1], mountain[high + 1]
elif high == len(height) - 1:
    print height[low], mountain[low]
    if h - height[low - 1] < height[high] - h:
        print height[low - 1], mountain[low - 1]
    else:
        print height[high], mountain[high]
elif h - height[low] < height[high] - h:
    print height[low], mountain[low]
    if h - height[low - 1] < height[high] - h:
        print height[low - 1], mountain[low - 1]
    else:
        print height[high], mountain[high]
else:
    print height[high], mountain[high]
    if h - height[low] < height[high + 1] - h:
        print height[low], mountain[low]
    else:
        print height[high + 1], mountain[high + 1]
