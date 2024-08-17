# Exercício 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = [[int(input(f"Digite o valor para a posição ({i}, {j}): ")) for j in range(3)] for i in range(3)]

print("Matriz 3x3:")
for row in matrix:
    print(' '.join(f"{cell:2}" for cell in row))
