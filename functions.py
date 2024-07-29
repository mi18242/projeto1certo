import pygame
import random
from settings import *

def gerar_bomba(pixels, comida_x, comida_y):
    bomba_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    bomba_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    while ([bomba_x, bomba_y] in pixels) or ([bomba_x, bomba_y] == [comida_x, comida_y]):
        bomba_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
        bomba_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return bomba_x, bomba_y

def desenhar_bomba(tamanho, bomba_x, bomba_y):
    pygame.draw.rect(tela, vermelha, [bomba_x, bomba_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [10, 10])

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        if velocidade_y != -tamanho_quadrado:
            velocidade_x = 0
            velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        if velocidade_y != tamanho_quadrado:
            velocidade_x = 0
            velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        if velocidade_x != -tamanho_quadrado:
            velocidade_x = tamanho_quadrado
            velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        if velocidade_x != tamanho_quadrado:
            velocidade_x = -tamanho_quadrado
            velocidade_y = 0
    return velocidade_x, velocidade_y

def fim_de_jogo(pontuacao, capturas_verdes, capturas_azuis, capturas_amarelas):
    fim_jogo = True
    while fim_jogo:
        tela.fill(preta)
        fonte = pygame.font.SysFont("Helvetica", 60)
        fonte_menor = pygame.font.SysFont("Helvetica", 40)
        fonte_captura = pygame.font.SysFont("Helvetica", 25)
        mensagem = fonte.render("Fim de Jogo", True, vermelha)
        capturas_verdes_texto = fonte_captura.render(f"Capturas verdes: {capturas_verdes}", True, verde)
        captura_azuis_texto = fonte_captura.render(f"Capturas azuis: {capturas_azuis}", True, azul)
        captura_amarelas_texto = fonte_captura.render(f"Capturas amarelas: {capturas_amarelas}", True, amarelo)
        pontuacao_texto = fonte_menor.render(f"Pontuação: {pontuacao}", True, branca)
        reiniciar = fonte_menor.render("Pressione ENTER para Jogar Novamente", True, branca)
        tela.blit(mensagem, (largura / 2 - mensagem.get_width() / 2, altura / 4.5))
        tela.blit(capturas_verdes_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.75))
        tela.blit(captura_azuis_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.5))
        tela.blit(captura_amarelas_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.25))
        tela.blit(pontuacao_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2))
        tela.blit(reiniciar, (largura / 2 - reiniciar.get_width() / 2, altura / 1.5))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    fim_jogo = False
                    from main import menu_principal
                    menu_principal()
