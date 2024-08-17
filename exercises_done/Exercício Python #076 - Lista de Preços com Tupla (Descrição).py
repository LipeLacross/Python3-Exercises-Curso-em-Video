# Exercício 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

products = (
    'Arroz', 2.50,
    'Feijão', 3.00,
    'Macarrão', 1.80,
    'Leite', 1.20,
    'Açúcar', 2.00
)

print("LISTAGEM DE PREÇOS")
for i in range(0, len(products), 2):
    print(f"{products[i]:.<20} R${products[i+1]:>7.2f}")
