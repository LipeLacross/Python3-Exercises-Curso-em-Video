# Exercício 106: Crie um programa que tenha uma função chamada análiseTexto() que vai receber uma string e deve retornar um dicionário com informações sobre o texto:
# - O total de letras em maiúsculas
# - O total de letras em minúsculas
# - O total de dígitos
# - O total de espaços em branco

def análiseTexto(text):
    return {
        'maiúsculas': sum(1 for c in text if c.isupper()),
        'minúsculas': sum(1 for c in text if c.islower()),
        'dígitos': sum(1 for c in text if c.isdigit()),
        'espaços': sum(1 for c in text if c.isspace())
    }

text = input("Digite um texto: ")
print(análiseTexto(text))
