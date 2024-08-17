# Exercício 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado.py não tenha sido informado corretamente.

def ficha(name='<desconhecido>', goals=0):
    print(f"Jogador: {name}")
    print(f"Gols: {goals}")

name = input("Nome do jogador (deixe em branco se não quiser informar): ")
goals = input("Número de gols (deixe em branco se não quiser informar): ")
goals = int(goals) if goals else 0

ficha(name, goals)
