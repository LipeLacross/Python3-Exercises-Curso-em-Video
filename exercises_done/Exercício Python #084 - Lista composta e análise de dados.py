# Exercício 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:

people = []
while True:
    name = input("Nome: ")
    weight = float(input("Peso: "))
    people.append((name, weight))

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

weights = [weight for name, weight in people]
print(f"\nForam cadastradas {len(people)} pessoas.")
print(f"O maior peso foi {max(weights)}kg. Peso de ", end='')
print(', '.join(name for name, weight in people if weight == max(weights)))
print(f"O menor peso foi {min(weights)}kg. Peso de ", end='')
print(', '.join(name for name, weight in people if weight == min(weights)))
