# Exercício 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    number = int(input("Digite um número para ver a tabuada (ou um número negativo para sair): "))
    if number < 0:
        break
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    print()
