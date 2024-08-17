# Exercício 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

max_weight = float('-inf')
min_weight = float('inf')

for _ in range(5):
    weight = float(input("Digite o peso: "))
    if weight > max_weight:
        max_weight = weight
    if weight < min_weight:
        min_weight = weight

print(f"Maior peso: {max_weight} kg")
print(f"Menor peso: {min_weight} kg")
