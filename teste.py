import pygame
import random
import os

# iniciar jogo:
pygame.init()

# nome do jogo:
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))  # setar o tamanho da tela
relogio = pygame.time.Clock()

# diretórios
diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal, 'sons')
sprite_sheet_comida1 = pygame.image.load(os.path.join(diretorio_imagens, 'comida1.png')).convert_alpha()
sprite_sheet_comida2 = pygame.image.load(os.path.join(diretorio_imagens, 'comida2.png')).convert_alpha()
sprite_sheet_comida3 = pygame.image.load(os.path.join(diretorio_imagens, 'comida3.png')).convert_alpha()

# cores:
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

# parâmetros da cobrinha:
tamanho_quadrado = 10
velocidade_jogo = 15

# classe comida
class Comida(pygame.sprite.Sprite):
    def __init__(self,pixels):
        pygame.sprite.Sprite.__init__(self)

        # decisão de qual comida será criada
        tipos_comida = [
        {"cor": verde, "pontos": 1},
        {"cor": azul, "pontos": 2},
        {"cor": amarelo, "pontos": 3}
    ]
        self.tipo_comida = random.choice(tipos_comida)

        # estabelecimento da SpriteSheet de acordo com qual comida foi escolhida
        if self.tipo_comida["cor"] == verde:
            tamanho_por_imagem = 10
            self.quantidade_imagens = 1
            sprite_sheet = sprite_sheet_comida1
            self.imagens_comida = []
            for i in range(self.quantidade_imagens):
                img = sprite_sheet.subsurface((i*tamanho_por_imagem, 0), (tamanho_por_imagem,tamanho_por_imagem))
                img = pygame.transform.scale(img, (tamanho_por_imagem*3, tamanho_por_imagem*3))
                self.imagens_comida.append(img)
        elif self.tipo_comida["cor"] == azul:
            tamanho_por_imagem = 10
            self.quantidade_imagens = 1
            sprite_sheet = sprite_sheet_comida2
            self.imagens_comida = []
            for i in range(self.quantidade_imagens):
                img = sprite_sheet.subsurface((i*tamanho_por_imagem, 0), (tamanho_por_imagem,tamanho_por_imagem))
                img = pygame.transform.scale(img, (tamanho_por_imagem*3, tamanho_por_imagem*3))
                self.imagens_comida.append(img)
        elif self.tipo_comida["cor"] == amarelo:
            tamanho_por_imagem = 10
            self.quantidade_imagens = 1
            sprite_sheet = sprite_sheet_comida3
            self.imagens_comida = []
            for i in range(self.quantidade_imagens):
                img = sprite_sheet.subsurface((i*tamanho_por_imagem, 0), (tamanho_por_imagem,tamanho_por_imagem))
                img = pygame.transform.scale(img, (tamanho_por_imagem*3, tamanho_por_imagem*3))
                self.imagens_comida.append(img)
        
        # estabelecimento da primeira imagem do objeto na SpriteSheet
        self.index_lista = 0
        self.image = self.imagens_comida[self.index_lista]

        # fazer uma lista com os retangulos da cobra
        retangulos_cobra = []
        for pixel in pixels:
            retangulos_cobra.append([pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado])
        
        # decisao da posicao da comida
        self.rect = self.image.get_rect() # criacao do retangulo da imagem
        self.comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
        self.comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
        self.rect.center = (self.comida_x, self.comida_y)
        while self.rect.collidelist(retangulos_cobra) != -1: #impedir que a comida apareça na mesma localização da cobra
            self.comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
            self.comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
            self.rect.center = (self.comida_x, self.comida_y)

    def update(self):
        if self.index_lista > (self.quantidade_imagens - 1):
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_comida[int(self.index_lista)]

# função para gerar bomba:
def gerar_bomba(pixels, comida_x, comida_y):
    bomba_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
    bomba_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    while ([bomba_x, bomba_y] in pixels) or ([bomba_x, bomba_y] == [comida_x, comida_y]): #impedir que a bomba apareça na mesma localização da cobra ou da comida
        bomba_x = round(random.randrange(0, largura - tamanho_quadrado) / 10.0) * 10.0
        bomba_y = round(random.randrange(0, altura - tamanho_quadrado) / 10.0) * 10.0
    return bomba_x, bomba_y

# função para desenhar bomba:
def desenhar_bomba(tamanho, bomba_x, bomba_y):
    pygame.draw.rect(tela, vermelha, [bomba_x, bomba_y, tamanho, tamanho])

# função para desenhar cobra:
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

# função para desenhar pontuação:
def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [10, 10])

# função selecionar velocidade:
def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        if velocidade_y != -tamanho_quadrado: #impedir que a cobra se movimente para o lado contrário daquele para o qual ela está andando
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

# função para exibir tela de fim de jogo:
def fim_de_jogo(pontuacao, capturas_verdes, capturas_azuis, capturas_amarelas):
    fim_jogo = True
    while fim_jogo:
        tela.fill(preta)
        
        fonte = pygame.font.SysFont("Helvetica", 60)
        fonte_menor = pygame.font.SysFont("Helvetica", 40) # para as mensagens de pontuação e reiniciar
        fonte_captura = pygame.font.SysFont("Helvetica", 25) # para as mensagens de pontuação e reiniciar
        
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
                    menu_principal()

# função para rodar jogo(contem o loop do jogo):
def rodar_jogo():
    fim_jogo = False
    # posição inicial da cobra:
    x = largura / 2
    y = altura / 2

    # velocidades da cobra em relação a pixels:
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []
    pontuacao = 0
    capturas_verdes = 0
    capturas_azuis = 0
    capturas_amarelas = 0

    # gerar comida e bomba, apenas uma inicialmente:
    todas_sprites = pygame.sprite.Group()
    comida = Comida(pixels)
    todas_sprites.add(comida)
    bomba_x, bomba_y = gerar_bomba(pixels, comida.comida_x, comida.comida_y)

    while not fim_jogo:
        tela.fill(preta)  # cor do fundo

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # acabou o jogo
                fim_jogo = True

            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)

        # atualizar posição da cobra:
        x += velocidade_x
        y += velocidade_y

        # verificar se a cobra bateu na borda:
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        # desenhar comida e a bomba:
        desenhar_bomba(tamanho_quadrado, bomba_x, bomba_y)
        
        # desenhar cobra:
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        # verificar se ele tá batendo:
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(pontuacao)

        # atualizar na tela:
        todas_sprites.draw(tela)
        todas_sprites.update()
        pygame.display.update()

        # criar uma nova comida:
        # criar nova bomba toda vez que uma comida for consumida
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
        # verificar colisão com a bomba:
        if x == bomba_x and y == bomba_y:
            fim_jogo = True



    fim_de_jogo(pontuacao, capturas_verdes, capturas_azuis, capturas_amarelas)

# função para exibir o menu principal:
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

# exibir o menu principal:
menu_principal()