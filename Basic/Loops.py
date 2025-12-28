# Imprima todos os números de 1 a 100.
# Crie uma tabuada interativa (usuário digita o número, o programa mostra a tabuada.
# Jogo de adivinhação: o programa escolhe um número aleatório de 1 a 10 e o usuário tenta acertar.

import random

"""
for i in range(1,101):
    print(i)
"""

"""
num = int(input("Digite o número que deseja ver a tabuada:\t"))

for x in range(0,11):
    multiplos = num * x
    print(f"{num} x {x} = {multiplos}")
"""


num_secreto = random.randint(0,10)

tentativas = 0

print("Jogo de Adivinhação! Tente adivinhar o número.\n")

while True:
    palpite = (input("Insira seu palmite entre os números interios entre 1 e 10.\n"))

    if not palpite.isdigit():
        print("Digite um número válido!")
        continue

    palpite = int(palpite)

    tentativas += 1

    if palpite == num_secreto:
        print("Parabéns, você acertou! O número secreto é:",palpite)
        print("Você tentou",tentativas,"vezes!")
        break

    else:
        print("Você errou!\nTente novamente!")