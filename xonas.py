import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong")

# Definições de cores
preto = (0, 0, 0)
branco = (255, 255, 255)

# Configurações da paleta do jogador
largura_paleta = 10
altura_paleta = 100
posicao_paleta_x = 50
posicao_paleta_y = altura_tela // 2 - altura_paleta // 2
velocidade_paleta = 5

# Configurações da bola
largura_bola = 20
altura_bola = 20
posicao_bola_x = largura_tela // 2 - largura_bola // 2
posicao_bola_y = altura_tela // 2 - altura_bola // 2
velocidade_bola_x = 5
velocidade_bola_y = 5

# Função para desenhar a paleta do jogador
def desenha_paleta(x, y):
    pygame.draw.rect(tela, branco, [x, y, largura_paleta, altura_paleta])

# Função para desenhar a bola
def desenha_bola(x, y):
    pygame.draw.rect(tela, branco, [x, y, largura_bola, altura_bola])

# Loop principal do jogo
def game_loop():
    global posicao_paleta_y, posicao_bola_x, posicao_bola_y, velocidade_bola_x, velocidade_bola_y
    jogo_ativo = True
    relogio = pygame.time.Clock()
    pontuacao = 0

    while jogo_ativo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_ativo = False

        # Captura das teclas pressionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            posicao_paleta_y -= velocidade_paleta
        if teclas[pygame.K_DOWN]:
            posicao_paleta_y += velocidade_paleta

        # Limites da tela para a paleta
        if posicao_paleta_y < 0:
            posicao_paleta_y = 0
        if posicao_paleta_y > altura_tela - altura_paleta:
            posicao_paleta_y = altura_tela - altura_paleta

        # Movimento da bola
        posicao_bola_x += velocidade_bola_x
        posicao_bola_y += velocidade_bola_y

        # Limites da tela para a bola
        if posicao_bola_y <= 0 or posicao_bola_y >= altura_tela - altura_bola:
            velocidade_bola_y = -velocidade_bola_y

        # Colisão com a paleta do jogador
        if (posicao_bola_x <= posicao_paleta_x + largura_paleta and
            posicao_bola_y + altura_bola >= posicao_paleta_y and
            posicao_bola_y <= posicao_paleta_y + altura_paleta):
            velocidade_bola_x = -velocidade_bola_x
            pontuacao += 1

        # Verificar se a bola saiu pela esquerda
        if posicao_bola_x < 0:
            jogo_ativo = False

        # Desenhar tudo
        tela.fill(preto)
        desenha_paleta(posicao_paleta_x, posicao_paleta_y)
        desenha_bola(posicao_bola_x, posicao_bola_y)

        # Mostrar a pontuação
        fonte = pygame.font.SysFont(None, 35)
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, branco)
        tela.blit(texto_pontuacao, [10, 10])

        pygame.display.flip()

        relogio.tick(60)

    pygame.quit()

# Iniciar o jogo
game_loop()
 