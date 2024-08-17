# Exercício 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

count = 0
total_sum = 0
max_value = float('-inf')
min_value = float('inf')

while True:
    number = int(input("Digite um número: "))
    count += 1
    total_sum += number

    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

average = total_sum / count

print(f"Média: {average:.1f}")
print(f"Maior valor: {max_value}")
print(f"Menor valor: {min_value}")
