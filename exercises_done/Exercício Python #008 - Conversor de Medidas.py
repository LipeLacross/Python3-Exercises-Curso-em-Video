# Exercício 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
meters = float(input("Digite um valor em metros: "))
centimeters = meters * 100
millimeters = meters * 1000
print(f"O valor em centímetros é {centimeters} cm.")
print(f"O valor em milímetros é {millimeters} mm.")
