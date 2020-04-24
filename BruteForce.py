import itertools,math,random

#Fungsi menghitung jarak antar dua kota (Pythagoras)
def jarakKota(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

#Fungsi menghitung jarak rute perjalanan
def jarakRute(tour):
    d = 0
    #Hitung jarak antar kota dari kota-1 SAMPAI kota-n
    for i in range(1,len(tour)):
        x1 = cities[tour[i-1]][0]
        y1 = cities[tour[i-1]][1]
        x2 = cities[tour[i]][0]
        y2 = cities[tour[i]][1]
        d += jarakKota(x1,y1,x2,y2)
    #Hitung jarak antara kota pertama DAN kota terakhir
    x1 = cities[tour[len(tour)-1]][0]
    y1 = cities[tour[len(tour)-1]][1]
    x2 = cities[tour[0]][0]
    y2 = cities[tour[0]][1]
    d += jarakKota(x1,y1,x2,y2)
    return d

n = 4
cities = [[23,45],
          [30,40],
          [15,15],
          [21,26]]
tour = random.sample(range(n),n) #Generate SATU Rute perjalanan
generateTour = list(itertools.permutations(tour)) #Membuat semua Rute Perjalanan yang memungkinkan

jarakTerpendek = 999999
ruteTerpendek = tour
for i in range(len(generateTour)):
    j = jarakRute(generateTour[i])
    if j<jarakTerpendek:
        jarakTerpendek = int(j)
        ruteTerpendek = i
