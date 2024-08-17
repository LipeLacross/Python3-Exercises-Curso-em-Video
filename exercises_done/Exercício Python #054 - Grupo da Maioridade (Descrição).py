# Exercício 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

current_year = datetime.now().year
underage_count = 0
of_age_count = 0

for _ in range(7):
    birth_year = int(input("Digite o ano de nascimento: "))
    age = current_year - birth_year
    if age < 18:
        underage_count += 1
    else:
        of_age_count += 1

print(f"Quantidade de pessoas menores de idade: {underage_count}")
print(f"Quantidade de pessoas maiores de idade: {of_age_count}")
