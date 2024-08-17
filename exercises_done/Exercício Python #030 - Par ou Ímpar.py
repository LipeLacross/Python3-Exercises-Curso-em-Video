# Exercício 030: Desenvolva um programa que leia o valor de um produto e mostre o valor com um aumento de 20%.
original_price = float(input("Digite o valor do produto: "))
increase = original_price * 0.20
price_with_increase = original_price + increase
print(f"Preço original: R${original_price:.2f}")
print(f"Preço com 20% de aumento: R${price_with_increase:.2f}")
