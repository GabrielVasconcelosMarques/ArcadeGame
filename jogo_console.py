from random import *
from pygame import *
saldo = 0
lista_saldo_atual = []
pontos = 0
lista_nomes_usuario = []
lista_pontuacao = []


# Função para ler os arquivos de perguntas
def pergunta(msg):
    global pontos
    arquivo = open(msg, 'r')
    resposta = ''
    soma_saldo_atual = (sum(lista_saldo_atual))
    print('=-'*50)
    for pos, linha in enumerate(arquivo):
        print(linha)
        if pos == 5:
            if resposta in linha:
                pontos += 1
                saldo_atual(saldo)
                print('Parabéns, você acertou')
                print()
            elif resposta not in linha:
                print('Que pena, você errou')
                print()
                print(f'O jogo acabou, seu saldo foi de {soma_saldo_atual} reais.')
                print(f'Sua pontuação foi de {pontos} pontos.')
                
                resposta = input(f'Você deseja continuar jogando? S/N: ').upper()
                if resposta in "Nn":
                    print(f'O jogo acabou, seu saldo foi de {soma_saldo_atual} reais.')
                    print(f'Sua pontuação foi de {pontos} pontos.')
                    adicionar_ranking('ranking.txt')
                    print(exibirranking())
                    exit()
                

        if pos == 4:
            resposta = input('Digite sua resposta: ').upper()

    arquivo.close()

    
# Função para reprodução da música de suspense
def musica():
    mixer.init()
    mixer.music.load('video1.mp3')
    mixer.music.play()


# Função para adicionar nome do usuário ao ranking
def adicionar_ranking(msg):
    listaR = []
    texto = '{} {}\n'.format(pontos, nome_usuario)
    listaR.append(texto)
    ranking = open(msg, 'a')
    ranking.write(texto)
    ranking.close()


# Função para exibir o ranking
def exibirranking():
    listaR = []
    arq1 = open('ranking.txt', 'r')
    for g in arq1:
        listaR.append(g)


    listaTuplas = []
    listaNomes = ''
    
    for i in listaR: 
        guardaPosicao = 0
        pontos = ''
        nomeJogador = ''
        for pos,j in enumerate(i):
            if j == " ":
                guardaPosicao = pos
                break

        for k in range(0,guardaPosicao):
            pontos += i[k]
                    
        for letra in range(guardaPosicao+1, len(i)):
            nomeJogador += i[letra]
				
                
        listaTuplas.append((int(pontos),nomeJogador))

        guardaPosicao = 0
        numeros = ''	
        nomeJogador = ''
    
    novaLista = sorted(listaTuplas, reverse=True)

    for pos,i in enumerate(novaLista):
        if pos < 10:
            listaNomes += '{}° - {}    \n      {}\n\n'.format(pos+1, i[1].replace('\n',''), i[0])

    return listaNomes
            



# Função para acumular o saldo
def saldo_atual(saldo):
    saldo = saldo
    saldo += 1500
    lista_saldo_atual.append(saldo)
    soma_saldo_atual = (sum(lista_saldo_atual))
    print(f'Seu saldo atual é de {soma_saldo_atual}')
    print()


# Função para o título ficar mais atrativo ao usuário
def titulo(msg):
    tamanho = len(msg) + 4
    print('~'* tamanho)
    print(f'  {msg}')
    print('~'* tamanho)



# Lista de perguntas organizadas de acordo com a dificuldade
lista_perguntas_facil = ['pergunta1.txt', 'pergunta2.txt', 'pergunta3.txt', 'pergunta4.txt']
lista_perguntas_medio = ['pergunta5.txt', 'pergunta6.txt', 'pergunta7.txt', 'pergunta8.txt'] 
lista_perguntas_dificil = ['pergunta9.txt', 'pergunta10.txt', 'pergunta11.txt', 'pergunta12.txt']


# Iteração com o usuário
musica()
titulo('                     Bem vindo Usuário                     ')
nome_usuario = input('Digite seu nome: ')
lista_nomes_usuario.append(nome_usuario)
print()
print(f'Seja bem vindo {nome_usuario} ao "SHOW DE DINHEIRO", onde o objetivo é acertar perguntas e ir acumulando dinheiro.')
comecar = input('Digite ENTER para começar...')

# sorteando perguntas, de acordo com o nivel de dificuldade
shuffle (lista_perguntas_facil) 
shuffle (lista_perguntas_medio) 
shuffle (lista_perguntas_dificil) 

# Chamando as perguntas de acordo com a dificuldade
while True:
    pergunta(lista_perguntas_facil[0])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_facil[1])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_facil[2])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_facil[3])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_medio[0])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_medio[1])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_medio[2])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_medio[3])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_dificil[0])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_dificil[1])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_dificil[2])
    print(f'Sua pontuação é de {pontos} pontos.')
    pergunta(lista_perguntas_dificil[3])
    print(f'Sua pontuação é de {pontos} pontos.')
    resposta = input(f'Você deseja continuar jogando? S/N').upper()

    print(lista_nomes_usuario)




