# Exercício 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = input("Digite uma expressão com parênteses: ")
stack = []

for char in expression:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if not stack:
            print("Expressão inválida.")
            break
        stack.pop()
else:
    if not stack:
        print("Expressão válida.")
    else:
        print("Expressão inválida.")
