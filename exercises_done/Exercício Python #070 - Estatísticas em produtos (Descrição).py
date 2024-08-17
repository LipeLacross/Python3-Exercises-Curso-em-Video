# Exercício 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

total_spent = 0
cheap_products_count = 0
cheapest_product_price = float('inf')
cheapest_product_name = ""

while True:
    name = input("Digite o nome do produto: ")
    price = float(input("Digite o preço do produto: "))

    total_spent += price

    if price < 50:
        cheap_products_count += 1

    if price < cheapest_product_price:
        cheapest_product_price = price
        cheapest_product_name = name

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

print(f"Total gasto: R${total_spent:.2f}")
print(f"Quantidade de produtos abaixo de R$50: {cheap_products_count}")
print(f"Produto mais barato: {cheapest_product_name} por R${cheapest_product_price:.2f}")
