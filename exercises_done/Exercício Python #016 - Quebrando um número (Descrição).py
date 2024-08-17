# Exercício 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

real_number = float(input("Digite um número real: "))
integer_part = math.floor(real_number)
print(f"A porção inteira de {real_number} é {integer_part}.")
