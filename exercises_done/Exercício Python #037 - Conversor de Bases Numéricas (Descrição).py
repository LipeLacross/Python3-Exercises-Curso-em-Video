# Exercício 037: Escreva um programa em que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

number = int(input("Digite um número inteiro: "))
conversion_choice = int(input("Escolha a base de conversão (1 para binário, 2 para octal, 3 para hexadecimal): "))

if conversion_choice == 1:
    print(f"{number} em binário é {bin(number)[2:]}.")
elif conversion_choice == 2:
    print(f"{number} em octal é {oct(number)[2:]}.")
elif conversion_choice == 3:
    print(f"{number} em hexadecimal é {hex(number)[2:]}.")
else:
    print("Opção inválida.")
