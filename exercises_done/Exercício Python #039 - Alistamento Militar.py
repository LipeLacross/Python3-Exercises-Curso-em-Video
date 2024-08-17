# Exercício 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Mostre também o tempo que falta ou que passou do prazo.

birth_year = int(input("Digite o ano de nascimento: "))
current_year = 2024
age = current_year - birth_year
age_diff = abs(age - 18)

if age < 18:
    print(f"Você ainda vai se alistar. Faltam {age_diff} anos.")
elif age == 18:
    print("É hora de se alistar.")
else:
    print(f"Você já passou do tempo de alistamento há {age_diff} anos.")
