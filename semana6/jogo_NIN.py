def computador_escolhe_jogada(n,m):
    
    loop = True
    cont = m
    if(n == m):
        return m
    elif(n - m == 1):
        return m
    else:
        while(loop):
            if(((n - cont ) % (m+1))== 0):
                loop = False
            cont = cont  - 1
    cont = cont + 1
    if(cont<= 0):
        cont=m
    return cont
        

def usuario_escolhe_jogada(n,m):
    i = True
    while i:

        peça_str = input("informe número de peças que irá ser retirado! ")
        peça = int(peça_str)
        if(peça <= 0):
            print("Oops! Jogada inválida! Tente de novo.")
        elif(peça > m):
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            i=False
    return peça


def partida():

    peças = int(input("quantidade de peças no tabuleiro? "))
    max_retira = int(input("quantidade de peças que pode ser retirada por vez? "))
    n = peças
    m = max_retira
    if(n<m):
        print("Oops! Jogada inválida! Tente de novo.")
        partida()
    else:
        if (n % (m+1) == 0):
            print("Você começa!")
            vez = True
        elif(n % (m+1) > 0):
            print("O computador começa")
            vez = False
        else:
            partida()

        i=True
        while i:
            if (vez):
                ret = usuario_escolhe_jogada(n, m)
                n -= ret
                print("Voce tirou {} peças.".format(ret))
                print("Agora resta apenas {} peça no tabuleiro.".format(n))
                if (n<=0):
                    print("Você ganhou!")
                    i=False
                vez = False
                        
            else:
                ret = computador_escolhe_jogada(n,m)
                n -= ret
                print("O computador tirou {} peça.".format(ret))
                print("Agora resta apenas {} peça no tabuleiro.".format(n))
                if (n<=0):
                    print("O computador ganhou!")
                    i = False
                vez = True

            

def campeonato():
    for i in range(3):
        partida()

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    tipo_partida = int(input(">>>"))
    
    
    if(tipo_partida == 1):
        print("Voce escolheu partida isolada!")
        partida()
    elif(tipo_partida == 2):
        print("Voce escolheu um campeonato!")
        for i in range(3):
            campeonato()


main()
#partida()
