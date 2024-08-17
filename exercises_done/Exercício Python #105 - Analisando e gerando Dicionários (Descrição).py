# Exercício 105: Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

def notas(*args):
    return {
        'total': len(args),
        'maior': max(args),
        'menor': min(args),
        'média': sum(args) / len(args)
    }

print(notas(5, 6.5, 7, 8, 9.5))
