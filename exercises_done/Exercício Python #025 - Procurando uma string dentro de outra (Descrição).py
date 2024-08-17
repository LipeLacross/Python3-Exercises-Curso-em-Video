# Exercício 025: Desenvolva um programa que calcule a área de um círculo e mostre o resultado.
import math

radius = float(input("Digite o raio do círculo: "))
area = math.pi * (radius ** 2)
print(f"A área do círculo é {area:.2f}.")
