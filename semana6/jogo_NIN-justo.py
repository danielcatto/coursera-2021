import time, random

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


def partida():

    peças = 50#int(input("quantidade de peças no tabuleiro? "))
    max_retira = 5#int(input("quantidade de peças que pode ser retirada por vez? "))
    n = peças
    m = max_retira
    if(n<m):
        print("Oops! Jogada inválida! Tente de novo.")
        partida()
    else:
        
        r = int(random.uniform(1, 3))
        if (r==1):
            vez = True
            print("#### o usuario começa ######\n\n")
        else:
            vez = False
            print("#### o computador começa ######\n\n")
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
                    vitoria = 1
                vez = False
                        
            else:
                ret = computador_escolhe_jogada(n,m)
                n -= ret
                print("O computador tirou {} peça.".format(ret))
                print("Agora resta apenas {} peça no tabuleiro.".format(n))
                if (n<=0):
                    print("O computador ganhou!")
                    vitoria = 0
                    i = False
                vez = True
            time.sleep(0)

    return vitoria
            

def campeonato():
    usuario = 0
    computador = 0
    for i in range(3):
        vitoria = partida()
        if vitoria == 1:
            print(vitoria)
            usuario += 1
        else:
            computador +=1
            

    print("Placar")
    print("usuario = {} vitorias!".format(usuario))
    print("computador = {} vitorias!".format(usuario))
    print(vitoria)



def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")

    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato 2")
    tipo_partida = 1#int(input(">>>"))
    
    
    if(tipo_partida == 1):
        print("Voce escolheu partida isolada!")
        vitoria = partida()
        print(vitoria)
        if(vitoria == 0):
            print("coputer ganhooo")
        
    elif(tipo_partida == 2):
        print("Voce escolheu um campeonato!")
        for i in range(3):
            campeonato()


main()
#partida()
