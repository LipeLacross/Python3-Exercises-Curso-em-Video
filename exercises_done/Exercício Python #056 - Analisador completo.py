# Exercício 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

total_age = 0
oldest_man_name = ""
oldest_man_age = 0
young_women_count = 0

for _ in range(4):
    name = input("Digite o nome: ")
    age = int(input("Digite a idade: "))
    sex = input("Digite o sexo (M/F): ").upper()

    total_age += age

    if sex == "M" and age > oldest_man_age:
        oldest_man_name = name
        oldest_man_age = age
    elif sex == "F" and age < 20:
        young_women_count += 1

average_age = total_age / 4

print(f"Média de idade do grupo: {average_age:.1f}")
print(f"Nome do homem mais velho: {oldest_man_name}")
print(f"Quantidade de mulheres com menos de 20 anos: {young_women_count}")
