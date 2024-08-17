# Exercício 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

def calculate_bills(amount):
    bills = [50, 20, 10, 5, 1]
    bill_count = {}

    for bill in bills:
        if amount >= bill:
            bill_count[bill] = amount // bill
            amount %= bill

    return bill_count

amount = int(input("Digite o valor a ser sacado: R$"))

if amount < 0:
    print("Valor inválido.")
else:
    bills = calculate_bills(amount)
    for bill, count in bills.items():
        print(f"Cédulas de R${bill}: {count}")
