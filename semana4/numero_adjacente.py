numero = input("Digite um número inteiro: ")
r = len(numero)
c = 0
res = False
i = 1
while c < r:
    ad = numero[c]
    if numero[c] == numero[c-1]:
        res = True
    c+=1
    
    
if res:
    print("sim")
else:
        print("não")