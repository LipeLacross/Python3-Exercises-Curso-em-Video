# Exercício 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

first_term = int(input("Digite o primeiro termo da PA: "))
reason = int(input("Digite a razão da PA: "))

for i in range(10):
    term = first_term + i * reason
    print(term, end=" ")
print()
