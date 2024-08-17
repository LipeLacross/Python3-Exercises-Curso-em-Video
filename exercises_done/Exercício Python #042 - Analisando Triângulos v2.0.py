# Exercício 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado.

side1 = float(input("Digite o comprimento do primeiro lado: "))
side2 = float(input("Digite o comprimento do segundo lado: "))
side3 = float(input("Digite o comprimento do terceiro lado: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        triangle_type = "Equilátero"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        triangle_type = "Isósceles"
    else:
        triangle_type = "Escaleno"
    print(f"Os lados formam um triângulo {triangle_type}.")
else:
    print("Os lados não formam um triângulo.")
