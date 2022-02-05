from maior_menor_temperatura import minima


def teste_pontual(lista, valor_esperado):
    if minima(lista) == -15:
        print("correto")

#testes temperatura minima
list_temp = [-15, 19,  13.5, 20.1, 30.5, 34 ]
teste_pontual(list_temp, -15)

