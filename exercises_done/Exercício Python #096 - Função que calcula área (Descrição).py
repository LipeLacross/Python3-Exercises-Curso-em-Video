# Exercício 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(width, length):
    return width * length

width = float(input("Largura do terreno: "))
length = float(input("Comprimento do terreno: "))

print(f"A área do terreno é {area(width, length)}m².")
