# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random

def sorteia(lst):
    lst.extend(random.sample(range(1, 101), 5))

def somaPar(lst):
    return sum(num for num in lst if num % 2 == 0)

numbers = []
sorteia(numbers)
print(f"Números sorteados: {numbers}")
print(f"Soma dos valores pares: {somaPar(numbers)}")
