# Exercício 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

values = [int(input(f"Digite o {i+1}º valor: ")) for i in range(7)]

even_values = sorted([v for v in values if v % 2 == 0])
odd_values = sorted([v for v in values if v % 2 != 0])

print(f"Valores pares: {even_values}")
print(f"Valores ímpares: {odd_values}")
