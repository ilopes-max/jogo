#importando o pygame e dando um nome 
import pygame as pg
from classe_inimigo import Inimigo
from classe_jogador import Jogador


pg.init() #inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

clock = pg.time.Clock()

#Criando a tela
tela = pg.display.set_mode((1000,500))

#configurando a tela
pg.display.set_caption ("JOGO DA POCOYOYA")

#carrengo imagens 
estrada = pg.image.load("scr/img/estrada.png")
hamster = pg.image.load("scr/img/pocoya1.png")
capa_inicio = pg.image.load("scr/img/bemvindo.png")



#diminuindo o tamanho da imagem
estrada = pg.transform.scale(estrada, (1000,500))
capa_inicio = pg.transform.scale(capa_inicio, (1000,500))


#criando um inimigo
lista_inimigo = [Inimigo("scr/img/carro1.png"),
                 Inimigo("scr/img/carro2.png"),
                 Inimigo("scr/img/carro3.png"),
                 Inimigo("scr/img/carro4.png"),
                 Inimigo('scr/img/carro5.png'),
                 Inimigo("scr/img/carro6.png"),
                 Inimigo('scr/img/carro7.png'),
                 Inimigo('scr/img/carro8.png'),
                 Inimigo("scr/img/carro9.png"),
                 Inimigo("scr/img/carro10.png")]

hamster = Jogador()
status_jogo = "INICIO"


#vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pg.event.get() #peggo todos os enventos que acontecem na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para SAIR
            pg.quit() #encerro o jogo
#pegando a lista de teclas pressionadas
    teclas_pressionadas = pg.key.get_pressed()
    if status_jogo == "INICIO":
        tela.blit(capa_inicio,(0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
    
    if status_jogo == "JOGANDO":
        tela.fill((255,255,255))
        tela.blit(estrada, (0,0))

        hamster.exibir(tela)
        hamster.andar(teclas_pressionadas)
    #fazendo o inimigo andar
        for inimigo in lista_inimigo:
            inimigo.andar()
            inimigo.exibir(tela)
            if hamster.mascara.overlap(inimigo.mascara,(hamster.pos_x - inimigo.pos_x_carro, hamster.pos_y - inimigo.pos_y_inimigo)):
                inimigo.voltar()
                hamster.gritar()
                hamster.voltar()

  
#atualizando a tela
    pg.display.update()
    #controlar o FPS (frames por segundo)
    clock.tick(60)
    #atualiza a tela
    pg.display.update()