# Exercício 040: Crie um programa que leia duas notas de um aluno e calcule sua média.
# Mostre uma mensagem no final, de acordo com a média atingida.

grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
average = (grade1 + grade2) / 2

if average >= 7:
    print(f"Nota final: {average:.2f}. Aluno aprovado.")
elif average >= 5:
    print(f"Nota final: {average:.2f}. Aluno em recuperação.")
else:
    print(f"Nota final: {average:.2f}. Aluno reprovado.")
