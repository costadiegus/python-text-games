def jogar():
    print("*********************************")
    print("****Bem vindo à Batalha Naval!***")
    print("*********************************")

    # modelo do mapa do jogador
    mapa_jogador = {"A": ["P", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "B": ["P", " ", " ", " ", " ", " ", " ", "R", " ", " "], 
                    "C": ["P", " ", " ", " ", " ", " ", " ", "R", " ", " "], 
                    "D": ["P", " ", " ", " ", "R", " ", " ", " ", " ", " "], 
                    "E": ["P", " ", " ", " ", "R", " ", " ", " ", " ", " "], 
                    "F": [" ", " ", " ", " ", " ", " ", " ", "T", "T", "T"], 
                    "G": ["C", "C", "C", "C", " ", " ", " ", " ", " ", " "], 
                    "H": [" ", " ", " ", " ", "T", "T", "T", " ", " ", " "], 
                    "I": [" ", " ", " ", " ", " ", " ", " ", " ", "S", " "], 
                    "J": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] }

    mapa_adversario = {"A": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "B": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "C": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "D": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "E": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "F": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "G": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "H": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "I": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
                    "J": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] }

    print('                     JOGADOR                                          ADVERSÁRIO')
    for m in mapa_jogador:
        print('{} {}'.format(mapa_jogador.get(m), mapa_adversario.get(m)))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()