# Exercício 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

first_term = int(input("Digite o primeiro termo da PA: "))
reason = int(input("Digite a razão da PA: "))

term = first_term
count = 0

while True:
    terms_to_show = int(input("Quantos termos você quer mostrar? (Digite 0 para sair): "))
    if terms_to_show == 0:
        break

    for _ in range(terms_to_show):
        print(term, end=" ")
        term += reason
        count += 1
    print()
print(f"Progressão finalizada com {count} termos mostrados.")
