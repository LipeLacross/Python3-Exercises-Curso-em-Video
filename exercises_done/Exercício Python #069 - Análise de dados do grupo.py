# Exercício 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

age_sum = 0
male_oldest_name = ""
male_oldest_age = 0
female_under_20_count = 0
people_count = 0

while True:
    name = input("Digite o nome: ")
    age = int(input("Digite a idade: "))
    sex = input("Digite o sexo (M/F): ").upper()

    age_sum += age
    people_count += 1

    if sex == "M" and age > male_oldest_age:
        male_oldest_name = name
        male_oldest_age = age
    elif sex == "F" and age < 20:
        female_under_20_count += 1

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

average_age = age_sum / people_count

print(f"Média de idade: {average_age:.1f}")
print(f"Nome do homem mais velho: {male_oldest_name}")
print(f"Quantidade de mulheres com menos de 20 anos: {female_under_20_count}")
