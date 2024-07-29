import pygame
import random
from settings import *

class Comida(pygame.sprite.Sprite):
    def __init__(self, pixels):
        pygame.sprite.Sprite.__init__(self)
        tipos_comida = [
            {"cor": verde, "pontos": 1},
            {"cor": azul, "pontos": 2},
            {"cor": amarelo, "pontos": 3}
        ]
        self.tipo_comida = random.choice(tipos_comida)

        # Estabelecer SpriteSheet
        sprite_sheets = {
            verde: sprite_sheet_comida1,
            azul: sprite_sheet_comida2,
            amarelo: sprite_sheet_comida3
        }
        sprite_sheet = sprite_sheets[self.tipo_comida["cor"]]
        tamanho_por_imagem = 10
        self.imagens_comida = []
        for i in range(1):
            img = sprite_sheet.subsurface((i*tamanho_por_imagem, 0), (tamanho_por_imagem, tamanho_por_imagem))
            img = pygame.transform.scale(img, (tamanho_por_imagem*3, tamanho_por_imagem*3))
            self.imagens_comida.append(img)

        self.index_lista = 0
        self.image = self.imagens_comida[self.index_lista]

        retangulos_cobra = [[pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado] for pixel in pixels]
        self.rect = self.image.get_rect()
        self.comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
        self.comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
        self.rect.center = (self.comida_x, self.comida_y)
        while self.rect.collidelist(retangulos_cobra) != -1:
            self.comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
            self.comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
            self.rect.center = (self.comida_x, self.comida_y)

    def update(self):
        if self.index_lista > 0:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_comida[int(self.index_lista)]

