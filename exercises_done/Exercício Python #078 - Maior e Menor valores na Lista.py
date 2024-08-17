# Exercício 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

values = [int(input(f"Digite o {i+1}º valor: ")) for i in range(5)]

print(f"Valores digitados: {values}")
print(f"Maior valor: {max(values)} na posição(s): {', '.join(str(i) for i, v in enumerate(values) if v == max(values))}")
print(f"Menor valor: {min(values)} na posição(s): {', '.join(str(i) for i, v in enumerate(values) if v == min(values))}")
