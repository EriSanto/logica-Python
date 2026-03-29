# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos Dólares ela pode comprar.

dinheiro =  float(input("Quanto dinehro você tem na carteira?"))

conversor = dinheiro / 3.27

print(f"Covertendo para Dólar você teria US${conversor:.2}")

