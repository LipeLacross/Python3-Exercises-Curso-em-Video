# Exercício 027: Desenvolva um programa que leia o valor de um produto e mostre o preço com desconto de 10%.
original_price = float(input("Digite o valor do produto: "))
discount = original_price * 0.10
price_with_discount = original_price - discount
print(f"Preço original: R${original_price:.2f}")
print(f"Preço com 10% de desconto: R${price_with_discount:.2f}")
