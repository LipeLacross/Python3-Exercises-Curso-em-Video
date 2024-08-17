# Exercício 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):
    result = 1
    for i in range(1, n + 1):
        result *= i
        if show:
            print(i, end=' ')
            if i < n:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return result

number = int(input("Número para calcular o fatorial: "))
print(fatorial(number, show=True))
