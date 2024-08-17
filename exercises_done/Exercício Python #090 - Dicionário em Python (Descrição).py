# Exercício 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

student = {}
student['name'] = input("Nome do aluno: ")
student['average'] = float(input("Média do aluno: "))

if student['average'] >= 7:
    student['status'] = 'Aprovado'
elif 5 <= student['average'] < 7:
    student['status'] = 'Recuperação'
else:
    student['status'] = 'Reprovado'

print(f"\nNome: {student['name']}")
print(f"Média: {student['average']}")
print(f"Situação: {student['status']}")
