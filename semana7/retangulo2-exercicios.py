lar = int(input("digite a largura: "))
alt = int(input("digite a altura: "))

i=0
j=0
while i < alt:
    while j < lar:
        if (i> 0 and i<=lar):
            
            print("#",end="")
        else:
            print("@", end="")
        j+=1
    print("")
    j=0
    i+=1