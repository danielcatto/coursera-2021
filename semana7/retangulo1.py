largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

i=0
j=0
while i < altura:
    while j < largura:
        print("#", end='')
        j+=1
    j=0
    print()
    i+=1

