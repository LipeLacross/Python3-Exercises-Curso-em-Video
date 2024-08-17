# Exercício 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

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

def resumo(value, aum, dim):
    print(f"Preço analisado: {moeda(value, 'R$')}")
    print(f"Dobro do preço: {dobro(value, True)}")
    print(f"Metade do preço: {metade(value, True)}")
    print(f"Aumento de {aum}%: {aumentar(value, aum, True)}")
    print(f"Diminuindo {dim}%: {diminuir(value, dim, True)}")
