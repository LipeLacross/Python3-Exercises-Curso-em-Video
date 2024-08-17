# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(value, percent):
    return value + (value * percent / 100)

def diminuir(value, percent):
    return value - (value * percent / 100)

def dobro(value):
    return value * 2

def metade(value):
    return value / 2
