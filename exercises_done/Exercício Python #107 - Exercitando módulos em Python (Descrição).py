# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda1

price = float(input("Digite o preço: R$ "))
print(f"Aumentando 10%: R$ {moeda1.aumentar(price, 10):.2f}")
print(f"Diminuindo 13%: R$ {moeda1.diminuir(price, 13):.2f}")
print(f"Dobro do preço: R$ {moeda1.dobro(price):.2f}")
print(f"Metade do preço: R$ {moeda1.metade(price):.2f}")
