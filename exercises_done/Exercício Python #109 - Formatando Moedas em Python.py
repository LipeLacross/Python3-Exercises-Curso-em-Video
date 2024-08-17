# Exercício 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda3

price = float(input("Digite o preço: R$ "))
print(f"Aumentando 10%: {moeda3.aumentar(price, 10, format=True)}")
print(f"Diminuindo 13%: {moeda3.diminuir(price, 13, format=True)}")
print(f"Dobro do preço: {moeda3.dobro(price, format=True)}")
print(f"Metade do preço: {moeda3.metade(price, format=True)}")
