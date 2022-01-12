computador = 0
usuario = 0
def computador_escolhe_jogada(n , m):
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

def usuario_escolhe_jogada(n, m):
    i = True

    numPecas = int(input("Informe quantidade de peças para ser retirada: "))

    while(i == True):
        if(n<m):
            print("Erro: perdeu a vez" )

        elif (numPecas <= m):
            i=False

        elif(numPecas > m):
            print("Oops! Jogada inválida! Tente de novo.")
            numPecas = int(input("Informe quantidade de peças para ser retirada: "))
            i=False
        else:
            print("Tente seguir as regras do jogo por favor")
            numPecas = int(input("Informe quantidade de peças para ser retirada: "))
    print("VocÊ tirou " , m, "restam(partida) ", n)
    return numPecas


def partida():
    global computador
    global usuario
    vez = True
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if(n<m):
        print("Oops! Jogada inválida! Tente de novo.")
        partida()
    else:

        if (n % (m+1) == 0):
            print("O usuário começa")
            vez = True
        elif(n % (m+1) > 0):
            print("O computador começa")
            vez = False
        else:
            partida()
    #ver se jogo é um campeonato(com três rodadas) ou partida única


        #controla a vez de quem joga
    i=True
    while(i):
        if(vez == True):
            r = usuario_escolhe_jogada(n, m)
            n = n - r
            print("O Usuario tirou " , r , " restam " , n)
            if(n <= 0):
                usuario+=1
                print("Usuario vence")
                i=False
            vez = False
        elif(vez == False):
            r = computador_escolhe_jogada(n, m)
            n = n - r
            print("O Computador tirou " , r , " restam " , n)
            if(n <= 0):
                print("computador vence")
                i=False
            vez = True
        else:
            pass


print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
print("2 - para jogar um campeonato ")
tipo_jogo = int(input(">>>>"))
print(" ")

if(tipo_jogo == 1):
    partida()
elif(tipo_jogo == 2):
    controle = 2
    rodada =1
    while(controle >= 0):
        print("Rodada ", rodada)
        partida()
        controle -= 1
        rodada = rodada + 1

print("**** final do compeonato ****")
print("placar você ", usuario, " X ", computador )