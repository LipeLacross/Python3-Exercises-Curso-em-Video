# Exercício 104: Crie um código que declare uma função chamada leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

number = leiaInt("Digite um número inteiro: ")
print(f"Você digitou: {number}")
