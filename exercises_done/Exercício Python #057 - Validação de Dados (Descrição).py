# Exercício 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sex = input("Digite o sexo (M/F): ").upper()
while sex not in ['M', 'F']:
    sex = input("Valor inválido. Digite o sexo (M/F): ").upper()
print(f"Sexo {sex} registrado com sucesso.")
