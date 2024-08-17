# Exercício 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:

values = []
while True:
    number = int(input("Digite um número: "))
    values.append(number)

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

print(f"Você digitou {len(values)} números.")
print(f"A lista em ordem crescente: {sorted(values)}")
print(f"A lista em ordem decrescente: {sorted(values, reverse=True)}")
print(f"A lista contém o número 5: {'5' in values}")
