import math

a = float(input("informe o valor de a: "))
b = float(input("informe o valor de b: "))
c = float(input("informe o valor de c: "))


delta =  b**2 - 4 * a * c


if(delta == 0):
    raiz1 = (-b + math.sqrt(delta)) / (2*c)
    print("a única raiz é {}".format(raiz1))
else:
    if (delta < 0):
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*c)
        raiz2 = (-b - math.sqrt(delta)) / (2*c)
        print("a raiz dupla desta equação é ")
        print("raiz 1: {}".format(raiz1))
        print("raiz 2: ", raiz2)