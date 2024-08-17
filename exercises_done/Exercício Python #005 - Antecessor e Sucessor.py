# Exercício 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
number = int(input("Digite um número inteiro: "))
successor = number + 1
predecessor = number - 1
print(f"O sucessor de {number} é {successor} e o antecessor é {predecessor}.")
