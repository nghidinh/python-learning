'''
Created on Jun 26, 2016

@author: NghiDinh
'''

mountain = ['Fujisan', 'Tateyama', 'Kitadake', 'Okuhodakadake', 'Ainodake',
'Yarigatake', 'Warusawadake', 'akaisidake', 'Karasawadake', 'Kitahodakadake',
'Oobamidake', 'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan',
'Noutoridake', 'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', ]
height = [3775, 3015, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101,
3090, 3084, 3083, 3067, 3051, 3046, 3032, 3032, 3026]
# change = True
# while change:
#     change = False
#     for i in range(0, len(height) - 1):
#         if height[i] < height[i+1]:
#             height[i], height[i+1] = height[i+1], height[i]
#             mountain[i], mountain[i+1] = mountain[i+1], mountain[i]
#             change = True
# for i in range(0, len(height)):
#     print mountain[i], height[i]
    
for j in range(len(height) - 1, 1, - 1):
    for i in range(0, j):
        if height[i] > height[i+1]:
            height[i], height[i+1] = height[i+1], height[i]
            mountain[i], mountain[i+1] = mountain[i+1], mountain[i]
for i in range(0, len(height)):
    print mountain[i], height[i]