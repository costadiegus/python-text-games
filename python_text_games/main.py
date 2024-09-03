import forca
import adivinhacao
import bn
import sudoku
import uno


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Sudoku Solver (4) Batalha Naval (5) Uno")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif jogo == 3:
        print("Jogando Sudoku Solver")
        sudoku.jogar()
    elif jogo == 4:
        print("Jogando Batalha Naval")
        bn.jogar()
    elif jogo == 5:
        print("Jogando Uno")
        uno.jogar()


if __name__ == "__main__":
    escolhe_jogo()
