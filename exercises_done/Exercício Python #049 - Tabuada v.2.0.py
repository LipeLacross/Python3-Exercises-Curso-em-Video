# Exercício 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

number = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
