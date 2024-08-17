# Exercício 017: Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.
number = int(input("Digite um número inteiro: "))
if number % 2 == 0:
    print(f"O número {number} é par.")
else:
    print(f"O número {number} é ímpar.")
