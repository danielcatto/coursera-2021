
def éPrimo(k):
    count = 0
    c = 1
    while c <= k:
        pr = k % c
        if pr == 0:
            count += 1
        c += 1

    if count == 2:
        return True
    else:
        return False    

def maior_primo(n):
    i = 0
    while i <= n:
        verifica_maior = éPrimo(i)
        if verifica_maior == True:
            maior = i
        i+=1
    return maior
print(maior_primo(100))