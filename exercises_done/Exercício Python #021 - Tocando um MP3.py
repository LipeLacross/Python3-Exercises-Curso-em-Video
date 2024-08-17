# Exercício 021: Faça um programa que leia a idade e o sexo de uma pessoa e mostre uma mensagem com base nas informações fornecidas.
age = int(input("Digite a sua idade: "))
sex = input("Digite o seu sexo (M/F): ").upper()
if sex == 'M':
    print("Você é do sexo masculino.")
elif sex == 'F':
    print("Você é do sexo feminino.")
else:
    print("Sexo inválido.")
if age < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
