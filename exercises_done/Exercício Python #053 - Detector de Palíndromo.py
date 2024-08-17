# Exercício 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

phrase = input("Digite uma frase: ").replace(" ", "").lower()
if phrase == phrase[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
