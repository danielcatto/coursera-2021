
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
    lista_primos = []
    i = 0
    while i <= n:
        verifica_maior = éPrimo(i)
        if verifica_maior == True:
            lista_primos.append(i)
        i+=1
    return lista_primos




def main():
    print("LISTA DE NÚMEROS PRIMOS\n")
    numero = int(input("Informe um número inteiro maior que 2:\n>>>>"))


    if numero > 2:
        lista_primos = maior_primo(numero)
    else:
        print("Por favor, informe um número inteiro maior que 2:\n>>>>")
        main()

    print(lista_primos)
    
main()