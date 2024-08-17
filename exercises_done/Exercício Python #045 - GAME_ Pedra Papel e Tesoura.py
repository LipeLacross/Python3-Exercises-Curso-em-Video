# Exercício 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random

choices = ["pedra", "papel", "tesoura"]
computer_choice = random.choice(choices)
user_choice = input("Escolha pedra, papel ou tesoura: ").lower()

if user_choice not in choices:
    print("Escolha inválida.")
else:
    print(f"Computador escolheu {computer_choice}.")
    if user_choice == computer_choice:
        print("Empate!")
    elif (user_choice == "pedra" and computer_choice == "tesoura") or \
            (user_choice == "papel" and computer_choice == "pedra") or \
            (user_choice == "tesoura" and computer_choice == "papel"):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
