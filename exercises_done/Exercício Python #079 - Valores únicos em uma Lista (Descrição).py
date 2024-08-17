# Exercício 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

values = []
while True:
    number = int(input("Digite um número: "))
    if number not in values:
        values.append(number)
    else:
        print("Número já existe na lista.")

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

print(f"Valores únicos digitados: {sorted(values)}")
