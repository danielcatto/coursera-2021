largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

caracter = '#'
espaco = (largura-2) * ' '

#primeira linha
print(caracter*largura)
#meio
i=0
alt_meio = altura-2
while (i < alt_meio):
    print('{}{}{}'.format(caracter,espaco,caracter))
    i+=1
#ultima linha
print(caracter*largura)
