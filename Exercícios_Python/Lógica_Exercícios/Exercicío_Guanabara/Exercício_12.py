# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

camisa = 59.99

desconto =  5

calculo = camisa * (desconto/100)

resultado = camisa - calculo



print(f"A camisa custa R${camisa} com deconto de 5% fica {resultado:.2f} ")