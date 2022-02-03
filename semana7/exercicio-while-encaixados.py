'''
x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        print(y)
        y = y + 1
    x = x + 1
fora = 5
while fora > 0:
  dentro = 0
  while dentro < fora:
    print("oi")
    dentro = dentro + 1
  fora = fora - 1
'''


'''não
tab = 1
while tab <= 10:
    print("Tabuada do", tab, ":", end="\t")
    i = 1
    print(tab*i, end = "\t")
    i = i + 1
    print()
    tab = tab + 1

    '''

'''
sim ruim
tab = 1
while tab <= 10:
    print("Tabuada do", tab, ":", end="\t")
    i = 1
    while i <= 10:
        print(tab*i, end = "\t")
        i = i + 1
    print()
    tab = tab + 1

sim bom
tab = 0
while tab < 10:
    tab = tab + 1
    i = 0
    while i < 10:
        i = i + 1
        print(tab,"x",i,"=",tab*i)
    print()
naõ
tab = 1
i = 1
while tab <= 10 and i <= 10:
    print(tab,"x",i,"=",tab*i)
    i = i + 1
    tab = tab + 1
print()
não
tab = 1
while tab <= 10:
    i = 1
    while i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
    print()
    tab = tab + 1


x = 2
cont = 0
while x >= 0:
    y = 0
    while y <= 4:
        print(y)            #comando qualquer
        y = y - 1
    x = x - 1

i = 0
while i < 3:
  j = 0
  while j < 3:
    print(3 * i + j + 1, end=" ")
    j = j + 1
  i = i + 1
'''

x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1