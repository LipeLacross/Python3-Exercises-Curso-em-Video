# Exercício 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

random_numbers = tuple(random.randint(1, 100) for _ in range(5))

print("Números sorteados:", random_numbers)
print(f"Maior número: {max(random_numbers)}")
print(f"Menor número: {min(random_numbers)}")
