import random

print("********************************")
print("*Bem vindo no jogo da mega sena*")
print("********************************")

total_de_numeros = 6
numeros_jogados = []
numeros_sorteados = []
acertos = 0

for interacao in range(0, total_de_numeros):
    #Interpolação de string
    numero_str = input("Digite o {}º número entre 1 e 60: ".format(interacao+1))
    numero     = int(numero_str)
    if(numero < 1 or numero > 60):
        print("Você deve digitar um número entre 1 e 60!")
        total_de_numeros = total_de_numeros + 1
        continue
    numeros_jogados.append(numero)

numeros_sorteados = random.sample(range(1,61), 6)
print(numeros_sorteados)
print(numeros_jogados)

for interacao1 in range(0, total_de_numeros):
    for interacao2 in range(0, total_de_numeros):
        if (numeros_jogados[interacao2] == numeros_sorteados[interacao1]):
            acertos = acertos + 1

if (acertos == 4):
    print("Parabéns você fez a quadra da mega sena!!!")
elif (acertos == 5):
    print("Parabéns você fez a quina da mega sena!!!")
elif (acertos == 6):
    print("Parabéns agora você é milionário!!!")
else:
    print("Você acertou {} números!".format(acertos))