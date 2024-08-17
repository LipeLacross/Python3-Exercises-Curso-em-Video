# Exercício 028: Faça um programa que leia a temperatura em Fahrenheit e a converta para Celsius.
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F é igual a {celsius:.2f}°C.")
