'''
Created on Jun 27, 2016

@author: NghiDinh
'''
mountain_data = [('Fujisan', 3775), ('Kitadake', 3193), ('Tateyama', 3015),
('Ainodake', 3190), ('Yarigatake', 3180), ('Warusawadake', 3141),
('Akaisidake',3120), ('Karasawadake', 3110), ('Kitahodakadake', 3106),
('Oobamidake', 3101), ('Maehodakadake', 3090), ('Nakadake', 3084),
('Arakawanakadake', 3083), ('Ontakesan', 3067), ('Noutoridake', 3051),
('Shiomidake', 3046), ('Minamidake', 3032), ('Senjougatake', 3032),
('Norikuradake', 3026), ('Okuhodakadake', 3190)]
def cmp(listi, listj):
    if listi[1] > listj[1]:
        return -1
    else:
        return 1
mountain_data.sort(cmp)
for i in range(0, len(mountain_data)):
    print mountain_data[i]