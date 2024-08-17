# Exercício 022: Crie um programa que leia o comprimento de três segmentos de reta e informe se eles podem ou não formar um triângulo.
a = float(input("Digite o comprimento do primeiro segmento: "))
b = float(input("Digite o comprimento do segundo segmento: "))
c = float(input("Digite o comprimento do terceiro segmento: "))

if a + b > c and b + c > a and c + a > b:
    print("Os segmentos podem formar um triângulo.")
else:
    print("Os segmentos não podem formar um triângulo.")
