from tkinter import *
from random import *
from pygame import *
from time import sleep
from tkinter import messagebox

play = "Iniciar Jogo"
rank = "Ranking"
info = "Informações"
fechar = "Fechar"

bt1 = ''
bt2 = ''
bt3 = ''
bt4 = ''
bt5 = ''

# Status definido para a função menu
status = False


# Inicio da confihuração da janela
janela = Tk()
janela.geometry('1280x1024')
janela.configure(background="gray")
image=PhotoImage(file='C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\arcade11.png')
image=image.subsample(1,1)
labelImage=Label(image=image)
labelImage.place(x=0,y=0,relwidth=1.0,relheight=1.0)
lbl = Label(text='Bem vindo ao "ARCADE DO GABRIEL!!!"', font="MathJax_Main 30", bg='#6A5ACD')
lbl.pack()
lb2 = Label(text='Digite seu nome neste espaço abaixo: ', font="MathJax_Main 15", bg='#6A5ACD')
lb2.pack()
lb3 = Label(text='00 ', font="MathJax_Main")
lb3.pack(side=BOTTOM)

# Labels caso o usuário deseje adicionar saldo
#lb3.pack(side=BOTTOM)
#lb2 = Label(text='Saldo: ', font="MathJax_Main")
#lb2.pack(side=BOTTOM)


listasorteio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resportaCorreta = ''

quantiDadeJogadas = 0

saldo = 0

# Função definidada para o usuário fechar o jogo
def fechar():
	global janela
	janela.destroy()


# Função para ocultar o conteudo do label e trazer outro plano de fundo para uma nova janela
def ocultar():
	global image
	image = PhotoImage(file="C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\arcade11.png")
	lbimagem = Label(image= image)
	lbimagem.place(x=0, y=0)


# Função definida para caso o usuário perca o jogo
def gameover():
	global lbl
	lbl['text'] = ''
	ocultar()
	global image
	image = PhotoImage(file="C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\over3.png")
	lbimagem = Label(image= image)
	lbimagem.place(x=0,y=0)


# Função definida para caso o usuário vença o jogo
def win():
	global lbl
	lbl['text'] = ''
	ocultar()
	global image
	image = PhotoImage(file="C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\win2.png")
	lbimagem = Label(image= image)
	lbimagem.place(x=10,y=-120)



# Função para reprodução da música de suspense
def musica():
    mixer.init()
    mixer.music.load('C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\video1.mp3')
    mixer.music.play()

# Função para reprodução de uma música caso o usuário erre a resposta
def musica_fim():
	mixer.init()
	mixer.music.load('C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\fim1.mp3')
	mixer.music.play()

# Função para reprodução de uma música caso o usuário acerte a resposta
def musica_passou():
	mixer.init()
	mixer.music.load('C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\passounivel.mp3')
	mixer.music.play()

# Função para reprodução de uma música caso o usuário vença o jogo
def aplausos():
	mixer.init()
	mixer.music.load('C:\\Users\\Gabriel Vasconcelos\\Desktop\\Gabriel\\arcade gabriel\\aplausos.mp3')
	mixer.music.play()


# Função para mostrar o saldo na tela
def saldo_na_tela():
	global saldo
	saldo +=100
	h = lb3['text']
	total = int(h) + 100
	lb3['text'] = str(total)


# Função criada para as instruções do jogo
def informacao():
	arq = open('informacao.txt','r', encoding='latin-1')
	perg = []
	for pos, i in enumerate(arq):
		perg.append(i)
		print(i)
	lbl['text'] = '{}\n{}\n{}\n{}\n'.format(perg[0], perg[1], perg[2], perg[3])

