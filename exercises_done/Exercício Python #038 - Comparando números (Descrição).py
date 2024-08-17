# Exercício 038: Escreva um programa que leia dois números inteiros e compare-os.
# Mostre na tela uma mensagem indicando qual é o maior, o menor ou se são iguais.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print("Os números são iguais.")
