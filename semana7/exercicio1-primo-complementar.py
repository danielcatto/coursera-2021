def n_primos(numero):    
    total_primos = 0
    i=0
    while(i<numero):

        count = 0
        c = 1
        while c <= i:
            pr = i % c
            if pr == 0:
                count += 1
            c += 1

        if count == 2:
            total_primos+=1
        
        i+=1
    return total_primos

print(n_primos(121))
