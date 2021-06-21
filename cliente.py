import pickle as pk
#Função do menu
def menu():
    print('   ','-'*3,' BEMVINDO AO BANCO ','-'*3)
    print('~'*10)
    print('1- Saque')
    print('2- Deposito')
    print('3- Veja o seu Saldo')
    print('4- Simulador de investimento')
    print('5- Sair')
    print('~'*10)
    pergunta = input('Escolha uma das opções: ')

    while not pergunta.isdigit():#Vereficador para não bugar
        print('     Digite apenas números/Digite apenas números da tabela')
        pergunta = input('Escolha uma das opções: ')
    
    pergunta = int(pergunta)
    while pergunta > 5:
        print('     Digite apenas números/Digite apenas números da tabela')
        pergunta = int(input('Escolha uma das opções: '))
    
    
    if pergunta == 1:
        saque() #Vai para função saque
        
    elif pergunta == 2:
        deposito()#Vai para função deposito
        
    elif pergunta == 3:
        v_saldo()#Vai para função do saldo

    elif pergunta == 4:
        print(4)
        s_investimento()#Vai para a parte do investimento
        
    elif pergunta ==5:
        exit()#Sai do programa

#Função do deposito
def deposito():
    conta = str(input('Me fale o numero da conta: ')).strip()
    try:
        busca = open(f'{conta}','rb')#Tenta ver se o arq existe
        
    except:
        print('Conta não existe')
        menu()#Se não achar volta para o menu
    senha = input('Digite a sua senha: ').strip()
    x = pk.load(busca)#Se der certo abre o arquivo e carrega a lista dentro do código
    individuo = x[0] #Pega o nome do individuo
    if x[6] == senha: #Verefica se a senha está correta
        print('O SALDO ATUAL: ', x[8],' reais') #Mostra o saldo atual
        deposito = input('Quanto você quer depositar? : ') 
        while not deposito.isdigit: #Para vereficar se é digito
            print('Coloque apenas números/não precisa colocar reais nem $')
            deposito = input('Qual o valor do deposito: ')
        deposito = int(deposito) #Transforma o input em int
        if deposito > 10000: #Verefica as codições do exercicio.
            print('Não é possivel sacar',deposito,'reais, tente novamente')
            menu()
        valor_total = x[8] + deposito #Acrescenta o valor do deposito
        x[8] = valor_total #Adciona o novo valor na lista do pickle
        adc_valor = x #Serve apenas para adc dentro do pickle
        arq = open(f'{conta}','wb') #Abre arq
        pk.dump(adc_valor, arq) #Adiciona no pickle
        arq.close()
        arq = open(f'{individuo}','wb') #Coloca no outro arquivo
        pk.dump(adc_valor, arq)
        arq.close()
        print('Deposito efetuado com sucesso')
        sair = input("Voltar para o menu?")#Pergunta para sair do código ou voltar para o menupara o gerente 
        while not sair.isdigit():#conseguir olhar as pessoas q estão na lista.
            print("Apenas números")
            sair = input("Voltar para o menu?")
        if sair == "1":
            exit()
        else: 
            menu()
    else:#Se errar a senha volta para o menu
        print('Você errou a senha, tente novamente')
        menu()

def saque():
    conta = str(input('Me fale o numero da conta: ')).strip()#Esse strip serve para tirar os possiveis espaços
    try: #Tenta abrir o arq
        busca = open(f'{conta}','rb')
        
    except:
        print('Conta não existe')
        menu()
    senha = input('Digite a sua senha: ').strip()
    x = pk.load(busca)
    individuo = x[0] 
    if x[6] == senha:#Verefica se a senha está correta
        print('O SALDO ATUAL: ', x[8],' reais') #Mostra Saldo
        print('Quanto você deseja sacar? :')
        valor = input('Digite o valor: ')
        while not valor.isdigit: #Verefica se é digito
            print('Coloque apenas números')
            valor = input('Digite o valor novamente: ')
        valor = int(valor)
        if x[8] == 0: #Faz as vereficações de acordo com exercicio
            print('Você não tem nada na conta')
            menu()
        elif valor > x[8]:
            print('Você está retirando mais do que tem')
            print('Voltando para o inicio ...')
            menu()
        elif valor < x[8]:
            total_valor = x[8] - valor #Retira da conta
            x[8] = total_valor
            novo_valor = x #Adiciona na variavel q vai para o pickle
            arq = open(f'{conta}','wb')
            pk.dump(novo_valor,arq) #Coloca no pickle
            arq.close()
            arq = open(f'{individuo}','wb') #Faz o mesmo no outro arq
            pk.dump(novo_valor,arq)
            
            print('Seu saldo atual é de: ',x[8],'reais') #Mostra o saldo
            arq.close()
            sair = input("Voltar para o menu?")
            while not sair.isdigit(): 
                print("Apenas números")
                sair = input("Voltar para o menu? ")
            if sair == "1":
                exit()
            else: 
                menu()

    else:
        print('Você errou a senha, tente novamente')
        menu()
    

def v_saldo():
    conta = str(input('Me fale o numero da conta: ')).strip()
    try:
        busca = open(f'{conta}','rb')
        
    except:
        print('Conta não existe')
        menu()
    x = pk.load(busca)
    senha = input('Digite a sua senha: ').strip()
    if x[6] == senha: # Verefica a senha
        print("="*10)
        print('O SALDO ATUAL: ', x[8],' reais') #Mostra o saldo
        print('Para colocar dinheiro na conta acesse a opção de deposito')
        sair = input("Voltar para o menu? |1| - Sair |2| - Menu ")
        while not sair.isdigit(): 
            print("Apenas números")
            sair = input("Voltar para o menu?|1| - Sair |2| - Menu ")
        if sair == "1":
            exit()
        else: 
            menu()
        
    else:
        print('Senha incorreta')
        menu()

def s_investimento():
    investimento_inicial = input('Qual será o valor do investimento inicial?')
    while not investimento_inicial.isdigit():
        print('Coloque apenas números')
        investimento_inicial = input('Qual será o valor do investimento inicial?')

    meses = input('Qual será o número em meses do investimento?')
    while not meses.isdigit():
        print('Coloque apenas números')
        meses = input('Qual será o número em meses do investimento?')
    
    #Fizemos desse jeito para evitar falhas no programa
    investimento_inicial = float(investimento_inicial)
    meses = int(meses)

    #calculos...
    if meses < 60:
        montante = investimento_inicial * ((1 + 0.015)**meses) * 0.99
        print('='*10)
        print('O montante será de', montante, 'reais.')
        print('='*10)
        print('By Problemas Bancários')
        menu()
    if meses > 60:
        montante = investimento_inicial * ((1 + 0.015)**meses) * 0.995
        print('='*10)
        print('O montante será de', montante, 'reais.')
        print('='*10)
        print('By Problemas Bancários')
        menu() #Tem que subir um pouco o 
#sair

menu()