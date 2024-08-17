# Exercício 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

words = ('banana', 'laranja', 'morango', 'melancia', 'maçã')

for word in words:
    vowels = ''.join(letter for letter in word if letter in 'aeiou')
    print(f"Palavra '{word}' tem as vogais: {vowels}")
