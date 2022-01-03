numero = input("Digite um número inteiro: ")
c = 0
total = 0
while c < len(numero):
    total += int(numero[c]) 
    c+=1

print(total)