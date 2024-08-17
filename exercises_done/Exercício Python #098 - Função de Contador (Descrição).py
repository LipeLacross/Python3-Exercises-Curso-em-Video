# Exercício 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

def contador(start, end, step):
    if step == 0:
        step = 1
    if start < end:
        for i in range(start, end + 1, step):
            print(i, end=' ')
    else:
        for i in range(start, end - 1, -step):
            print(i, end=' ')
    print()

print("Contagem de 1 a 10 de 1 em 1:")
contador(1, 10, 1)

print("Contagem de 10 a 0 de 2 em 2:")
contador(10, 0, 2)

print("Contagem de 0 a 100 de 10 em 10:")
contador(0, 100, 10)
