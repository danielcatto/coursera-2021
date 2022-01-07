import math

a = float(input("informe o valor de a: "))
b = float(input("informe o valor de b: "))
c = float(input("informe o valor de c: "))

  
delta =  b**2 - 4 * a * c
print("delta", delta)

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    print("A unica raiz é: ", raiz1)
else:
    if delta < 0:
        print("Essa equação não possui raizes reais.")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)

        print("A primeira raiz é: ", raiz1)
        print("A segunda raiz é: ", raiz2)
