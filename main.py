#importando o pygame e dando um nome 
import pygame as pg
from classe_inimigo import Inimigo


pg.init() #inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

clock = pg.time.Clock()

#Criando a tela
tela = pg.display.set_mode((1000,500))

#configurando a tela
pg.display.set_caption ("Jogo da Isa")

#carrengo imagens 
estrada = pg.image.load("scr/img/estrada.png")
hamster = pg.image.load("scr/img/bicho1.png")



#diminuindo o tamanho da imagem
estrada = pg.transform.scale(estrada, (1000,500))
hamster = pg.transform.scale(hamster, (60,60))

#criando um inimigo
lista_inimigo = [Inimigo("scr/img/carro2.png"),
                 Inimigo("scr/img/carro3.png"),
                 Inimigo("scr/img/carro2.png"),
                 Inimigo('scr/img/carro3.png'),
                 Inimigo('scr/img/carro2.png'),
                 Inimigo('scr/img/carro3.png')]

#criando uma variavel que vai definir a posição do hamster
pos_x_hamster=0
pos_y_hamster=0


#vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pg.event.get() #peggo todos os enventos que acontecem na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para SAIR
            pg.quit() #encerro o jogo
#pegando a lista de teclas pressionadas
    teclas_pressionadas = pg.key.get_pressed()

    #verifico se a tecla da direita está pressionada 
    if teclas_pressionadas[pg.K_RIGHT]:
        pos_x_hamster = pos_x_hamster +5
    if teclas_pressionadas[pg.K_LEFT]:
        pos_x_hamster = pos_x_hamster -5
    if teclas_pressionadas [pg.K_UP]:
        pos_y_hamster = pos_y_hamster -5                           
    if teclas_pressionadas[pg.K_DOWN]:
        pos_y_hamster = pos_y_hamster +5
    
# ===== LIMITES =====

#esquerda
    if pos_x_hamster < 0:
        pos_x_hamster = 0

#direita
    if pos_x_hamster > 950 :
        pos_x_hamster = 950 

#cima
    if pos_y_hamster< 0:
        pos_y_hamster= 0

#baixo
    if pos_y_hamster > 450:
        pos_y_hamster = 450
#exibindo a imagem do hamster 
    tela.blit(estrada, (0,0))
    tela.blit(hamster,(pos_x_hamster,pos_y_hamster))
#fazendo o inimigo andar
    for inimigo in lista_inimigo:
        inimigo.andar()
        inimigo.exibir(tela)
    
    



#atualizando a tela
    pg.display.update()
    #controlar o FPS (frames por segundo)
    clock.tick(60)
    #atualiza a tela
    pg.display.update()