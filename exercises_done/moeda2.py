# Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def moeda(value, currency='R$'):
    return f"{currency} {value:.2f}".replace('.', ',')

def aumentar(value, percent):
    return moeda(value + (value * percent / 100))

def diminuir(value, percent):
    return moeda(value - (value * percent / 100))

def dobro(value):
    return moeda(value * 2)

def metade(value):
    return moeda(value / 2)

