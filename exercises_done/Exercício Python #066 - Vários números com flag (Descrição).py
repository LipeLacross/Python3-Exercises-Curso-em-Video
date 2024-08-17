# Exercício 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

count = 0
total_sum = 0

while True:
    number = int(input("Digite um número (ou 999 para parar): "))
    if number == 999:
        break
    count += 1
    total_sum += number

print(f"Foram digitados {count} números e a soma é {total_sum}.")
