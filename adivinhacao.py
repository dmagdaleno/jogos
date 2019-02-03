import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.random() *100)
total_de_tentativas = 0
pontos = 1000

print("\nEscolha um nível.")
nivel = int(input("\n(1) Fácil, (2) Médio ou (3) Difícil: "))

if(nivel == 1):
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 3

for rodada in range(0, total_de_tentativas):
    print("\n## Rodada ({}/{}) ##".format(rodada +1, total_de_tentativas))

    chute_str = input("Digite um número entre 0 e 100: ")
    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    if(chute < 0 or chute > 100):
        print("Número inválido")
        continue

    if (chute == numero_secreto):
        print("Você acertou!!")
        break
    elif(chute > numero_secreto):
        print("Você errou!! Seu chute foi maior que o número secreto")
    else:
        print("Você errou!! Seu chute foi menor que o número secreto")

    delta = abs(numero_secreto - chute)

    if(nivel == 3):
        delta = delta *2
    
    pontos = pontos - delta

print("Fim do jogo. Você marcou {} pontos!".format(pontos))