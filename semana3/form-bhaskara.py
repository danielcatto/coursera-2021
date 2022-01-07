import math

a = 10#float(input("informe o valor de a: "))
b = 25#float(input("informe o valor de b: "))
c = 10#float(input("informe o valor de c: "))

  
delta =  b**2 - 4 * a * c
print("delta", delta)
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)


print("raiz 1: ", raiz1)
print("raiz 2: ", raiz2)

'''
if(delta == 0):
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    print("esta equação não possui raízes reais")
else:
    if (delta < 0):
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        if(raiz1<raiz2):
            print("as raízes da equação são {} e {} ".format(raiz1, raiz2))
        else:
            print("as raízes da equação são {} e {} ".format(raiz2, raiz1))
'''