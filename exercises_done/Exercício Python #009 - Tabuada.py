# Exercício 009: Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
number = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
