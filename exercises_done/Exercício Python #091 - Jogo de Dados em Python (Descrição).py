# Exercício 091: Crie um programa onde 4 jogadores joguem um dado.py e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.py.

import random

results = {f'Jogador {i+1}': random.randint(1, 6) for i in range(4)}

sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print("Resultados dos jogadores:")
for player, result in sorted_results:
    print(f"{player} tirou {result}")

print(f"\nO vencedor foi {sorted_results[0][0]} com {sorted_results[0][1]}")
