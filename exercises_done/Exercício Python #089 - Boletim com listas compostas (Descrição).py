# Exercício 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

students = []

while True:
    name = input("Nome do aluno: ")
    note1 = float(input("Primeira nota: "))
    note2 = float(input("Segunda nota: "))
    average = (note1 + note2) / 2
    students.append([name, note1, note2, average])

    continue_input = input("Quer continuar? (S/N): ").upper()
    if continue_input == 'N':
        break

print("\nBoletim:")
for student in students:
    print(f"{student[0]}: Média = {student[3]}")

while True:
    query = input("Deseja ver as notas de qual aluno? (Digite 'Sair' para encerrar): ")
    if query == 'Sair':
        break

    for student in students:
        if student[0] == query:
            print(f"{student[0]}: Nota 1 = {student[1]}, Nota 2 = {student[2]}")
            break
    else:
        print("Aluno não encontrado.")
