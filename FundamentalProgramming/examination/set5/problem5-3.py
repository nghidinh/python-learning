'''
Created on Jul 13, 2016

@author: nghind
'''
# mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
# 'Warusawadake', 'akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake',
# 'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake',
# 'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
# height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090,
# 3084, 3083, 3067, 3051, 3046, 3032, 3032, 3026, 3015]
# x = int(raw_input('Enter a height'))
# low, high = 0, len(mountain)
# while high - low >= 0:
#     mid = (low + high)/2
#     print low, high, mid
#     if height[mid] < x:
#         high = mid - 1
#     else:
#         low = mid + 1
# if height[high] - x < x - height[low]:
#     print mountain[high], 'height = ', height[high]
# else:
#     print mountain[low], 'height = ', height[low]

mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
'Warusawadake', 'akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake',
'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake',
'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090,
3084, 3083, 3067, 3051, 3046, 3032, 3032, 3026, 3015]
x = int(raw_input('Enter a height '))
low, high = 0, len(mountain)
while high - low >= 0:
    mid = (low + high)/2
    print low, high, mid
    if height[mid] < x:
        high = mid - 1
    else:
        low = mid + 1
        if height[high] - x < x - height[low]:
            print mountain[high], 'height = ', height[high]
        else:
            print mountain[low], 'height = ', height[low]
