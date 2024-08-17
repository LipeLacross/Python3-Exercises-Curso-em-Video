# Exercício 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

from utilidadesCeV import moeda5, dado
def leiaDinheiro(prompt):
    while True:
        try:
            value = input(prompt).replace(',', '.')
            return float(value)
        except ValueError:
            print("Entrada inválida. Digite um valor monetário válido.")

# Programa principal
from utilidadesCeV import moeda5, dado

price = leiaDinheiro("Digite o preço: R$ ")
#price = dado.leiaDinheiro("Digite o preço: R$ ")
moeda5.resumo(price, 10, 13)
