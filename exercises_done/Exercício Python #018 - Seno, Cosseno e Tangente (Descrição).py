# Exercício 018: Faça um programa que leia um número inteiro e mostre na tela o seu fatorial.
import math

number = int(input("Digite um número inteiro: "))
factorial = math.factorial(number)
print(f"O fatorial de {number} é {factorial}.")
