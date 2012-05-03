import cv

#Configuracoes
caminho_para_foto = "Magic.jpg" #Ideal q seja 640x480
titulo_janela = "Magic Game Card"
nome_jogador_1 = "Nome Jogador 1" 
nome_jogador_2 = "Nome Jogador 2"
vida_jogador_1 = 20
vida_jogador_2 = 20

class Magic:

	def __init__(self):
		imagem_de_fundo = cv.LoadImage(caminho_para_foto)
		cv.NamedWindow(titulo_janela, 1)
		cv.MoveWindow(titulo_janela,400,50)

		cv.CreateTrackbar(nome_jogador_1, titulo_janela, vida_jogador_1, 30, self.atualiza_vida_jogador_1)
		cv.CreateTrackbar(nome_jogador_2, titulo_janela, vida_jogador_2, 30, self.atualiza_vida_jogador_2)

		self.atualiza_vida_jogador_1(vida_jogador_1)
		self.atualiza_vida_jogador_2(vida_jogador_2)
		cv.ShowImage(titulo_janela,imagem_de_fundo)

	def atualiza_vida_jogador_1(self,vida_jogador_1):
		print "{0} esta com {1} pontos de vida".format(nome_jogador_1, vida_jogador_1)
		if vida_jogador_1 == 0:
			print "{0} morreu !\n{1} venceu a batalha !".format(nome_jogador_1,nome_jogador_2)
	def atualiza_vida_jogador_2(self,vida_jogador_2):
		print "{0} esta com {1} pontos de vida".format(nome_jogador_2, vida_jogador_2)
		if vida_jogador_2 == 0:
			print "{0} morreu !\n{1} venceu a batalha !".format(nome_jogador_2,nome_jogador_1)

if __name__ == "__main__":
	print "   ----- Log da Batalha -----"
	Magic()
	while True:
		tecla_apertada = cv.WaitKey(7) % 0x100 
		if tecla_apertada == 27:
			break

	print "Programa Finalizado"
	print "Elisson Michael - UENF"
