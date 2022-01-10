
def numeros_primos(numero):
    count = 0
    c = 1
    while c <= numero:
        pr = numero % c
        if pr == 0:
            count += 1
        c += 1

    if count == 2:
        return numero
    
def maior_primo(n):
    i = 0
    verifica_maior = 1
    while i <= n:
        verifica_maior = numeros_primos(n)
        print(verifica_maior)

maior_primo(8)