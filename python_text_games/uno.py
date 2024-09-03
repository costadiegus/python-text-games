import random


class Carta:
    def __init__(self, cor: str, valor: str):
        self.cor = cor
        self.valor = valor

    def __str__(self):
        return f"[{self.valor}{self.cor[0].upper()}]"


class Baralho:
    def __init__(self):
        self.cartas = self.gerar_cartas()

    def gerar_cartas(self):
        cartas = []
        cores = ["Vermelho", "Azul", "Verde", "Amarelo"]
        for cor in cores:
            for i in range(10):
                cartas.append(Carta(cor, str(i)))
            cartas.append(Carta(cor, "C+2"))
            cartas.append(Carta(cor, "Inverter"))
            cartas.append(Carta(cor, "Pular"))
        cartas.append(Carta("Coringa", "C+4"))
        cartas.append(Carta("Coringa", "Coringa"))
        return cartas

    def comprar_carta(self):
        if self.cartas:
            return self.cartas.pop()
        return None


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.cartas = []

    def adicionar_carta(self, carta: Carta):
        self.cartas.append(carta)

    def jogar_carta(self, indice: int):
        return self.cartas.pop(indice) if 0 <= indice < len(self.cartas) else None

    def gritar_uno(self):
        if len(self.cartas) == 1:
            print(f"{self.nome} gritou 'Uno'!")


class Tabuleiro:
    def __init__(self):
        self.baralho = Baralho()
        self.monte_descartes = []
        self.jogadores = []
        self.turno_atual = 0
        self.estado_jogo = "ativo"

    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)

    def iniciar_jogo(self):
        for _ in range(7):
            for jogador in self.jogadores:
                jogador.adicionar_carta(self.baralho.comprar_carta())
        self.monte_descartes.append(self.baralho.comprar_carta())

    def proximo_turno(self):
        self.turno_atual = (self.turno_atual + 1) % len(self.jogadores)

    def verificar_vitoria(self):
        for jogador in self.jogadores:
            if not jogador.cartas:
                self.estado_jogo = "finalizado"
                print(f"{jogador.nome} venceu!")
                return True
        return False

    def jogar_turno(self, indice_carta: int):
        jogador_atual = self.jogadores[self.turno_atual]
        carta_jogada = jogador_atual.jogar_carta(indice_carta)
        if carta_jogada:
            self.monte_descartes.append(carta_jogada)
            self.verificar_vitoria()
            self.proximo_turno()


def jogar():
    num_jogadores = int(input("Digite o número de jogadores: "))
    tabuleiro = Tabuleiro()

    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i + 1}: ")
        tabuleiro.adicionar_jogador(Jogador(nome))

    tabuleiro.iniciar_jogo()

    while tabuleiro.estado_jogo == "ativo":
        jogador_atual = tabuleiro.jogadores[tabuleiro.turno_atual]
        print(f"\nÉ a vez de {jogador_atual.nome}")
        print("Cartas na mão:")
        for i, carta in enumerate(jogador_atual.cartas):
            print(f"{i}: {carta}")

        print(f"Carta no monte de descarte: {tabuleiro.monte_descartes[-1]}")
        escolha = int(input("Escolha uma carta para jogar (ou -1 para comprar): "))

        if escolha == -1:
            nova_carta = tabuleiro.baralho.comprar_carta()
            if nova_carta:
                jogador_atual.adicionar_carta(nova_carta)
                print(f"{jogador_atual.nome} comprou {nova_carta}")
        else:
            tabuleiro.jogar_turno(escolha)
            jogador_atual.gritar_uno()
