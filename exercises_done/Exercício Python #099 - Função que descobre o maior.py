# Exercício 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*args):
    if args:
        return max(args)
    return None

values = [int(input("Digite um valor (ou '0' para parar): "))]
while values[-1] != 0:
    values.append(int(input("Digite um valor (ou '0' para parar): ")))

print(f"O maior valor digitado foi {maior(*values[:-1])}")
