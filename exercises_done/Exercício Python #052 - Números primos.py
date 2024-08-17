# Exercício 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input("Digite um número inteiro: "))

if number < 2:
    print("Número não é primo.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Número é primo.")
    else:
        print("Número não é primo.")
