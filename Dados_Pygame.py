import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da Tela
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Dados")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 255)

# Fonte
fonte = pygame.font.Font(None, 34)

# Botões
botao_jogar = pygame.Rect(200, 320, 230, 50)
botao_confirmar = pygame.Rect(200, 250, 230, 50)  # Novo botão para confirmar o palpite

# Variáveis do Jogo
lancamento1, lancamento2, lancamento3 = None, None, None
palpite = None
mensagem = ""
jogando = True
aguardando_resultado = False  # Estado intermediário para entrada do palpite

# Caixa de Entrada do Usuário
input_ativo = False
input_texto = ""

# Função para desenhar texto na tela
def desenhar_texto(texto, x, y, cor=BRANCO):
    render = fonte.render(texto, True, cor)
    tela.blit(render, (x, y))

# Função principal do jogo
def jogo():
    global lancamento1, lancamento2, lancamento3, palpite, mensagem, input_ativo, input_texto, jogando, aguardando_resultado
    
    rodando = True
    while rodando:
        tela.fill(PRETO)  # Limpa a tela
        
        desenhar_texto("Jogo de Dados", 200, 20, BRANCO)
        
        if jogando:
            desenhar_texto("Pressione o botão abaixo ", 150, 110, BRANCO)
            desenhar_texto("para lançar os dados", 170, 140, BRANCO)

            pygame.draw.rect(tela, VERDE, botao_jogar)
            desenhar_texto("Lançar Dados", 220, 335, PRETO)
        
        elif aguardando_resultado:
            desenhar_texto(f"Lançamento 1: {lancamento1}", 200, 80, BRANCO)
            desenhar_texto(f"Lançamento 2: {lancamento2}", 200, 120, BRANCO)
            desenhar_texto("Digite abaixo o seu palpite:", 180, 160, BRANCO)
            
            # Caixa de entrada do usuário
            pygame.draw.rect(tela, BRANCO, (200, 190, 200, 40))
            desenhar_texto(input_texto, 220, 200, PRETO)

            # Botão para confirmar o palpite
            pygame.draw.rect(tela, VERDE, botao_confirmar)
            desenhar_texto("Confirmar Palpite", 205, 265, PRETO)

            desenhar_texto(mensagem, 150, 300, AZUL)

        else:  # Exibir o resultado e a opção de jogar novamente
            desenhar_texto(f"Lançamento 1: {lancamento1}", 200, 80, BRANCO)
            desenhar_texto(f"Lançamento 2: {lancamento2}", 200, 120, BRANCO)
            desenhar_texto(f"Lançamento 3: {lancamento3}", 200, 160, BRANCO)
            desenhar_texto(mensagem, 150, 220, AZUL)

            pygame.draw.rect(tela, VERDE, botao_jogar)
            desenhar_texto("Jogar Novamente", 215, 335, PRETO)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            if jogando:
                if evento.type == pygame.MOUSEBUTTONDOWN and botao_jogar.collidepoint(evento.pos):
                    # Gera os lançamentos
                    lancamento1 = random.randint(1, 6)
                    lancamento2 = random.randint(1, 6)
                    lancamento3 = random.randint(1, 6)

                    input_texto = ""
                    mensagem = ""
                    jogando = False
                    aguardando_resultado = True  # Agora o jogo espera o palpite do jogador
                    input_ativo = True
            
            elif aguardando_resultado:
                if evento.type == pygame.KEYDOWN and input_ativo:
                    if evento.key == pygame.K_BACKSPACE:
                        input_texto = input_texto[:-1]
                    else:
                        input_texto += evento.unicode

                # Novo botão para confirmar o palpite
                if evento.type == pygame.MOUSEBUTTONDOWN and botao_confirmar.collidepoint(evento.pos):
                    try:
                        palpite = int(input_texto)
                        if 1 <= palpite <= 6:
                            input_ativo = False
                            aguardando_resultado = False  # Agora o jogo exibe o resultado
                            if palpite == lancamento3:
                                mensagem = " Você Acertou!"
                            else:
                                mensagem = f" Errou! O número era {lancamento3}"
                        else:
                            mensagem = "Erro! Escolha um número entre 1 e 6."
                    except ValueError:
                        mensagem = "Erro! Digite um número válido."
            
            else:  # Estado final (exibição do resultado)
                if evento.type == pygame.MOUSEBUTTONDOWN and botao_jogar.collidepoint(evento.pos):
                    jogando = True  # Reinicia o jogo
                    aguardando_resultado = False
                    input_ativo = False

    pygame.quit()

# Rodar o jogo
jogo()
