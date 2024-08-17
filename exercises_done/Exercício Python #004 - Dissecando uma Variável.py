# Exercício 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
value = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(value)}")
print(f"É um número? {value.isnumeric()}")
print(f"É alfabético? {value.isalpha()}")
print(f"É alfanumérico? {value.isalnum()}")
print(f"Está em maiúsculas? {value.isupper()}")
print(f"Está em minúsculas? {value.islower()}")
print(f"Está capitalizado? {value.istitle()}")
