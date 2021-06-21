#Vou tentar usar o pickle
from os import close
import pickle as pk
import random as rd

#CRIAR ARQUIVO PARA VEREFICAR AS CONTAS

try: #verifica a existência de um arquivo contas ja criadas
    file = open("dados", "rb")
    file.close()
except:
    # Caso não existe, cria o arquivo para armazenar as contas
    dados = []
    nome_dados = []
    file = open("dados", "wb")
    pk.dump(dados, file)
    file = open("nome_dados",'wb')
    pk.dump(nome_dados, file)
    file.close()


def cria_cliente():
    n = rd.randint(10000,99999)
    arq = open("dados","rb")
    dados = pk.load(arq)
    for i in dados:
        if i == n:
            n = rd.randint(10000,99999)
            continue

    dados.append(n)
    arq = open('dados','wb')
    pk.dump(dados, arq)
    arq.close()
    numero_conta = [n]
    pessoa = input('Nome:').strip().upper()
    cliente = [pessoa]
    busca = [pessoa]
    arq = open('nome_dados','rb')
    nome_dados = pk.load(arq)
    nome_dados.append(busca[0])
    arq = open('nome_dados','wb')
    pk.dump(nome_dados,arq)
    arq.close()
    telefone = input('Telefone: ')
    while not telefone.isdigit():
        print('Coloque apenas números')
        telefone = input('Telefone: ')
    profissao = input('profissão: ').strip().upper()
    renda = input('Renda mensal:')
    while not renda.isdigit():
        print('Coloque apenas números')
        renda = input('Renda mensal: ')
    endereco = input('Endereço: ').strip().upper()
    cidade = input('cidade: ').strip().upper()
    senha = input('Senha para o cliente acessar: ')
    v = verefica_senha(senha)
    print('='*20)
    print('O NÚMERO DA SUA CONTA É: ',n)
    print('='*20)
    saldo = 0
    file = open(f'{numero_conta[0]}','wb')
    numero_conta[0] = [pessoa, cidade, telefone, endereco, profissao, n, v,renda,saldo]
    pk.dump(numero_conta[0],file)
    file.close()
    arq = open(f'{cliente[0]}','wb')
    pk.dump(numero_conta[0],arq)
    arq.close()
    sair = input("Voltar para o menu?")
    while not sair.isdigit():
        print("Apenas números")
        sair = input("Voltar para o menu?")
    if sair == "1":
        exit()
    else: 
        menu()

def gerente_busca_cliente(nome_dados, nome):
    mostra_busca = [] #Cria função
    for i in range(len(nome_dados)):
        if nome in nome_dados[i]:
            mostra_busca.append(nome_dados[i])

    for i in range(len(mostra_busca)):
        arq = open(f'{mostra_busca[i]}','rb')
        x = pk.load(arq)
        print('='*20)
        print(i+1)
        print('Nome:', x[0])
        print('Cidade:', x[1])
        print('Telefone: ', x[2])
        print('Endereço: ', x[3])
        print('Profissão: ', x[4])
        print('Número da conta: ', x[5])
        print('Senha da conta: ', x[6])
        print('A sua renda mensal é de', x[7],' reais')
        print('='*20)
        arq.close()
    sair = input("Voltar para o menu?")#Pergunta para sair do código ou voltar para o menupara o gerente 
    while not sair.isdigit():#conseguir olhar as pessoas q estão na lista.
        print("Apenas números")
        sair = input("Voltar para o menu?")
    if sair == "1":
        exit()
    else: 
        menu()
    
#Função para trocar a senha
def troca_senha():
    conta = str(input('Me fale a conta: '))

    try:#Ele tenta abrir a conta que foi escrito no input
        arq = open(f'{conta}','rb')#Se estiver ok ele vai abrir o arquivo da conta.
    except:
        print("Conta não existe: ")
        menu()#Se não coseguir volta para o menu.
    
    x = pk.load(arq)
    new_senha = input('Me fale a sua nova senha: ')
    v = verefica_senha(new_senha)#Verefica se a conta está ok.
    individuo = x[0]#Busca o nome do individuo na lista
    x[6] = v #Na posição da senha ele adc a nova senha
    adc = x #Essa variavel serve apenas para colocar no arq.
    arq = open(f'{conta}','wb')
    pk.dump(adc,arq)
    file.close()
    arq = open(f'{individuo}','wb')#Faz a mesma coisa só que num outro arquivo pickle
    pk.dump(adc,arq)
    file.close()
    print("Realizado com sucesso!")#Print para mostrar que tudo deu certo
    sair = input("Voltar para o menu?")
    while not sair.isdigit():
        print("Apenas números")
        sair = input("Voltar para o menu?")
    if sair == "1":
        exit()
    else: 
        menu()
    
#Função para vereficar a senha escrita pelo usuário.
def verefica_senha(senha):
    tam = len(senha)
    while not senha.isalnum() or tam < 4 or tam > 8:
        print('Apenas letras e números')
        senha = input('Digite a senha novamente: ')
        senha_nova = senha
    
    if tam >4 and tam <8:
        return senha
    return senha_nova

def menu():
    print('-'*5,'Program by Problemas Bancarios','-'*5)
    print("     ",'-'*5,'GERENTE','-'*5)
    print('     1- Criar cliente')
    print('     2- Buscar cliente')
    print('     3- Trocar senha do cliente')
    print('     4- Sair')
    print('     ','-'*20)
    pergunta = input('Escolha uma das opções: ')

    while not pergunta.isdigit():
        print('     Digite apenas números/Digite apenas números da tabela')
        pergunta = input('Escolha uma das opções: ')
    
    pergunta = int(pergunta)
    while pergunta > 4:
        print('     Digite apenas números/Digite apenas números da tabela')
        pergunta = int(input('Escolha uma das opções: '))
    
    
    if pergunta == 1:
        cria_cliente()
    elif pergunta == 2:
        nome = str(input('Me fale o seu nome para a busca: ')).strip().upper()
        nome = f'{nome}'
        arq = open('nome_dados','rb')
        nome_dados = pk.load(arq)
        gerente_busca_cliente(nome_dados, nome)
    elif pergunta == 3:
        troca_senha()
    elif pergunta == 4:
        exit()

menu()
