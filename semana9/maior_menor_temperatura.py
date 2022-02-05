

def MinMax(lista):
    print("a menor temperatura foi: ", minima(lista))
    print("a maior temperatura foi: ", maxima(lista))


def minima(lista):
    min = lista[0]
    for temp in lista:
        if temp < min:
            min = temp
    
    return min


def maxima(lista):
    max = lista[0]
    for temp in lista:
        if temp > max:
            max = temp
    return max
    


def main():
    temp_lista = [9,8,6,15,20,14,13,19,35,30,32]
    MinMax(temp_lista)

main()
