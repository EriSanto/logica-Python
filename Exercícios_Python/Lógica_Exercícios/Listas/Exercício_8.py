# Faça um programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

impar = []

par = []

x = 0

while x < 20:
    
    x += 1

    numero = int(input("Dgigite um número: "))

    if numero % 2 == 0:
        par.append(numero)
        
    elif numero % 2 == 1:
        impar.append(numero)


print(f"Números Totais\n{sorted(impar+par)}")
print(f"Números Impares\n{impar}")
print(f"Números Pares\n{par}")
        