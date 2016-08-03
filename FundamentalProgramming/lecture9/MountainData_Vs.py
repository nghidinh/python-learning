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

h = int(raw_input('Enter height: '))

low, high = 0, len(mountain) - 1
while high - low > 1:
    mid = (low + high)/2
    if height[mid] < h:
        high = mid
    else:
        low = mid
if height[low] - h < h - height[high]:
    print mountain[low], 'height = ', height[low]
else:   
    print mountain[high], 'height = ', height[high]
    

# low, high = 0, len(mountain)
# while high - low >= 0:
#     mid = (low + high)/2
#     print low, high, mid
#     if height[mid] < 3100: #If we set high = mid - 1, low= mid+1 then we have
#         high = mid - 1      #faster convergence.
#     else:                   #We exit the loop when high < low.
#         low = mid + 1 
#     print low, high
#     if height[high] - 3100 < 3100 - height[low]:
#         print mountain[high], 'height = ', height[high]
#     else:
#         print mountain[low], 'height = ', height[low]