# Exercício 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

house_value = float(input("Digite o valor da casa: "))
salary = float(input("Digite o salário do comprador: "))
years = int(input("Digite em quantos anos o empréstimo será pago: "))

monthly_installment = house_value / (years * 12)
max_installment = salary * 0.30

if monthly_installment <= max_installment:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
