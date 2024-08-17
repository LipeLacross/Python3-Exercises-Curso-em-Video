# Exercício 034: Crie um programa que leia o valor de dois números e mostre o quociente da divisão inteira e o resto da divisão.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
quotient = num1 // num2
remainder = num1 % num2
print(f"O quociente da divisão de {num1} por {num2} é {quotient}.")
print(f"O resto da divisão de {num1} por {num2} é {remainder}.")
