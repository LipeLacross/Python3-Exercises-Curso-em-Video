# Exercício 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

sum_of_evens = 0
for _ in range(6):
    number = int(input("Digite um número inteiro: "))
    if number % 2 == 0:
        sum_of_evens += number

print(f"A soma dos números pares é {sum_of_evens}.")
