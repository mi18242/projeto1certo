import pygame
import os

# Configurações
pygame.init()
largura, altura = 800, 600
tamanho_quadrado = 10
velocidade_jogo = 15

# Tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Snake Python")
relogio = pygame.time.Clock()

# Diretórios
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

# Imagens
sprite_sheet_comida1 = pygame.image.load(os.path.join(diretorio_imagens, 'comida1.png')).convert_alpha()
sprite_sheet_comida2 = pygame.image.load(os.path.join(diretorio_imagens, 'comida2.png')).convert_alpha()
sprite_sheet_comida3 = pygame.image.load(os.path.join(diretorio_imagens, 'comida3.png')).convert_alpha()

# Cores
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

