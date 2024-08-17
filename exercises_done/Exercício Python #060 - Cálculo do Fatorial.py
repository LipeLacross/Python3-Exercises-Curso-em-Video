# Exercício 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

import math

number = int(input("Digite um número para calcular o fatorial: "))
factorial = math.factorial(number)
print(f"O fatorial de {number} é {factorial}.")
