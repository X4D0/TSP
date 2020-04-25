import itertools,math,random,time
import matplotlib.pyplot as plt

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

cities = [[23,45],[30,40],
          [15,15],[21,26],
          [23,70],[33,29],
          [13,36],[64,56],
          [61,67],[10,10]]
n = int(input("Masukkan jumlah kota (1-7) : "))

x = []
y = []
x.append(0)
y.append(0)

t0 = time.perf_counter()

for k in range(1,n+1):
    x.append(k)
    
    tour = random.sample(range(k),k) #Generate SATU Rute perjalanan
    generateTour = list(itertools.permutations(tour)) #Membuat SEMUA Rute Perjalanan yang memungkinkan

    jarakTerpendek = 999999
    ruteTerpendek = tour
    for i in range(len(generateTour)):
        j = jarakRute(generateTour[i])
        if j<jarakTerpendek:
            jarakTerpendek = int(j)
            ruteTerpendek = i
    y.append(time.perf_counter()-t0)
    print("Jarak terpendek",k,"kota yaitu",jarakTerpendek,"KM")
    print("    Dengan Rute :",generateTour[i])

fig, ax = plt.subplots()
ax.plot(x,y,'ro-')
ax.set(xlabel = 'Number of Cities',ylabel = 'Times (s)')
ax.set(xticks = list(range(0,7)))
ax.grid()
plt.show()
