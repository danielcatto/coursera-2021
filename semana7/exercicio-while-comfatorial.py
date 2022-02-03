#ator informa um numero e o sistema retorna o fatorial!
#saida do sitema digite o número zero
import os
def fatorial(num):
    f = 1
    c = num
    while c > 1:
        f *= c
        c -= 1
    #print(f)
    return f

def main():
    i=True
    fat = 0
    os.system('clear')
    print(">>>FATORIAL<<<")
    print("informe um número inteiro positivo, por favor.")
    print("0 para sair!")
    while i:
        
        num = int(input(">>> "))
        
        if(num>0):
            fat = fatorial(num)
            print(fat)
        
        else:
            break
        
main()