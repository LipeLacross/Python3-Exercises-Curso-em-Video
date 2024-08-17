# Exercício 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
rental_days = int(input("Quantos dias o carro foi alugado? "))
km_driven = float(input("Quantos Km foram percorridos? "))
price_per_day = 60
price_per_km = 0.15
total_price = (rental_days * price_per_day) + (km_driven * price_per_km)
print(f"Total a pagar: R${total_price:.2f}")
