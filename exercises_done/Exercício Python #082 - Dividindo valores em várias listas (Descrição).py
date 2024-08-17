# Exercício 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

numbers = []
even_numbers = []
odd_numbers = []

while True:
    number = int(input("Digite um número: "))
    numbers.append(number)
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

print(f"Lista completa: {numbers}")
print(f"Números pares: {even_numbers}")
print(f"Números ímpares: {odd_numbers}")
