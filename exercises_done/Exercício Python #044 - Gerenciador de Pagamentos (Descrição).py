# Exercício 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento.

product_price = float(input("Digite o preço do produto: "))
payment_condition = int(input("Escolha a condição de pagamento (1 à vista em dinheiro/cheque, 2 à vista no cartão, 3 em até 2x no cartão, 4 em 3x ou mais no cartão): "))

if payment_condition == 1:
    final_price = product_price * 0.90
elif payment_condition == 2:
    final_price = product_price * 0.95
elif payment_condition == 3:
    final_price = product_price
    print(f"Preço sem desconto: R${final_price:.2f}")
elif payment_condition == 4:
    final_price = product_price * 1.20
    print(f"Preço com 20% de juros: R${final_price:.2f}")
else:
    print("Opção inválida.")

print(f"O valor final do produto é R${final_price:.2f}.")
