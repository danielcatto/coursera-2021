num = int(input("informe um numero positivo: "))
i=0
c=1
while i < num:
    if c % 2  != 0:
        print(c)
        i+=1
        if i == num:
            break
    c += 1
    
    