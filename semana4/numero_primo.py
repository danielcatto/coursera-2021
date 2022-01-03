numero = int(input("Digite um número inteiro: "))
count = 0
c = 1
while c <= numero:
    pr = numero % c
    if pr == 0:
        count += 1
    c += 1

if count == 2:
    print("primo")
else:
    print("não primo")