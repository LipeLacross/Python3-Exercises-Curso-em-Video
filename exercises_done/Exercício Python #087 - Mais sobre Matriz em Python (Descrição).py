# Exercício 087: Aprimore o desafio anterior, mostrando no final:

matrix = [[int(input(f"Digite o valor para a posição ({i}, {j}): ")) for j in range(3)] for i in range(3)]

print("Matriz 3x3:")
for row in matrix:
    print(' '.join(f"{cell:2}" for cell in row))

sum_even = sum(cell for row in matrix for cell in row if cell % 2 == 0)
sum_third_col = sum(row[2] for row in matrix)
max_row = max(matrix, key=sum)

print(f"Soma dos valores pares: {sum_even}")
print(f"Soma dos valores da terceira coluna: {sum_third_col}")
print(f"Maior soma de linha: {sum(max_row)}")
