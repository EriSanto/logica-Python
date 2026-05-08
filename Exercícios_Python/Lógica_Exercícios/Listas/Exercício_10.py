# Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

numeros = [2,6,7,3,5]

soma = sum(numeros)
mult = numeros[0] * numeros[1] * numeros[2] * numeros[3] * numeros[4]
somaa = ' + '.join(map(str, numeros))
multa = ' x '.join(map(str, numeros))

print(somaa,"=", soma )
print(multa,"=", mult)
