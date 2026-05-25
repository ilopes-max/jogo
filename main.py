#importando o pygame e dando um nome 
import pygame as pg

pg.init() #inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

#Criando a tela
tela = pg.display.set_mode((800,300))

#configurando a tela
pg.display.set_caption ("Meu primeiro jogo")

#trocando a cor da tela 
tela.fill (161,226,241)

#vou criar um loop infinito para manter a janela aberta
while True:
    lista_eventos = pg.event.get() #peggo todos os enventos que acontecem na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para SAIR
            pg.quit() #encerro o jogo

    #atualizando a tela
    pg.display.update()