# Exercício 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

total_wins = 0

while True:
    user_number = int(input("Digite um número: "))
    user_choice = input("Par ou Ímpar? (P/I): ").upper()

    computer_number = random.randint(0, 10)
    total = user_number + computer_number
    is_even = total % 2 == 0

    if (user_choice == 'P' and is_even) or (user_choice == 'I' and not is_even):
        print(f"Você ganhou! Computador escolheu {computer_number}. Total: {total}")
        total_wins += 1
    else:
        print(f"Você perdeu! Computador escolheu {computer_number}. Total: {total}")
        break

print(f"Você teve {total_wins} vitórias consecutivas.")
