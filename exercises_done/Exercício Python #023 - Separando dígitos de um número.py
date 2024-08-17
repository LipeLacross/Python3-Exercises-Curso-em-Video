# Exercício 023: Faça um programa que calcule e mostre a área de um trapézio.
base1 = float(input("Digite o comprimento da primeira base do trapézio: "))
base2 = float(input("Digite o comprimento da segunda base do trapézio: "))
height = float(input("Digite a altura do trapézio: "))
area = ((base1 + base2) / 2) * height
print(f"A área do trapézio é {area:.2f}.")
