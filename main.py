import pygame
from settings import *
from sprites import Comida
from functions import gerar_bomba, desenhar_bomba, desenhar_cobra, desenhar_pontuacao, selecionar_velocidade, fim_de_jogo

def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    pixels = []
    pontuacao = 0
    capturas_verdes = 0
    capturas_azuis = 0
    capturas_amarelas = 0
    todas_sprites = pygame.sprite.Group()
    comida = Comida(pixels)
    todas_sprites.add(comida)
    bomba_x, bomba_y = gerar_bomba(pixels, comida.comida_x, comida.comida_y)

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        x += velocidade_x
        y += velocidade_y

        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        desenhar_bomba(tamanho_quadrado, bomba_x, bomba_y)
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(pontuacao)
        todas_sprites.draw(tela)
        todas_sprites.update()
        pygame.display.update()

        if pygame.Rect.colliderect(comida.rect, [pixels[-1][0], pixels[-1][1], tamanho_quadrado, tamanho_quadrado]):
            tamanho_cobra += 4
            if comida.tipo_comida['cor'] == verde:
                capturas_verdes += 1
            elif comida.tipo_comida['cor'] == azul:
                capturas_azuis += 1
            elif comida.tipo_comida['cor'] == amarelo:
                capturas_amarelas += 1
            pontuacao += comida.tipo_comida['pontos']
            todas_sprites.remove(comida)
            comida = Comida(pixels)
            todas_sprites.add(comida)
            bomba_x, bomba_y = gerar_bomba(pixels, comida.comida_x, comida.comida_y)
        relogio.tick(velocidade_jogo)
        if x == bomba_x and y == bomba_y:
            fim_jogo = True

    fim_de_jogo(pontuacao, capturas_verdes, capturas_azuis, capturas_amarelas)

def menu_principal():
    menu = True
    while menu:
        tela.fill(preta)
        fonte = pygame.font.SysFont("Helvetica", 50)
        titulo = fonte.render("Jogo Snake Python", True, verde)
        jogar = fonte.render("Pressione ENTER para Jogar", True, branca)
        tela.blit(titulo, (largura / 2 - titulo.get_width() / 2, altura / 3))
        tela.blit(jogar, (largura / 2 - jogar.get_width() / 2, altura / 2))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    menu = False

    rodar_jogo()

menu_principal()

