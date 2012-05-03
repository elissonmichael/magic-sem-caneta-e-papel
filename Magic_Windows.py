import cv
from os import system

#Configuracoes
caminho_para_foto = "Magic.jpg" #Ideal q seja 640x480
titulo_janela = "Magic Game Card"
nome_jogador_1 = "Elisson" 
nome_jogador_2 = "Krishynan"
vida_jogador_1 = 20
vida_jogador_2 = 20
vida_maxima = 40

class Magic:

	def __init__(self):
		self.imagem_de_fundo = cv.LoadImage(caminho_para_foto)
		cv.NamedWindow(titulo_janela, 1)
		cv.MoveWindow(titulo_janela,400,50)
		self.imprime_texto_titulo()
		self.atualizar_tela()
	
	def imprime_texto_titulo(self):
		print "   ----- Log da Batalha -----"
		print "    {0} VersuS {1} ".format(nome_jogador_1,nome_jogador_2)		
	
			
	def atualizar_tela(self):
		cv.CreateTrackbar(nome_jogador_1, titulo_janela, vida_jogador_1, vida_maxima, self.atualiza_vida_jogador_1)
		cv.CreateTrackbar(nome_jogador_2, titulo_janela, vida_jogador_2, vida_maxima, self.atualiza_vida_jogador_2)
		cv.ShowImage(titulo_janela,self.imagem_de_fundo)


	def atualiza_vida_jogador_1(self,vida_jogador_1):
		if vida_jogador_1 == 0:
			print "\n\n\n{0} morreu !\n{1} venceu a batalha !\n\n\n".format(nome_jogador_1,nome_jogador_2)
		print "$ {0} $".format(nome_jogador_1)
		self.atualizar_tela()

	def atualiza_vida_jogador_2(self,vida_jogador_2):
		
		if vida_jogador_2 == 0:
			print "\n\n\n{0} morreu !\n{1} venceu a batalha !\n\n\n".format(nome_jogador_2,nome_jogador_1)
		print "# {0} #".format(nome_jogador_2)
		self.atualizar_tela()

if __name__ == "__main__":
	
	partida = Magic()
			
	while True:
		tecla_apertada = cv.WaitKey(7) % 0x100
		
		if tecla_apertada == 32 or tecla_apertada == 114:
			vida_jogador_1 = 20
			vida_jogador_2 = 20
			partida.atualiza_vida_jogador_1(vida_jogador_1)			
			partida.atualiza_vida_jogador_2(vida_jogador_2)
			system("clear")
			partida.imprime_texto_titulo()

		if tecla_apertada == 97: # A
			vida_jogador_1 = vida_jogador_1 - 1
			partida.atualiza_vida_jogador_1(vida_jogador_1)
			print "Perdeu 1 ponto de vida. ({0}) ".format(vida_jogador_1)
		
		if tecla_apertada == 115:# S
			vida_jogador_2 = vida_jogador_2 - 1
			partida.atualiza_vida_jogador_2(vida_jogador_2)
			print "Perdeu 1 ponto de vida. ({0}) ".format(vida_jogador_2)
		
		if tecla_apertada == 100:# D
			vida_jogador_1 = vida_jogador_1 + 1
			partida.atualiza_vida_jogador_1(vida_jogador_1)
			print "Ganhou vida em 1 ponto. [{0}] ".format(vida_jogador_1)
		
		if tecla_apertada == 119:# W
			vida_jogador_2 = vida_jogador_2 + 1
			partida.atualiza_vida_jogador_2(vida_jogador_2)
			print "Ganhou vida em 1 ponto. [{0}] ".format(vida_jogador_2)
		
		if tecla_apertada == 27:
			break

	

	print "Programa Finalizado"
	print "Elisson Michael - UENF"
