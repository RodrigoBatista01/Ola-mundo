from selenium.webdriver import Chrome
from time import sleep #Com isso não precisa de "time." para sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sys import exit
from os import system,name


#FUNCÕES------- 

def conectar_cel():
    global total_de_conversas
    global ativacao
    
    
    
    try:
        total_de_conversas=navegador.find_elements(By.CLASS_NAME,'_3OvU8')
    except:
        print('...')    
    
    if total_de_conversas== []:
        print('Erro: Conclua a autenticação QRCODE e espera uns instantes.')
        sleep(1)
        print('Tente novamente.')
        inicio()
    else:
        print('Conexão bem sucedida.')
        ativacao=True
        
        inicio()


def achar_numero(aux_total,conversas_do_zap):
    global local_conversa
    #--- Esse variavel vai recebe por cada vez um numero que o selenium conseguiu lê
    numero_do_pv=[]
    
    for x in range(aux_total):
        try:
            local_conversa.append(conversas_do_zap[x].find_element(By.CLASS_NAME,'zoWT4'))
            numero_do_pv.append(local_conversa[x].find_element(By.TAG_NAME,'span').text)
            

            print(f'Conversas n° {x}-> {numero_do_pv[x]}')
                

        except:
            print('Erro na leitura dan conversa recente...')
            n_teste=0
    
    return numero_do_pv

def mandar_mensagem(mensagem,localizar):
    
    y=0
    while y!=5:
        #--- Procurar o elemento da mensagem que é a classe 'p3_M1'
        try: 
            localizar.click()
            sleep(1)
            teste_3=navegador.find_element(By.CLASS_NAME,'p3_M1')
            teste_3.click()
            #teste_3.send_keys(f"{mensagem}" + Keys.ENTER)
            # O codigo de cima , desativei para não mandar a mensagem 
            # apenas escrever.
            
            teste_3.send_keys(f"{mensagem}")
            print('Mensagem enviada ;)')
            break 

        except:
            print(f' TENTANDO MANDAR MENSAGEM,tentativa(s)= {y}')
            y += 1
            sleep(2)


def segunda_conf():
    #--- Essas variaveis, são somenta para auxliar. Depois eu tirarei elas.
    global aux_total
    aux_total=len(total_de_conversas)

def ler_mensagens(localizar):
    global conversas_lidas
    
    #--- Essas variaveis vão auxiliar na navegação do selenium entre as classes.
    localizar.click()
    #--- Variaveis de navegação
    h=navegador.find_element(By.CLASS_NAME,'_3K4-L')
    h_2 = h.find_elements(By.CLASS_NAME,'_22Msk')  
    #---
    conversas_lidas=[None]*len(h_2)
    ilegivel=0

    for x in range(20):
        
        try:
            # Bugado o vetor, usar o y
            y=x+1
            
            h_3 = h_2[-y].find_element(By.CLASS_NAME,'_1Gy50') 
            h_4 = h_3.find_elements(By.TAG_NAME,'span')
            conversas_lidas[x] = h_4[0].find_element(By.TAG_NAME,'span').text
            
            sleep(0.2)
            print(conversas_lidas[x],end='\n')
        except:
            ilegivel+=1 
    
    print(f' Total de {ilegivel} mensagens que não foram lidas')

    return conversas_lidas

def limpar():
    system('cls' if name == 'nt' else 'clear')


def inicio():
    global localizacao
    global conversas
    global selecionado
    
    if ativacao==False:
        
        print( '-----------------------------------------------------------\n',
            '> Digite 1: Para verificar a conexão do whatsapp.\n',
            '> Digite 2: Para encerrar o programa.\n'
            '-----------------------------------------------------------')

        opcao=input('Digite a opção --> ')
        limpar()

        if opcao=='1':
            conectar_cel()

        elif opcao=='2':
            exit()
        
        else:
            inicio()


    else:
        print(  
        '---------------------------------------------------------------------------\n',
        '> Digite 3: Procurar por nome ou numero que esteja na sua conversa recente.\n',
        '> Digite 4: Enviar mensagem para a conversa selecionada\n',
        '> Digite 5: lê as ultimas mensagens na conversa selecionada.\n',
        '> Digite 6: Para encerrar.\n' 
        '---------------------------------------------------------------------------' )
        
        opcao=input('Digite a opção --> ')
        limpar()
        
        if opcao=='3':
            segunda_conf()
            #print('Qual numero ou nome salvo no contato ? Obs: Tem que ser exato.')
            #numero_procurado=input('Numero/nome --> ')
            localizacao=achar_numero(aux_total,total_de_conversas)
            
            if localizacao==0:
                print('Infelizmente não encontrei,Tente novamente...')
                inicio()
            else:
                try:
                    n_da_conversa=int(input('Escolha o n° da conversa para seleciona a conversa.\nDigite o n°: '))
                    selecionado=local_conversa[n_da_conversa]
                    print('A conversa foi Selecionada')
                except:
                    print('A conversa não foi selecionada corretamente.')
            inicio()

        elif opcao=='4':
            sua_mensagem=input('Atenção: A conversa tem que está selecionada\nSua mensagem: ')
            try:
                mandar_mensagem(sua_mensagem,selecionado)
            except:
                print('Error ao mandar a mensagem...\nA conversa está selecionada?')
            
            inicio()

        elif opcao=='5':
            print('--- Lendo a conversa selecionada ---')
            sleep(1)
            conversas=ler_mensagens(selecionado)
            inicio()
        
        elif opcao=='6':
            exit()

        else:
            inicio()
    




# --- Variaveis inicias:
url='https://web.whatsapp.com/'
ativacao=False
local_conversa=[]





## INICIO DO PROGRAMA
primeiro=input('------INICIO------\nAperta o ENTER para iniciar o navegador.')
navegador= Chrome()
navegador.get(url) #Iniciar o zap zap...

inicio()







