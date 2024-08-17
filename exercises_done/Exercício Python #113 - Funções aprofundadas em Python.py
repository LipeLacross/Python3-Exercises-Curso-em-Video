# Exercício 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def leiaFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número real.")

number_int = leiaInt("Digite um número inteiro: ")
print(f"Você digitou o inteiro: {number_int}")

number_float = leiaFloat("Digite um número real: ")
print(f"Você digitou o real: {number_float}")
