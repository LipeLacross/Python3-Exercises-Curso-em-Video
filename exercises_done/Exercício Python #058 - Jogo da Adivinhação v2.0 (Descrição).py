# Exercício 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

computer_number = random.randint(0, 10)
guess = -1
attempts = 0

while guess != computer_number:
    guess = int(input("Adivinhe o número entre 0 e 10: "))
    attempts += 1

print(f"Parabéns! Você acertou o número {computer_number} em {attempts} tentativas.")
