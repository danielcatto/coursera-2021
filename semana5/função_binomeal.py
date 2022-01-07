def fatoral(num):
    f = 1
    c = num
    while c > 1:
        f *= c
        c -= 1
    return f

def coeficiente(n, p):
    r = fatoral(n) / (fatoral(p)*fatoral((n-p)))
    return r

n = int(input("numerador: "))
p = int(input("denominador: "))
print(coeficiente(n,p))


print('zero fatorial ', fatoral(0))