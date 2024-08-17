# Exercício 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade.

birth_year = int(input("Digite o ano de nascimento: "))
current_year = 2024
age = current_year - birth_year

if age <= 9:
    category = "Mirim"
elif age <= 14:
    category = "Infantil"
elif age <= 19:
    category = "Junior"
elif age <= 25:
    category = "Sênior"
else:
    category = "Master"

print(f"O atleta está na categoria {category}.")
