decrescente = True
lista = []

anterior = int(input("Digite o primeiro valor"))
num = anterior
valor =1
while valor != 0 and decrescente:
    valor =  int(input("Digite o proximo valor"))
    if (valor > anterior):
        decrescente = False
    anterior = valor
    num = valor
    lista.append(num)
    
if (decrescente):
    print("Os valores informados estão em ordem decrescente...")
else:
    print("Os valores informados não estão em ordem decrescente...")

for j in range(len(lista)):
    print(j)