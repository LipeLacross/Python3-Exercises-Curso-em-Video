# Exercício 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

sum_of_multiples = sum(number for number in range(1, 501) if number % 3 == 0)
print(f"A soma dos múltiplos de 3 no intervalo de 1 até 500 é {sum_of_multiples}.")
