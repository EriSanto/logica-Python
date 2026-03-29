# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta necessária para 
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

lagura_parede = float(input("Me informe a largura da parede: "))
altura_parede = float(input("Me informe a altura da parede: "))

area = lagura_parede * altura_parede
tinta = area / 2



print(f"Você ususará {tinta}l de tinta.")
