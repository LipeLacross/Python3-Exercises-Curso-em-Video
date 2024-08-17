# Exercício 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
original_salary = float(input("Digite o salário do funcionário: "))
increase = original_salary * 0.15
new_salary = original_salary + increase
print(f"Salário original: R${original_salary:.2f}")
print(f"Salário com 15% de aumento: R${new_salary:.2f}")
