numero = input("Digite um número inteiro: ")
r = len(numero)#tamanho do laço
c = 0 #contador de inicio que vai fazer o laço
adj = 1 #numero ajacente ao anterior
res = False #condição para a resposta

#laço percorre todo os caracteres da string e 
while c< r:
    #verifica se o caracter adjacente é maior que o range do laço
    #se for verdadeiro ele faz a verificação seguinte
    if adj != r:
        #verifica se o caracter adjacente é igual ao atual
        if numero[c] == numero[adj]:
            res = True
    #soma as variaveis de contagem para o laço
    c+=1
    adj+=1

#saida do sistema
if res:
    print("Sim")
else:
    print("não")


    