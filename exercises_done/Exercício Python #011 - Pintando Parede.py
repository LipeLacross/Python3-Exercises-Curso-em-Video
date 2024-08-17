# Exercício 011: Faça um algoritmo que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
width = float(input("Digite a largura da parede em metros: "))
height = float(input("Digite a altura da parede em metros: "))
area = width * height
paint_needed = area / 2
print(f"A área da parede é {area:.2f} m².")
print(f"Você precisará de {paint_needed:.2f} litros de tinta para pintar a parede.")
