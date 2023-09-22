import pygame
import sys


# Cores
VERDE_CLARO = pygame.Color("lightgreen")  # Cor de fundo verde claro
BRANCO = pygame.Color("white")  # Cor de fundo branco
PRETO = pygame.Color("black")  # Cor de fundo preto
VERMELHO = pygame.Color("red")  # Cor de fundo vermelho
VERDE = pygame.Color("green")  # Cor de fundo verde

pygame.init()
pygame.font.init()

# Fontes
FONTES = {"padrao": pygame.font.Font(None, 36), "grande": pygame.font.Font(None, 72)}

# Tamanhos
LARGURA = 1280
ALTURA = 720
LARGURA_BOTAO = LARGURA // 2
ALTURA_BOTAO = 80

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_ativa=VERDE, cor_inativa=BRANCO):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.texto = texto
        self.cor_ativa = cor_ativa
        self.cor_inativa = cor_inativa

        # Adicionando o atributo retangulo
        self.retangulo = pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, janela, acao=None):
        mouse = pygame.mouse.get_pos()
        clique = pygame.mouse.get_pressed()

        if self.retangulo.collidepoint(mouse):
            pygame.draw.rect(janela, self.cor_ativa, self.retangulo)
            if clique[0] == 1 and acao is not None:
                pygame.time.delay(200)
                acao()
        else:
            pygame.draw.rect(janela, self.cor_inativa, self.retangulo)

        texto_botao = FONTES["padrao"].render(self.texto, True, PRETO)
        janela.blit(texto_botao, (self.x + (self.largura // 2 - texto_botao.get_width() // 2), self.y + (self.altura // 2 - texto_botao.get_height() // 2)))

class SimuladorListas:
    def __init__(self):

        self.janela_principal = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption("Simulador de Listas")

        # Texto do título no menu principal
        self.titulo = FONTES["grande"].render("Simulador de Listas", True, PRETO)

        # Dicionário para armazenar os botões do menu
        self.botoes = {}

        # Cria os botões do menu usando a função criar_botao       
        self.botoes["lse"] = Botao(LARGURA // 4, ALTURA // 4, LARGURA_BOTAO, ALTURA_BOTAO, "Lista Simplesmente Encadeada")
        self.botoes["lde"] = Botao(LARGURA // 4, ALTURA // 2, LARGURA_BOTAO, ALTURA_BOTAO, "Lista Duplamente Encadeada")
        self.botoes["lista_sequencial"] = Botao(LARGURA // 4, 3 * ALTURA // 4, LARGURA_BOTAO, ALTURA_BOTAO, "Lista Sequencial")

        # Estado inicial
        self.estado = "menu"  # Pode ser "menu", "lse", "lde" ou "lista_sequencial"

    def criar_janela(self, titulo):
        nova_janela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(titulo)
        return nova_janela

    def executar(self):
        # Loop principal
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.estado == "menu":
                        # Verifica se algum botão do menu foi clicado
                        for nome, botao in self.botoes.items():
                            if botao.retangulo.collidepoint(evento.pos):
                                # Muda o estado para o nome do botão clicado
                                self.estado = nome

                    elif self.estado != "menu":
                        # Voltar para o menu principal quando o botão "Voltar" for pressionado
                        if self.botao_voltar.retangulo.collidepoint(evento.pos):
                            self.estado = "menu"

            # Preencha a janela com a cor de fundo verde claro
            self.janela_principal.fill(VERDE_CLARO)

            if self.estado == "menu":
                # Desenha os botões do menu na tela
                for botao in self.botoes.values():
                    botao.desenhar(self.janela_principal)
                # Desenha o texto do título no menu principal
                self.janela_principal.blit(self.titulo, self.titulo.get_rect(center=(LARGURA // 2, ALTURA // 7)))

            elif self.estado in ["lse", "lde", "lista_sequencial"]:
                #Conteúdo das telas secundárias
                TITULOS = {"lse": "", "lde": "", "lista_sequencial": ""}
                texto_conteudo = TITULOS[self.estado]

                self.botao_adicionar_valores= Botao(500, 200, 250, 50, 'Adicionar Valores')
                self.botao_adicionar_valores.desenhar(self.janela_principal)
                self.botao_consultar_valores = Botao(500, 300, 250, 50, 'Consultar Valores')
                self.botao_consultar_valores.desenhar(self.janela_principal)
                self.botao_trocar_valores = Botao(500, 400, 250, 50, 'Trocar Valores')
                self.botao_trocar_valores.desenhar(self.janela_principal)

                texto_conteudo_renderizado = FONTES["padrao"].render(texto_conteudo, True, PRETO)
                self.janela_principal.blit(texto_conteudo_renderizado, texto_conteudo_renderizado.get_rect(center=(LARGURA // 2, ALTURA // 2)))

                # Botão "Voltar"
                self.botao_voltar = Botao(20, 20, 100, 50, "Voltar")
                self.botao_voltar.desenhar(self.janela_principal)

            pygame.display.flip()

        # Encerre o Pygame
        pygame.quit()
        sys.exit()

# Cria uma instância do simulador e executa o programa
if __name__ == "__main__":
    simulador = SimuladorListas()
    simulador.executar()
