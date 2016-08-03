'''
Created on Jul 14, 2016

@author: nghind
'''
mountain = ['Fujisan', 'Kitadake', 'Okuhodakadake', 'Ainodake', 'Yarigatake',
'Warusawadake', 'Akaisidake', 'Karasawadake', 'Kitahodakadake', 'Oobamidake',
'Maehodakadake', 'Nakadake', 'Arakawanakadake', 'Ontakesan', 'Noutoridake',
'Shiomidake', 'Minamidake', 'Senjougatake', 'Norikuradake', 'Tateyama']
height = [3775, 3193, 3190, 3190, 3180, 3141, 3120, 3110, 3106, 3101, 3090,
3084, 3083, 3067, 3051, 3046, 3032, 3032, 3026, 3015]
while True:
    mountainName = raw_input("Enter a mountain name: ")
    try:
        i = mountain.index(mountainName)
        print height[i]
    except:
        print 'No such name'
        break