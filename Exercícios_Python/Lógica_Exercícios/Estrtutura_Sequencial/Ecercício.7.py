# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metro_qua = int(input("Me infome os metros quadrados da área a ser pintada:"))

consumo = metro_qua / 3
latas = consumo / 18
preco = latas * 80




print(f"Para pintar {metro_qua}m² {consumo} {latas} {preco} ")