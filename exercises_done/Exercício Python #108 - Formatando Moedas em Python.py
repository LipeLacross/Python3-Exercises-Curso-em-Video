# Exercício 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda2

price = float(input("Digite o preço: R$ "))
print(f"Aumentando 10%: {moeda2.aumentar(price, 10)}")
print(f"Diminuindo 13%: {moeda2.diminuir(price, 13)}")
print(f"Dobro do preço: {moeda2.dobro(price)}")
print(f"Metade do preço: {moeda2.metade(price)}")
