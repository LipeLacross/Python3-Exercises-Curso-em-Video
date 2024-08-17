# Exercício 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

player = {}
matches = []

player['name'] = input("Nome do jogador: ")
num_matches = int(input("Quantas partidas ele jogou? "))

for i in range(num_matches):
    goals = int(input(f"Quantos gols na partida {i+1}? "))
    matches.append(goals)

player['goals'] = matches
player['total_goals'] = sum(matches)

print(f"\n{player['name']} jogou {num_matches} partidas e fez {player['total_goals']} gols.")
for i, goals in enumerate(matches):
    print(f"Na partida {i+1} fez {goals} gols.")
