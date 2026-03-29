#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#  de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt

cateto_oposto = int(input("Me informe o cateto oposto: "))
cateto_adjacente = int(input("Me informe o cateto adjacente: "))

calculo = sqrt(cateto_oposto*cateto_oposto + cateto_adjacente*cateto_adjacente)

print(calculo)