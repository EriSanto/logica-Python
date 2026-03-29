# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan, radians

angulo = int(input("Me informe o ângulo que você deseja: "))

radianos =  radians(angulo)

seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f"O ângulo de graus {angulo} tem:\nSeno: {seno:.2f}\nCosseono: {cosseno:.2f}\nTangente: {tangente:.2f}")