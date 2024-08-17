# Exercício 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def moeda(value, currency='R$'):
    return f"{currency} {value:.2f}".replace('.', ',')

def aumentar(value, percent, format=False):
    result = value + (value * percent / 100)
    return moeda(result) if format else result

def diminuir(value, percent, format=False):
    result = value - (value * percent / 100)
    return moeda(result) if format else result

def dobro(value, format=False):
    result = value * 2
    return moeda(result) if format else result

def metade(value, format=False):
    result = value / 2
    return moeda(result) if format else result
