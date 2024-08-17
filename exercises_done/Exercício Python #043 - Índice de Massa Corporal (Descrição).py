# Exercício 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:

weight = float(input("Digite o peso em kg: "))
height = float(input("Digite a altura em metros: "))

imc = weight / (height ** 2)

if imc < 18.5:
    status = "Abaixo do peso"
elif imc < 24.9:
    status = "Peso normal"
elif imc < 29.9:
    status = "Sobrepeso"
elif imc < 34.9:
    status = "Obesidade grau 1"
elif imc < 39.9:
    status = "Obesidade grau 2"
else:
    status = "Obesidade grau 3"

print(f"Seu IMC é {imc:.2f}. Status: {status}.")
