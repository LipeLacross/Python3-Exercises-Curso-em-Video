# Exercício 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(year_of_birth):
    age = datetime.now().year - year_of_birth
    if age < 16:
        return "Não vota"
    elif 16 <= age < 18 or age >= 65:
        return "Voto opcional"
    else:
        return "Voto obrigatório"

year_of_birth = int(input("Ano de nascimento: "))
print(f"Situação de voto: {voto(year_of_birth)}")
