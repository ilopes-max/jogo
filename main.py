#importando o pygame e dando um nome 
import pygame as pg
from classe_inimigo import Inimigo
from classe_jogador import Jogador
from caminho_relativo import resource_path as rp 


pg.init() #inicializa os módulos do pygame, a maioria iria funcionar sem, mas alguns necessitam inicializar

clock = pg.time.Clock()

#Criando a tela
tela = pg.display.set_mode((1000,500))

#configurando a tela
pg.display.set_caption ("JOGO DA POCOYOYA")

#carrengo imagens 
estrada = pg.image.load(rp("scr/img/estrada.png"))
hamster = pg.image.load(rp("scr/img/pocoya1.png"))
capa_inicio = pg.image.load(rp("scr/img/bemvindo.png"))
capa_perdeu = pg.image.load(rp("scr/img/voceperdeu.png"))
capa_ganhar = pg.image.load(rp("scr/img/voceganhou.png"))



#diminuindo o tamanho da imagem
estrada = pg.transform.scale(estrada, (1000,500))
capa_inicio = pg.transform.scale(capa_inicio, (1000,500))
capa_perdeu = pg.transform.scale (capa_perdeu,(1000,500))
capa_ganhar = pg.transform.scale (capa_ganhar, (1000,500))


#criando um inimigo
lista_inimigo = [Inimigo(rp("scr/img/carro1.png")),
                 Inimigo(rp("scr/img/carro2.png")),
                Inimigo(rp("scr/img/carro3.png")),
                Inimigo(rp("scr/img/carro4.png"))
                ]

fonte = pg.font.SysFont("Elephant", 16,True,False)

hamster = Jogador()
status_jogo = "INICIO"

contador_morte = 0

contador_pontos = 0 



#vou criar um loop infinito para manter a janela aberta
rodando = True 
while rodando:
    lista_eventos = pg.event.get() #pego todos os enventos que acontecem na janela
    for evento in lista_eventos: #percorro os eventos
        if evento.type == pg.QUIT: #verifico se um dos eventos é para SAIR
            rodando = False
#pegando a lista de teclas pressionadas
    teclas_pressionadas = pg.key.get_pressed()
    if status_jogo == "INICIO":
        tela.blit(capa_inicio,(0,0))
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
    
    if status_jogo == "JOGANDO":
        tela.fill((255,255,255))
        tela.blit(estrada, (0,0))
        #renderizando e inserindo o  texto
        texto_pontuacao = fonte.render(f"Pontuação: {contador_pontos}", True,(255,255,255),None)
        tela.blit(texto_pontuacao,(0,0))

        hamster.exibir(tela)
        hamster.andar(teclas_pressionadas)
    #fazendo o inimigo andar
        for inimigo in lista_inimigo:
            inimigo.andar()
            inimigo.exibir(tela)
            if hamster.mascara.overlap(inimigo.mascara,(inimigo.pos_x_carro - hamster.pos_x,  inimigo.pos_y_inimigo - hamster.pos_y)):
                inimigo.voltar()
                hamster.gritar()
                hamster.voltar()
                contador_morte += 1
                if contador_morte ==3:
                    status_jogo = "PERDEU"
                    hamster.gritar()
                    contador_morte = 0  
                    contador_pontos = 0
                
            
    if hamster.pos_x == 500:
        contador_pontos = contador_pontos +1
        hamster.voltar()
        if contador_pontos ==5:
         status_jogo = "GANHOU"
         
         if status_jogo =="GANHOU":
            tela.blit(capa_ganhar,(0,0))
            hamster.ganhou()
    
       

    if status_jogo == "PERDEU":
        tela.blit(capa_perdeu,(0,0))
       
        if teclas_pressionadas[pg.K_KP_ENTER] or teclas_pressionadas[pg.K_RETURN]:
            status_jogo = "JOGANDO"
    
   

  
#atualizando a tela
    pg.display.update()
    #controlar o FPS (frames por segundo)
    clock.tick(60)
    #atualiza a tela
    pg.display.update()