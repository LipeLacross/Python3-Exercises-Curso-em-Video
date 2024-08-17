# Exercício 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

first_term = int(input("Digite o primeiro termo da PA: "))
reason = int(input("Digite a razão da PA: "))

term = first_term
count = 0

while count < 10:
    print(term, end=" ")
    term += reason
    count += 1
print()
