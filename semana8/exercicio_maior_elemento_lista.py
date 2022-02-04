lista = [-90,-27,-12]

def maior_elemento(lista):
    maior=-100000
    for item in lista:
        if item > maior:
            maior=item
        
    return maior

print(maior_elemento(lista))