import pygame as pg
import random

class Inimigo:
    def __init__(self, endereco_imagem):
        self.carro = pg.image.load(endereco_imagem)
        self.carro = pg.transform.scale(self.carro, (80,80))
        self.pos_x_carro = -10
    #criando um atributo
        self.pos_y_inimigo = random.randint(0,500)
        self.velocidade = random.randint(1,20)


    def andar(self):
         self.pos_x_carro = self.pos_x_carro +self.velocidade

         if self.pos_x_carro>900:
              self.voltar()


    def exibir(self,tela_do_jogo):
         tela_do_jogo.blit(self.carro, (self.pos_x_carro, self.pos_y_inimigo))

    def voltar(self):
        self. pos_x_carro = -100
        self.pos_y_inimigo = random.randint(0,500)
        self.velocidade = random.randint(1,20)


