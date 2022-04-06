import forca
import adivinhacao
import bn

def escolhe_jogo ( ):
    print('*********************************')
    print('*******Escolha o seu jogo!*******')
    print('*********************************')

    print("(1) Forca (2) Adivinhação (3) Batalha Naval")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Jogando batalha naval")
        bn.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
