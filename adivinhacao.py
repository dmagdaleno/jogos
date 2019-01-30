print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 3

for rodada in range(0, total_de_tentativas):
    print("\n## Rodada ({}/{}) ##".format(rodada +1, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    if (chute == numero_secreto):
        print("Você acertou!!")
    elif(chute > numero_secreto):
        print("Você errou!! Seu chute foi maior que o número secreto")
    else:
        print("Você errou!! Seu chute foi menor que o número secreto")

print("Fim do jogo.")