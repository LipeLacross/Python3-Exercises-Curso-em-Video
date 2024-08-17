# Exercício 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(text):
 length = len(text) + 4
 print(f"{'*' * length}")
 print(f"* {text} *")
 print(f"{'*' * length}")

text = input("Digite o texto a ser exibido: ")
escreva(text)
