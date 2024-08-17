# Exercício 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

values = []
for _ in range(5):
    number = int(input("Digite um número: "))
    if not values or number > values[-1]:
        values.append(number)
    else:
        for i in range(len(values)):
            if number <= values[i]:
                values.insert(i, number)
                break

print(f"Lista ordenada: {values}")
