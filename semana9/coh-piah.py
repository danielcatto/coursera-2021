import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


#####################################################
#############################################################################
#############################################################################
#############################################################################
def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)
#############################################################################
#############################################################################
#############################################################################



def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    sub_ass = 0
    for i in range(6):
        sub_ass += abs(as_a[i]) - abs(as_b[i])
    grau_similaridade = sub_ass/6
    return grau_similaridade
        

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    
    #obtendo alguns parametros
    tamanho_sentenca = len(separa_sentencas(texto))
    tamanho_palavra = 0
    palavras = separa_palavras (texto)
    total_palavras = len(palavras)
    frases = len(separa_frases(texto))
    
    #Tamanho medio das palavras
    for palavra in palavras:
        tamanho_palavra += len(palavra)
    tamanho_medio_palavras = tamanho_palavra / total_palavras
  
    #Calcula o type_token
    palavras_unicas = n_palavras_unicas(texto)
    type_token = palavras_unicas/total_palavras
    
    #calcular o hapax
    hapax = n_palavras_unicas(texto) / total_palavras
    
    #tamanho medio das sentenças
    tamanho_palavra = tamanho_palavra / tamanho_sentenca

    #complexidade das sentenças
    complexidade_sentenca = frases / tamanho_sentenca
    
    #tamanho medio da frase
    tamanho_medio_frase = tamanho_palavra 
    
    return [tamanho_medio_palavras, type_token, hapax, tamanho_palavra, complexidade_sentenca, tamanho_medio_frase]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass = []
    for i in textos:
        ass.append(calcula_assinatura(i))
    
    for ass_ind in ass:
        print(compara_assinatura(ass_ind, ass_cp))


def main():
    ass_cp = le_assinatura()
    list_ass = []
    textos = le_textos() #retorna lista de textos
    avalia_textos(textos, ass_cp)
    
main()