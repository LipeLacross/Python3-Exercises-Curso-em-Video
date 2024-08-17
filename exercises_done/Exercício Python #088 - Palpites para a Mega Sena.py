# Exercício 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

def generate_mega_sena_game():
    return sorted(random.sample(range(1, 61), 6))

num_games = int(input("Quantos jogos você quer gerar? "))
games = [generate_mega_sena_game() for _ in range(num_games)]

print(f"Seus jogos são:")
for i, game in enumerate(games, start=1):
    print(f"Jogo {i}: {game}")
