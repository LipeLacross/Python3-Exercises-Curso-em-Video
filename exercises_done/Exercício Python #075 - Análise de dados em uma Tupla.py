# Exercício 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:

values = (int(input("Digite o primeiro valor: ")),
          int(input("Digite o segundo valor: ")),
          int(input("Digite o terceiro valor: ")),
          int(input("Digite o quarto valor: ")))

print(f"Você digitou os valores: {values}")
print(f"O valor 9 apareceu {values.count(9)} vezes.")

if 3 in values:
    print(f"O primeiro valor 3 apareceu na posição {values.index(3) + 1}.")
else:
    print("O valor 3 não foi digitado.")
