def tabuada():
    linha = 1
    coluna = 1

    while(linha <= 10):
        while(coluna<=10):
            print(linha ,' X ' , coluna, ' = ',linha * coluna,end='\n')
            coluna+=1
        linha+=1
        coluna=1
        print(' ')

tabuada()