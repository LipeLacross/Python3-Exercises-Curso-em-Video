# Exercício 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

person = {}
current_year = datetime.now().year

person['name'] = input("Nome: ")
birth_year = int(input("Ano de nascimento: "))
person['age'] = current_year - birth_year
person['ctps'] = int(input("Carteira de Trabalho (0 se não tiver): "))

if person['ctps'] != 0:
    person['hiring_year'] = int(input("Ano de contratação: "))
    person['salary'] = float(input("Salário: "))
    person['retirement_age'] = (person['hiring_year'] + 35) - birth_year
    person['retirement_year'] = person['hiring_year'] + 35
else:
    person['hiring_year'] = None
    person['salary'] = None
    person['retirement_age'] = None
    person['retirement_year'] = None

print("\nInformações da pessoa:")
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")
