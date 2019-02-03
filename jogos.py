import adivinhacao
import forca

def escolher_jogo():
    print("***************************")
    print("Bem vindo, escolha um jogo!")
    print("***************************")

    print("\n(1) Adivinhação\n(2) Forca")

    jogo = int(input("Jogo: "))

    if(jogo == 1):
       adivinhacao.jogar()
    elif (jogo == 2):
       forca.jogar()
    else:
       print("Jogo inválido!")

if(__name__ == "__main__"):
    escolher_jogo()