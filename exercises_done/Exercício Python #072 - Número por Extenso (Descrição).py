# Exercício 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numbers_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

number = int(input("Digite um número entre 0 e 20: "))

if 0 <= number <= 20:
    print(f"O número {number} por extenso é '{numbers_extenso[number]}'.")
else:
    print("Número fora do intervalo permitido.")
