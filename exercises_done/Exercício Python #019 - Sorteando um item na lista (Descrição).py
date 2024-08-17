# Exercício 019: Desenvolva um programa que leia um número real e mostre a sua parte inteira.
import math

real_number = float(input("Digite um número real: "))
integer_part = math.trunc(real_number)
print(f"A parte inteira de {real_number} é {integer_part}.")
