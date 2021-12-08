num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))
num3 = int(input("informe o terceiro número: "))

if (num1 < num2 and num2 < num3):
    print("crescente")
else:
    print("não está em ordem crescente")