nomeusuario = ''
# Função criada para verificação da resposta do usuário
def verificaRespota(rUser):	
	global nomeusuario
	if quantiDadeJogadas == 0:
		if tbRes.get().upper() == '':
			messagebox.showerror('Erro', 'Por favor informe seu nome: ')
		else:
			nomeusuario = tbRes.get()
			bt1['text'] = "Confirma Resposta"
			mudar()


	elif rUser == resportaCorreta:
		musica_passou()
		sleep(6)
		musica()
		saldo_na_tela()
		print('	C O R R E T O')
		mudar()

	else:
		gameover()
		musica_fim()
		salvar_ranking()
		print(' E R R O O O U U U U')

	#limpar respota do usuario, iniciando do 0 até o FIM
	tbRes.delete(0, END)
	global status
	status = False

# Função criada para salvar o ranking
def salvar_ranking():
	listaR = []
	texto = '{} {}\n'.format(saldo, nomeusuario)
	arq1 = open('ranking.txt', 'a')
	arq1.write(texto)


# Função criada para aleatoriedade das questões
def listas_sorteio():
        n = 0

        if len(listasorteio) == 0:
                pass
        else:
                n = choice(listasorteio)
                listasorteio.remove(n)
        return n

# Função criada para mudar a tela caso o usuário vença o jogo e para ler os arquivos de perguntas
def mudar():
	global bt3
	global bt5
	global resportaCorreta
	global quantiDadeJogadas

	meuIndice = listas_sorteio()

	if meuIndice == 0:
		salvar_ranking()
		win()
		aplausos()
		print('Acabou')
	else:
		arq = open('pergunta{}.txt'.format(str(meuIndice)),'r', encoding='latin-1')
		perg = []

		for pos, i in enumerate(arq):
			perg.append(i)

		resportaCorreta = perg[5]
		lbl['text'] = '{}\n\n{}\n{}\n{}\n{}'.format(perg[0],perg[1],perg[2],perg[3],perg[4])
		bt3.destroy()
		bt5.destroy()
		lb2['text'] = 'Digite aqui a alternativa que você escolheu: '

		quantiDadeJogadas += 1

musica()
tbRes = Entry(bg='#FF0000', font="MathJax_Main 20")
tbRes.pack()

# Função criada para definir o menu
def menu():
	global bt1
	global bt2
	global bt3
	global bt4
	global bt5
	bt1 = Button(text='Iniciar Jogo', font="MathJax_Main", width='55', bg="#4169E1", fg="black", height = '2', command=lambda: verificaRespota(tbRes.get().upper()))
	bt1.pack()

	bt2 = Button(text='Fechar', font="MathJax_Main", width='55', bg="#4169E1", fg="black", height = '2', command=fechar)
	bt2.pack()

	bt3 = Button(text='Instrução', font="MathJax_Main", width='55', bg="#4169E1", fg="black", height = '2', command=informacao)
	bt3.pack()

	bt5 = Button(text='Ranking', font="MathJax_Main", width='55', bg="#4169E1", fg="black", height = '2', command=ranking)
	bt5.pack()

	
	if status == False:
		bt4 = Button(text='Voltar menu', font="MathJax_Main", width='55', bg="#4169E1", fg="black", height = '2', command=voltar_menu)
		bt4.pack()


# Função criada para elaboração do ranking
def ranking():
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

    
	novaLista = sorted(listaTuplas, reverse=True)


	for pos,i in enumerate(novaLista):
		if pos < 10:
			listaNomes += '{}° - {}    \n      {}\n\n'.format(pos+1, i[1].replace('\n',''), i[0])

	messagebox.showinfo("RANK", listaNomes)
	#print(listaNomes)

# Função criada para o botão volta menu
def voltar_menu():
	global quantiDadeJogadas
	global status
	
	if status == False:
		status = True
		quantiDadeJogadas = 0
		bt1.destroy()
		bt2.destroy()
		bt3.destroy()
		menu()
		lbl['text'] = 'Bem vindo ao "SHOW DO MILHÃO!!!"'
		bt1['text'] = 'Iniciar Jogo'
		

menu()
janela.mainloop()


