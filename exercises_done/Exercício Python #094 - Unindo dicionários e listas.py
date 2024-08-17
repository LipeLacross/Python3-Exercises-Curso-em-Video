# Exercício 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:

people = []
while True:
    person = {}
    person['name'] = input("Nome: ")
    person['sex'] = input("Sexo (M/F): ").upper()
    person['age'] = int(input("Idade: "))
    people.append(person)

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

total_people = len(people)
average_age = sum(person['age'] for person in people) / total_people
women = [person['name'] for person in people if person['sex'] == 'F']
over_18 = [person for person in people if person['age'] > 18]

print(f"\nTotal de pessoas cadastradas: {total_people}")
print(f"Média de idade: {average_age:.2f}")
print(f"Mulheres cadastradas: {', '.join(women)}")
print(f"Pessoas maiores de 18 anos: {', '.join(person['name'] for person in over_18)}")
