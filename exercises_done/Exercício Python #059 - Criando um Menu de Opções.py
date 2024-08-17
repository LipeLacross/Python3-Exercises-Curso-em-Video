# Exercício 059: Crie um programa que leia dois valores e mostre um menu na tela.

value1 = float(input("Digite o primeiro valor: "))
value2 = float(input("Digite o segundo valor: "))

menu_option = 0
while menu_option != 5:
    print("""
    Menu:
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    5 - Sair
    """)
    menu_option = int(input("Escolha uma opção: "))

    if menu_option == 1:
        print(f"Soma: {value1 + value2}")
    elif menu_option == 2:
        print(f"Subtração: {value1 - value2}")
    elif menu_option == 3:
        print(f"Multiplicação: {value1 * value2}")
    elif menu_option == 4:
        if value2 != 0:
            print(f"Divisão: {value1 / value2}")
        else:
            print("Não é possível dividir por zero.")
    elif menu_option != 5:
        print("Opção inválida.")
