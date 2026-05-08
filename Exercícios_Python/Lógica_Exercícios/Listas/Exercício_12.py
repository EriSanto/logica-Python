# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

A = [2,3,4,5,6,7,8,9,10,12]

somar = 0
# 528
for n in A:
    
    somar += n ** 2
print(f"A soma dos quadrados é: ",somar)

