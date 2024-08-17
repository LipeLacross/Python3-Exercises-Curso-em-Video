# Exercício 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input("Digite o número de termos da sequência de Fibonacci: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
