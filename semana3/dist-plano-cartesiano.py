import math
x1 = int(input("coordenada x1: "))
x2 = int(input("coordenada x2: "))
y1 = int(input("coordenada y3: "))
y2 = int(input("coordenada y4: "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)







if(dist >= 10):
    print("longe")
else: 
    print("perto")
