# Exercício 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
grade1 = float(input("Digite a primeira nota: "))
grade2 = float(input("Digite a segunda nota: "))
average = (grade1 + grade2) / 2
print(f"A média entre {grade1} e {grade2} é {average:.2f}.")
