# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = int(input("Me informe quantos Kms percorrido: "))
qtd_dias = int(input("Me informe a quantidade de dias que foi alugado: "))

calculo = 60 * qtd_dias + km_percorrido * 0.15


print(f"Total a pagar é: R${calculo}")