# Exercício 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
original_price = float(input("Digite o preço do produto: "))
discount = original_price * 0.05
price_with_discount = original_price - discount
print(f"Preço original: R${original_price:.2f}")
print(f"Preço com 5% de desconto: R${price_with_discount:.2f}")
