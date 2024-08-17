# Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
money_brl = float(input("Quantos reais você tem na carteira? "))
usd_exchange_rate = float(input("Qual é a cotação do dólar? "))
usd_amount = money_brl / usd_exchange_rate
print(f"Com R${money_brl:.2f}, você pode comprar ${usd_amount:.2f}.")
