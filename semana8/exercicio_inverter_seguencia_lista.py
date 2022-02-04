lista = []
while  True:
    num = int(input("Digite um número: "))
    if num > 0:
        lista.append(num)
    else:
        break

#print(lista)
lista_reversa = reversed(lista)
for i in lista_reversa:
    print(i)