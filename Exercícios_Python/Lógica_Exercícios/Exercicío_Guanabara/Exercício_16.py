# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Ex: Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

from math import floor

numero = float(input("Digite um número real: "))

conversao = floor(numero)

print(f"A parte inteira do número {numero} é {conversao}")